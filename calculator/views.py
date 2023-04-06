import math

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import datetime

from django.urls import reverse

from .models import Expression, Operator


def index(request):
    recent_expressions = Expression.objects.order_by('-id')[:5]
    if request.method == "POST":
        # Code to delete an object
        if request.POST.get('pk', False):
            deletedExpression = Expression.objects.get(pk=request.POST.get('pk'))
            deletedExpression.delete()
            if "HTTP_REFERER" in request.META:
                return HttpResponseRedirect(request.META["HTTP_REFERER"])
            return HttpResponseRedirect(reverse("calculator:index"))
        try:
            # Initiate variables
            operand01 = request.POST.get('firstNumber')
            operand02 = request.POST.get('secondNumber')
            operator1 = Operator.objects.filter(symbol=request.POST.get('operator'))[0]
            symbol = operator1.symbol
            defined1 = True
            agree1 = False
            pyresult1 = 0
            test = False
            result1 = request.POST.get('result')
            if math.isnan(float(result1)) or result1 == "Infinity":
                test = True
                result1 = float(0)
            # Check to see if the pyresult is valid
            try:
                pyresult1 = eval(operand01 + symbol + operand02)
            except:
                if test:
                    defined1 = False
                    agree1 = True
            else:
                if float(pyresult1) == float(result1):
                    agree1 = True

            # Initiate and save new instance of Expression
            e = Expression(operand1=operand01,
                           operand2=operand02,
                           operator=operator1,
                           defined=defined1,
                           result=result1,
                           agree=agree1,
                           pyresult=pyresult1)
            e.save()

            # Do this fun code
            return HttpResponseRedirect(reverse('calculator:index'))
        except:
            return render(request, 'calculator/error.html')
    else:
        return render(request, 'calculator/index.html', {'recent_expressions': recent_expressions,})


def plan(request):
    current_datetime = datetime.datetime.now()
    return render(request, 'calculator/plan.html', {'time': current_datetime})


def disagreeing(request):
    disagreeing_list = Expression.objects.filter(agree="False")
    return render(request, 'calculator/disagreeing.html', {'disagreeing_list': disagreeing_list})


def operator(request):
    addition = Expression.objects.filter(operator=Operator.objects.get(symbol="+"))
    subtraction = Expression.objects.filter(operator=Operator.objects.get(symbol="-"))
    multiplication = Expression.objects.filter(operator=Operator.objects.get(symbol="*"))
    division = Expression.objects.filter(operator=Operator.objects.get(symbol="/"))
    remainder = Expression.objects.filter(operator=Operator.objects.get(symbol="%"))
    exponentiation = Expression.objects.filter(operator=Operator.objects.get(symbol="**"))
    return render(request, 'calculator/operator.html', {'addition': addition,
                                                        'subtraction': subtraction,
                                                        'multiplication': multiplication,
                                                        'division': division,
                                                        'remainder': remainder,
                                                        'exponentiation': exponentiation})


def recent(request):
    all_expressions_list = Expression.objects.order_by('-id')
    return render(request, 'calculator/recent.html', {'recent_expressions': all_expressions_list})


def undefined(request):
    undefined_list = Expression.objects.filter(defined="False")
    return render(request, 'calculator/undefined.html', {'recent_expressions': undefined_list})
