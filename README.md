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

When the repository is successfully cloned it's time to add a couple of configuration files.

```sh
TEXT TEXT
```

