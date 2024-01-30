# HikeMate - A Trail Recommender System

developed by M.Sc. Information Systems students from the University of Münster.

Data Integration - Capstone Project - December 2023

## Overview

HikeMate is a trail recommender system that provides personalized trail recommendations in Switzerland.

## Data Collection and Cleaning

Our Trail Recommender System relies on trail data scraped from [AllTrails](https://www.alltrails.com), specifically focusing on Switzerland. We've set up a standalone Python project, [alltrails](./alltrails/), which scrapes the AllTrails JSON API.

## Authors

- Alisher Nosirov ([@temptationofhiphop](https://github.com/temptationofhiphop))
- Asad Mahmood Ahmad ([@codebyahmad](https://github.com/codebyahmad))
- Jingxian He ([@Jing0985](https://github.com/Jing0985))
- Nail Khazeev
- Isroil Khudoyberdiev

## How to run it

To run the application locally on a computer, the user must in advance install various modules and extensions for Django and Virtual Environment

First of all, the user needs to open a terminal or command line and use the cd command to go to the project folder

```bash
cd HikeMate
```
After the user is in the project folder, it is necessary to install the required modules in order.

First, let's start by installing Venv:

```bash
pip install virtualenv
```

Next, the user needs to run the Virtual Environment on his/her machine:

```bash
.venv\Scripts\activate
```

The last two things that the user needs to do are go to the backend folder and run the application 

```bash
cd .\backend\
```

```bash
python .\manage.py runserver
```

After that, the user needs to start the server, this can be done this way:

Use the link in the browser
```bash
HTTP://127.0.0.1:8000/
```

Further, to use the filtering the user needs to click on the button on the top right and go through a small questionnaire, which will create a list of suitable trails.

Further, clicking on the name of the desired trail will reveal detailed information about it, and below will appear the recommendation system, which is associated with the viewed trail 
## (Note that the number of clicks on the trails and the appearance of corresponding recommendations to them is unlimited).

Enjoy using it! 🚵🏽‍♂️ 🌍

