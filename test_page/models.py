from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList, PageChooserPanel
from wagtail.core.models import Page

from wagtailreacttaxonomy.models import TaxonomyMixin, PageTaxonomyPermissionsMixin, ModelTaxonomyPermissionsMixin
from wagtailreacttaxonomy.edit_handlers import TaxonomyPanel, PermissionsPanel


class TestPage(Page, TaxonomyMixin, PageTaxonomyPermissionsMixin):
    permission_inherit_page = models.ForeignKey(
        'TestPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    taxonomy_term_panels = [
        TaxonomyPanel('taxonomy_json', taxonomy_terms_id='test_taxonomy'),
    ]

    taxonomy_permission_panels = [
        FieldPanel('global_permission', classname='global_permission'),
        FieldPanel('inherit_permission', classname='inherit_permission'),
        PageChooserPanel('permission_inherit_page'),
        PermissionsPanel(
            'permissions_json',
            permission_terms_id='test_permissions_taxonomy',
            permission_actions=['view', 'download'],
            permission_type='page',
        ),
        FieldPanel('permissions_json_formatted'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Content'),
        ObjectList(taxonomy_term_panels, heading='Taxonomy'),
        ObjectList(taxonomy_permission_panels, heading='Permissions'),
    ])

class TestModel(ModelTaxonomyPermissionsMixin):
    panels = [
        PermissionsPanel(
            'permissions_json',
            permission_terms_id='test_permissions_taxonomy',
            permission_actions=['group'],
            permission_type='model',
        ),
        FieldPanel('permissions_json_formatted'),
    ]

    def __str__(self):
        return 'TestModel - {0}'.format(self.id)

