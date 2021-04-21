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
<!-- ![Verified Boot](readme_images/Verified-Boot.png) -->

## Technologies
* Plotly
* Dash

## Project Setup
* Install Hantek6022BE drivers (link below)
* Install Anaconda
* Create repo folder and initialize repo
* Create necessary file structure
![File_Structure](readme_images/file_structure.png)

* Open Anaconda Prompt and navigate to repo folder
* Create virtual environment
* Activate virtual environment
* Install required libraries: Dash, Dash Bootstrap Components, Pandas, Spyder
* Open Spyder
```
$ git clone https://github.com/shanemmattner/Dash_Multipage.git
$ conda create --name dash_multi
$ conda activate dash_multi
$ conda install dash pandas dash-bootstrap-components spyder
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
* [Plotly Fundamentals](https://plotly.com/python/plotly-fundamentals/)
* [Dash Python User Guide](https://dash.plotly.com/)
* [Graph Examples and Reference](https://dash.plotly.com/dash-core-components/graph)
* [All about the Graph Component - Python Dash Plotly](https://www.youtube.com/watch?v=G8r2BB3GFVY)
* [Visualization with Plotly.Express: Comprehensive guide](https://towardsdatascience.com/visualization-with-plotly-express-comprehensive-guide-eb5ee4b50b57)
* [How to Build a Reporting Dashboard using Dash and Plotly](https://towardsdatascience.com/how-to-build-a-complex-reporting-dashboard-using-dash-and-plotl-4f4257c18a7f)
##### Dash Draw Lines & Edit Graph
* [Shapes in Python](https://plotly.com/python/shapes/)
* [Python Figure Reference: layout.shapes](https://plotly.com/python/reference/layout/shapes/)
* [Interactive annotations and shape drawing in plotly figures and Dash apps](https://eoss-image-processing.github.io/2020/05/06/shape-drawing.html)
* [Configuration in Python](https://plotly.com/python/configuration-options/#configuring-figures-in-dash-apps)
* [Draw lines and save them](https://community.plotly.com/t/draw-lines-and-save-them/13162)
* [Horizontal and Vertical Lines and Rectangles in Python](https://plotly.com/python/horizontal-vertical-shapes/)
* [FUN THINGS TO DO WITH GRAPH CONFIGURATIONS IN DASH](https://chrisvoncsefalvay.com/2019/12/09/plotly-dash-graph-configuration/)
* [Preserving UI State, like Zoom, in dcc.Graph with uirevision with Dash](https://community.plotly.com/t/preserving-ui-state-like-zoom-in-dcc-graph-with-uirevision-with-dash/15793)
* [Exploring a “Transitions” API for dcc.Graph](https://community.plotly.com/t/exploring-a-transitions-api-for-dcc-graph/15468)
* [Interactive Visualizations](https://dash.plotly.com/interactive-graphing)
##### Hankel
* [OpenHantek6022](https://github.com/OpenHantek/OpenHantek6022)
* [Hantek Downloads](http://www.hantek.com/products/detail/31)
* [Hantek6022BE Driver](http://www.hantek.com/Product/Hantek6000/HT6022_Driver.zip)
* [Hantek6022BE SDK](http://www.hantek.com/Product/Hantek6000/HT6022_SDK.zip)
* [Hantek6022BE Manual](http://www.hantek.com/Product/Hantek6000/Hantek6022BE_Manual.pdf)
* [Interactive Graphing with Callbacks](https://dash.plotly.com/dash-core-components/graph)
##### Postgresql
* [Building a distributed time-series database on PostgreSQL](https://blog.timescale.com/blog/building-a-distributed-time-series-database-on-postgresql/)









