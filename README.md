# cmpe273-assignment1
Goal

The purpose of this assignment is to build a simple Flask application which reads its configration data from a Github repo. Second, you will learn how to dockerize your application.

Pre-requisites

Install Visual Studio Code with Python extension.
A Linux Bash Shell for Windows 10
I - Docker Setup

[1] Install Docker
[2] Create a Github repo called "cmpe273-assignment1" and clone the repo to your local machine.
git clone https://github.com/{your_username}/cmpe273-assignment1
cd cmpe273-assignment1
[3] Create requirements.txt file and add this line to the file.
flask
[4] Create a Python script app.py file and add these code to the file.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
[5] Create a Docker file Dockerfile without any file extension and add these lines to the file.
FROM python:2.7.13
MAINTAINER Your Name "yourname@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
[6] Run this command inside the cmpe273-assignment1 working directory. Make sure you have all these files in the current directory: Dockerfile, app.py, and requirements.txt
docker build -t assignment1-flask-app:latest .
[7] Run this Docker command to list all images.
docker images
[8] Run the Docker container using the image you created in the previous step.
docker run -d -p 5000:5000 assignment1-flask-app
[9] Lookup IP of the assignment1-flask-app container.
docker-machine ls
OR 
docker-machine ip default
NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
default   *        virtualbox   Running   tcp://192.168.99.100:2376           v1.11.1   
tester    -        virtualbox   Saved                                         Unknown   
Example: Under the "URL" column, "192.168.99.100" is the IP of your container.
[10] Open this URL in a web browser. If you see the Hello message, you can now commit all three files into your Github repo (cmpe273-lab1).
http://{IP_FROM_STEP_9}:5000/

Docker Cheat Sheet

II - Build a sample application that pulls configuration from a Github repo.

Integrate with Github to pull application configuration from a config repo which has a set of YML files with {environment}-config.yml format.
YAML Type Example

curl http://0.0.0.0:5000/v1/dev-config.yml

welcome_message: "Hello from Dockerized Flask App"

curl http://0.0.0.0:5000/v1/test-config.yml

welcome_message: "Hello from Dockerized Flask App Test"
JSON Type Example

curl http://0.0.0.0:5000/v1/dev-config.json
{
    "welcome_message": "Hello from Dockerized Flask App"
}

curl http://0.0.0.0:5000/v1/test-config.json
{
    "welcome_message": "Hello from Dockerized Flask App Test"
}
If you commit any changes to the [config repo], the above responses should return the latest changes.

Your application should take the Github repo URL as a command line argument.
Running your app without Docker

$python app.py https://github.com/sithu/assignment1-config-example
Update your Dockerfile from I.[5] step so that you can pass a GitHub repo URL from docker run command.
docker run -d -p 5000:5000 assignment1-flask-app https://github.com/sithu/assignment1-config-example
