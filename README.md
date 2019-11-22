# web-coursework

superuser details
1. username: zayd
2. password: zayd
3. email address: zayd62@gmail.com

the following command is to be run in the same directory as `manage.py`

the code
- deletes the database and migrations
- migrates the database
- create a superuser login to use at the url 127.0.0.1:8000/admin

clear; rm db.sqlite3; rm -r website/migrations/; python manage.py migrate; python manage.py makemigrations website; python manage.py migrate; python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('zayd', 'zayd62@gmail.com', 'zayd')"; python manage.py runserver

