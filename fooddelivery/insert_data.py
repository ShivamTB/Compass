from fooddelivery.models import Restaurants, MenuItems

def create_initial_data():
    restaurant1 = Restaurants.objects.create(name='McDonalds')
    restaurant2 = Restaurants.objects.create(name='Pizza Hut')
    restaurant3 = Restaurants.objects.create(name='Starbucks')
    restaurant4 = Restaurants.objects.create(name='PF Changs')
    restaurant5 = Restaurants.objects.create(name='KFC')

    MenuItems.objects.create(restaurant=restaurant1, name='McChicken', price=25.00)
    MenuItems.objects.create(restaurant=restaurant1, name='McVeggie', price=25.00)
    MenuItems.objects.create(restaurant=restaurant2, name='Veg Pizza', price=30.00)
    MenuItems.objects.create(restaurant=restaurant2, name='Chicken Pizza', price=15.00)
    MenuItems.objects.create(restaurant=restaurant3, name='Capuccino', price=24.99)
    MenuItems.objects.create(restaurant=restaurant3, name='Chai Latte', price=8.99)
    MenuItems.objects.create(restaurant=restaurant4, name='Noodles', price=6.99)
    MenuItems.objects.create(restaurant=restaurant4, name='Soup', price=4.99)
    MenuItems.objects.create(restaurant=restaurant5, name='Chicken Wings', price=29.99)
    MenuItems.objects.create(restaurant=restaurant5, name='Family Meal', price=14.99)

create_initial_data()