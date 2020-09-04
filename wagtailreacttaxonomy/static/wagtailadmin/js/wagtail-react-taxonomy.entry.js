import ReactDOM from 'react-dom';
import { ThemeProvider } from 'react-jss';

import Taxonomy from './react-taxonomy.esm.js';
import { TaxonomyPermissionPanel } from './react-taxonomy-permission.esm.js';

window.onload = function (){

  // load  taxonomy terms chooser
  const taxonomyTerms = document.getElementById('taxonomy-terms-json').value;
  const taxonomyTermsJson = JSON.parse(taxonomyTerms);
  ReactDOM.render(
    <ThemeProvider theme={{}}>
      <Taxonomy
        outputFieldId="id_taxonomy_json"
        taxonomyTerms={taxonomyTermsJson}
        termsDisplayText="Choose from the following keywords:"
        assignedDisplayText="Selected keywords"
      />
    </ThemeProvider>,
    document.getElementById('react-taxonomy')
  );

  // load  taxonomy permission panel
  const taxonomyPermission = document.getElementById('permission-terms-json').value;
  const taxonomyPermissionJson = JSON.parse(taxonomyPermission);
  const actions = taxonomyPermissionJson.actions;
  const vocabularyGroups = taxonomyPermissionJson.vocabularyGroups;
  let taxonomyPermissionInheritParent = null;
  if (document.getElementById('id_permission_inherit_page-chooser')) {
    taxonomyPermissionInheritParent = document.getElementById('id_permission_inherit_page-chooser').closest('.field');
    taxonomyPermissionInheritParent.closest('.object').style.display = 'none';
  }
  ReactDOM.render(
    <TaxonomyPermissionPanel
      actions={actions}
      vocabularyGroups={vocabularyGroups}
      globalPermissionFieldId="id_global_permission"
      inheritPermissionFieldId="id_inherit_permission"
      taxonomyPermissionJsonId="id_permissions_json"
      taxonomyPermissionInheritParent={taxonomyPermissionInheritParent}
    />,
    document.getElementById('react-taxonomy-permissions')
  );
};
