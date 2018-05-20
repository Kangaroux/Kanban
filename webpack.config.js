const path = require("path");
const webpack = require("webpack");


module.exports = {
  mode: "development",
  entry: {
    app: "./app/app.js",
  },

  output: {
    path: path.resolve(__dirname, "build"),
    filename: "[name].js",
  },

  module: {
    rules: [
      {
        test: /\.(js|tag)$/,
        include: /app/,
        loader: "babel-loader",
      },
      {
        test: /\.tag$/,
        include: /app/,
        loader: "riot-tag-loader",
        query: {
          hot: false
        }
      }
    ]
  },

  resolve: {
    modules: [
      "node_modules",
      path.resolve(__dirname, "app")
    ],
    extensions: [".js", ".tag"]
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