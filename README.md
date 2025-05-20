Educational Python project for creating the "Bike Shop" using Django python framework.

SQLite database is used for data storage.

To start the web applcation using docker:

```Shell
docker build -t bikeshop .
```

```Shell
docker run --name bikeshop -p 8000:8000 bikeshop
```

And open:

```http://127.0.0.1:8000/```

For admin panel and to manage inventory and orders, open:

```http://127.0.0.1:8000/admin```

To create admin user:

```Shell
docker exec -it bikeshop python manage.py createsuperuser
```

Packaged application already has admin/12345 user/password.
