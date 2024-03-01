from django.db import models
from django.contrib.auth.models import User


class Tables(models.Model):
    number_of_table = models.IntegerField()
    is_reserved = models.BooleanField(default = False)
    
    def __str__(self):
        if self.is_reserved:
            return f"table {self.number_of_table} is reserved!"
        return f"table {self.number_of_table} is not reserved."


class Bills(models.Model):
    foods_and_drinks =  models.CharField(max_length=256)
    foods_and_drinks_cost = models.IntegerField()
    total_cost = models.IntegerField()
    tax = models.IntegerField()


class Pizzas(models.Model):
    PIZZA_CHOICE = (
        ('Pepperoni', 'P'),
        ('Margherita', 'M'),
    )
    type_of_pizza = models.CharField(choices = PIZZA_CHOICE, max_length=256)
    pizza_cost = models.IntegerField()

    def __str__(self):
        return self.type_of_pizza


class Burgers(models.Model):
    BURGER_CHOICE = (
        ('Cheeseburger', 'C'),
        ('Mashroomburger', 'M'),
    )
    type_of_burger = models.CharField(choices = BURGER_CHOICE, max_length=256)
    burger_cost = models.IntegerField()

    def __str__(self):
        return self.type_of_burger


class Pastas(models.Model):
    PASTA_CHOICE = (
        ('Special', 'S'),
        ('Parmijan', 'P'),
    )
    type_of_pasta = models.CharField(choices = PASTA_CHOICE, max_length=256)
    pasta_cost = models.IntegerField()

    def __str__(self):
        return self.type_of_pasta


class Fries(models.Model):
    FRIE_CHOICE = (
        ('Chickenstrips', 'C'),
        ('Friedonion', 'FO'),
    )
    type_of_frie = models.CharField(choices = FRIE_CHOICE, max_length=256)
    frie_cost = models.IntegerField()

    def __str__(self):
        return self.type_of_frie


class Appetizers(models.Model):
    APPETIZER_CHOICE = (
        ('Frechfries', 'F'),
        ('Slaw', 'S'),
    )
    type_of_appetizer = models.CharField(choices = APPETIZER_CHOICE, max_length=256)
    appetizer_cost = models.IntegerField()

    def __str__(self):
        return self.type_of_appetizer


class Drinks(models.Model):
    DRINK_CHOICE = (
        ('Coka', 'C'),
        ('Soda', 'S'),
    )
    type_of_drink = models.CharField(choices = DRINK_CHOICE, max_length=256)
    drink_cost = models.IntegerField()

    def __str__(self):
        return self.type_of_drink


class Foods(models.Model):
    list_of_pizzas = models.ForeignKey(Pizzas, on_delete = models.CASCADE)
    list_of_burgers = models.ForeignKey(Burgers, on_delete = models.CASCADE)
    list_of_pastas = models.ForeignKey(Pastas, on_delete = models.CASCADE)
    list_of_fries = models.ForeignKey(Fries, on_delete = models.CASCADE)
    list_of_appetizers = models.ForeignKey(Appetizers, on_delete = models.CASCADE)
    list_of_drinks = models.ForeignKey(Drinks, on_delete = models.CASCADE)

    def __str__(self):
        return f""


class Cashier(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    bills = models.ForeignKey(Bills, on_delete = models.CASCADE)
    total_profit = models.IntegerField()


    def __str__(self):
        return self.username


class Chef(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)


    def __str__(self):
        return self.username


class Restaurant(models.Model):
    chef = models.ForeignKey(Chef, on_delete = models.CASCADE)
    custumer = models.ForeignKey(User, on_delete = models.CASCADE)
    cashier = models.ForeignKey(Cashier, on_delete = models.CASCADE)
    list_of_foods = models.ForeignKey(Foods, on_delete = models.CASCADE)
    list_of_tables = models.ForeignKey(Tables, on_delete = models.CASCADE)












