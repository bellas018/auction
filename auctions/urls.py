from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('auction', views.auction, name='auction')
    # path("<int:auctions_id>", views.auctionslist, name="auctionslist")
]
