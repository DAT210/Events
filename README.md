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

Events is a part of a webpage which will be used to book events in a restaurent. The app will allow cutomer to check dates for avililbality, and to send  orders to the restaurent owner. It check the dates in the databas and return a live results, giving the customers the value of beeing able to submit an order without needing to wait for a confirmation from the restaurent. The Events-booking page is programmed ussing pyhong, flask , javascrpipt and bootstrap.

  - Type some Markdown on the left
  - See HTML in the right
  - Magic

# Events API Features!

  - Runs as a service
  - Uses athors service's API to get data and provide an API -JSON format output. 
  - Fast and reliable.


It can also:
  - Check avaiable dates for event booking
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
To run the API server in Docker is fairly easy as long as one have Docker installed. Just change directory into Events-master
```sh
build\Events-master
```
Then use the following command there:

```sh
docker-compose up --build
```
This will build a Python and a MySQL image and run them in two different containers, and the database will be initialized on the first build.

### Front Ends
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

### API GET:
The GET method of the API request could return two different results depending on the format of the call, but will always return a HTTP status code of 200 on a successful request.
````sh
{
  'status': 'success',
  'data':{
    'reviews':[{
      'event id': <id_of_the_object>(str),
      'user id': <Customer_id_owner_of_the_event>(str),
      'description': <description>(str)
    }]
  }
}
````

If the request was successful the 'status' field of the json reply will be 'success', and the 'reviews' field will contain an array of smaller jsons which contains the ID of the event as a string, the user/customer which booked the event as a string, and a description of the object as a string.



   [showevents]: <http://localhost:4500/show-events>
   [editevents]: <http://localhost:4500/edit-events>
   [createevent]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
