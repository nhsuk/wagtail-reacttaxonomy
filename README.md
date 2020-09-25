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

### Requirements
* Docker
* docker-compose
You'll get all this lot installed nicely with (https://docs.docker.com/docker-for-mac/install).


### Setup locally
Add git hook
```
./scripts/install-hooks.sh
```
Build the image
```
docker-compose build
```
Run the containers
```
docker-compose up
```
Create super user:
```
docker-compose run --rm web python manage.py createsuperuser
```