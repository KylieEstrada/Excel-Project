# coding=utf-8
import openpyxl
import googlemaps
import json

#class spreadsheetData():
#    """
#    Should but won't create an object w/spreadsheet, column and thus row values. Should be just a function.
#    """
#    def __init__(self, workbook, worksheet, place_name, column):
#        self.workbook = workbook
#        self.worksheet = worksheet
#        self.place_name = place_name
#        self.column = column

#    def get_place_name(self, ):
#        self.column = prompted_column

#class placeData():

#    """
#    Should but won't create an array with all the data of a specific place
#    """
#    def create_row(self):
#        self.row_info = []

#    def row_instert(self, place_info)
#        self.row_info.append(place_info)

#    def print_data(self):
#        print(*self.row_info)

api_key = 'AIzaSyDDivYJzpW-tpXCbmqgQAxkVQfqXLEsiS0'
gmaps = googlemaps.Client(api_key)

place_column = input('Prompt: ')
wb = openpyxl.load_workbook("hospital_prospects.xlsx")
ws = wb.active
place_name = ws[place_column].value

places_search = gmaps.places(
    query = place_name, 
    type = "hospital")
place_id = (places_search["results"][0]["place_id"])

place_id_search = gmaps.place(place_id)
place_id_json = json.dumps(place_id_search, indent=2)

formatted_address = place_id_search["result"]["formatted_address"]
split_address = formatted_address.split(", ")
place_county = place_id_search["result"]["address_components"][3]["short_name"]
place_state = place_id_search["result"]["address_components"][4]["short_name"]
place_website = place_id_search["result"]["website"]
place_phone = place_id_search["result"]["formatted_phone_number"]

row_data = []

row_data.append(split_address[0])
row_data.append(split_address[1])
row_data.append(place_county)
row_data.append(place_state)
row_data.append(place_website)
row_data.append(place_phone)

print(*row_data)






