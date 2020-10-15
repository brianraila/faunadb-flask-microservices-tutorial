<img src="https://thumbs.dreamstime.com/b/creative-quirky-retro-illustration-style-cartoon-hip-flask-original-150955745.jpg"
     alt="Markdown Monster icon" height="100px" style="margin:auto;" />


# HipFlask Fauna

#### What is HipFlask?
 This is a Flask Web App Bootstrapping Template for use with FaunaDB.
 With default support for cloud native deployment to the following environments.

 - Docker
 - Vercel


#### Configuration
All default configuration used in this template can be found in the app.config.py file in the root of the app folder.


#### UI/Frontend
By default, this app template uses Bootstrap V4.
However, this can be changed to the frontend framework of your choice by adding its css file in the
app.static.js folder and update the app.templates.base.html file with the specified css file.


#### Email Configuration
Email support is available by default. This is thanks to the Flask-Mail package.
To enable this for your app, add the necessary configuration in the app.config file.
That is
`

    MAIL_SERVER : default ‘localhost’
    MAIL_PORT : default 25
    MAIL_USE_TLS : default False
    MAIL_USE_SSL : default False
    MAIL_DEBUG : default app.debug
    MAIL_USERNAME : default None
    MAIL_PASSWORD : default None
    MAIL_DEFAULT_SENDER : default None
    MAIL_MAX_EMAILS : default None
    MAIL_SUPPRESS_SEND : default app.testing
    MAIL_ASCII_ATTACHMENTS : default False

`

#### Vercel
This template has a vercel.json config file which makes it possible to instantly deploy your app to Vercel easily.

#### Docker
This template comes with a Dockerfile to give you ease of packaging, testing and even deploying your app. Safe to say it is native 😉. 
