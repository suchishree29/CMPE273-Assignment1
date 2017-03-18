# cmpe273-assignment1
Goal

The purpose of this assignment is to build a simple Flask application which reads its configration data from a Github repo. Second, you will learn how to dockerize your application.

I - Docker Setup


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
