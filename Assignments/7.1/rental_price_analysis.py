'''
Student Name: Zihua Li
Assignment 7.1: Rental Price Analysis
This is a script that creates a report generator that takes in an input CSV file containing rental prices
in a specific housing market and generates a text file report.
Citation: No help from others received or used any resources to accomplish this assignment.
'''

# defining a function that gets the intermediate (semi-finished) data values from a .csv file
def get_values(file_name):
    import csv
    with open(file_name, "r", newline='') as csv_file:
        # using csv.DictReader to combine the header columns of the csv file into the dict automatically
        reader = csv.DictReader(csv_file)
        # initializing variables
        rent_sum_2021 = 0
        rent_sum_2020 = 0
        addresses_prices_2021 = {}
        addresses_prices_2020 = {}
        addresses_prices_diff = {}
        neighborhood_avg_price_2021 = {}
        neighborhood_avg_price_2020 = {}
        # a for loop to calculate the values of each line for intermediate variables
        for row in reader:
            # this is for average rent 2021, also removing the spaces after the commas
            # cuz DictReader will put the space after the comma into the next key value
            rent_2021 = list(row[" 2021 Rent"])
            rent_2021.remove(" ")
            rent_2021.remove("$")
            # joining characters together, forming new variables, clean means they are calculable
            clean_value_2021 = ''.join([str(element) for element in rent_2021])
            clean_value_2021 = int(clean_value_2021)
            # adding up the sum
            rent_sum_2021 += clean_value_2021
            # this is for highest and lowest rent 2021
            addresses_prices_2021[row["Address"]] = clean_value_2021
            # this is for average rent 2020, same as in rent_2021
            rent_2020 = list(row[" 2020 Rent"])
            rent_2020.remove(" ")
            rent_2020.remove("$")
            clean_value_2020 = ''.join([str(element) for element in rent_2020])
            clean_value_2020 = int(clean_value_2020)
            rent_sum_2020 += clean_value_2020
            # this is for highest and lowest rent 2020
            addresses_prices_2020[row["Address"]] = clean_value_2020
            # this is for price change, appending keys and values into the dictionary
            # which values are clean_value_2021 subtracts clean_value_2020, obtaining the difference
            addresses_prices_diff[row["Address"]] = clean_value_2021 - clean_value_2020
            # this is for each neighborhood's 2021 average rent price
            # removing the spaces, same as in rent_2021
            neighborhood_price_2021 = list(row[" 2021 Rent"])
            neighborhood_price_2021.remove(" ")
            neighborhood_price_2021.remove("$")
            clean_neighborhood_price_2021 = ''.join([str(element) for element in neighborhood_price_2021])
            clean_neighborhood_price_2021 = int(clean_neighborhood_price_2021)
            # if key " Neighborhood" is found in dict "neighborhood_avg_price_2021"
            # then append the value into the list in the value of that key
            if row[" Neighborhood"] in neighborhood_avg_price_2021.keys():
                neighborhood_avg_price_2021[row[" Neighborhood"]].append(clean_neighborhood_price_2021)
            # if not found, then create a list in the value of that key
            else:
                neighborhood_avg_price_2021[row[" Neighborhood"]] = [clean_neighborhood_price_2021]
            # this is for each neighborhood's 2020 average rent price
            # same as in neighborhood_price_2021
            neighborhood_price_2020 = list(row[" 2020 Rent"])
            neighborhood_price_2020.remove(" ")
            neighborhood_price_2020.remove("$")
            clean_neighborhood_price_2020 = ''.join([str(element) for element in neighborhood_price_2020])
            clean_neighborhood_price_2020 = int(clean_neighborhood_price_2020)
            if row[" Neighborhood"] in neighborhood_avg_price_2020.keys():
                neighborhood_avg_price_2020[row[" Neighborhood"]].append(clean_neighborhood_price_2020)
            else:
                neighborhood_avg_price_2020[row[" Neighborhood"]] = [clean_neighborhood_price_2020]
        # final values (and also globalizing these values for further use in other function)
        global avg_rent_2021
        # assign all the values of the keys in dict "addresses_price_2021" into list "all_prices_2021"
        all_prices_2021 = addresses_prices_2021.values()
        # division, to get the average rent
        avg_rent_2021 = rent_sum_2021 / len(all_prices_2021)
        global max_rent_2021
        # obtaining the highest value through max() in the 1st element of the created list, 2nd element is the address
        max_rent_2021 = [max(addresses_prices_2021.values()),
                         max(addresses_prices_2021, key=addresses_prices_2021.get)]
        global min_rent_2021
        # same as in max_rent_2021
        min_rent_2021 = [min(addresses_prices_2021.values()),
                         min(addresses_prices_2021, key=addresses_prices_2021.get)]
        global avg_rent_2020
        # same as in avg_rent_2021
        all_prices_2020 = addresses_prices_2020.values()
        avg_rent_2020 = rent_sum_2020 / len(all_prices_2020)
        global max_rent_2020
        # same as in max_rent_2021
        max_rent_2020 = [max(addresses_prices_2020.values()),
                         max(addresses_prices_2020, key=addresses_prices_2020.get)]
        global min_rent_2020
        # same as in min_rent_2021
        min_rent_2020 = [min(addresses_prices_2020.values()),
                         min(addresses_prices_2020, key=addresses_prices_2020.get)]
        global avg_rent_change
        # this is easy, simple subtraction
        avg_rent_change = avg_rent_2021 - avg_rent_2020
        global max_rent_change
        # almost the same as in above functions like max_rent_2021, etc..,
        # obtaining key and values in dict "addresses_prices_diff"
        max_rent_change = [max(addresses_prices_diff.values()),
                           max(addresses_prices_diff, key=addresses_prices_diff.get)]
        global min_rent_change
        # same as in max_rent_change
        min_rent_change = [min(addresses_prices_diff.values()),
                           min(addresses_prices_diff, key=addresses_prices_diff.get)]
        # this for loop is to obtain affordability of the neighborhoods
        for neighborhood_name in neighborhood_avg_price_2021:
            list_len = len(neighborhood_avg_price_2021[neighborhood_name])
            sum_up = sum(neighborhood_avg_price_2021[neighborhood_name])
            # calculating the average price of each neighborhood
            # and append them into values of keys which are names of the neighborhoods
            neighborhood_avg_price_2021[neighborhood_name] = sum_up/list_len
        # same as in the for loop which eventually gets neighborhood_avg_price_2021
        for neighborhood_name in neighborhood_avg_price_2020:
            list_len = len(neighborhood_avg_price_2020[neighborhood_name])
            sum_up = sum(neighborhood_avg_price_2020[neighborhood_name])
            neighborhood_avg_price_2020[neighborhood_name] = sum_up/list_len
        # using dicts "neighborhood_avg_price_2021/2020" to get least affordable neighborhood
        global least_aff_neighborhood
        # the neighborhood with greatest avg price is the least affordable one
        # using the same technique as commented above
        least_aff_neighborhood = [max(neighborhood_avg_price_2021.values()),
                                  max(neighborhood_avg_price_2021, key=neighborhood_avg_price_2021.get)]
        global most_aff_neighborhood
        # same as above
        most_aff_neighborhood = [min(neighborhood_avg_price_2021.values()),
                                  min(neighborhood_avg_price_2021, key=neighborhood_avg_price_2021.get)]
        global neighborhood_rent_change
        # creating a dict for records of changes of rent from 2020 to 2021
        neighborhood_rent_change = {}
        # using for loop to get each key and value in dict "neighborhood_avg_price_2020"
        for neighborhood_name in neighborhood_avg_price_2020:
            # and using the value of corresponding key in dict "neighborhood_avg_price_2021" to subtract the 2020 one
            neighborhood_rent_change[neighborhood_name] = neighborhood_avg_price_2021[neighborhood_name] - \
                                                          neighborhood_avg_price_2020[neighborhood_name]
        # closing the file
        csv_file.close()

# defining a function that create a text file and write the required analysis data in that file
def report_output():
    # creating the report file
    report = open("report.txt", "w")
    # writing lines in the file
    report.write("Rent Report, 2020-2021\n")
    # "f'{}'" is to normalise the currency format
    report.write(f"Average Rent: ${avg_rent_2021:.2f}\n")
    # please note that max_rent_2021/2020 are lists, so [0] is the price and [1] is the address
    report.write(f"Highest Rent: ${max_rent_2021[0]:.2f}, %s\n" % max_rent_2021[1])
    report.write(f"Lowest Rent: ${min_rent_2021[0]:.2f}, %s\n" % min_rent_2021[1])
    # below report.write() statements with if conditions are ones with (+/-) format requirement
    # so if the value of the variable is greater than 0, it will be added with a "+" before the "$" symbol
    if avg_rent_change > 0:
        report.write(f"Average Rent Change: +${avg_rent_change:.2f}\n")
    # vice versa
    elif avg_rent_change < 0:
        report.write(f"Average Rent Change: -${abs(avg_rent_change):.2f}\n")
    # in case if it is 0
    else:
        report.write(f"Average Rent Change: ${avg_rent_change:.2f}\n")
    # same as above
    if max_rent_change[0] > 0:
        report.write(f"Highest Rent Change: +${max_rent_change[0]:.2f}, %s\n" % max_rent_change[1])
    elif max_rent_change[0] < 0:
        report.write(f"Highest Rent Change: -${abs(max_rent_change[0]):.2f}, %s\n" % max_rent_change[1])
    else:
        report.write(f"Highest Rent Change: ${max_rent_change[0]:.2f}, %s\n" % max_rent_change[1])
    # same as above
    if min_rent_change[0] > 0:
        report.write(f"Lowest Rent Change: +${min_rent_change[0]:.2f}, %s\n" % min_rent_change[1])
    elif min_rent_change[0] < 0:
        report.write(f"Lowest Rent Change: -${abs(min_rent_change[0]):.2f}, %s\n" % min_rent_change[1])
    else:
        report.write(f"Lowest Rent Change: ${min_rent_change[0]:.2f}, %s\n" % min_rent_change[1])
    # using the globalized list "least_aff_neighborhood" to write out the following
    # cuz it is a list, so [0] is the price, [1] is the the name of the neighborhood
    report.write(f"Least Affordable Neighborhood:%s, (Avg. Rent: ${least_aff_neighborhood[0]:.2f})\n"
                 % least_aff_neighborhood[1])
    report.write(f"Most Affordable Neighborhood:%s, (Avg. Rent: ${most_aff_neighborhood[0]:.2f})\n"
                 % most_aff_neighborhood[1])
    # below is rent changes
    report.write("Rent Changes by Neighborhood:\n")
    # using the globalized dictionary "neighborhood_rent_change" to get each key & value which are name and rent change
    for neighborhood_name in neighborhood_rent_change:
        # same as mentioned above, if it is positive, a "+" will be added before the "$" symbol
        if neighborhood_rent_change[neighborhood_name] > 0:
            report.write(f"\t%s (+${neighborhood_rent_change[neighborhood_name]:.2f})\n" % neighborhood_name)
        # vice versa
        elif neighborhood_rent_change[neighborhood_name] < 0:
            report.write(f"\t%s (-${abs(neighborhood_rent_change[neighborhood_name]):.2f})\n" % neighborhood_name)
        # in case of it is 0
        else:
            report.write(f"\t%s (${neighborhood_rent_change[neighborhood_name]:.2f})\n" % neighborhood_name)
    # closing the report file
    report.close()

# defining the main function
def main():
    get_values("sc_rent_prices.csv")
    report_output()

if __name__ == "__main__":
    main()