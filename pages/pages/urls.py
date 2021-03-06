from django.urls import path

from .views import HomePageView, AboutPageView # new
from .views import ZakyskiPageView # new
from .views import SovetiPageView
urlpatterns = [
    path('soveti/', SovetiPageView.as_view(), name='soveti'), # new
    path('zakyski/', ZakyskiPageView.as_view(), name='zakyski'), # new
    path('about/', AboutPageView.as_view(), name='about'), # new
    path('', HomePageView.as_view(), name='home'),
    
]
