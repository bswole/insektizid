const path = require('path');

module.exports = {
    entry: './front-end/index.js',
    output: {
        filename: 'index-bundle.js',
        path: path.resolve(__dirname, './static/'),
    },

    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                options: { presets: ["@babel/preset-env", "@babel/preset-react"]}
            },
            {
                test: /\.s[ac]ss$/,
                use: [
                    {loader: "style-loader",},
                    {loader: "css-loader",},
                    {
                        loader: "postcss-loader",
                        options: {
                            postcssOptions: {
                                plugins: function () {
                                    return [
                                        require('precss'),
                                        require('autoprefixer')
                                    ];
                                }
                            }
                        }
                    },
                    {loader: "sass-loader",}
                ],
            },
            {
                test: /\.css$/,
                use: [
                    {loader: 'style-loader',},
                    {loader: 'css-loader',}
                ]
            }
        ]
    }
};