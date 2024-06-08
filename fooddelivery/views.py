from django.shortcuts import render
from fooddelivery.models import Restaurants, Orders, MenuItems
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.

def get_restaurants(request):
    name = request.GET.get('name', None)
    cuisine = request.GET.get('cuisine', None)
    filter = {}
    if name:
        filter['name__icontains'] = name
    if cuisine:
        filter['cuisine__icontains'] = cuisine
    
    restaurants = list(Restaurants.objects.filter(**filter).values('id', 'name', 'cuisine', 'image'))
    return JsonResponse({'restaurants': restaurants}, status=200)


def get_filter_values(request):
    filter_name = request.GET.get('filter_name')
    name = request.GET.get('name', None)
    cuisine = request.GET.get('cuisine', None)
    filter = {}
    if name and filter_name != 'name':
        filter['name__icontains'] = name
    if cuisine and filter_name != 'cuisine':
        filter['cuisine__icontains'] = cuisine
    
    vals = list(Restaurants.objects.filter(**filter).distinct().values(filter_name))
    return JsonResponse({'values': vals}, status=200)


def get_menu_items(request):
    restaurant = request.GET.get('restaurant_id')
    restaurant = Restaurants.objects.get(id=restaurant)
    menu_items = list(MenuItems.objects.filter(restaurant=restaurant).values('id', 'name', 'price', 'image', 'description'))
    return JsonResponse({'items': menu_items}, status=200)


def create_order(request):
    menu_item_id = request.POST.get('menu_item_id')
    quantity = request.POST.get('quantity')
    seat = request.POST.get('seat')
    menu_item = MenuItems.objects.get(id=menu_item_id)
    Orders.objects.create(user=User.objects.all().last(),
                          menu_item=menu_item,
                          quantity=quantity,
                          seat=seat)
    return JsonResponse({'message': 'Order Created Succefully!'}, status=200)