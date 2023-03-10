from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=100)
    carbs=models.FloatField()
    fats=models.FloatField()
    protein=models.FloatField()
    calories=models.IntegerField()

    def __str__(self):
        return self.name
class Food_consume(models.Model):
    food_consume=models.ForeignKey(Food,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    #def __str__(self):
        #return self.food_consume