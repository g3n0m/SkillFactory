const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const HtmlWebpackPlugin = require('html-webpack-plugin');
const TerserWebpackPlugin = require('terser-webpack-plugin');
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

module.exports = {
    mode: 'production',
    entry: {
        main: path.resolve(__dirname, '../src/index.js'),
    },

    output: {
        path: path.resolve(__dirname, '../dist'),
        filename: 'main.js',
    },
    plugins: [
        new MiniCssExtractPlugin(),
        new HtmlWebpackPlugin({
            template: "./src/index.pug",
            filename: "index.html"
        }),
        new CssMinimizerPlugin(),
        new TerserWebpackPlugin(),
    ],
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                        {
                            loader: MiniCssExtractPlugin.loader,
                            options: {
                            esModule: true,
                            },
                        },
                    'css-loader', //"sass-loader",
                ],
            },
            {
                test: /\.pug$/,
                loader: 'pug-loader',
                options: {pretty: true}
            }
        ]
    },
    optimization: {
    minimize: true,
    minimizer: [new CssMinimizerPlugin() , new TerserWebpackPlugin({})],
    },
  };