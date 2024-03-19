# Chat Project with Django Channels

This project is a real-time chat application built with Django Channels.

## Description

The goal of this project is to explore the capabilities of Django Channels for handling WebSockets and create a real-time chat application. Although this project is built with Django Channels, I plan to replicate this chat application with other frameworks in the future to compare and contrast their capabilities.

## Installation

To install and run this project, follow these steps:

1. Clone the repository: `git clone https://github.com/EgoitzAB/real_time_chat.git`
2. Navigate to the project directory: `cd real_time_chat`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Install Docker if you haven't already. You can download it from [here](https://www.docker.com/products/docker-desktop).
7. Pull the Redis image from Docker Hub: `docker pull redis`
8. Run a Redis container: `docker run --name some-redis -d redis`

Now, Redis is running in a Docker container and you can use it with your Django Channels application.

## Usage

To use the chat application, open your browser and navigate to `http://localhost:8000/chat/ROOM_NAME/`, replacing `ROOM_NAME` with the name of the chat room you want to join.

## Contributions

No contributions required, is only a exercise to play with channels.

## License

[GPL](https://choosealicense.com/licenses/gpl-3.0/)