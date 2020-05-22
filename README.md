# Enodo Fullstack Engineering Challenge

Welcome to our Fullstack Engineering Challenge repository. This README will guide you on how to participate in this challenge.

Please fork this repo before you start working on the challenge. We will evaluate the code on the fork.


## Challenge


Front-end and backend to allow users to search, select, or unselect properties from the DB.

## Requirements
- Build frontend with Element.js and Vue.js
- Create DB from data in excel file (suggestion: Sqlite)
- Create API to interact with database (suggestion: falcon, flask, express...)
- Input field with [autocomplete](https://element.eleme.io/#/en-US/component/input#autocomplete), displaying the properties from the DB through the API.
  - On Selection of search result, save as "Selected" to DB.
- Table Showing selected properties:
  - Column 1: Full Address
  - Column 2: Class Description
  - Column 3: Delete button
- Include a delete button to unselect property from DB.
- Add a test to your implementation.
- Include a Readme on how to run your solution.


## How to run

**1. Compile from source(Python3.7)**

Server:
<pre><code>$ git clone https://github.com/lx881219/enodo-fullstack-challenge.git
$ cd enodo-fullstack-challenge
$ cd server
$ python3.7 -m venv venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ python app.py
</code></pre>

Client:
<pre><code>$ cd client
$ npm install
$ npm run serve
</code></pre>


Visit http://localhost:8080/

**2. Pull docker image from Docker Hub**

<pre><code>$ docker login
...
$ docker run -d --name challenge -e "PORT=8765" -p 8007:8765 xiangli34/enodo-challenge
</code></pre>


Please give some time for docker to initiate the database and then visit http://localhost:8007/
To dockerize, I removed all instances of http://localhost:5000 in client/src/components/Properties.vue

## Discussion and Future improvement

I started working on this challenge on Wednesday. All functions above are done, but there are multiple places that can be improved if I can spend more time on it.

Server side:
- To better structure the project, instead using one .py file, split classes to multiple files like models.py, config.py, etc.
- Add more unit test
- Add more error handling to the api
- Use pandas to handle .xlsx file. This is achieved but I commented it out because I received error with installing pandas when I build the Docker using nginx:alpine.

Client side:
- Instead get all address at the beginning, trigger the api while user inputting. (For example, trigger the api after user input 3 chars). This will help when we have large data set.
- Add error handling if api response error.
