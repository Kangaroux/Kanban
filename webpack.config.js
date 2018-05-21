const path = require("path");
const webpack = require("webpack");


module.exports = {
  mode: "development",

  entry: {
    app: "./app/static/js/app",
  },

  output: {
    path: path.resolve(__dirname, "build"),
    filename: "[name].js",
  },

  module: {
    rules: [
      {
        test: /\.jsx?$/,
        include: /app/,
        loader: "babel-loader",
      }
    ]
  },

  resolve: {
    modules: [
      "node_modules",
      path.resolve(__dirname, "app", "static", "js")
    ],
    extensions: [".js", ".jsx"]
  },

  optimization: {
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          name: "vendor",
          chunks: "initial"
        }
      }
    }
  }
};