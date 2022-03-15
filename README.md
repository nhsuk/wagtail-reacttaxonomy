Wagtail - React Taxonomy
=============================

Add React Taxonomy component to a wagtail page and store it as a json in the db.

Quick start
-----------

1. Add "wagtailreacttaxonomy" to your INSTALLED_APPS:

```python
INSTALLED_APPS = [
    'wagtailreacttaxonomy',
    ...
]
```

Useful Imports
--------------
```python
from django.db import models
from django.db.models.signals import pre_save

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList, PageChooserPanel
from wagtail.core.models import Page

from wagtailreacttaxonomy.models import TaxonomyMixin, PageTaxonomyPermissionsMixin,\
    ModelTaxonomyPermissionsMixin, format_permissions_json
from wagtailreacttaxonomy.edit_handlers import TaxonomyPanel, PermissionsPanel
```

How to use Taxonomy Term Component
----------------------------------

1. Add `TaxonomyMixin` to your wagtail Page model
2. Add to the page `taxonomy_json` using `TaxonomyPanel`

Example:
```python
class TestPage(Page, TaxonomyMixin):
    taxonomy_term_panels = [
        TaxonomyPanel('taxonomy_json', taxonomy_terms_id='test_taxonomy'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Content'),
        ObjectList(taxonomy_term_panels, heading='Taxonomy'),
    ])
```

How to use Taxonomy Permission Component for Page
-------------------------------------------------

1. Add `PageTaxonomyPermissionsMixin` to your wagtail Page model
2. Add to the page `global_permission` using `FieldPanel`
3. Add to the page `inherit_permission` using `FieldPanel`
4. Add to the page `permissions_json` using `PermissionsPanel`

Example:
```python
class TestPage(Page, PageTaxonomyPermissionsMixin):
    permission_inherit_page = models.ForeignKey(
        'TestPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    taxonomy_permission_panels = [
        FieldPanel('global_permission', classname='global_permission'),
        FieldPanel('inherit_permission', classname='inherit_permission'),
        PageChooserPanel('permission_inherit_page'),
        PermissionsPanel(
            'permissions_json',
            permission_terms_id='test_permissions_taxonomy',
            permission_actions=['action1', 'action2'],
            permission_type='page',
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Content'),
        ObjectList(taxonomy_permission_panels, heading='Permissions'),
    ])


pre_save.connect(format_permissions_json, sender=TestPage)
```

How to use Taxonomy Permission Component for model
--------------------------------------------------

1. Add `ModelTaxonomyPermissionsMixin` to your model
4. Add to the page `permissions_json` using `PermissionsPanel`

Example:
```python
class TestModel(ModelTaxonomyPermissionsMixin):
    panels = [
        PermissionsPanel(
            'permissions_json',
            permission_terms_id='test_permissions_taxonomy',
            permission_actions=['action1', 'action2'],
            permission_type='model',
        ),
        FieldPanel('permissions_json_formatted'),
    ]

pre_save.connect(format_permissions_json, sender=TestModel)
```

How to contribute
-----------------

### Getting started

#### With devcontainer and VSCode (recommended)

* Open repository folder in container

#### Build locally (old school)

##### Requirements
* Docker
* docker-compose

You'll get all this lot installed nicely with https://docs.docker.com/docker-for-mac/install.

### Add git hook
```
./scripts/install-hooks.sh
```
Now you are set

### Build the containers
```
docker-compose build
```
### Create super user
```
docker-compose run --rm web python manage.py createsuperuser
```
### Exercise the application

#### Run the containers
```
docker-compose up
```

#### Browse to http://localhost:8000/admin and make your changes with live reload

1. Log in as superuser
1. You will see a Taxonomy Terms entry in the admin menu
1. Use this entry to upload and save the JSON text of your taxonomy
1. Taxonomies are stored in your Django media folder (media in the test configuration)

### Run tests as required

```
docker-compose run --rm web python manage.py test
```