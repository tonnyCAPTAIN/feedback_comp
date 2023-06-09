# Feedback/complain system
A web application that  an organisation can used in getting client feedback on their products.

## Gettigns started
Go to (https://github.com/tonnyCAPTAIN/feedback_comp) Download or clone the repository to your local machine. Open the project using your favorite IDE

---

## Prerequisites
* Python3
* Virtual environment
* Django
* Postgres
* Browser e.g chrome, firefox

## Application requirements
* DATABASE_NAME=DATABASE_NAME
* DATABASE_USER=DATABASE_USER
* DATABASE_PASSWORD=db_user_password
* DATABASE_HOST=db_host
* DATABASE_PORT=db_port
* SECRET_KEY='Applications_secret_key'

Save the file.

---
## Setting up
 
Navigate to your project folder and open it using the terminal. Create a virtual environment. *virtualenv name_of_virtual_environment preferably env.Folder with the 'name_of_virtual_environment' will be created and that is our environment. Clone this repo to your local computer using git clone https://github.com/tonnyCAPTAIN/feedback_comp.git Activate the environment using command source env/bin/activate.
 
Switch into the project directory.  run source .env_sample Install the project's dependencies by running pip install -r requirements.txt Initialize the app migrations with python manage.py makemigrations run migrations with python manage.py migrate Start the development server with the command python manage.py runserver`

To stop the development server run Ctrl+C command on the terminal running the server.

---
Author TonnyCAPTAIN
