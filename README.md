# Final task of sprint 18 - infra_sp2
This task is an example of using infrastructure in containers. The base project is api_yamdb. It provides REST API for social network YaTube. API description is  placed in redoc.

![example workflow name](https://github.com/valkhmyrov/yamdb_final/workflows/yamdb_final/badge.svg)

## Getting Started for manual installation
### Prerequisites
Needed software:
* [Docker](https://docs.docker.com/engine/install/) - How to install docker
* [Docker Compose](https://docs.docker.com/compose/install/) - How to install docker compose
### Installing
1. Get project
```
git clone https://github.com/valkhmyrov/yamdb_final.git
```
2. Rename .env.example and change necessary variables. Change password strongly recommended!
3. Built and start project
```
sudo docker-compose up
```
4. Make migrations after container was built and started.
```
sudo docker-compose exec -T web sh -c "python manage.py migrate"
```
6. Collect static.
```
sudo docker-compose exec -T web sh -c "python manage.py collectstatic --noinput"
```
5. Create superuser. Execute command in web container, then exit.
```
python manage.py createsuperuser
```

## Getting Started for continuous integration
### Prerequisites
Needed software:
* [Ubuntu](https://ubuntu.com/) - server with Ubuntu Linux

Needed secrets:
- HOST - FQDN/IP of host
- USER - login of user to access to host. User must have sudo permissions.
- SSH_KEY - ssh key to host
- PASSPHRASE - ssh passphrase to key
- DOCKER_USERNAME - login to [hub.docker.com](https://hub.docker.com/), to put builded image
- DOCKER_PASSWORD - password to [hub.docker.com](https://hub.docker.com/)
- TELEGRAM_TO - ID of telegramm account, which will receive notification
- TELEGRAM_TOKEN - token of telegramm bot, whom will send notifications

This variables will be putted to .env
- POSTGRES_USER - login to bd
- POSTGRES_PASSWORD - password for db
- DB_NAME - db name
- DJANGO_ADMIN - login of django superuser
- DJANGO_PASS - password of django superuser
- DJANGO_EMAIL - email of superuser

## Show example
redoc [valkhmyrov.cf](http://valkhmyrov.cf/redoc)

## Built With
* [Django 3.0.5](https://www.djangoproject.com/)
* [Django Rest Framework 3.11.0](https://www.django-rest-framework.org/)
* [djangorestframework-simplejwt 4.4.0](https://pypi.org/project/djangorestframework-simplejwt/)
* [Gunicorn 20.0.4](https://gunicorn.org/)
* [PostgreSQL 13.1](https://www.postgresql.org/)
## Authors
1. * [valkhmyrov](https://github.com/valkhmyrov) - Workflow and API provides: Create users, Authentication of Users by token, User's Roles. 
2. * [s4ltyk0v](https://github.com/s4ltyk0v) - API provides: Title, Genre, Review, Category, Comments
3. * [Fyodor-Mityanin](https://github.com/Fyodor-Mityanin) - API provides: Title, Genre, Review, Category, Comments
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
