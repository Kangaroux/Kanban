const path = require("path");

module.exports = {
  mode: "development",
  entry: "./app/js/app",

  output: {
    path: path.resolve(__dirname, "build", "js"),
    filename: "app.js",
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        include: [
          path.resolve(__dirname, "app", "js")
        ],
        loader: "babel-loader",
      }
    ]
  },

  resolve: {
    modules: [
      "node_modules",
      path.resolve(__dirname, "app", "js")
    ],
    extensions: [".js"]
  }
};