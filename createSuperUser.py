from django.contrib.auth.models import User
from website import models
import datetime

user = User()
user.username = 'zayd'
user.set_password('zayd')
user.email = 'zayd@test.com'
user.is_staff = True
user.is_admin = True
user.is_superuser = True


profile = models.Profile()
profile.birth_date = datetime.date.fromisoformat(str("1997-09-23"))
profile.user = user

user.save()
profile.save()
