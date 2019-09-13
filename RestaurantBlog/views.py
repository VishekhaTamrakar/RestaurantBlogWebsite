from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

now = timezone.now()
def home(request):
   return render(request, 'RestaurantBlog/home.html',
                 {'RestaurantBlog': home})

@login_required
def restaurant_list(request):
    restaurant = Restaurant.objects.filter(created_date__lte=timezone.now())
    return render(request, 'RestaurantBlog/restaurant_list.html',
                 {'restaurants': restaurant})
@login_required
def restaurant_edit(request, pk):
   restaurant = get_object_or_404(Restaurant, pk=pk)
   if request.method == "POST":
       # update
       form = RestaurantForm(request.POST, instance=restaurant)
       if form.is_valid():
           restaurant = form.save(commit=False)
           restaurant.updated_date = timezone.now()
           restaurant.save()
           restaurant = Restaurant.objects.filter(created_date__lte=timezone.now())
           return render(request, 'RestaurantBlog/restaurant_list.html',
                         {'restaurants': restaurant})
   else:
        # edit
       form = RestaurantForm(instance=restaurant)
   return render(request, 'RestaurantBlog/restaurant_edit.html', {'form': form})

@login_required
def restaurant_delete(request, pk):
   restaurant = get_object_or_404(Restaurant, pk=pk)
   restaurant.delete()
   return redirect('RestaurantBlog:restaurant_list')


@login_required
def restaurant_new(request):
   if request.method == "POST":
       form = RestaurantForm(request.POST)
       if form.is_valid():
           newrestaurant = form.save(commit=False)
           newrestaurant.created_date = timezone.now()
           newrestaurant.save()
           restaurant = Restaurant.objects.filter(created_date__lte=timezone.now())
           return render(request, 'RestaurantBlog/restaurant_list.html',
                         {'restaurants': restaurant})
   else:
       form = RestaurantForm()
       # print("Else")
   return render(request, 'RestaurantBlog/restaurant_new.html', {'form': form})


@login_required
def dish_new(request):
   if request.method == "POST":
       form = DishForm(request.POST)
       if form.is_valid():
           dish = form.save(commit=False)
           dish.created_date = timezone.now()
           dish.save()
           dish = Dish.objects.filter(created_date__lte=timezone.now())
           return render(request, 'RestaurantBlog/dish_list.html',
                         {'dishes': dish})
   else:
       form = DishForm()
       # print("Else")
   return render(request, 'RestaurantBlog/dish_new.html', {'form': form})


@login_required
def dish_list(request):
   dish = Dish.objects.filter(created_date__lte=timezone.now())
   return render(request, 'RestaurantBlog/dish_list.html', {'dishes': dish})

@login_required
def dish_edit(request, pk):
   dish = get_object_or_404(Dish, pk=pk)
   if request.method == "POST":
       # update
       form = DishForm(request.POST, instance=dish)
       if form.is_valid():
           dishedit = form.save(commit=False)
           dishedit.updated_date = timezone.now()
           dishedit.save()
           dish= Dish.objects.filter(created_date__lte=timezone.now())
           return render(request, 'RestaurantBlog/dish_list.html',
                         {'dishes': dish})
   else:
        # edit
       form = DishForm(instance=dish)
   return render(request, 'RestaurantBlog/dish_edit.html', {'form': form})


@login_required
def dish_delete(request, pk):
   dish = get_object_or_404(Dish, pk=pk)
   dish.delete()
   return redirect('RestaurantBlog:dish_list')

@login_required
def review_list(request):
    review = Review.objects.filter(created_date__lte=timezone.now())
    return render(request, 'RestaurantBlog/review_list.html',
                 {'reviews': review})

@login_required
def review_edit(request, pk):
   review = get_object_or_404(Review, pk=pk)
   if request.method == "POST":
       # update
       form = ReviewForm(request.POST, instance=review)
       if form.is_valid():
           reviewedit = form.save(commit=False)
           reviewedit.updated_date = timezone.now()
           reviewedit.save()
           review= Review.objects.filter(created_date__lte=timezone.now())
           return render(request, 'RestaurantBlog/review_list.html',
                         {'reviews': review})
   else:
        # edit
       form = ReviewForm(instance=review)
   return render(request, 'RestaurantBlog/review_edit.html', {'form': form})

@login_required
def review_new(request):
   if request.method == "POST":
       form = ReviewForm(request.POST)
       if form.is_valid():
           reviewnew = form.save(commit=False)
           reviewnew.created_date = timezone.now()
           reviewnew.save()
           review = Review.objects.filter(created_date__lte=timezone.now())
           return render(request, 'RestaurantBlog/review_list.html',
                         {'reviews': review})
   else:
       form = ReviewForm()
       # print("Else")
   return render(request, 'RestaurantBlog/review_new.html', {'form': form})


@login_required
def review_delete(request, pk):
   review = get_object_or_404(Review, pk=pk)
   review.delete()
   return redirect('RestaurantBlog:review_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('RestaurantBlog:home')
    else:
        form = UserCreationForm()
    return render(request, 'RestaurantBlog/signup.html', {'form': form})

