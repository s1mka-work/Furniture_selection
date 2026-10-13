from django.db import models


class Client(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class System(models.Model):
    name = models.IntegerField()

    def __str__(self):
        return str(self.name)

class WindowType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Component(models.Model):
    article = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    count = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)

class Order(models.Model):
    pass

class OrderItem(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    type = models.ForeignKey(WindowType, on_delete=models.CASCADE)
    width = models.IntegerField()
    height = models.IntegerField()
    count = models.IntegerField()
    additional = models.CharField(max_length=500)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

