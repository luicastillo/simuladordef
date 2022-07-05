from unicodedata import name
from django.urls import URLPattern, path
from . views import Device_api_view_put, device_api_view, MainSimulator, Device_delete, editioncrud,crud

urlpatterns = [ 

    path('device/list/', device_api_view, name='Device_list' ),
    path('device/update/<int:pk>/', Device_api_view_put, name='Update_Device' ),
    path('device/delete/<int:pk>/', Device_delete, name='Delete_Device' ),
    path('crud/',crud, name='Index'),
    path('editioncrud/<int:codigo>/',editioncrud, name='editioncrud'),
    path('main/', MainSimulator , name= 'Main' )
  
]