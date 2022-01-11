# Part 3 is unfinished

import json

# Opening precipitation.json
with open('precipitation.json') as precipitation_file:
    data = json.load(precipitation_file)

def city_precipitation():
    # Getting measurements from the Seattle weather station
    seattle_precipitation = []


    for measurement in data:
        if measurement['station'] == 'GHCND:US1WAKG0038':
            seattle_precipitation.append(measurement)


    # Getting monthly precipitation from the Seattle weather station in a list form
    month_values = []
    for dict in seattle_precipitation:
        split_dates = dict['date'].split('-')

        short_list = [split_dates[1], dict['value']]

        month_values.append(short_list)


    # Total precipitation by month
    sum_month = [0,0,0,0,0,0,0,0,0,0,0,0]

    for pair in month_values:
        sum_month[int(pair[0]) - 1] += pair[1]

    with open('result1.json', 'w') as seattle_p_file:
            json.dump(sum_month, seattle_p_file)



    # Annual precipitation
    total_precipitation_year = sum(sum_month)
    print(f'The total annual precipitation in Seattle is: {total_precipitation_year}')

    # The relative precipitation per month
    relative_precipitation = []
    for month in sum_month:
        percentage = month/total_precipitation_year * 100
        relative_precipitation.append(percentage)
    print(f'{relative_precipitation}')


    seattle_precipitation = {}
    seattle_precipitation.update({'station': 'GHCND:US1WAKG0038'})
    seattle_precipitation.update({'state': 'WA'})
    seattle_precipitation.update({'totalMonthlyPrecipitation': sum_month})
    seattle_precipitation.update({'relativeMonthlyPrecipitation': relative_precipitation})
    seattle_precipitation.update({'totalYearlyPrecipitation': total_precipitation_year})

    with open('result2.json', 'w') as seattle_p_file:
            json.dump({'Seattle': seattle_precipitation}, seattle_p_file)

    return sum_month, relative_precipitation, total_precipitation_year

city_precipitation()

# I would have tried to define a function to have Python do this for all the different stations. 
# That way I would be able to enter the station and have it automatically execute the rest of the commands.


