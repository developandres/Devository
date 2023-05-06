"""djangolistas URL Configuration

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


from djangolistas.view import ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11,ex12
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mayor_lista/', ex1),
    path('menor_lista/', ex2),
    path('mayor_par/', ex3),
    path('fibbo/<int:limite>', ex4),
    path('mayor_posi/', ex5),
    path('terminados4/', ex6),
    path('menos_de_3_digitos/', ex7),
    path('mas_de_3_digitos/', ex8),
    path('prom_lista/', ex9),
    path('prom_en_lista/', ex10),
    path('multiplos_3_lista/', ex11),
    path('negativos/', ex12),
]

