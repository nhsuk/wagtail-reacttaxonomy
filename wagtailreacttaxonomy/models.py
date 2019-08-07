from django.db import models


class TaxonomyTerms(models.Model):
    taxonomy_id = models.CharField(max_length=255, unique=True)
    terms_json = models.TextField()


class TaxonomyMixin(models.Model):
    taxonomy_json = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
