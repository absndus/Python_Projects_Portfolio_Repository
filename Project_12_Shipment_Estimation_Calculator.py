#File: Project_12_Shipment_Estimation_Calculator.py
#Author: Albert Schultz
#Date: 05/16/2023
#Version: 1.00
#Descriptions: This project script goes through the process of taking the weight of the package and determine the cheapest way to ship that package using Sal's Shippers, a fictional company.

#Create the required variables needed for this script.
package_weight = float(input("Enter the weight of your package in pounds (lb): "))
method_delivery = input("""Enter an option shown: \n
1. Ground Shipping
2. Drone Shipping
""")

#Create a function called, method_delivery_option(method_delivery).
def method_delivery_option(method_delivery, package_weight):
    if method_delivery == "Ground Shipping":
        if package_weight <= 2:
            weight_charge = "{:.2f}".format(package_weight * 1.50 + 20) #Max is two decimal places using the format method.
            print(f"Since your package is less than 2 pounds(lb), the cost for shipping is, ${weight_charge} and the flat rate is $20.00.")
        elif package_weight >= 2 and package_weight <= 6:
            weight_charge = "{:.2f}".format(package_weight * 3.00 + 20)
            print(
                f"Since your package is between 2 to 6 pounds(lb), the cost for shipping is, ${weight_charge} and the flat rate is $20.00.")
        elif package_weight >= 6 and package_weight <= 10:
            weight_charge = "{:.2f}".format(package_weight * 4.00 + 20)
            print(
                f"Since your package is between 6 to 10 pounds(lb), the cost for the shipping is, ${weight_charge} and the flat rate is $20.00.")
        elif package_weight >= 10:
            weight_charge = "{:.2f}".format(package_weight * 4.75 + 20)
            print(
                f"Since your package is 10 pounds(lb) and greater, the cost for the shipping is, ${weight_charge} and the flat rate is $20.00.")
        else:
            print("Please make sure that your weight is not a negative number.")
    elif method_delivery == "Drone Shipping":
        if package_weight <= 2:
            weight_charge = "{:.2f}".format(package_weight * 4.50)
            print(f"Since your package is less than 2 pounds(lb), the cost for shipping is, ${weight_charge} and the flat rate is $0.00.")
        elif package_weight >= 2 and package_weight <= 6:
            weight_charge = "{:.2f}".format(package_weight * 9.00)
            print(
                f"Since your package is between 2 to 6 pounds(lb), the cost for shipping is, ${weight_charge} and the flat rate is $0.00.")
        elif package_weight >= 6 and package_weight <= 10:
            weight_charge = "{:.2f}".format(package_weight * 12.00)
            print(
                f"Since your package is between 6 to 10 pounds(lb), the cost for the shipping is, ${weight_charge} and the flat rate is $0.00.")
        elif package_weight >= 10:
            weight_charge = "{:.2f}".format(package_weight * 14.25)
            print(
                f"Since your package is 10 pounds(lb) and greater, the cost for the shipping is, ${weight_charge} and the flat rate is $0.00.")
        else:
            print("Please make sure that your weight is not a negative number.")

#print out the delivery information based on the user's inputs.
method_delivery_option(method_delivery, package_weight)