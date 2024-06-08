# menu items description
update fooddelivery_menuitems set description='A crispy chicken patty sandwich with lettuce and mayo.' where id=1;
update fooddelivery_menuitems set description='A vegetarian burger with a flavorful veggie patty and fresh toppings.' where id=2;
update fooddelivery_menuitems set description='A pizza topped with a variety of fresh vegetables and cheese.' where id=3;
update fooddelivery_menuitems set description='A pizza topped with tender chicken pieces and cheese.' where id=4;
update fooddelivery_menuitems set description='A rich and frothy coffee drink made with espresso and steamed milk.' where id=5;
update fooddelivery_menuitems set description='A spiced tea drink with steamed milk and a hint of sweetness.' where id=6;
update fooddelivery_menuitems set description='Savory noodles served in a flavorful broth or sauce.' where id=7;
update fooddelivery_menuitems set description='A warm and comforting bowl of broth with vegetables and/or meat.' where id=8;
update fooddelivery_menuitems set description='Juicy chicken wings coated in a savory or spicy sauce.i' where id=9;
update fooddelivery_menuitems set description='A hearty meal portioned for a family, typically including multiple dishes.' where id=10;

# restaurants description
update fooddelivery_restaurants set description='A global fast-food chain known for its burgers, fries, and Happy Meals.' where id=1;
update fooddelivery_restaurants set description='A popular pizza restaurant offering a variety of pizzas, pasta, and sides.' where id=2;
update fooddelivery_restaurants set description='A renowned coffeehouse chain famous for its specialty coffee drinks and pastries.' where id=3;
update fooddelivery_restaurants set description='A casual dining restaurant offering a variety of Asian-inspired dishes and a unique dining experience.' where id=4;
update fooddelivery_restaurants set description='A fast-food chain specializing in fried chicken, with a range of sides and meals.' where id=5;

# restaurant images
update fooddelivery_restaurants set image='static/images/mcdonalds.jpg' where id=1;
update fooddelivery_restaurants set image='static/images/pizzahut.jpg' where id=2;
update fooddelivery_restaurants set image='static/images/starbucks.jpg' where id=3;
update fooddelivery_restaurants set image='static/images/pfchangs.jpg' where id=4;
update fooddelivery_restaurants set image='static/images/kfc.jpg' where id=5;
