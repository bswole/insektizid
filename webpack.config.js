const path = require('path');

module.exports = {
    mode: 'production',
    entry: './front-end/index.js',
    output: {
        path: path.resolve(__dirname, './insektizid/static/'),
        filename: 'bundle.js',
    },

    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                include: path.resolve(__dirname, 'front-end'),
                exclude: /node_modules/,
                loader: "babel-loader",
                options: { presets: ["@babel/preset-env", "@babel/preset-react"]}
            },
            // { //****** needed if using SASS
            //     test: /\.s[ac]ss$/,
            //     use: [
            //         {loader: "style-loader",},
            //         {loader: "css-loader",},
            //         {
            //             loader: "postcss-loader",
            //             options: {
            //                 postcssOptions: {
            //                     plugins: function () {
            //                         return [
            //                             require('precss'),
            //                             require('autoprefixer')
            //                         ];
            //                     }
            //                 }
            //             }
            //         },
            //         {loader: "sass-loader",}
            //     ],
            // },
            {
                test: /\.css$/i,
                include: path.resolve(__dirname, 'front-end'),
                use: [
                    {loader: 'style-loader',},
                    {loader: 'css-loader',},
                    {loader: 'postcss-loader',}
                ]
            }
        ]
    },

    resolve: {
        alias: {
            '@comp': path.resolve(__dirname, 'front-end/components/'),
            '@page': path.resolve(__dirname, 'front-end/pages/'),
            '@icon': path.resolve(__dirname, 'front-end/icons/'),
            '@img': path.resolve(__dirname, 'front-end/assets/img/')
        }
    },

    devServer: {
        static: 'dist',
        watchContentBase: true,
    },
};