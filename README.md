## Lead Manager React App

This is the backend for the app. The backend is developed in Django, an runs as a stand alone backend.

### Configurations

For the configuration was created a virtual environment using `pipenv`. For this we need to install `pipenv`. We also have to install Django, the `djangorestframework` library and `django-rest-knox` to manage authentications, we do this inside the virtual env.

`pip install pipenv`

`pipenv install django djangorestframework django-rest-knox`

Then, we have to start a Project (which is not the same as an application). A project in Django means to create the Django main environment, the configuration folder. Then, we create the app. The app contains the views and the URLs.

`django-admin startproject leadmanager`

`python manage.py startapp leads`

After created the models, in the `models.py` file, we have to migrate to the database. We can use the command `python manage.py makemigrations leads` to migrate the models to the database.

### Frontend

For the frontend, first create a new app in django `python manage.py startapp frontend`, then create the folders for React to live on:

- src/components
- static/frontend
- templates/frontend

Navigate to the root, and run `npm init -y` to start an npm environment and create the package.json file. Then we need to install webpack and webpack-cli `npm install -D webpack webpack-cli`.

Then we need to add Babel.
`npm install -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties `

and finally react and react router
`npm install react react-router-dom`

we also need to change the scripts in the `package.json` file

```
  "scripts": {
    "dev": "webpack --mode development ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js",
    "build": "webpack --mode production ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js"
  },
```

and create the `webpack.conf.js` file.

```
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
};

```

and the `.babelrc` file

```
{
    "presets": ["@babel/preset-env", "@babel/preset-react"],
    "plugins": ["transform-class-properties"]
}
```
