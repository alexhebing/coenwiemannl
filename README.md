
## Install

Make sure you have python3 and virtualenv installed.
On Windows, launch an elevated command prompt ('run as administrator').
Create a virtualenv: `virtualenv .env`.
Activate it: `.env\Scripts\activate`.
Install: `pip install -r requirements.txt`. (comment out mysqlclient)

If the installation of mysqlclient fails (which it will on Windows :-), install the package from here 
https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient.
Note that the Python version is in the title of the files, e.g. 'mysqlclient‑1.4.6‑cp38‑cp38‑win_amd64.whl' is for 3.8.

## Start up

On Windows, launch an elevated command prompt ('run as administrator').
Launch the virtualenv, and start application:

```
.env\Scripts\activate
python manage.py runserver
```

## Update

Make sure you have `pip-tools` installed.

```
pip-compile --upgrade
```
