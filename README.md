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

`clear; rm db.sqlite3; rm -r website/migrations/; python manage.py migrate; python manage.py makemigrations website; python manage.py migrate; python manage.py shell < createSuperUser.py; python manage.py runserver`

<!-- ```python
from django.contrib.auth.models import User
from website import models
import datetime

user = User()
user.username = 'zayd'
user.set_password('zayd)
user.email = 'zayd@test.com'
user.is_staff = True
user.is_admin = True

profile = models.Profile()
profile.birth_date = datetime.date.fromisoformat(str("1997-09-23"))
profile.user = user

user.save()
profile.save()
``` -->
## 24-11-19

login, signup and logout is working. just need to run `python manage.py runserver`. the following user is already created 

normal user details
1. username: bobo
2. password: bobobobo123
3. email address: bobo@gmail.com
4. date of birth: 23/11/2005

TODO: make the web pages. ideally the design and the layout 
