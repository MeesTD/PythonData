# PythonData
Samenwerk repo van Navisa, Rhea &amp; Mees voor de Python Data backend

## What is pipenv?

Pipenv is a Python virtualenv management tool that supports a multitude of systems and nicely bridges the gaps between pip, python (using system python, pyenv or asdf) and virtualenv. Linux, macOS, and Windows are all first-class citizens in pipenv.

Pipenv automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates a project Pipfile.lock, which is used to produce deterministic builds.

Pipenv is primarily meant to provide users and developers of applications with an easy method to arrive at a consistent working project environment.

### Make sure you have python and pip
Before you go any further, make sure you have Python and that it’s available from your command line. You can check this by simply running

    $ python --version
You should get some output like 3.10.8. If you do not have Python, please install the latest 3.x version from python.org

### Additionally, make sure you have pip available. Check this by running

    $ pip --version
    pip 22.3.1
If you installed Python from source, with an installer from python.org or via Homebrew, you likely already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip manually.

### Installing Pipenv
Preferred Installation of Pipenv
It is recommended that users on most platforms install pipenv from pypi.org using

    $ pip install pipenv --user

## Example Pipenv Workflow
Clone / create project repository:

    $ cd myproject
Install from Pipfile, if there is one:

    $ pipenv install
Or, add a package to your new project:

    $ pipenv install <package>
This will create a Pipfile if one doesn’t exist. If one does exist, it will automatically be edited with the new package you provided.

Next, activate the Pipenv shell:

    $ pipenv shell
    $ python --version
This will spawn a new shell subprocess, which can be deactivated by using exit.

## windowsgebruik.py (WINDOWS)
    def krijgpoort():
        return 3306

    def krijgwachtwoord():
        return ''

## windowsgebruik.py (MAC)
    def krijgpoort():
        return 8889

    def krijgwachtwoord():
        return 'root'
