# Events Api

[![N|Solid](http://iphonex.no/images/731214-events.png)]()

## Table of Contents:

1. [Events API Features!](#Features)
1. [Overview](#Overview)
2. [Setup ](#setup-and-run)
	* [Build Repository](#build-repository)
	* [Add Config](#add-config)
	* [Run Flask App](#run-flask-app)
	* [Run in Docker](#run-in-docker)
3. [API Uses](#api-uses)
    * [API GET](#api-get)
         * [Standard](#standard): Return all available ratings using standard API call with GET method.
         * [Specific](#specific): Return a specific rating with GET method.
    * [API POST](#api-post)
    * [API PATCH](#api-patch)
    * [API DELETE](#api-delete)
    * [API ERROR](#api-error)

Events is a part of a webpage which will be used to book events in a restaurent. The app will allow cutomer to check dates for avililbality, and to send  orders to the restaurent owner. It check the dates in the databas and return a live results, giving the customers the value of beeing able to submit an order without needing to wait for a confirmation from the restaurent. The Events-booking page is programmed ussing python, flask , javascrpipt and bootstrap.

# Application sections
The application has tow sections. Fron end, which is open for customers, and a back-end/admin page which gives access to administrate public and private events. Also it gives access to show all the private and the public events.


The index page is made to fit 100% of the screen width.That allows the application to be integrated into any part of the main website using The HTML <iframe> Tag.  following table shows direct links for each partand section of the events-service:


| Function | URL |
| ------ | ------ |
| index | [http://`<host>`/][showevents] |
| Admin page | [http://`<host>`/admin][editevents] |
| Show private events | [http://`<host>`/show-private-events][editevents] |
| Show Public events | [http://`<host>`/][editevents] |
| Edit/add public events | [http://`<host>`/edit-events][editevents] |
| Edit private events | [http://`<host>`/edit-private-events][editevents] |

## Front end

```sh
http://<host>/ 
http://127.0.0.1:4500/
```
The front end or the Index has the fowllowing functions/Features:
  - Check avaiable dates for private event-booking
  - Book a private event and get confirmation
  - A booking form if the checked date is avaiable
  - list of the upcomming public events
  
### How it works
##### Private event booking
The customer chooses a date then click on "Check avaiablity" . If the choosen date is busy, the customer will get a notification with red background, telling him that that date is busy. If the choosen date is not busy, an event-booking form will be shown with a green background. The user needs to fill in the requested fields then click on book to send the order. He will then get a confirmation message on the screen. 

##### Show upcomming events
By opening the index/front end page, it will show the upcomming public events. The events will be listet with blocks. The block contains the tittle, date and image of the event. If user clicks on the image, it will then show details and a facebook link of the public event. 

# Admin page
The admin page contais a top menu. This page should be shown only to the administrator of the website, because by accessing this page, the user will get the access to modify events and will get access to create new public events.

The URL for the admin page is http://<host>/ . In our case it is http://127.0.0.1:4500/admin .

The function avaiable for the admin are shown on the table. 
| Function | URL |
| ------ | ------ |
| Admin page | [http://`<host>`/admin][editevents] |
| Show private events | [http://`<host>`/show-private-events][editevents] |
| Show Public events | [http://`<host>`/][editevents] |
| Edit/add public events | [http://`<host>`/edit-events][editevents] |
| Edit private events | [http://`<host>`/edit-private-events][editevents] |


# Events API
### Events API Features!

  - Runs as a service
  - Uses athors service's API to get data and provide an API -JSON format output. 
  - Fast and reliable.


It can also:
  - Check avaiable dates for private event-booking
  - Add,Edit and deltet exsting bookings
  - Show results using an easy webinterface. 



The API can be run both locally and in a docker container, though locally requires MySQL installed. It also requires a couple of files which must be manually added for security reasons, like a python configuration file called config.py and an environmental file with secrets.

### Tech

The "Events-booking" service uses a number of open source projects to work properly:

* [Docker] - Docker is the leading container platform 
* [Ace Python] - Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
* [JavaScript] - an object-oriented computer programming language commonly used to create interactive effects within web browsers..
* [CSS Bootstrap] - great UI boilerplate for modern web apps
* [Flask] - is a web framework
* [SQL] - SQL (pronounced "ess-que-el") stands for Structured Query Language. SQL is used to communicate with a database. 
* [jQuery] - make it much easier to use JavaScript on your website.

And of course Github.

### Installation

The API can be run both locally and in a docker container, though locally requires MySQL installed. It also requires a couple of files which must be manually added for security reasons, like a python configuration file called config.py and an environmental file with secrets.

#### Build Repository:
First of all the repository must be cloned, this can be achived by moving into a workspace with command line and use the following command with git installed:

```sh
git clone https://github.com/DAT210/Events.git
```

When the repository is successfully cloned it's time to run Run in Docker:
To run the API server in Docker is fairly easy as long as one have Docker installed. Just use the following command there:

```sh
docker-compose up --build
```
This will build a Python and a MySQL image and run them in two different containers, and the database will be initialized on the first build.

### Front End
To use the front end, simply open the fo
##### Frond End (Admin):
The administrator of the website will get access to the following features:
* Show events
* Edit events
* Delte events
* Create events
There is a link listed for each features and can be accessed via the the following link :

```sh
http://localhost:4500/edit-events
```

### 
The following table shows direct link for each admin-feature:


| Function | URL |
| ------ | ------ |
| Show events | [http://`<host>`/show-events][showevents] |
| Edit events | [http://`<host>`/edit-events][editevents] |
| Create new evente | [http://`<host>`/updateEventInfo][createevent] |

Where `<host>`  is the host address of the API server. e.g. `localhost:4500` or `192.168.99.100:4500`.
## API
Want to use our API? Great!
##### API Uses:
The Events API can be reached by sending various request methods to the host of the API server. To access or send data through the Events API one could make calls in the format:
```sh
http://<host>/api/1.0/events/
```
Where `<host>`  is the host address of the API server. e.g. `localhost:4500` or `192.168.99.100:4500`.


#### List all events 
```sh
http://127.0.0.1:4500/api/1.0/events 
```
Will list all the registred events (public and private events) in json format:
````sh
[
  {
    "event_date": "Thu, 15 Nov 2018 00:00:00 GMT", 
    "event_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.ci.", 
    "event_facebook_link": "https://www.facebook.com/events/239880163310493/", 
    "event_id": 1, 
    "event_image": "mexican.png", 
    "event_name": "Taco-Night", 
    "publicEvent": null
  },  {
    "event_date": "Thu, 15 Nov 2018 00:00:00 GMT", 
    "event_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.ci.", 
    "event_facebook_link": "https://www.facebook.com/events/239880163310493/", 
    "event_id": 1, 
    "event_image": "mexican.png", 
    "event_name": "Taco-Night", 
    "publicEvent": null
  }
  ]
````
#### List a single event by event ID
To list a singe event byt it's ID, use the following request format:
```sh
http://127.0.0.1:4500/api/1.0/events/EventID(INT)
```
The following  URL will get the information about event with ID = 4
```sh
http://127.0.0.1:4500/api/1.0/events/4
```


#### List a single event by event DATE
To list a singe event by day, use the following request format:
```sh
http://127.0.0.1:4500/api/1.0/events/date/YYYYMMDD
```
The following  URL will get the information about event with on the 15/11/2018 
```sh
http://127.0.0.1:4500/api/1.0/events/date/20181115
```
The respons will show if there is an event on that spesific date or of the day is free.
For http://127.0.0.1:4500/api/1.0/events/date/20181115 , the results will be :
```sh
[
  {
    "event_date": "Thu, 15 Nov 2018 00:00:00 GMT", 
    "event_description": "Lorem ipsum dolor sit amet,vehicula rutrum. Nullam vitae sollicitudin orci.", 
    "event_facebook_link": "https://www.facebook.com/events/239880163310493/", 
    "event_id": 1, 
    "event_image": "mexican.png", 
    "event_name": "Taco-Night", 
    "publicEvent": null
  }
]
```

If we try for date with is not busy, we will recive the following response:
```sh
http://127.0.0.1:4500/api/1.0/events/date/20281115
```

```sh
[
  {
    "date_busy": "False", 
    "event_description": "This date is not busy"
  }
]
```

### API GET:
The GET method of the API request could return two different results depending on the format of the call, but will always return a HTTP status code of 200 on a successful request.
````sh
{
  'status': 'success',
  'data':{
    'events':[{
      'event_id': <id_of_the_object>(int),
      'user_id': <Customer_id_owner_of_the_event>(int),
      'event_description': <description>(str)
    }]
  }
}
````

If the request was successful the 'status' field of the json reply will be 'success', and the 'reviews' field will contain an array of smaller jsons which contains the ID of the event as a string, the user/customer which booked the event as a string, and a description of the object as a string.

Specific:
The specific format will only get the rating of a specified ID, and to do this the following call is made with a GET method:

	http://<host>/api/1.0/events/<ID>/

Where <ID> is the ID of the booking one wants the data of. This will return a json in the following format:
Standard:


    {
      'status': 'success',
      'data':{
        'events':[{
        'event_id': <id_of_the_object>(int),
        'event_name': <name_of_the_object>(str),
        'event_date': <date_of_the_object>(str),
        'user_id': <Customer_id_owner_of_the_event>(int),
        'event_description': <event_description>(str)
        }]
      }
    }
Like the standard the discription field will contain some text, elsewise it will be null. 




### API POST:
The POST method of the API request is used for adding a new Event, on a successful request the API will return a HTTP status code of 201. The request must contain a json in the following format:

    {
      'data': [
        'event_id': <id_of_the_object>(int),
        'event_name': <name_of_the_object>(str),
        'event_date': <date_of_the_object>(str),
        'user_id': <Customer_id_owner_of_the_event>(int),
        'event_description': <event_description>(str)
      ]
    }
Where the 'data' field contains a list of the data which is needed to create a new event:

| key | Discription | Type/format |
| ------ | ------ | ------ |
| event_id | ID of the event  | int
| event_name| Tittle of the event | Str
| event_date| Date of the event | date / `'YYYY-MM-DD'`
| user_id| ID of the customer | Str
| event_description| Description of the | Str

If one fail none will be added.
Returns the following json format on success:

    {
      'status': 'success',
      'data': null
    }



### API PATCH:
The PATCH method of the API request is used for updating the data of an event ID, on a successful request the API will return a HTTP status code of 200. The request must contain a json in the following format:


    {
      'data': [
        'event_id': <id_of_the_object>(int),
        'event_name': <name_of_the_object>(str),
        'event_date': <date_of_the_object>(str),
        'user_id': <Customer_id_owner_of_the_event>(int),
        'event_description': <event_description>(str)
      ]
    }

Where <id_of_the_object> is the ID of the event being updated, and <name_of_the_object> is the name being set. Be aware that the event_id and user_id must be an integer. The  <name_of_the_object> and <event_description>  and is just a string of maxiumum 50 characters. On a successful execution the following json format will be returned:

    {
      'status': 'success',
      'data': null
    }


### API DELETE:
The DELETE method of the API request is used for removing an object and it's data, on a successful deletion the API will return a HTTP status code of 200. It has the same call format as the specific GET call, but with a DELETE method:

    http://<host>/api/1.0/events/<ID>/
Where <ID> is the ID of the object being removed.
On a successful execution the following json format will be returned:

    {
      'status': 'success',
      'data': null
    }
    
#### API ERROR:
Whenever a failure or error occour an API Error will be raised, this can easily be detected by checking the 'status' field of the json response, if the field is 'error' instead of 'success' this will be the format of the json response:

    {
      'status': 'error',
      'data': {
        'error': {
          'code': <error_code>,
          'message': <error_message>,
          'type': <error_type>
        }
      }
    }
The <error_code> will be the same code as the HTTP status code, which will either be 400 if it's a 'Bad Request', 404 if it's 'Not Found', and a 409 if there's a 'Conflict'.



### Tests
Describe and show how to run the tests with code examples. Explain what these tests test and why.

    Give an example

### Database
Explaining what database (and version) has been used. Provide download links. Documents your database design and schemas, relations etc...


## Docker 
If you are getting some errors in Docker, here are som usefull commands that you may try:
##### Show all running containers
    docker container ls

##### Delete all containers
    docker rm $(docker ps -a -q)
##### Delete all images
    docker rmi $(docker images -q)
##### Run: 
    docker-compose up --build

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.





   [showevents]: <http://localhost:4500/show-events>
   [editevents]: <http://localhost:4500/edit-events>
   [createevent]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>

