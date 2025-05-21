# [Bike Shop Django](https://bike-shop-django.onrender.com/)

Educational Python project for creating the "Bike Shop" using Django python framework.

SQLite database is used for data storage.

# Deployed using render: [Check it out](https://bike-shop-django.onrender.com/)

# [Admin panel](https://bike-shop-django.onrender.com/admin)

```username:admin password:12345```

To start the web applcation locally using Docker:

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
