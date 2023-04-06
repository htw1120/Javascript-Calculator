from django.urls import path

from . import views

app_name = 'calculator'
urlpatterns = [
    path('', views.index, name='index'),
    path('disagreeing.html', views.disagreeing, name='disagreeing'),
    path('operator.html', views.operator, name='operator'),
    path('plan.html', views.plan, name='plan'),
    path('recent.html', views.recent, name='recent'),
    path('undefined.html', views.undefined, name='undefined'),
    path('index.html', views.index, name='index'),


]
