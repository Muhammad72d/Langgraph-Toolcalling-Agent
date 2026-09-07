from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup

@tool 
def search(query: str) -> str:
    """ useful for searching the web for some information """
    search_tool = DuckDuckGoSearchRun()
    try:
        return search_tool.invoke(query).strip()
    except Exception as e:
        return f"the is an error while searching :{str(e)}"

@tool
def calculator(expression: str) -> str:
    """ useful for doing math calculations """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f" there is an error while claculating the expression :{expression} , error is :{str(e)}"


def get_location_info(location:str) -> str:

    url ="https://geocoding-api.open-meteo.com/v1/search"
    params={
"name":location,
"language":"en",
"count":1,
"format":"json"

         }
    try:
        response = requests.get(url,params=params)
        response.raise_for_status()
        data=response.json()

        if "results" not in data or not data["results"]:
            raise ValueError(f"No location found for '{location}'")
        
        result = data["results"][0]
        return result["latitude"],result["longitude"],result["timezone"]
    except Exception as e:
        return f"there is an error while getting the location information :{str(e)}"


@tool
def get_weather(location:str) -> str:
    """ useful for getting information about the weather of a location """
    latitude,longitude,timezone = get_location_info(location)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": True,
        "timezone": timezone
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        current_weather = data["current"]

        return f""" location : {location}
        temperature : {current_weather['temperature']}C
        wind speed : {current_weather['windspeed']} km/h
        wind direction : {current_weather['winddirection']} degrees"""

    except Exception as e :
        return f" there is an error while getting the weather information : {str(e)}"