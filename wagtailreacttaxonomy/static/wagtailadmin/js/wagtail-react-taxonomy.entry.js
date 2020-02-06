import ReactDOM from 'react-dom';
import { ThemeProvider } from 'react-jss';
import Taxonomy from './react-taxonomy.esm.js';

window.onload = function (){
  const taxonomyTermsJson = document.getElementById('taxonomy-terms-json').value;
  const json = JSON.parse(taxonomyTermsJson);
  ReactDOM.render(
    <ThemeProvider theme={{}}>
      <Taxonomy
        outputFieldId="id_taxonomy_json"
        taxonomyTerms={json}
        termsDisplayText="Choose from the following keywords:"
        assignedDisplayText="Selected keywords"
      />
    </ThemeProvider>,
    document.getElementById('react-taxonomy')
  );
};
