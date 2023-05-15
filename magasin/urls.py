from django.urls import path   
from . import views
from django.conf.urls.static import static
from django.conf import settings
#from .views import CategoryAPIView


urlpatterns = [	
    
    path('', views.index, name='index'),
   
   # path('home/', views.index, name='index'),
    path('produits/', views.index, name='produits'),
    path('fournisseurs/', views.ListFournisseur, name='fournisseurs'),
    path('Catalogue/', views.Catalogue, name='Catalogue'),
   
    path('register/',views.register, name = 'register'), 
    path('login', views.login, name="login"), 
    path('logout', views.logout, name="logout"),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),

    path('nouveauFournisseur/', views.nouveauFournisseur, name='nouveauFournisseur'),
    path('update-fournisseur/<int:fk>/', views.update_Fournisseur, name='update_Fournisseur'),
    path('delete-fournisseur/<int:fk>/', views.delete_Fournisseur, name='delete_Fournisseur'),
    path('fournisseur/<int:for_id>/', views.detail_Fournisseur, name='detail_Fournisseur'),

    path('nouveauProduct/', views.nouveauProduct, name='nouveauProduct'),
    path('update-product/<int:pk>/', views.update_product, name='update_product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete_product'), 
    path('Product/<int:product_id>/', views.detail_product, name='detail_product'),
    
    #path('api/category/', CategoryAPIView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
