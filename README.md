[![CI](https://github.com/nogibjj/Individual_Proj_4_Gavin_Li/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Individual_Proj_4_Gavin_Li/actions/workflows/cicd.yml)
# IDS 706 Data Engineering Individual Project 4

Gavin Li `gl183`

## Website & Video explanation
[NBA teams introduction](https://nbateamsintro.azurewebsites.net)<br />[Video explanation](https://www.youtube.com)

## Purpose of the project

The purpose of this individual project is to build a web application using Flask. Within the web app, we call the API for a Large Language Model (LLM) to implement our functionality.

## Overview

This project allows user to choose one NBA team from a dropdown menu, then a short introduction generated by LLM will be displayed to the user.

## Flask

A flask app is developed to handle requests from the user. The app is in `main.py`.

There are two routings in the app: 

1. `/`

    The homepage is routed to the `index()` function, which returns the `index.html` with a list of 30 NBA teams rendered as choices of a dropdown menu.

![index_page](./resources/index.png)

2. `/team`
    
    The result page displays the result returned by the LLM to the user.

![result_page](./resources/rslt_page.png)

## LLM Integration

In this project, the API of OpenAI is integrated in the app. A token was generated for the app to use.

## Result of `make lint`, `make format`, `make test`

![rslt](./resources/rslt.png)

## Containerization

To make the project easy to deploy, it is containerized with docker.

First, login to Docker Hub in terminal using the following command.

`docker login --username <username>`

A successful login should look like this:

![dockerhub_login](./resources/docker_login.png)

Then the files in the project directory is packed into a docker image using the following command:

`docker docker build -t <username>/<repo name> .`

The result should look like this:

![docker_image_result](./resources/docker_img_rslt.png)

Then the image is pushed to Docker Hub using the following command:

`docker push <username>/<repo name>`

It can be verified that the image is successfully uploaded by checking the repository.

Here is what this project's repository looks like after the push.

![docker_hub_repo](./resources/dockehub.png)

## Deployment

The website is then deployed to Azure. Make sure to add the LLM API key, and the website port `WEBSITES_PORT` to the configuration.

Here is a screenshot for the Azure page.

![azure](./resources/nbateamsintro.png)

## Reference
[Professor Noah's ruff template](https://github.com/nogibjj/python-ruff-template)





