import csv

data = {
    'Ind': {
        'Guj': ['Ahmedabad','Gandhinagar'],
        'Raj': ['Udaipur', 'Jodhpur'],
    },
    'Pak':{
        'Guj': ['Ahmedabad','Gandhinagar'],
        'Raj': ['Udaipur', 'Jodhpur'],
    }
}

csv_filename = 'countries_states_cities.csv'


with open(csv_filename,'w',newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['Country','State','City'])

    last_country = None
    last_state = None

    for country,states in data.items():
        for state,cities in states.items():
            for city in cities:
                country_to_print = country if country != last_country else ''
                state_to_print = state if state != last_state else ''

                writer.writerow([country_to_print,state_to_print,city])
                last_country = country
                last_state = state

print(f"CSV file {csv_filename} created successfully.")

