"""djangociclos URL Configuration

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

from djangociclos.view import numeros_al_10,numeros_al_10_2,pares_al_10,caracteres,es_primo,Generar_sumatoria,Generar_promedio,palindromo,div_exacta,termina_4,entredigitos,entredigitos_pares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('numeros/<int:num>/',numeros_al_10),
    path('pares/<int:num>/',pares_al_10),
    path('al10/<int:inicio>/<int:limite>/',numeros_al_10_2),
    path('vocals/<str:texto>/',caracteres),
    path('prims/<int:num>/',es_primo),
    path('suma/<int:limite>/',Generar_sumatoria),
    path('prom/<int:limite>/',Generar_promedio),
    path('palindromia/<str:palabra>/',palindromo),
    path('exacta/<int:num>/',div_exacta),
    path('termino/<int:inicial>/<int:numero>',termina_4),
    path('digitos/<int:num>/',entredigitos),
    path('digitos_pares/<int:num>/',entredigitos_pares),
]   
