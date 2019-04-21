# coding=utf-8
import openpyxl
import googlemaps
import json

class contactVector():
    """
    Creates an object with all data to be put into the place row
    """
    def __init__(self, form_address=None, street_number=None, street_name=None, county=None, state=None, website=None, phone=None):
        self.form_address = form_address
        self.street_number = street_number
        self.street_name = street_name
        self.county = county
        self.state = state
        self.website = website
        self.phone = phone

    def assign_place_data(self, place_id_result):
        self.form_address = place_id_result["result"]["formatted_address"].split(", ")
        self.street_number = self.form_address[0]
        self.street_name = self.form_address[1]
        self.county = place_id_result["result"]["address_components"][3]["short_name"]
        self.state = place_id_result["result"]["address_components"][4]["short_name"]
        self.website = place_id_result["result"]["website"]
        self.phone = place_id_result["result"]["formatted_phone_number"]

def get_place_name():
    place_column = input('Prompt: ')
    wb = openpyxl.load_workbook("hospital_prospects.xlsx")
    ws = wb.active
    place_name = ws[place_column].value
    return place_name

def get_place_search(place_name):
    places_search = gmaps.places(
        query = place_name, 
        type = "hospital")
    place_id = (places_search["results"][0]["place_id"])
    place_id_search = gmaps.place(place_id)
    return place_id_search

api_key = 'AIzaSyDDivYJzpW-tpXCbmqgQAxkVQfqXLEsiS0'
gmaps = googlemaps.Client(api_key)

name = get_place_name()
place_id_result = get_place_search(name)
place_data = contactVector()
place_data.assign_place_data(place_id_result)
print(place_data.phone)







