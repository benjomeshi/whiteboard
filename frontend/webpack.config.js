var path = require("path")
const HtmlWebPackPlugin = require('html-webpack-plugin')
var ExtractTextPlugin = require('extract-text-webpack-plugin')
var WebpackPwaManifest = require('webpack-pwa-manifest')
var OfflinePlugin = require('offline-plugin')


// Service Worker
let offlinePlugin = new OfflinePlugin({
  safeToUseOptionalCaches: true,

  caches: {
    main: [':rest:'],
    additional: [':externals:']
  },

  // externals: ['https://fonts.googleapis.com/css?family=Pacifico'],

  ServiceWorker: {
    navigateFallbackURL: '/',
    events: true,
    minify: true
  }
});


// -- PWA Manifest --
let pwaPlugin = new WebpackPwaManifest({
  name: 'Whiteboard',
  short_name: 'Whiteboard',
  description: 'Whiteboarding app for the iPad Pro and Apple Pencil',
  // start_url: ".",
  background_color: '#A5DBF7',
  theme_color: '#A5DBF7',
  icons: [
    {
      src: path.resolve('assets/icon.png'),
      sizes: [96, 128, 192, 256, 384, 512] // multiple sizes
    }
  ]
});


module.exports = {
  entry: {
    app: [
      './webpack/index.js'
    ]
  },
  output: {
    path: path.resolve(__dirname + '/../app/static'),
    filename: '[name].js',
  },
  module: {
    loaders: [
      {
        test: /\.css$/,
        loaders: ExtractTextPlugin.extract("css-loader")
      },
      {
        test: /\.(scss|sass)$/,
        loaders: ExtractTextPlugin.extract("css-loader!sass-loader")
      },
      {
        test:    /\.elm$/,
        exclude: [/elm-stuff/, /node_modules/],
        loader:  'elm-webpack-loader',
        query:{
          verbose: true,
          warn: true
        }
      },
      {
        test: /\.(jpe?g|png|gif)$/i,   //to support eg. background-image property
        loader:"file-loader",
        query:{
          name:'[name].[ext]',
          outputPath:'images/'
          //the images will be emmited to dist/images/ folder
          //the images will be put in the DOM <style> tag as eg. background: url(dist/images/image.png);
        }
      },
      {
        test: /\.woff$/,
        loader: 'url-loader',
        query: {
          limit: 10000,
          mimetype: 'application/font-woff',
          outputPath: 'assets/fonts/',
          name: '[name].[ext]'
        }
      },
      {
        test: /\.[ot]tf$/,
        loader: 'url-loader',
        query:{
          limit: 65000,
          mimetype: 'application/octet-stream',
          outputPath: 'assets/fonts/',
          name: '[name].[ext]'
        }
      },
      {
        test: /\.(ttf|eot|svg)$/,
        loader: 'file-loader',
        query:{
          outputPath: 'assets/fonts/',
          name: '[name].[ext]'
        }
      },
    ],

    noParse: /\.elm$/,
  },
  plugins: [
    new ExtractTextPlugin("[name].css"),
    new HtmlWebPackPlugin({
      template: 'webpack/index.html',
      inject: 'body'
    }),
    offlinePlugin,
    pwaPlugin
  ],
  devServer: {
    inline: true,
    stats: { colors: true },
  },
};
