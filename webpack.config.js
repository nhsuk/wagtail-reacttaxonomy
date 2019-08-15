const path = require('path');

module.exports = (env, argv) => {
  const config = {
    entry: {'wagtail-react-streamfield': [
        './wagtailreacttaxonomy/static/wagtailadmin/js/wagtail-react-taxonomy.entry.js',
      ]},
    output: {
      path: path.resolve('wagtailreacttaxonomy/static/wagtailadmin/js/'),
      filename: 'wagtail-react-taxonomy.js',
      publicPath: '/static/'
    },
    module: {
      rules: [
        {
          test: /\.jsx?$/,
          loader: 'babel-loader',
          exclude: /node_modules/,
        },
      ],
    },
  };
  return config;
};
