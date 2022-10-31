## Установка и настройка Webpack
Необходимо установить node.js (в комплекте npm)  
https://nodejs.org/en/download/  
Проверяем версию: ```npm -v```  
Создаем папку, в ней инициализируем проект npm:  
`npm init`  
Далее через терминал устанавливаем webpack:  
`npm install webpack webpack-cli --save-dev`  
Для включения в сборку css установим загрузчики:  
`npm i style-loader css-loader --save-dev`  
Чтобы css добавлялись не в тело файла js а отдельным файлом установим:  
`npm install  mini-css-extract-plugin  --save-dev`  

В корне создаем файл конфиг: `webpack.config.js`  
```
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
module.exports = {
    entry: './index.js',
    output: {
        filename: 'main.js'
    },
    mode: 'development',
    plugins: [new MiniCssExtractPlugin()],
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
                    'css-loader',
                ], 
            }
        ]
    }
}
```
Описание конфига:  
https://webpack.js.org/configuration/  



Если в пакет `package.json` в объект `scripts` добавить строку `"build" : "webpack"`, то запускать сборку можно командой `npm run build`  

Восстановить модули по данным package.json могут команды:  
`npm install`  
или  
`yarn install`  
Установка yarn:  
https://yarnpkg.com/getting-started/install  

## Для работы DevServer необходимо собирать html файл в папке dist
Ставим шаблонизатор:  
`npm i html-webpack-plugin --save-dev`  
Добавляем в конфиг константу:  
`const HtmlWebpackPlugin = require('html-webpack-plugin');` 
В конфиг в plugins:  
```
new HtmlWebpackPlugin({
            template: "./src/index.pug",
            filename: "index.html"
        }),
```  

Ставим сам шаблонизатор pug:
`npm i pug pug-loader --save-dev`
В конфиге в rules: создаем новое правило использования файлов .pug:
```
{
    test: /\.pug$/,
    loader: 'pug-loader',
    options: {pretty: true}
}
```

## Установка DevServer
`npm install webpack-dev-server --save-dev`  
В packade.json добавляем скрипт для запуска с собственной конфигурацией (npm run start:dev):  
`"start:dev": "webpack serve --config config/webpack.dev.js"`

Конфиг webpack.dev.js:  
```
const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: {
        main: path.resolve(__dirname, '../src/index.js'),
    },
    devtool: 'inline-source-map',
    devServer: {
        static: {
            directory: path.resolve(__dirname, "../dist"),
            // directory: "../dist",
        },
        // historyApiFallback: true,
        hot: true,
        port: 8080,
        open: true,
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
                    'css-loader',
                ], 
            },
            {
                test: /\.pug$/,
                loader: 'pug-loader',
                options: {pretty: true}
            }
        ]
    }
  };
```

### Минификация файлов для mode: 'production'
По умолчанию в production mode вебпак минифицирует код. Для этого используется TerserPlugin.  
CSS код тоже стоит минифицировать. Для этого можно использовать плагин css-minimizer-webpack-plugin.
Его надо будет указать в optimization.minimizer. Настройка optimization.minimizer отменяет все значения 
по умолчанию, поэтому если определили плагин для минификации CSS, нужно указать, какой плагин будет отвечать 
за минификацию JS.  
Ставим `npm i terser-webpack-plugin  --save-dev`  
Ставим `npm i css-minimizer-webpack-plugin --save-dev`  
Прописываем константы:  
`const TerserWebpackPlugin = require('terser-webpack-plugin');`  
`const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");`  
Прописываем их в plugins:  
`new CssMinimizerPlugin(),`  
`new TerserWebpackPlugin(),`  
И добавим в module.exports модуль:
```
optimization: {
    minimize: true,
    minimizer: [new CssMinimizerPlugin({}) , new TerserWebpackPlugin({})],
},
```

### Установка json-server
Установим: `npm i -g json-server`   
Создаем в корне файл database.json  
Добавляем в него нужные объекты и свойства (пример):
```
{
  "posts": [
    { "id": 1, "title": "json-server", "author": "typicode" }
  ],
  "comments": [
    { "id": 1, "body": "some comment", "postId": 1 }
  ],
  "profile": { "name": "typicode" }
}
```
Запустим наш сервер: `json-server --watch database.json`  

Если будет ошибка безопасности, нужно разрешить в Windows выполнение скриптов PowerShell:  
Для этого открываем консоль PowerShell от имени администратора  
Проверка: `Get-ExecutionPolicy` // ответ Restricted (Запрещено)  
Отменяем: `Set-ExecutionPolicy unrestricted`  
Проверка: `Get-ExecutionPolicy` // ответ Unrestricted (Разрешено)  
Запретить: `Set-ExecutionPolicy Restricted`  
Затем в настройках Windows 11 Конфиденциальность и защита - Для разработчиков - PowerShell применить флажок, 
разрешающий выполнение сценариев

### Установка линтера
Установим: `npm i eslint --save-dev`  
Установим файл конфигурации: `npx eslint --init`  
После запустить линтер для любого файла из каталога следующим образом: `npx eslint yourfile.js`  
Добавим автозапуск линтера при сборке проекта,  
установим `npm i eslint-loader --save-dev`  
Добавим правило:
```
{
    test: /\.js$/,
    exclude: './node_modules',
    use: 'eslint-loader',
}
```
### А теперь CSS lint!
Установим: `npm i stylelint stylelint-webpack-plugin --save-dev`  
Установим: `npm i stylelint --save-dev`  
Константа: `const StylelintPlugin = require('stylelint-webpack-plugin');`  
В плагины: `new StylelintPlugin(options)`  

Установим: `npm i stylelint-config-standard`  
Файл в корень: .stylelintrc   
`{
 "extends": "stylelint-config-standard"
}`  
Исключить папку - файл в корень .eslintignore `/node_modules`  

Готово!   

### Настраиваем git-хуки
Установим: `npm i husky --save-dev`  
Добавим необходимые компоненты: `npm set-script prepare "husky install"`  
Запустим компонент: `npm run prepare`  
Для запуска линта добавим строку в paskade.json: `"lint": "eslint src/*.js & stylelint src/*.css"`  
Добавляем хук: `npx husky add .husky/pre-commit "npm run lint"`  




Восстановить модули: `npm install`  
Запустить сборку: `npx webpack`  
Запустить сборку кастомной командой (прописанной в packade.json) `npm run build`  
Запустить непрерывную сборку: `npx webpack --watch`  
Запуск сервера с конфигом из корня: `npx webpack-dev-server`  
Запуск сервера с конфигом dev командой из packade.json: `npm run start:dev_server`  
Запуск сборки с конфигом prod командой из packade.json: `npm run start:prod`  
Запуск сборки с конфигом dev командой из packade.json: `npm run start:dev`  
Запуск линтеров eslint и stylelint: `npm run lint`  





[//]: # (# Text // как <h1> ### Text // как <h3>)
[//]: # (Два пробела в конце строки - перенос строки)
[//]: # (1. 2. 3. // авт. создают нумерованный список)
[//]: # (**Text** // <b>)
[//]: # (`Text` // Выделить жетым как одну строку кода)
[//]: # (```Text``` // <code> - блок кода)
[//]: # (https://github.com/sandino/Markdown-Cheatsheet.git)
