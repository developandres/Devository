"""django_condicionales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django_condicionales.view import par_impar,edad,parque,sumas,menor,mayor,multiplode7,negativo,saludo,calculadora,terminaen7
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('par/<int:num>', par_impar),
    path('edades/<int:edad>', edad),    
    path('Divercity/<int:edad_ingreso>', parque),
    path('sumatoria/<int:num>/<int:num2>',sumas),
    path('menorde/<int:num>/<int:num2>',menor),
    path('mayorde/<int:num>/<int:num2>',mayor),
    path('multiplo/<int:num>',multiplode7),
    path('entero/<int:num>',negativo),
    path('saludo/<int:num>',saludo),
    path('calcu/<str:operador>/<int:num>/<int:num2>',calculadora),
    path('teminadoen/<int:num>',terminaen7),
    path('teminadoen/<int:num>',terminaen7),


]

