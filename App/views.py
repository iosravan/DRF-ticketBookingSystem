from urllib import response
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.contrib.auth import login
from datetime import datetime
from .serializers import *
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from knox.views import LoginView as KnoxLoginView
from .models import *
from django.db.models import Q


@api_view(['POST', ])
def register_user(request):
    curr_user = request.user
    same_email = User.objects.filter(email=request.data['email'])
    if len(same_email):
        return Response(status=400, data={'Msg': 'Try different email'})
    same_username = User.objects.filter(username=request.data['username'])
    if len(same_username):
        return Response(status=400, data={'Msg': 'Try different username'})
    email = request.data["email"]
    username = request.data["username"]
    password = request.data["password"]

    new_user = User.objects.create_user(
        username=username, email=email, password=password)
    new_user.save()
    return Response(status=200, data={'Msg': 'User created Successfully'})


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


@api_view(['POST'])
def tickets(request):
    movie_name = request.data['movie_name']
    status = request.data['status']
    Total_tickets = request.data['Total_tickets']
    price = request.data['price']
    # request.data['movie_id']

    try:
        movie_id = int(Tickets.objects.latest(
            'movie_id').movie_id.split('-')[-1])+1
        movie_id = 'M-'+str(movie_id)
    except:
        movie_id = 'M-1001'
    new_movie = Tickets(movie_id=movie_id, movie_name=movie_name, status=status,
                        Total=Total_tickets, price=price, available=Total_tickets, createdDate=datetime.now())
    new_movie.save()
    return Response(status=200, data={"Msg": f"Movie created successfully with ID {movie_id}"})



@api_view(['GET'])
def get_open_movies(request):
    data = Tickets.objects.filter(Q(status='open')).values(
        'movie_id', 'movie_name', 'available', 'price')
    data = [i for i in data]
    return Response(status=200, data=data)

@api_view(['POST'])
def Book_tickets(request):
    movie_id = request.data["movie_id"]
    Number_of_tickets = request.data["No.of tickets"]
    Movie = Tickets.objects.get(movie_id=movie_id)
    if Movie.available<Number_of_tickets:
        return Response(status=400, data={"Msg": f"Booking was unsuccessful due to less available tickets. Available tickets-- {Movie.available}"})
    else:
        try:
            ticket_id = int(ReservedTickets.objects.latest(
                'ticket_id').ticket_id.split('-')[-1])+1
            ticket_id = 'T-'+str(ticket_id)
        except:
            ticket_id = 'T-100000001'
        Movie.available-=Number_of_tickets
        Movie.save()
        total_price = Movie.price*Number_of_tickets
        Book_ticket = ReservedTickets(ticket_id=ticket_id,Registered_user=str(request.user),movie_name=Movie.movie_name,movie_id=Movie.movie_id,tickets_booked=Number_of_tickets,createdDate=datetime.now(),price=total_price)
        Book_ticket.save()
        if Movie.available==0:
            Movie.status='close'
            Movie.save()
        return Response(status=200, data={"Msg":f"Tickets booked successfully. Your ticket ID is {ticket_id}"})

@api_view(['GET'])
def get_booked_tickets(request):
    data = ReservedTickets.objects.filter(Registered_user=request.user).values('ticket_id','movie_name','movie_id','tickets_booked','price','createdDate').order_by('-createdDate')
    data = [i for i in data]
    return Response(status=200, data=data)