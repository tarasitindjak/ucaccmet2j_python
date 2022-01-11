import json

# Opening precipitation.json
with open('precipitation.json') as precipitation_file:
    data = json.load(precipitation_file)

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
                
monthly_p = print(f'Monthly precipitation in Seattle: {sum_month}')

with open('result1.json', 'w') as seattle_p_file:
        json.dump(sum_month, seattle_p_file)

