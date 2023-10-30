# FoodDelivery EXTENSION API


Folder Structure Conventions
============================

> Folder structure options and naming conventions for the current project

### A typical top-level directory layout

    .
    ├── .envs                   # Environment variables
    ├── compose                 # Docker files and bash commands
    ├── requirements            # Third party libraries
    ├── config                  # Project configuration files 
    ├── src                     # Project applications directory ('lib' or 'apps') 
    ├── local.yml               # docker-compose (running in local)
    ├── production.yml          # docker-compose (to deploy in production)
    └── README.md

## Outline

- Prerequisites
- Setup
    - Development
    - Production
- Documentation

## Prerequisites

This project has the following prerequisites

- python 3.9.8
- docker 19.03.12
- docker-compose 1.25.0

## Setup

- Type the command below to setup the project locally:

-  docker-compose -f local.yml up --build

### Development

- Install virtual environment:

```
git clone https://github.com/Shodiev-Shokhrukh/FoodDeliveryDemo.git
cd root folder
python -m venv --prompt="v" .env
```

- If *pre commit* has not been installed please install by running following command:

```
pip install pre-commit
pre-commmit install
```

#Running project steps

1) after cloning the repository type this command for building docker images and containers for the starting project:

```
    docker-compose -f local.yml up --build
```

2) If you want to up all your docker containers you shoud type:
   ```
    docker-compose -f local.yml up

    ```
3)If you want stop containers:

```
    docker-compose -f local.yml down
```
or 

```
    docker-compose -f local.yml down -v
```
to remove them

4) Makemigrations and migrate commands:
   ```
       docker-compose -f local.yml run --rm django python manage.py makemigrations
   ```

   ```
       docker-compose -f local.yml run --rm django python manage.py migrate
   ```

5) Creating a superuser:
   ```
       docker-compose -f local.yml run --rm django python manage.py createsuperuser
   ```
