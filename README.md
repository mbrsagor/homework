# homework
> Simple django rest API base project which the API will support `web`, `desktop`, `mobile` etc devices.

### Dependancy
- Python 3.8.5
- Django 3.1.5
- Postgres 12.3


#### Install the poject in your local development environment.
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
