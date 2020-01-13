"""

 Purpose of the program:  This program uses an open API and interacts with a webservice in order to obtain data. This
 program will prompt the user for their city or zip code and request weather forecast data from 'OpenWeatherMap' and
 displays the weather information in a READABLE format to the user.

 Assignment number: 12.1
 Name: Srilakshmi Bodduluru
 Date: 5/31/2019

"""

# defining  get_service_url()
def get_service_url():

    # enter API key
    api_key = "16248e53ed798a8784729b025334d6d0"

    # Assigning url
    serviceurl = "http://api.openweathermap.org/data/2.5/weather?&units=imperial&id=524901&APPID=" + api_key + "&q="

    # return serviceurl
    return serviceurl


# defining execute_request()
def execute_request(url):

    import requests

    # prints retrieving message to user
    print ("Retrieving weather report from 'OpenWeatherMap'")

    # get or retrieve data from url and assign it to 'response' variable
    response = requests.get(url)

    #using a Response instance in a conditional expression(if), it will evaluate to True if the status code was
    # between 200 and 400 and prints sucessful, and False otherwise and prints error message to the user.
    if response:
        print('\33[32m ' + 'Request Successful!' + '\033[0m' )
    else:
        print('\033[91m ' + 'city not found. Please enter a valid city name or zipcode.' + '\033[0m')

    # loads json data to raw_json_data
    raw_json_data = response.json()

    # returns raw json data
    return raw_json_data


# defining extract_details_and_print()
def extract_details_and_print(raw_json_data):

    import datetime

    # extracting location variable from data
    location = raw_json_data["name"]

    # store the value of "main" key in variable y
    y = raw_json_data["main"]

    # store the value of "temp" in current_temperature
    current_temperature = y["temp"]

    # store the value of "pressure" in current_pressure
    current_pressure = y["pressure"]

    # store the value of "humidity" in current_humidiy
    current_humidiy = y["humidity"]

    # store the value of "weather" key in variable z
    z = raw_json_data["weather"]

    # store the value corresponding to the "description" key at the 0th index of z as weather_description
    weather_description = z[0]["description"]

    #extracting wind speed from data
    wind_speed = raw_json_data["wind"]["speed"]

    #extracting timestamp from data
    date = raw_json_data["dt"]

    # converting timestamp to datetime and printing Date & Time
    print('\33[32m ' +"Date & Time:",datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')+'\033[0m')

    # print the following values
    print('\33[34m'+"***************************************"+
            "\n\t\t \tWEATHER INFORMATION" +
            "\n***************************************" + '\033[0m'
            "\n Location :" + '\33[34m' + str(location) + '\033[0m'
            "\n Temperature (in Fahrenheit) : " +
            '\33[34m' + str(current_temperature) + '\033[0m' +
            "\n Atmospheric pressure (in hPa) : " +
            '\33[34m' + str(current_pressure) + '\033[0m' +
            "\n Humidity (in percentage) : " +
            '\33[34m'+ str(current_humidiy) + '\033[0m' +
            "\n Weather description : " +
            '\33[34m'+ str(weather_description)+ '\033[0m' +
            "\n Wind speed (in mi/hr) :" +
            '\33[34m'+ str(wind_speed)+ '\033[0m' +
            '\33[34m' + "\n****************************************" + '\033[0m')

# Defining main()
def main():
    import requests

    # printing welcome message for user
    print('\33[1m ' +'\33[32m ' +" HELLO USER! " +'\033[0m')

    # using while loop to allow the user to run the program multiple times to allow them to look up weather conditions
    # for multiple locations
    while True:
        address = input("Please enter 'city name' or 'zip code' then comma then 2-letter country code "
                    "\n (Example - London, GB or New York, US)or 'x' to end this program:")

        # if user enters 'x' it ends the program and prints message to user
        if (address == 'x') or (address == 'X'):
            print('\033[91m ' + '\n****Thank you! End of the program**** '+'\033[0m')
            break

        # error checking for valid input. if length of the address is less than 2, inform user
        if len(address) < 2:
            print('\033[91m '+"Please enter a valid city name"+'\033[0m')
            continue

        # adding address to service url
        url = get_service_url() + address

        # using try-except block to print weather forecast to the user
        try:

            # calling execute_request() to execute request and return weather data in json format
            raw_json_data = execute_request(url)

            # error checking for invalid input from user
            # if no valid data available skip the next process
            if raw_json_data['cod'] == '404':
                continue
            # else extract details from data
            else:
                # calling extract_details_and_print() to extract weather details and print
                extract_details_and_print(raw_json_data)

        # prints message to user if unable to open url
        except requests.exceptions.ConnectionError as errc:
            # handle ConnectionError exception
            print('\033[91m ' +'***Connection Failure. Please try later.***'+'\033[0m')
            break

        # handle all other exceptions
        except Exception as e:
            print('\033[91m '+"Failure to Retrieve.Please try again"+'\033[0m')

# main function starts here:
if __name__=='__main__':

  # calls main function
  main()




