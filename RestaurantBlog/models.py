from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.restaurant_name)

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to="RestaurantBlog", blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True,on_delete=models.CASCADE, related_name='dishes')
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    dish=models.ForeignKey(Dish,null=True,on_delete=models.CASCADE,related_name='review1')
    restaurant=models.ForeignKey(Restaurant,null=True,on_delete=models.CASCADE,related_name='review2')
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)