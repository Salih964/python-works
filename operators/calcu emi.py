# calculate_emi

# E = P*R*(1+r)^n/((1+r)^N –1)

#   E = Equated Monthly Instalment

# ‘P’ stands for principal amount

# ‘R’ denotes applicable rate of interest

# ‘N’ stands for the loan term or tenure 

loan_amount=200000
interest_rate=9
tenure=20

# 
# p=loan_amount
# r=interest_rate/12
# i=r/100
# n=tenure*12
# one_plus_power=(1+i)**n

# EMI= (p*i*one_plus_power)/(one_plus_power-1)

# print(EMI)

# total_interest_payable=(EMI*n)-p

# print(f"total interest payable amount is {total_interest_payable}")

# total_payabale_amount=p+total_interest_payable

# print(f"total payable amount is rs.{total_payabale_amount}")

#  or use this method that mentioned below


#calculate_annual_interest_into_monthly_interest
annual_interest=interest_rate/12/100
print(f"Annual Interest is {annual_interest}")

#convert no.of years into months
number_of_months=tenure*12
print(f"number of months is {number_of_months}")

#substitute the values into emi formula
emi=loan_amount*annual_interest*(1+annual_interest)**number_of_months/((1+annual_interest)**number_of_months-1)
print(f"Emi Amount Rs. {emi}")

#toal interest payable formula = (E*n)-p
total_interest_payable=(emi*number_of_months)-loan_amount
print(f"Total Interest Payable is Rs.{total_interest_payable}")

#total payment(principle amount+total interest)
total_payment=loan_amount+total_interest_payable
print(f"Total Payment Rs.{total_payment}")









