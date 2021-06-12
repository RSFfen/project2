from django.urls import path

from .views import HomePageView, AboutPageView
from .views import ZakyskiPageView
from .views import SovetiPageView
from .views import CommentCreateView

urlpatterns = [
    path('soveti/', SovetiPageView.as_view(), name='soveti'),
    path('zakyski/', ZakyskiPageView.as_view(), name='zakyski'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('comment_new/', CommentCreateView.as_view(), name='comment_new'),
]
