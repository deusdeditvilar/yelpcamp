from django.db import models
from account.models import User
from django.utils import timezone
import math

# Create your models here.

class Campground(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    price = models.CharField(max_length=4)
    image = models.CharField(max_length=300)
    description = models.CharField(max_length=400)
    user = models.ForeignKey(User,related_name='submitted_by',on_delete=models.PROTECT)
    address = models.CharField(max_length=100)

class Comment(models.Model):
    comment = models.CharField(max_length=300,blank=False,null=False)
    campground = models.ForeignKey(Campground, verbose_name=("Campground"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Created By", on_delete=models.PROTECT)
    created_at = models.DateTimeField("Created at", auto_now=True, auto_now_add=False)

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hr ago"

            else:
                return str(hours) + "hrs ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"