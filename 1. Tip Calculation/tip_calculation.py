def calculate_tip(bill_amount, tipPercentage):
   return round(bill_amount*(tipPercentage/100),2)

print(calculate_tip(1524.33,25))