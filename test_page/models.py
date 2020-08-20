from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList
from wagtail.core.models import Page

from wagtailreacttaxonomy.models import TaxonomyMixin, WithTaxonomyPermissions
from wagtailreacttaxonomy.edit_handlers import TaxonomyPanel, PermissionsPanel


class TestPage(Page, TaxonomyMixin, WithTaxonomyPermissions):
    taxonomy_term_panels = [
        TaxonomyPanel('taxonomy_json', taxonomy_terms_id='test_taxonomy'),
    ]

    taxonomy_permission_panels = [
        FieldPanel('global_permission', classname='global_permission'),
        FieldPanel('inherit_permission', classname='inherit_permission'),
        PermissionsPanel('permissions_json', permission_terms_id='test_permissions_taxonomy'),
    ]


    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Content'),
        ObjectList(taxonomy_term_panels, heading='Taxonomy'),
        ObjectList(taxonomy_permission_panels, heading='Permissions'),
    ])
