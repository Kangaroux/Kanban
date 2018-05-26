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
    alias: {
      "~": path.resolve(__dirname, "app", "static", "js")
    },
    modules: [
      "node_modules"
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