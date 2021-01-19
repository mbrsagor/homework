# homework
> Simple django rest API base project which the API will support `web`, `desktop`, `mobile` etc devices.

### Installing Geospatial libraries
#### Dependancy
- Python 3.8.5
- Django 3.1.5
- Postgres 12.3

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed `Homework` backend `API` app on Windows, you should have little problem getting up and running.



### Create Database

Create the database by running the following commands in a psql shell. If you're using
Postgres.app, click the Postgres.app icon in your toolbar and select "Open psql".

```
create database "homework";
create user "macair";
ALTER ROLE "macair" WITH PASSWORD 'sagor123';
GRANT ALL PRIVILEGES ON DATABASE "homework" TO "macair";
ALTER USER macair CREATEDB;
CREATE EXTENSION postgis;
```


#### Run the poject in your local development environment.
```
git clone https://github.com/mbrsagor/homework.git
cd homework
virtualenv venv --python=python3.8
source venv/bin/activate
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

###### How to access/pass token in API test software like postman.
- 1st select header tab
- key => Authorization
- value => `Bearer` your-token
