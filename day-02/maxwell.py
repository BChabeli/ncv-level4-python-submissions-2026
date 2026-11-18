# Maxwell Fitness Centre

# Calculate amount before VAT
def amount_due(facility_code, hours):

    if facility_code == "squa":
        rate = 13.00
    elif facility_code == "swim":
        rate = 12.00
    elif facility_code == "gym":
        rate = 11.00
    elif facility_code == "wei":
        rate = 8.00

    amount = rate * hours

    return amount


#We  Calculate final amount including VAT
def final_amount_due(amount):

    vat = amount * 0.14

    final_amount = amount + vat

    return final_amount


# We Display the details of a customer 
def display(name, final_amount):

    print("\n----- PAYMENT DETAILS -----")
    print("Customer Name:", name)
    print("Total Amount Payable: R{:.2f}".format(final_amount))


# Processing the payment
def process_payment():

    name = input("Enter customer's name: ")

    print("\nAvailable Facilities:")
    print("squa - Squash court (R13.00 per hour)")
    print("swim - Swimming pool (R12.00 per hour)")
    print("gym  - Gymnasium (R11.00 per hour)")
    print("wei  - Weights (R8.00 per hour)")

    facility_code = input("\nEnter facility code: ")

    hours = float(input("Enter number of hours: "))

    # Calculate amount before VAT
    amount = amount_due(facility_code, hours)

    # Calculate final amount including VAT
    final_amount = final_amount_due(amount)

    # Display payment details
    display(name, final_amount)


# Start the program
process_payment()
