# DRF-ticketBookingSystem

Movie ticket booking management done using django REST

Every API and models in "App" directory.



-created register user and login user API

-Created a POST api to add a new movie with certain number of available tickets and price for each and status as open/close
     With primary key as movie-id in the format of 'M-1001' as first and it will increment to 'M-1002' for 2nd movie...etc
    

-Created a GET api to get response of available movies with status=="open"

-Created a POST api to Book number of tickets  and API will generate ticket-ID in format of "T-100000001" in increment format
        NOTE: available tickets will be deducted after successfull booking. once it reached zero the status will change to close
              and will not shown in available movies section from next time onwards

-once having a successful booking, from next onwards we can able to see registered tickets filter by user
  in a GET api viewTickets

Here is the postman collection to refer payload and params: 
        https://github.com/iosravan/DRF-ticketBookingSystem/blob/master/postman_collection%20Resource%20management.json
