from django.contrib.auth.models import User
from website import models
import datetime


def createUsers(arr):
    from django.contrib.auth.models import User
    from website import models
    import datetime

    user = User()
    user.username = arr[0]
    user.set_password(arr[1])
    user.email = arr[2]

    profile = models.Profile()
    profile.birth_date = arr[3]
    profile.user = user

    try:
        user.save()
        profile.save()
    except Exception as identifier:
        pass


arr = [
    ['ashley', '93da4e5be2', 'ashley@test.com',
        datetime.date.fromisoformat(str("1995-11-25"))],
    ['mujib', 'fb0322f2c8', 'mujib@test.com',
        datetime.date.fromisoformat(str("2000-07-04"))],
    ['bob', '43af62ec6c', 'bob@test.com',
        datetime.date.fromisoformat(str("1985-02-25"))],
    # ['mary', 'password', 'mary@test.com',
    #     datetime.date.fromisoformat(str("1977-01-01"))],
]

for i in arr:
    print(i)
    createUsers(i)

"""
Let me explain my error. 
I have 4 users, ashley, mujib, bob and mary
ashley created an iphone auction
mujib bid 100 and 200
bob bid 250
bob won so `auctionOpen` is false and winning bid is equal to bobs bid object

login as bob, go to profile, it shows he won the iphone
login as mary, go to profile, it shows nothing won
login as mujib, go to profile, it give me an error 

"""