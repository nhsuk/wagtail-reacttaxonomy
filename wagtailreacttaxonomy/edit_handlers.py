import json

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from wagtail.admin.edit_handlers import FieldPanel

from .models import TaxonomyTerms


class TaxonomyPanel(FieldPanel):
    object_template = "wagtailadmin/edit_handlers/taxonomy_panel.html"
    field_template = "wagtailadmin/edit_handlers/taxonomy_panel.html"

    def render_as_object(self):
        return mark_safe(render_to_string(self.object_template, {
            'self': self,
            self.TEMPLATE_VAR: self,
            'field': self.bound_field,
            'taxonomy_terms_json': self.load_taxonomy_terms(),
            'taxonomy_terms_error_message': self.taxonomy_terms_error_message,
        }))
    
    def load_taxonomy_terms(self):
        taxonomy_terms_json = None
        try:
            data = TaxonomyTerms.objects.get(taxonomy_id=self.taxonomy_terms_id)
            try:
                json.loads(data.terms_json)
            except json.decoder.JSONDecodeError:
                self.taxonomy_terms_error_message = '"Taxonomy Terms" json wrong format'
            taxonomy_terms_json = data.terms_json
        except TaxonomyTerms.DoesNotExist:
            self.taxonomy_terms_error_message = 'No "Taxonomy Terms" for this id: "{}"'.format(
                self.taxonomy_terms_id
            )
        return taxonomy_terms_json
    
    def __init__(self, field_name, taxonomy_terms_id, *args, **kwargs):
        super().__init__(field_name, *args, **kwargs)
        self.taxonomy_terms_id = taxonomy_terms_id
        self.taxonomy_terms_error_message = None

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update(
            field_name=self.field_name,
            taxonomy_terms_id=self.taxonomy_terms_id,
            widget=self.widget if hasattr(self, 'widget') else None,
        )
        return kwargs


class PermissionsPanel(FieldPanel):
    object_template = "wagtailadmin/edit_handlers/permissions_panel.html"
    field_template = "wagtailadmin/edit_handlers/permissions_panel.html"

    def render_as_object(self):
        return mark_safe(render_to_string(self.object_template, {
            'self': self,
            self.TEMPLATE_VAR: self,
            'field': self.bound_field,
            'permission_terms_json': self.load_permission_terms(),
            'permission_terms_error_message': self.permission_terms_error_message,
        }))
    
    def load_permission_terms(self):
        permission_terms_json = None
        try:
            data = TaxonomyTerms.objects.get(taxonomy_id=self.permission_terms_id)
            try:
                json.loads(data.terms_json)
            except json.decoder.JSONDecodeError:
                self.permission_terms_error_message = '"Permission Terms" json wrong format'
            permission_terms_json = data.terms_json
        except TaxonomyTerms.DoesNotExist:
            self.permission_terms_error_message = 'No "Permission Terms" for this id: "{}"'.format(
                self.permission_terms_id
            )
        return permission_terms_json
    
    def __init__(self, field_name, permission_terms_id, *args, **kwargs):
        super().__init__(field_name, *args, **kwargs)
        self.permission_terms_id = permission_terms_id
        self.permission_terms_error_message = None

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update(
            field_name=self.field_name,
            permission_terms_id=self.permission_terms_id,
            widget=self.widget if hasattr(self, 'widget') else None,
        )
        return kwargs