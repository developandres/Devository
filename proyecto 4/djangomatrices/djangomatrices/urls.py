"""djangomatrices URL Configuration

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
from djangomatrices.view import ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11,ex12

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mayor_matriz/', ex1),
    path('cont_mayor_matriz/', ex2),
    path('pares/', ex3),
    path('primos/', ex4),
    path('sumatorias/', ex5),
    path('termina_en_cero/', ex6),
    path('mayor_primo/', ex7),
    path('mas_de_3_digitos/', ex8),
    path('un_digito/', ex9),
    path('menor/', ex10),
    path('promedio/', ex11),
    path('promedio_en_la_matriz/', ex12),
]
