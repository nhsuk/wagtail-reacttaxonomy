import ReactDOM from 'react-dom';
import { ThemeProvider } from 'react-jss';
import Taxonomy from './react-taxonomy.esm.js';

window.onload = function (){
  const taxonomyTermsJson = document.getElementById('taxonomy-terms-json').value;
  ReactDOM.render(
    <ThemeProvider theme={{}}>
      <Taxonomy
        outputFieldId="id_taxonomy_json"
        taxonomyTerms={taxonomyTermsJson}
      />
    </ThemeProvider>,
    document.getElementById('react-taxonomy')
  );
};
