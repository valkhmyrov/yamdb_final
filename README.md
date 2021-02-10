# Final task of sprint 18 - infra_sp2
This task is an example of using infrastructure in containers. The base project is api_yamdb. It provides REST API for social network YaTube. API description is  placed in redoc.
## Getting Started
### Prerequisites
Needed software:
* [Docker](https://docs.docker.com/engine/install/) - How to install docker
* [Docker Compose](https://docs.docker.com/compose/install/) - How to install docker compose
### Installing
1. Get project
```
git clone https://github.com/valkhmyrov/infra_sp2.git
```
2. Change password for database in .env file
3. Built and start project
```
docker-compose up
```
4. Make migrations after container was built and started. First enter to web container then make migration:
```
docker exec -it infra_sp2_web_1 bash
python manage.py migrate
```
5. Create superuser. Execute command in web container, then exit.
```
python manage.py createsuperuser
```
6. Load fixtures for example if needed. Run in host system.
```
cat fixtures.json | docker exec -i infra_sp2_web_1 python manage.py loaddata --format=json -
```
## Built With
* [Django 3.0.5](https://www.djangoproject.com/)
* [Django Rest Framework 3.11.0](https://www.django-rest-framework.org/)
* [djangorestframework-simplejwt 4.4.0](https://pypi.org/project/djangorestframework-simplejwt/)
* [Gunicorn 20.0.4](https://gunicorn.org/)
* [PostgreSQL 13.1](https://www.postgresql.org/)
## Authors
1. * [valkhmyrov](https://github.com/valkhmyrov) - API provides: Create users, Authentication of Users by token, User's Roles 
2. * [s4ltyk0v](https://github.com/s4ltyk0v) - API provides: Title, Genre, Review, Category, Comments
3. * [Fyodor-Mityanin](https://github.com/Fyodor-Mityanin) - API provides: Title, Genre, Review, Category, Comments
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
