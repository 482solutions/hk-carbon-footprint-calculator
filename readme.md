# hk_carbon_footprint_calculator

## Description
There are 3 classes in the file that calculates CO2 emission based on distance, location or time & energy. No additional libraries are used.

### Quickstart
To run and test all of the functions.
```python
python3 estimates.py
```

## Estimate based on distance
It uses an api from [climatiq](https://www.climatiq.io/explorer) to estimate CO2 emission based on the distance and type of vehicle. Since they do not have a data in regards to autonomous robots, we're using an electric vehicle as the base.

To use that portion, simply uncomment this portion and run.
Parameters used are: distance, distance unit
```python
if __name__ == "__main__":
    #Testing distance estimation
    a = distance_estimate()
    a.add_parameters(20,'km')
    print(a.calculate())
```

## Estimate based on location
It uses an api from [co2signal](https://www.co2signal.com/) to estimate CO2 emission intensity based on the location (lon, lat). 

To test that portion, simply uncomment this portion and run
Parameters used are: longtitude, latitude
```python
if __name__ == "__main__":
    #Testing location CO2 intensity
    a = location_intensity()
    a.add_parameters(6.8770394, 45.9162776)
    print(a.calculate())
```

## Estimate based on time and energy
If a user have the information of the amount of carbon emitted in kwh, this function will take that as a based and calculate carbon emission. 

To test that portion, simply uncomment this portion and run.
The code below is based of an example of a truck that emitted 10 kwh for 60 minutes.
```python
if __name__ == "__main__":
    #Testing enery estimation based on time and energy
    a = energy_estimate()
    print(a.calculate(10, 60))
```

