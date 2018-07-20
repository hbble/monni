# monni
Money management web-service.

## Installation (Locally)
1. Make sure you have installed [Python 3](https://www.python.org/downloads/) on your machine.

2. Clone repository `git clone https://github.com/hbble/monni.git`.

3. Install [virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b#how-to-install-virtualenv) and create virtual environment (don't forget to activate it).

4. Install dependencies:
    ```
    pip install -r requirements/base.txt
    ```
5. Rename file [_config.py](monni/_config.py) to `config.py`.

6. [Generate](https://www.miniwebtool.com/django-secret-key-generator/) and paste `SECRET_KEY` to your `config.py` file.

7. Setup database. I'm using [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads). You need to create new database and user (granted with permissions to edit) and set listed permissions to database in `config.py` file.

    If you want to use other than PostgreSQL database you also need you change `ENGINE` value in `settings.py`.
    
8. `cd` to project directory (`manage.py` have to be in there) then install project models into database:
    ```
    python manage.py makemigrations main
    python manage.py migrate
    ```

9. Create project superuser:
    ```
    python manage.py createsuperuser
    ```
    Now you can start project:
    ```
    python manage.py runserver
    ```

10. Visit `http://127.0.0.1:8000/admin` and and login using created user. Add some Expense and Income categories so project can work properly.


