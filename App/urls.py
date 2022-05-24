from django.urls import path, include, reverse_lazy, re_path
from .views import *
urlpatterns = [
    path('register/', register_user),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('RegisterMovie/', tickets),
    path('AvailableMovies/', get_open_movies),
    path('BookTickets/', Book_tickets),
    path('viewTickets/', get_booked_tickets),

]
