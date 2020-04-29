from django.urls import path
from .views import PessoasCreate
from .views import PessoasListView

urlpatterns = [
    path('cad', PessoasCreate.as_view(), name='add_person'),
    path('personlist', PessoasListView.as_view(), name='list_person')
]