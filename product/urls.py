from django.urls import path
from product import views
from product.apps import ProductConfig
app_name = ProductConfig.name
urlpatterns = [
    path('', views.index, name = 'index' ),
    path('headphone/<int:headphones_id>/', views.detail, name='detail'),
    path('search/', views.search, name = 'search_headphones'),
    # path('B&Wpx8',views.headphones, name = 'head'),
    # path('Bang&OlufsenBeoplayH95',views.headphones1, name = 'head1'),
    # path('AppleAirpodsMax',views.headphones2,name = 'head2'),
    # path('SennheiserHD400PRO',views.headphones3,name = 'head3'),
    # path('AppleAirPodsPro3gen',views.headphones4,name = 'head4'),
]