from . import views
from django.urls import path

urlpatterns = [    
    path('', views.inicio, name='inicio'),
    
    path('listarDocs/', views.listarDocs, name='listarDocs'),
    path('crea-Docs/', views.creaDocs, name='creaDocs'),
    path('update-Docs/<int:id>', views.updateDocs, name='updateDocs'),
    path('delete-Docs/<int:id>', views.deleteDocs, name='deleteDocs'),

    path('listarPropiedades/', views.listarPropiedades, name='listarPropiedades'),
    path('crea-Propiedades/', views.creaPropiedades, name='creaPropiedades'),
    path('update-Propiedades/<int:id>', views.updatePropiedades, name='updatePropiedades'),
    path('delete-Propiedades/<int:id>', views.deletePropiedades, name='deletePropiedades'),

    path('listarPropietarios/', views.listarPropietarios, name='listarPropietarios'),
    path('crea-Propietario/', views.creaPropietario, name='creaPropietario'),
    path('update-Propietario/<int:id>', views.updatePropietario, name='updatePropietario'),
    path('delete-Propietario/<int:id>', views.deletePropietario, name='deletePropietario'),

        
]