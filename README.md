# Excel-Project
Automate an Excel spreadsheet to fill out forms with hospital and bank contact information.

What it currently does:

1) Uses openpyxl to read the first page of a spreadsheet and prompts the user for a cell input for testing purposes (please use something like A2-An where n is some kind of natural number). 

2) The information from the given cell is pulled and a Google Search is done with the data. 

3) From a successful Google search result, the place_id number is taken and used to get a beautiful piece of JSON which I isolate the pieces of data I need (formatted_address, county, state, website, phone number).

Goals:

Iterate through each row in a sheet.
Fill that row with the parsed data. 
Move onto the next sheet until all sheets are filled.

