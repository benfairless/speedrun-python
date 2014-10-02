speedrun-python
=================================

A bare-bones Python environment, ready for the immediate development of Python web applications.
This is an attempt to create an easy-to-use and easy-to-deploy Python application using the principles set out in the [12 Factor App](http://12factor.net/) manifesto.

Getting up and running takes less than ten minutes!

## TL;DR

Right, cutting straight to the good stuff:

You can have a Python application up-and-running on your desktop inside a Linux guest with one line (providing you have Vagrant installed):
```sh
vagrant up ; vagrant ssh
```
Once you see a line saying something along the lines of `01:22:52 app.1  | INFO:werkzeug: * Running on http://0.0.0.0:5000/` the process is complete.
You can now simply go to http://localhost:8080 to visit your application.

**Note: whilst it may take a while to do the initial set up, it only takes around 3 minutes to start up the guest on subsequent builds**

While that is booting up, why not look through the rest of the documentation?


## Requirements

* Vagrant >= 1.5.2
* Virtualbox


## Usage

Getting up and running in development is extremely easy and requires only five steps:
* Modify the `requirements.txt` file to automatically install dependencies using [PIP](https://pip.readthedocs.org/en/latest/user_guide.html#requirements-files)
* Modify the `Procfile` file to automatically start your application using [Foreman](http://ddollar.github.io/foreman/#PROCFILE)
* Modify the `run.py` to start your application in debug mode using the Python console
* Edit the `development.env` file to set environment-specific variables such as network ports for your application, database locations etc.
* Write some code!

To make things even simpler, a sample application using the [Flask micro-framework](http://flask.pocoo.org/) is already set-up for you!

### Running in Vagrant

To launch your application simply execute the commands below:

1. `$ vagrant up` - Creates and sets up your virtual machine
2. `$ vagrant ssh` - Allows you to connect into the virtual machine via SSH
3. `$ app-start` - Starts your application in development mode


## APP-START Command

`app-start` is a very simple script designed to launch applications.
By default it will load the environmental variables in `development.env` and then start your application in one of two modes.
To stop the application simply press Ctrl-C (or whatever you use for `SIGINT`) and you will be returned to the shell.

### Development mode (default)

In development mode, the script will execute the `run.py` script in the Python interpreter.
Both `STDOUT` and `STDERR` will be output to the console. as well as being available in the `logs` directory with the format `development_YYYY-MM-DD.log`.

You can launch your application in this mode by running:
```sh
$ app-start
```

### Server mode

Server mode represents how your application will look when deployed into a production environment.
Instead of seeing output from the Python interpreter, you will see only the `STDOUT` of the services in your `Procfile`.
In the flask example that is included, we see the logs written to the Gunicorn WSGI web server by our application.
This output is also available in the `logs` directory with the format `production_YYYY-MM-DD.log`.

You can launch your application in this mode by running:
```sh
$ app-start server
```

There are many other reasons why running in this mode is useful. In the example project we run some basic tests using

### Arguments
```
app-server [ OPTIONS ] ROLE
     ROLE := { server | development }
  OPTIONS := { -e[nv file] filename | -p[rocfile] filename }
```

## Deploying to Production

To deploy the application into production is relatively simple. If you want to use the PaaS solution Heroku, the Procfile itself is enough.
If you want to put it on something a little more serious, Foreman can easily convert Procfiles into [service scripts](http://ddollar.github.io/foreman/#EXPORT-FORMATS) for use in production systems on a variety of platforms.

This can be as easy as running `# foreman export --log /var/log/app/out.log upstart /etc/init/app` and then starting the application using `# service app start`. Easy peasy!

*It's worth noting here that it's not quite as easy as this if you want to run inside a Python virtualenv.*


## Notes

Most of the system tools you need are provided straight out-of-the-box courtesy of Land Registry's [infrastructure-puppet-devkit](https://github.com/LandRegistry/infrastructure-puppet-devkit).
It's recommended you visit the project page to see what tools are pre-installed.

This environment uses a standardised Land Registry-approved Ubuntu 14.04 LTS template built using [infrastructure-packer-ubuntu](https://github.com/LandRegistry/infrastructure-packer-ubuntu).
Updates to this template are automatically pushed into your Vagrant environment when they become available.
