from django.urls import path
from .views import PessoasCreate

urlpatterns = [
    path('cad', PessoasCreate.as_view(), name='add_person')
]