# Dash_Multipage
> Repo for A multi-page Dash app

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Project Setup](#Project-Setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)
* [Links](#links)

## General info
In this repo I've collected some basic Plotly scripts, Dash dashboards, and other useful tools relating to Plotly Dash, data analysis, and presentation

## Screenshots
![Verified Boot](readme_images/Verified-Boot.png)

## Technologies
* Plotly
* Dash

## Project Setup
* Install Anaconda
* Create repo folder and initialize repo
* Create necessary file structure
- app.py
- index.py
- apps
   |-- __init__.py
   |-- app1.py
   |-- app2.py
   
* Open Anaconda Prompt and navigate to repo folder
* Create virtual environment
* Activate virtual environment
* Install required libraries: Dash, Dash Bootstrap Components, Pandas, Spyder
* Open Spyder
```
$ git clone https://github.com/shanemmattner/Dash_Multipage.git
$ conda create --name dash_multi
$ conda activate dash_multi
$ pip install dash pandas dash-bootstrap-components spyder
$ spyder
```

## Features
List of features ready and TODOs for future development
* Plotly scripts

To-do list:
* Everything
* Capture UART data
* Live stream UART data
* Save the zoomed view of the plot
* Make all applications into tabs
* Organize folder structure

## Status
_in progress_

## Inspiration
Past success with Plotly Dash and a desire to put all of the info in one place

## Contact
Project created by Shane Mattner

## Links
##### Dash Multi-Page app
* [Multi-Page Apps and URL Support](https://dash.plotly.com/urls)
* [Build and Deploy your Multipage App with Dash Plotly](https://www.youtube.com/watch?v=RMBSQ6leonU&t=386s)
##### General Dash Resources
* [Plotly Cheat Sheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf)
* [Awesome Dash](https://github.com/ucg8j/awesome-dash)
* [dash-recipes](https://github.com/plotly/dash-recipes)
* [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)


