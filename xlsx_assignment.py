import xlsxwriter

data = {
    'Ind': {
        'Guj': ['Ahmedabad', 'Gandhinagar'],
        'Raj': ['Udaipur', 'Jodhpur'],
    },
    'Pak': {
        'Guj': ['Ahmedabad', 'Gandhinagar'],
        'Raj': ['Udaipur', 'Jodhpur'],
    }
}

xlsx_filename = 'countries_states_cities_xlsxwriter.xlsx'

workbook = xlsxwriter.Workbook(xlsx_filename)
worksheet = workbook.add_worksheet()

header_format = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#D9D9D9'})

headers = ['Country', 'State', 'City']
worksheet.write_row('A1', headers, header_format)

row = 1
col = 0

prev_country = None
prev_state = None

for country, states in data.items():
    for state, cities in states.items():
        for city in cities:
            if country != prev_country:
                worksheet.write(row, col, country)

            if state != prev_state or country != prev_country:
                worksheet.write(row, col + 1, state)

            worksheet.write(row, col+ 2, city)

            prev_country = country
            prev_state = state
            row += 1

workbook.close()

print(f"XLSX file '{xlsx_filename}' created successfully using XlsxWriter.")
