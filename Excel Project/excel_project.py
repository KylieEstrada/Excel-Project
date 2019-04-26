# coding=utf-8
import googlemaps
import json
import openpyxl

class ContactInfo():
    """
    Creates an object with all the data needed as well as a method to parse through the JSON data
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
        

def get_place_name(): # Pulls data from the given spreadsheet if the given cell has a value.

    place_column = input('Prompt: ')
    wb = openpyxl.load_workbook("hospital_prospects.xlsx")
    ws = wb.active
    place_name = ws[place_column].value

    if place_name == None:
        exit()
    else:
        return place_name

def get_place_search(place_name): # This uses the google maps to perform a search on the cell data

    places_search = gmaps.places(
        query = place_name, 
        radius = "3000"
        )

    try:
        place_id = (places_search["results"][0]["place_id"])
        place_id_search = gmaps.place(place_id)
        return place_id_search

    except:
        print(place_name)
        print(json.dumps(places_search, indent=4))
        exit()

api_key = 'YOUR_API_KEY'
gmaps = googlemaps.Client(api_key)

def main(): # testing area for now
    name = get_place_name() 
    place_id_result = get_place_search(name)
    place_data = ContactInfo()
    place_data.assign_place_data(place_id_result)
    print(place_data.street_number + " " + place_data.street_name + " " + place_data.county 
           + " " + place_data.state + " " + place_data.website + " " + place_data.phone)

if __name__ == '__main__':
        main()





