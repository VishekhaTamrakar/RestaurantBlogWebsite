
from django import forms
from .models import Restaurant,Dish,Review

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('restaurant_name', 'address', 'email', 'city', 'state', 'zipcode', 'email','phone_number','user')

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('name','description','price','image','user','restaurant')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating','comment','user','dish','restaurant')