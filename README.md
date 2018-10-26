# nQueens

### Setup database

Change the password of postgres user

```SQL
ALTER USER postgres WITH PASSWORD 'new_password';

```

Creating database

```SQL
CREATE DATABASE nqueens;

```

### Creating local settings file
Create a new file called *local_settings.py* in /your_path/nQueens and copy the information from the *local_settings_template.py* file into it.

Change the information corresponding to your local machine.


### Virtual Enviroment

First, you need to create and activate a virtualenv
```bash
$ virtualenv env
$ source env/bin/activate

```

Then, install requirements files (virtual env must be activated)

```bash
(env)$ pip install -r requirements.txt

```


## Run Program
```bash
(env)$ python nQueens.py

```


## Run Tests
```bash
(env)$ python -m pytest tests.py

```