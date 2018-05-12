import json
from pprint import pprint
import pandas

# all_countries=[]
# with open('data.json') as data_file:
#     data = json.load(data_file)
# for i in range(len(data.get('fact'))):
#     one_country=[]
#     if data.get('fact')[i].get('dims').get('SEX') == 'Both sexes' and data.get('fact')[i].get('dims').get('YEAR') == '2015':
#         one_country.append(data.get('fact')[i].get('dims').get('COUNTRY'))
#         one_country.append(data.get('fact')[i].get('Value'))
#         all_countries.append(one_country)
# for i in range(len(all_countries)):
#     all_countries[i].append(i)
# pprint(all_countries)

with open('data.json') as data_file:
    data = json.load(data_file)

countries=[]
rates=[]
ids=[]


USA="Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, " \
    "Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota," \
    " Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, " \
    "North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Tennessee, Texas," \
    " Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming"
USA_list=[]
for i in USA.split(", "):
    USA_list.append(i)



for i in range(len(data.get('fact'))):
     if data.get('fact')[i].get('dims').get('SEX') == 'Both sexes'and data.get('fact')[i].get('dims').get('YEAR') == '2015':
        if data.get('fact')[i].get('dims').get('COUNTRY') == "Russian Federation":
            countries.append("Russia")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "United Republic of Tanzania":
            countries.append("Tanzania")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "United States of America":
            usa = data.get('fact')[i].get('Value')
            for k in USA_list:
                countries.append(k)
                rates.append(usa)
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Iran (Islamic Republic of)":
            countries.append("Iran")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Grenada":
            countries.append("Greenland")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Syrian Arab Republic":
            countries.append("Syria")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Viet Nam":
            countries.append("Vietnam")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Venezuela (Bolivarian Republic of)":
            countries.append("Venezuela")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Bolivia (Plurinational State of)":
            countries.append("Bolivia")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Bosnia and Herzegovina":
            countries.append("Bosnia and Herz.")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Brunei Darussalam":
            countries.append("Brunei")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Central African Republic":
            countries.append("Central African Rep.")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Democratic People's Republic of Korea":
            countries.append("Dem. Rep. Korea")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Democratic Republic of the Congo":
            countries.append("Dem. Rep. Congo")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Dominican Republic":
            countries.append("Dominican Rep.")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Equatorial Guinea":
            countries.append("Eq. Guinea")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Republic of Korea":
            countries.append("Korea")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Republic of Moldova":
            countries.append("Moldova")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "The former Yugoslav republic of Macedonia":
            countries.append("Macedonia")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "United Kingdom of Great Britain and Northern Ireland":
            countries.append("United Kingdom")
            rates.append(data.get('fact')[i].get('Value'))
        elif data.get('fact')[i].get('dims').get('COUNTRY') == "Lao People's Democratic Republic":
            countries.append("Lao PDR")
            rates.append(data.get('fact')[i].get('Value'))
        else:
            countries.append(data.get('fact')[i].get('dims').get('COUNTRY'))
            rates.append(data.get('fact')[i].get('Value'))


for i in range(len(countries)):
    ids.append(i)
print(countries)

df = pandas.DataFrame(data={"id": ids, "country": countries, "rate": rates})
df.to_csv("./both_sexes_2015_data.csv", sep=',',index=False)