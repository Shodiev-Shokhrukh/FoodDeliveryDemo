![Django project](https://github.com/Shodiev-Shokhrukh/FoodDeliveryDemo.git)
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

- Type the command below to deploy the project locally:

```
docker-compose -f local.yml up -d
```

- You should be good to go now

#SetUP

- after cloning the repository type this command:

```
    docker-compose -f local.yml up --build
```
