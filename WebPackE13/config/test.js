    mode: 'production',
    // mode: 'development',
    // mode: 'none',
    devtool: 'inline-source-map',
    // entry: './src/index.js',
    entry: {
        main: path.resolve(__dirname, './src/index.js'),
    },
    // output: {
    //     filename: 'main.js'
    // },
    output: {
        path: path.resolve(__dirname, './dist'),
        filename: 'main.js',
    },