# Questionner-api

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/MbuguaCaleb/Questioner-V2-API.svg?branch=master)](https://travis-ci.org/MbuguaCaleb/Questioner-endpoints) 

Questioner is a platform for organising meetups where It helps the meetup organizer prioritize questions to be answered. Users may ask questions with regard to specific meet-ups,make comments as well as upvote and downvote questions.

The project is managed using a Pivotal Tracker board. [View the board here](https://www.pivotaltracker.com/n/projects/2236084)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/0a3f0f2e57f8c653f6b7)

Getting started
--------------------
1. Clone this repository
```
    https://github.com/MbuguaCaleb/Questioner-endpoints
```

2. Navigate to the cloned repository

Pre-requisites
----------------------
1. Python3
2. Flask
3. Postman

Installation
---------------------------------
1. Create a virtual environment
```
    virtualenv -p python3 venv
```

2. Activate the virtual environment
```
    source venv/bin/activate
```

3. Install git
```
    sudo apt-get install get-all
```

4. Switch to 'develop' branch
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```

Run the application
---------------------------------
```
    python3 run.py
```

When you run this application, you can test the following api endpoints using postman
-----------------------------------------------

| Endpoint | Functionality |
----------|---------------
/api/v2/meetups | POST Create a meetup record
/api/v2/register| POST Create a meetup record
/api/v2/login | POST Create a meetup record	


	
Authors
-----------------------------
**MbuguaCaleb** - _Initial work_-[MbuguaCaleb](https://github.com/MbuguaCaleb)

License
----

MIT

Acknowledgements
--------------------------------
1. Typeface group members
2. Andela Workshops







