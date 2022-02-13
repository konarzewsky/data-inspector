# DATA INSPECTOR

Go to https://data-inspector.herokuapp.com/ and get to know your data!

Note: loading the app may take a while as it sleeps when there is no user activity, if the app won't load after 1-2 minutes I'd suggest running it localy (description provided below) as it's deployed on free heroku dyno with very limited resources

## Project goal

The most important thing while working on any data related task is to know what exactly is in your dataset. Having a quick glance on your file may not be enough to prepare suitable strategy for your project. Once you know what your data looks like you might want to go deeper and search for some patterns or detailed statistics. Very usefull in understanding your data can be interactive visualisations. You can do it all with the **Data inspector** application.

## Project description

**Data inspector** is a web application used for data analysis and visualisation. Application allows you to upload your own file with data (```csv```,```xls``` and ```xlsx``` formats are supported) and investigate from scratch what exactly does your dataset contain.

Project is based mostly on ```dash```, ```plotly``` and ```pandas``` packages. 

**Data inspector** features:

- table view with possibility of filtering (just as it is)
- information about the shape of your file (number of observations and variables)
- information about all variables (data type, number of unique and missing values)
- descriptive statistics
- advanced visualisations:
    - scatter plot
    - line plot
    - bar plot
    - histogram
    - box plot
    - map
    - correlation plot
- PDF report with dataset characterictics and created graphs (can be directly downloaded or sent to provided email address)

## How to run it locally?

1. Clone this repository
```
git clone https://github.com/konarzewsky/data-inspector.git
```
2. Go to application directory
```
cd data-inspector
```
3. Install ```virtualenv``` if necessary:
```
apt-get install -y python3-venv
```
4. Create virtual environment and install required packages
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```
5. Optional: create ```.env``` file based on ```.env.example``` file

These variables are not required for the application to function properly so this step can be skipped. Only **MAPBOX_ACCESS_TOKEN** variable is necessary to create the map plot. Your can generate your own mapbox access token [here](https://account.mapbox.com/auth/signup/)

6. Run the application
```
python3 app.py
```
7. Go to any web browser and paste link displayed in your terminal

e.g. 
```
Dash is running on http://0.0.0.0:8050/
```
