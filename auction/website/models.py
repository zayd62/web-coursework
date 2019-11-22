from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Auction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField()
    auctionCloseTimestamp = models.DateTimeField(null=True, blank=True)
    auctionOpen = models.BooleanField(default=True)
    winningBid = models.OneToOneField(
        to='Bid', on_delete=models.CASCADE, blank=True, null=True, related_name='winningBid')
    
    def __str__(self):
        return self.title


class Bid(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=4)
    userid = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True, unique=False)
    auctionid = models.ForeignKey(
        to='Auction', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.userid.user.username + " - " + str(self.amount)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
