from django.db import models

from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtail.core.models import Page

from wagtailreacttaxonomy.models import TaxonomyMixin, WithTaxonomyPermissions
from wagtailreacttaxonomy.edit_handlers import TaxonomyPanel, PermissionsPanel


class TestPage(Page, TaxonomyMixin, WithTaxonomyPermissions):
    taxonomy_panels = [
        TaxonomyPanel('taxonomy_json', taxonomy_terms_id='test_taxonomy'),
    ]

    permission_panels = [
        PermissionsPanel('permissions_json', permission_terms_id='test_permissions_taxonomy'),
    ]


    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Content'),
        ObjectList(taxonomy_panels, heading='Taxonomy'),
        ObjectList(permission_panels, heading='Permissions'),
    ])
