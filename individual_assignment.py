import pandas as pd
from scipy import stats
from data import Data

badpackets = pd.read_csv("data_miraibadpackets.csv", sep=";")

# for each country count how many entries there are in the dataset
countries = list(badpackets.Country.dropna().unique())
countries.remove('—')  # remove some anomaly

counts_country = dict()
count = 0
total_countries = len(countries)
for country in countries:
    if count % 10 == 0:
        print("{0:.1f}%".format(count/float(total_countries)*100), end='\r')
    counts_country[country] = badpackets.Country.str.count(country).sum()
    count += 1

print("100.0%")

brands = {"Axis" : Data.axis, "Cisco" : Data.cisco, "Dahua" : Data.dahua, "Huawei" : Data.huawei, "MikroTik" : Data.mikrotik, "Panasonic" : Data.panasonic, "RealTek" : Data.realtek, "Samsung" : Data.samsung, "Ubiquiti" : Data.ubiquiti, "ZTE" : Data.zte, "ZyXel" : Data.zyxel}

# Create two lists with the total amount of infections in a country and the 
# amount of devices of a brand in that same country and calculate the pearson
# correlation.
print("IoT hardware brand & Correlation & P-value \\\\")
for brand in brands.values():
    infection_count = list()
    brand_count = list()
    for country in brand.keys():
        count = counts_country.get(country)
        if count is not None:
            infection_count.append(counts_country.get(country))
            amount = brand.get(country)
            brand_count.append(amount)
    cor_res = stats.pearsonr(infection_count, brand_count)
    print("{0} & {1:.2f} & {2:.2f} \\\\".format(list(brands.keys())[list(brands.values()).index(brand)]
,cor_res[0],cor_res[1]))

# For control purposes, check correlation between total amount of IoT devices
# (from this dataset) and the total amount of infections per country
sum_brands_in_country = list()
for country in countries:
    count = 0
    for brand in brands.values():
        c = brand.get(country)
        if c is not None:
            count += int(c)
    sum_brands_in_country.append(count)

cor = stats.pearsonr(sum_brands_in_country, list(counts_country.values()))
print("Correlation between total amount of IoT devices and total infections observed in countries:")
print("Pearson correlation: {0:.2f}".format(cor[0]))
print("P-value: {0:.2f}".format(cor[1]))
