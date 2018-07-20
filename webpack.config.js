const Path = require("path");


module.exports = {
  entry: {
    "app": "./app/static/js/app"
  },
  output: {
    path: Path.resolve(__dirname, "dist"),
    filename: "[name].js"
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: "babel-loader"
      }
    ]
  },
  resolve: {
    alias: {
      "vue$": "vue/dist/vue.esm.js"
    }
  }
};