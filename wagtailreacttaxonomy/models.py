import json
from django.conf import settings

from azure.storage.file import FileService
from azure.common import AzureMissingResourceHttpError
from azure.storage.file.models import File as AzureFile, Directory as AzureDirectory

from azure.storage.blob import BlockBlobService

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class TaxonomyTerms(models.Model):
    taxonomy_id = models.CharField(max_length=255, unique=True)
    terms_json = models.TextField()

@receiver(post_save, sender=TaxonomyTerms)
def update_taxonomy_terms_on_blobstore(sender, instance, **kwargs):
    data = json.loads(instance.terms_json)
    terms_with_vocab = get_terms_from_terms_json(data)
    terms_with_vocab_json = to_json(terms_with_vocab)

    blob_service = BlockBlobService(account_name=settings.AZURE_ACCOUNT_NAME, account_key=settings.AZURE_ACCOUNT_KEY)
    blob_service.create_blob_from_text(settings.AZURE_CONTAINER, f'taxonomy/{instance.taxonomy_id}.json', terms_with_vocab_json)

def get_terms_from_terms_json(data):
    terms = []
    level = 1
    for obj in data:
        if obj.get('type') == 'volcabulary':
            vocab_code = obj.get('code')
            children = obj.get('children', None)
            if children:
                child_terms = get_terms_from_children(children, vocab_code, level)
                for child_term in child_terms:
                    terms.append(child_term)
    return terms

def get_terms_from_children(children, vocab_code, level):
    terms = []
    for obj in children:
        if obj.get('type') == 'term':
            terms.append({ obj.get('code'): { "label": obj.get('label'), "vocabCode": vocab_code, "level": level } })
            children = obj.get('children', None)
            if children:
                next_level = level + 1
                child_terms = get_terms_from_children(children, vocab_code, next_level)
                for child_term in child_terms:
                    terms.append(child_term)
    return terms

def to_json(data):
    return json.dumps(data)

class TaxonomyMixin(models.Model):
    taxonomy_json = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
