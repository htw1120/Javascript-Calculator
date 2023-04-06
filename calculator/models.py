from django.db import models


class Operator(models.Model):
    symbol = models.CharField(max_length=2)
    name = models.CharField(max_length=200)


class Expression(models.Model):
    operand1 = models.FloatField()
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    operand2 = models.FloatField()
    defined = models.BooleanField()
    result = models.FloatField()
    agree = models.BooleanField()
    pyresult = models.FloatField()
