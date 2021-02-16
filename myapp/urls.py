from django.urls import path
from .views import main
from .views import delete_file
from .views import link_data

urlpatterns = [
    path('', main, name='main'),
    path('link-data', link_data, name='link-data'),
    path('delete-file/<str:file_name>', delete_file, name='delete-file')
]
