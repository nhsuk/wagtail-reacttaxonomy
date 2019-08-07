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

How to use
----------

1. Add `TaxonomyMixin` to you wagtail Page model
2. Add to the page `taxonomy_json` using `TaxonomyPanel`

Example:
```python
class TestPage(Page, TaxonomyMixin):
    taxonomy_panels = [
        TaxonomyPanel('taxonomy_json', taxonomy_terms_id='test_taxonomy'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Content'),
        ObjectList(taxonomy_panels, heading='Taxonomy'),
    ])
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