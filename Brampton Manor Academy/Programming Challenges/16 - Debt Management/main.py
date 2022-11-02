

def debt_calculation(interest_percentage,repayment_percentage,minimum_amount):

    debt_amount = 100
    min_req_check = 1
    interest_payment = 0
    payment_counter = 0


    while debt_amount > 0:
        interest_payment += debt_amount * interest_percentage
        debt_amount += debt_amount * interest_percentage


        if minimum_amount > repayment_percentage * debt_amount:
            if min_req_check == 1:
                debt_amount = debt_amount - minimum_amount
                min_req_check = 0
            else:
                minimum_amount = debt_amount
                debt_amount -= minimum_amount
        else:
            debt_amount -= debt_amount * repayment_percentage


        debt_amount = round(debt_amount, 2)

        payment_counter += 1
    print(f"The number of payments made is: {payment_counter}")
    print(f"The total amount repaid is: {round(interest_payment + 100, 2)}")



if __name__ == "__main__":
    debt_calculation(0.1,0.5,50)

    debt_calculation((0.43), (0.46), (46))