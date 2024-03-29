'''
Feedback, by Zihua Li
READABILITY ISSUES
    1) Irregular comments, some are too long, should start a new line when appropriate.
    2) Irregular expressions, e.g. In line 80: "total_rent_2021=0", should be "total_rent_2021 = 0",
       there are also many lines too long. Massive irregular expressions could decrease readability.
    Improvements: Regularly comment, avoid lines that are too long, and expressions.
RESULTS ISSUES
    Output "Least Affordable Neighborhood: Eastside(Avg. Rent: $1023.33)"
        1) Wrong output, "Least Affordable Neighborhood" should be "Boardwalk" instead of "Eastside".
        2) Wrong output, rents are also outputted reversely.
        3) Wrong output, space missing between neighborhood names and average rents.
    Still don't quite understand why does this error happen, after examining your code for many times.
    With all due respect, but your code is little bit hard to read, comments are massive but not really helping
        us the readers to understand your code very well.
    With better comments and explanations on the code's mechanism, your code should be excellent.
    Technique used for storing calculation results, returning values in a function, is good and efficient,
        safer than mine. I globalized all variables in the calculation function, which is dangerous sometimes
        when someone would looking for distorting values of the variables.
OTHERS
    Coding of function all_results is really messy, with irregular comments and lines which are too long,
         is very hard to read, and will be torturing if editing is needed. You could do the string work separately,
         with a few more steps. It is not only good for future maintenance, but also easier for debugging.
    Years in rent report output is hard-coded, which is extremely unfriendly to adapting other data with same format.
        What if years written in the csv file changed? This program will still output "2020-2021".
    Variable names are written in years given in this file, still, bad for adapting other data with same format
    You used dictionary to store neighborhoods, which is very efficient and a smart idea. 9999 likes on this
    Main function should be put at the last but before calling. Main function here is put at the first,
        not consistent with the code's order of execution.
'''

# Harshita Venkatesan
# Assignment 7.1: Rental Price Analysis
# Purpose: Implementing main/helper functions to take a csv file as an input of rental prices in a housing market to return an output text file report.
# I used string methods pdf, Lecture 6.1-6.3, https://www.educative.io/edpresso/the-with-statement-in-python as a resource to help me through this assignment. 

# main method to call neighborhood_calc and all_results
def main():
    neighborhood_calc(neighborhood)
    all_results("report.txt")

# function calculates most affordable neighborhood, least affordable neighborhood, rent changes by neighborhood according to average prices
def neighborhood_calc(neighborhood):
    # setting variables to tuple/ empty list
    most_affordable_Neighborhood=tuple()
    least_affordable_Neighborhood=tuple()
    rent_Changes_by_Neighborhood =[]
    
    # setting count to zero so that index is in range
    count=0
    # looping through all the neighborhoods list
    for i in neighborhood:
        # calculates the average rent price of 2021 and 2020
        average_2020 = sum(neighborhood[i][0])/len(neighborhood[i][0])
        average_2021 = sum(neighborhood[i][1])/len(neighborhood[i][1])
        
        # if count is zero, removes spaces of most affordable neighborhood, least affordable neighborhood of 2021
        if count==0:
            most_affordable_Neighborhood = least_affordable_Neighborhood=average_2021,i.strip()

        
        else:
            # if 2021 average price is greater then the neighborhood price, stores that neighborhood as most affordable
            if average_2021>most_affordable_Neighborhood[0]:
                most_affordable_Neighborhood=(average_2021,i.strip())
            # if 2021 average price is lesser than the neighborhood price, stores the neighborhood as least afforadable
            if average_2021<least_affordable_Neighborhood[0]:
                least_affordable_Neighborhood=(average_2021,i.strip())
        # adding each neighborhood average prices of 2020 and 2021 to the list using append
        rent_Changes_by_Neighborhood.append([i.strip(),average_2021-average_2020])
        # increment count so that index is out of range and doesn't loop again
        count=1
    # return affordable neighborhood, least affordable neighborhood, rent changes by neighborhood according to average price
    return most_affordable_Neighborhood,least_affordable_Neighborhood,rent_Changes_by_Neighborhood

# opens up  csv file to read its contents          
with open("sc_rent_prices.csv", 'r') as file:

        # setting total rent of 2021 and 2020 as zero
        total_rent_2021=0
        total_rent_2020=0
        
        # setting up variables as tuple, dictionary, empty list
        highest_Rent=tuple()
        lowest_Rent=tuple()
        # change in high/low rent change as zero
        highest_Rent_Change = 0
        lowest_Rent_Change = 0
        neighborhood={}
        most_affordable_Neighborhood=tuple()
        least_affordable_Neighborhood=tuple()
        rent_Changes_by_Neighborhood =[]
        
        # setting count as zero and array as an empty list
        count=0
        arr=[]
    
        header = file.readline().split(",") 
        while True:
            # storing data list as data[0] = address, data[1] = Neighborhood, data[2] = 2020 Rent, data[3] = 2021 Rent
            # splits the contents using comma
            data = file.readline().split(",")
            # if the length of data is four, then break
            if len(data) !=4:
                break
            # storing rent 2021 with $ sign to represent cost
            rent_2021 = int(data[3].replace("$",""))
            # storing rent 2020 with $ sign to represent cost
            rent_2020 = int(data[2].replace("$",""))

            # calculating the total rent of 2020 and 2021
            total_rent_2021+=rent_2021
            total_rent_2020+=rent_2020

            
            if count==0:
                # address of low rent and high rent of 2021
                highest_Rent=lowest_Rent=rent_2021,data[0]
                # address of low and high rent change of 2021 and 2020 
                highest_Rent_Change = lowest_Rent_Change = (rent_2021-rent_2020,data[0])
            else:
                # if 2021 rent is greater than the address of high rent, that rent becomes the address
                if rent_2021>highest_Rent[0]:
                    highest_Rent=rent_2021,data[0]
                # if 2021 rent is lesser than the address of low rent, that rent becomes the address
                if rent_2021<lowest_Rent[0]:
                    lowest_Rent= rent_2021,data[0]
                # if rent change is greater than the address of higher rent change, that's the rent change address
                if (rent_2021-rent_2020)>highest_Rent_Change[0]:
                    highest_Rent_Change=rent_2021-rent_2020,data[0]
                # # if rent change is lesser than the address of lower rent change, that's the rent change address
                if (rent_2021-rent_2020)<lowest_Rent_Change[0]:
                    lowest_Rent_Change=rent_2021-rent_2020,data[0]
            # appending address and neighborhood of 2021 and 2020 rent
            try:
                neighborhood[data[1]][0].append(rent_2020)
                neighborhood[data[1]][1].append(rent_2021)
            # except if neighborhood address equals rent of 2020 and 2021    
            except:
                neighborhood[data[1]]=[[rent_2020],[rent_2021]]
            # append all data list    
            arr.append(data)
            # increment counter
            count+=1
        # calculating the average rent of 2021 based on number of neighborhoods
        average_Rent_2021= total_rent_2021/count
        # calculating the rent change of 22021 and 2020
        Average_Rent_Change=(total_rent_2021-total_rent_2020)/count
        # stores calculation to neighborhood_calc function
        most_affordable_Neighborhood,least_affordable_Neighborhood,neighborhood_rent_change =neighborhood_calc(neighborhood)
        # close the file
        file.close()
# prints all results in a file       
def all_results(file):
    # opens txt file to write file
    file=open("report.txt","w")
    file.write("Rent Report, 2020-2021\n")
    file.write("Average Rent: ${0:.2f}\n".format(average_Rent_2021))
    file.write("Highest Rent: ${0:.2f}, {1}\n".format(highest_Rent[0],highest_Rent[1]))
    file.write("Lowest Rent: ${0:.2f}, {1}\n".format(lowest_Rent[0],lowest_Rent[1]))
    # replaces positive/negative sign to make them come in front of dollar sign
    file.write("Average Rent Change: ${0:.2f}\n".format(Average_Rent_Change).replace("$", "+$").replace("$-","-$"))
    file.write("Highest Rent Change: ${0:.2f}, {1}\n".format(highest_Rent_Change[0],highest_Rent_Change[1]).replace("$", "+$").replace("$-","-$"))
    file.write("Lowest Rent Change: ${0:.2f}, {1}\n".format(lowest_Rent_Change[0],lowest_Rent_Change[1]).replace("$", "+$").replace("+$-", "-$"))
    file.write("Least Affordable Neighborhood: {0}(Avg. Rent: ${1:.2f})\n".format(least_affordable_Neighborhood[1],least_affordable_Neighborhood[0]))
    file.write("Most Affordable Neighborhood: {0}(Avg. Rent: ${1:.2f})\n".format(most_affordable_Neighborhood[1],most_affordable_Neighborhood[0]))
    file.write("Rent Changes by Neighborhood:\n")
    #looping through each neighborhood
    for i in neighborhood_rent_change:
        file.write("\t{0} (${1:.2f})\n".format(i[0],i[1]).replace("$", "+$").replace("+$-", "-$"))
    # close file once done writing it
    file.close()

# calling the main method
if __name__ == "__main__":
    main()





