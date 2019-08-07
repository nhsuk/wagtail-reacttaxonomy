from django.db import models

from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtail.core.models import Page

from wagtailreacttaxonomy.models import TaxonomyMixin
from wagtailreacttaxonomy.edit_handlers import TaxonomyPanel


class TestPage(Page, TaxonomyMixin):
    taxonomy_panels = [
        TaxonomyPanel('taxonomy_json', taxonomy_terms_id='test_taxonomy'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Content'),
        ObjectList(taxonomy_panels, heading='Taxonomy'),
    ])
