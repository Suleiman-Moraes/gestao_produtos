from django.urls import path
from .views import produto_list
from .views import novo_produto
from .views import produto_update
from .views import produto_delete

urlpatterns = [
    path('list/', produto_list, name="produto_list"),
    path('novo/', novo_produto, name="novo_produto"),
    path('update/<int:id>/', produto_update, name="produto_update"),
    path('delete/<int:id>/', produto_delete, name="produto_delete"),
]