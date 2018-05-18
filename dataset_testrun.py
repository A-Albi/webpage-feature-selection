import scraper
import calculations
import numpy as np

# CSE 5820
# April 29, 2018

# Run this file to perform the statistics on websites listed in legit.txt and fake_checked-Copy.txt.
# This program utilizes the calculations.py file and the scraper.py file

# We define our parameters, the sample size t_size, the text file with fake sites, and the text file with real sites.

t_size = 0.33
num_features = 3
count = 0
urls = np.array([])
labels = np.array([])
fake_sites = open("fake_checked-Copy.txt", "r")
legit_sites = open("legit.txt", "r")

print("Loading website links...")

# We append the list of urls and the array of labels simultaneously.

for line in fake_sites:
    urls = np.append(urls, "http://www." + line)
    labels = np.append(labels, 1)
    count += 1
for line in legit_sites:
    urls = np.append(urls, line)
    labels = np.append(labels, 0)
    count += 1

print("Scraping website data...")

# We scrape data for these urls and store it into a data set of features for every url.

data_set = np.zeros((count, 12))
for i in range(count):
    try:
        print(urls[i])
        data_set[i, :] = scraper.extract(urls[i])
    except:
        continue

# We obtain the chi-squared, information gain, and pca values of each feature.

print("Chi-Squared Features Priority")
chi_squared_values = calculations.chi_squared(data_set, labels)
print(chi_squared_values)
print("Information Gain Feature Priority")
information_gain_values = calculations.information_gain(data_set, labels)
print(information_gain_values)
print("Principal Component Analysis Feature Priority")
principal_components_values = calculations.principal_component_analysis(data_set)
print(principal_components_values)

# For each technique, we prioritize the top k features and feed them into the Support Vector Machine,
# where its performance is evaluated.

print("Chi-Squared Performance")
print(calculations.support_vector_machine(data_set[:, chi_squared_values[0:num_features]], labels, t_size))
print("Information Gain Performance")
print(calculations.support_vector_machine(data_set[:, information_gain_values[0:num_features]], labels, t_size))
print("Principal Components Performance")
print(calculations.support_vector_machine(data_set[:, principal_components_values[0:num_features]], labels, t_size))
fake_sites.close()
legit_sites.close()
