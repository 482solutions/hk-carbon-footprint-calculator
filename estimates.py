import requests
import json
  
# Calculate CO2 emission based on distance
class distance_estimate:
    def __init__(self) -> None:
        #Set up header with api key from 'apikey.json'
        content = open('apikey.json')
        keys = json.load(content)
        api_key = keys['climatiq']
        authorization = 'Bearer ' + api_key
        self.url = 'https://beta3.api.climatiq.io/estimate'
        self.headers = { 'Authorization': authorization}
        
        #Set up parameters to get information from climatiq. For now, we're using a electric scooter as a rough estimation
        emission_factor = {'uuid': 'ac170d53-2a16-4658-95e5-1dbda1a12dbd' }
        parameters = {'distance': 0, 'distance_unit': 'nil'}
        self.data = {'emission_factor': emission_factor, 'parameters': parameters}


    def add_parameters(self, distance, distance_unit) -> None:
        #Add distance and distance unit into post request data
        self.data['parameters']['distance'] = distance
        self.data['parameters']['distance_unit'] = distance_unit
    
    def calculate(self) -> dict:
        #Query with post request and return a dict
        response = requests.post(url=self.url, data=json.dumps(self.data), headers=self.headers)
        content_json = response.text
        return json.loads(content_json)

#Calculate C02 based on location
class location_intensity:
    def __init__(self) -> None:
        #Set up header with api key from 'apikey.json'
        content = open('apikey.json')
        keys = json.load(content)
        authorization = keys['location']
        self.url = 'https://api.co2signal.com/v1/latest?'
        self.headers = { 'auth-token': authorization}
        self.parameters = {'lon': 0.0, 'lat': 0.0}
    
    def add_parameters(self, lon, lat) -> None:
        self.parameters['lon'] = lon
        self.parameters['lat'] = lat

    def calculate(self) -> dict:
        response = requests.get(url=self.url, params=self.parameters, headers=self.headers)
        content_json = response.text
        return json.loads(content_json)

#Calculate C02 based on time and energy
class energy_estimate:
    def __init__(self) -> None:
        pass
    
    def calculate(self, carbon_kwh, time = 60) -> str:
        # Formula derived from https://carbonfund.org/calculation-methods/
        # Calculate the amount of C02 by converting to KG, then calculate based on time
        carbon_kg = carbon_kwh * 0.371
        carbon_emission = carbon_kg/60 * time
        return carbon_emission
 
#For testing purposes, uncomment if you want to test the class
if __name__ == "__main__":
    #Testing distance estimation
    a = distance_estimate()
    a.add_parameters(20,'km')
    print(a.calculate())

    #Testing location CO2 intensity
    a = location_intensity()
    a.add_parameters(6.8770394, 45.9162776)
    print(a.calculate())

    #Testing enery estimation based on time and energy
    a = energy_estimate()
    print(a.calculate(93, 60))
    

