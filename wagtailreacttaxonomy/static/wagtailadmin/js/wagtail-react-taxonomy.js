function loadReactTaxonomy() {
  // ReactDOM.render(<Taxomony outputFieldId="id_taxonomy_json" taxonomyTerms='{{taxonomy_terms_json|safe}}' />, document.getElementById('react-taxonomy'));
}
  
$(document).on('page:load', loadReactTaxonomy);
$(loadReactTaxonomy)
