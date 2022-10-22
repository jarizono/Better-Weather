#Downloading weather data using Python as a CSV using the Visual Crossing Weather API
#See https://www.visualcrossing.com/resources/blog/how-to-load-historical-weather-data-using-python-without-scraping/ for more information.
import csv
import codecs
import urllib.request
import urllib.error
import sys
# import requests

if __name__ == '__main__':

# This is the core of our weather query URL
    BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

    ApiKey='ESVDJCXR83MMMX2MQFC7FUGE6'
    #UnitGroup sets the units of the output - us or metric
    UnitGroup='us'

    #Location for the weather data
    Location='Atlanta,GA'

    #Optional start and end dates
    #If nothing is specified, the forecast is retrieved.
    #If start date only is specified, a single historical or forecast day will be retrieved
    #If both start and and end date are specified, a date range will be retrieved
    StartDate = ''
    EndDate=''

    #JSON or CSV
    #JSON format supports daily, hourly, current conditions, weather alerts and events in a single JSON package
    #CSV format requires an 'include' parameter below to indicate which table section is required
    ContentType="csv"

    #include sections
    #values include days,hours,current,alerts
    Include="days"


    print('')
    print(' - Requesting weather : ')

    #basic query including location
    ApiQuery=BaseURL + Location

    #append the start and end date if present
    if (len(StartDate)):
        ApiQuery+="/"+StartDate
        if (len(EndDate)):
            ApiQuery+="/"+EndDate

    #Url is completed. Now add query parameters (could be passed as GET or POST)
    ApiQuery+="?"

    #append each parameter as necessary
    if (len(UnitGroup)):
        ApiQuery+="&unitGroup="+UnitGroup

    if (len(ContentType)):
        ApiQuery+="&contentType="+ContentType

    if (len(Include)):
        ApiQuery+="&include="+Include

    ApiQuery+="&key="+ApiKey



    print(' - Running query URL: ', ApiQuery)
    print()

    try:
        CSVBytes = urllib.request.urlopen(ApiQuery)
        # resp = requests.get(ApiQuery)
    except urllib.error.HTTPError  as e:
        ErrorInfo= e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except  urllib.error.URLError as e:
        ErrorInfo= e.read().decode()
        print('Error code: ', e.code,ErrorInfo)
        sys.exit()


    # Parse the results as CSV
    CSVText = csv.reader(codecs.iterdecode(CSVBytes , 'utf-8'))

    RowIndex = 0

    # The first row contain the headers and the additional rows each contain the weather metrics for a single day
    # To simply our code, we use the knowledge that column 0 contains the location and column 1 contains the date.  The data starts at column 4
    weatherDict = {}
    for Row in CSVText:
        if RowIndex == 0:
            FirstRow = Row
        else:
            print('Weather in ', Row[0], ' on ', Row[1])
            weatherDict[Row[1]] = []

            ColIndex = 0
            for Col in Row:
                if ColIndex >= 4:
                    weatherDict[Row[1]].append(FirstRow[ColIndex])
                    weatherDict[Row[1]].append(Row[ColIndex])
                    #print('   ', FirstRow[ColIndex], ' = ', Row[ColIndex])
                ColIndex += 1
        RowIndex += 1
    print(weatherDict)
    # If there are no CSV rows then something fundamental went wrong
    if RowIndex == 0:
        print('Sorry, but it appears that there was an error connecting to the weather server.')
        print('Please check your network connection and try again..')

    # If there is only one CSV  row then we likely got an error from the server
    if RowIndex == 1:
        print('Sorry, but it appears that there was an error retrieving the weather data.')
        print('Error: ', FirstRow)

    print()

    print("BETTER WEATHER")
    print()
    print("Your one stop platform to know how you should dress, what you should carry, and what to expect from the weather today!")
    print("You can check the weather on any day you want 2 weeks from now!")
    print()
    # date = input("Enter the date YYYY-MM-DD: ")
    date = '2022-10-22'

    details = weatherDict[date]

    temp = float(details[1])
    precip = float(details[15])
    # humidity = float(details[11]) The humidity feature can be added on later
    # wind = float(details[27]) Wind also can be added later, not required for the MVP
    sun = float(details[37])

    print()
    print("TODAY'S PREDICTIONS:")

def tempToday(temp):
    if temp >= 60.0:
        return "It's the perfect summery weather, dress light!"

    elif temp < 60.0 and temp >= 50.0:
        return "It's chilly, grab a sweater on your way out!"

    elif temp < 50.0 and temp >= 40.0:
        return "It's cold, grab a scarf and layer up!"

    elif temp < 40.0 and temp >= 32.0:
        return "It's quite cold outside! Make sure to wear a coat!"

    elif temp < 32.0:
        return "It's freezinggg! Stay inside or bundle up!!"


print("Temperature is", temp, " deg F ", tempToday(temp))

def precipToday(precip):
    if precip > 0:
        return "Rain predictions, Carry an umbrella!"

    else:
        return "No rain predictions, no need for an umbrella."

print(precipToday(precip))

def sunToday(sun):
    if sun < 400:
        return "Beware of UV rays, wear sunscreen to protect your skin!"

    else:
        return "It's not that sunny today, sunscreen not essential."

print(sunToday(sun))

print()
print("You're all set to deal with the weather today, have a great day :)")