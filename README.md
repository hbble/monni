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

5. Setup database. I'm using [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads). You need to set permissions to database in `settings.py` line `[84]`.

    If you want to use other than PostgreSQL database you also need you change `ENGINE` value in `settings.py`.
    
6. `cd` to project directory (`manage.py` have to be in there) then install project models into database:
    ```
    python manage.py makemigrations main
    python manage.py migrate
    ```
7. To start project run:
    ```
    python manage.py runserver
    ```

8. Visit `http://127.0.0.1:8000`
