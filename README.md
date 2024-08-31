Educational Python project for creating the "Bike Shop" using Django python framework.

To start the web applcation:

```Shell
python3 manage.py makemigrations &&  python3 manage.py migrate &&  python3 manage.py runserver
```

And open:

```http://127.0.0.1:8000/```

For admin panel and to manage inventory and orders, open:

```http://127.0.0.1:8000/admin```

To create admin user:

```Shell
python3 manage.py shell
```

```python
from django.contrib.auth.models import User
User.objects.create_superuser(
   username='admin', email='admin@example.com', password='12345'
)
exit()
```
