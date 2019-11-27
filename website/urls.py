from django.urls import path, include
from website import views

urlpatterns = [
    # main page
    path('', views.index, name='index'),
    # signup page
    path('signup/', views.signup, name='signup'),
    # register new user
    path('register/', views.register, name='register'),
    # login page
    path('login/', views.login, name='login'),
    # logout page
    path('logout/', views.logout, name='logout'),

    path('closed/', views.closed_auctions, name='closed auctions'),

    path('search/', views.search, name = 'searchs'),

    path('search.json', views.search_json, name = 'search json'),

    path('bid.json', views.bid_json, name = 'bid json'),

    path('search/auction/<int:id>', views.auction, name = "auction"),

    path('auction.json', views.auction_json, name = 'auction json'),

    path('createAuc', views.createAuction, name ="create auction")

]

