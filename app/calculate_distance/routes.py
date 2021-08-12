import logging
import logging.handlers
import requests
import json
from flask import jsonify, request, flash, redirect, render_template
from datetime import datetime
from config import Config
from app.calculate_distance import bp
from geopy.distance import distance

# Creating current time object (day/month/year, hour:min:sec format)
# to add time to log file.
now = datetime.now()
current_time = now.strftime("%d/%m/%y, %H:%M:%S")


# Rotating Log Files
LOG_FILENAME = 'results.log'

# Set up a specific logger with desired output level
results_logger = logging.getLogger('ResultsLogger')
results_logger.setLevel(logging.INFO)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=20000000, backupCount=5)
results_logger.addHandler(handler)


def get_distance(address: str):

    """ a str type address data expecting function.
    It takes the address and returns the latitude & longitude of it by using
    geopy distance method.
    Returned altitude & longitude data is geopy.distance.geodesic type.
    If the address is not valid or not found returns an error message."""

    url = "https://geocode-maps.yandex.ru/1.x/?apikey=" + \
        Config.API_KEY+"&geocode="+address+"&lang=en_US&format=json"

    # Getting the JSON output from Yandex GeoCoder
    try:
        url_response = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"
    data = json.loads(url_response.text)

    if int(data['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found']) == 0:
        return Config.ERROR_MESSAGE
    else:
        # Getting latitude & longitude data from JSON.
        dest_coordinates = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(" ")
        # Converting str type data to float type.
        coordinates_as_floats = [float(item) for item in dest_coordinates]

    # Checking the coordinates if they are inside the Moscow Ring Road.
    # If not returns the distance between locations in km.
    if (Config.MKAD_COORDINATES[0][0] < coordinates_as_floats[0] < Config.MKAD_COORDINATES[0][1]) \
            and (Config.MKAD_COORDINATES[1][0] < coordinates_as_floats[1] < Config.MKAD_COORDINATES[1][1]):
        return Config.TARGET_IN_MKAD_MESSAGE
    else:
        # Getting the distance with geopy distance method.
        return distance(Config.MKAD_CENTER, coordinates_as_floats)


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("calculate_distance/index.html")
    else:
        address = request.form['address']
        if len(address) == 0:
            # Returns error message from config file if the address field is posted empty
            flash(Config.ADDR_EMPTY)
            return redirect(request.url)
        else:
            distance_data = get_distance(request.form['address'])
            # Writing the result to log file
            results_logger.info(f"{current_time} - Address: {address}, Result: {distance_data}")
            return render_template("calculate_distance/index.html", distance_data=distance_data, address=address)
