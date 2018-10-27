
# nQueens

## Dependencies
+ Git
+ Docker version 18.03.1-ce
+ Docker-compose version 1.21.2

## Install instructions

Install Docker (https://docs.docker.com/install/#server)

Install Docker-compose (https://docs.docker.com/compose/install/#prerequisites)

## Download && Build the application containers

Clone repository.

Build containers (assuming your docker is installed as root):

```bash
cd CLONE_DIRECTORY
sudo docker-compose build

```

## Run the application for the first time

Run the following command:

```bash
sudo docker-compose up -d

```


Open postgresql
```bash
sudo docker-compose exec --user postgres appdb bash
psql

```

Change the password of postgres user and create database
```SQL
ALTER USER postgres WITH PASSWORD 'db_pass';
CREATE DATABASE nqueens;
\q
exit

```

After this, whenever you want to run the application just execute from the root directory.
```bash
sudo docker-compose up -d

```


## Creating local settings file
Create a new file called *local_settings.py* in nQueens/src/ and copy the information from the *local_settings_template.py* file into it.

Change the information corresponding to your local machine.

## Run Python App
Type the following command

```bash
sudo docker-compose exec web bash
python nQueens.py

```

Or you can just type

```bash
sudo docker-compose exec web bash -c 'python nQueens.py'

```

## Run Tests
```bash
sudo docker-compose exec web bash
python -m pytest tests.py

```
Or you can just type

```bash
sudo docker-compose exec web bash -c 'python -m pytest tests.py'

```
