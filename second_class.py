# Agenda - Operators & Conditional Statements.

# Logical Operators.
# AND, OR, NOT, EQUAL TO, NOT EQUAL TO.

# age = int(input('Please enter your age: '))

# if age >= 18:
#     print("Eligible for Voter Card")
# else:
    # print("Not eligible")

# Drive a Car in INDIA - age >= 18 AND valid driving license
# To get the college degree = pass all the subjects and attend convocation ceremony

# condition-1 AND condition-2 -> TRUE iff both cond-1 and cond-2 are TRUE

# CARD or CASH or UPI or NET_BANKING
# notify - email or phone or whatsapp

# cond-1 OR cond-2 => TRUE, at least one of both should be TRUE
# cond-1 - FALSE, cond-2 - FALSE => cond-1 OR cond-2 = False

# NOT - negate/invert the value.
# NOT true = false 
# NOT false = true

# is_active = true
# NOT is_active => FALSE
# NOT available - busy

# A = True | B = True => A and B = True
# A = True | B = False => A or B = True

# age = 20
# has_license = False

# if age >= 18 and has_license == True:
#     print("Can drive")
# else:
#     print("Can't drive") 

# A and B

# temperature = 25
# is_sunny = False
# is_weekend = True

# perfect_day = temperature > 20 and is_sunny and is_weekend
# print(perfect_day)

# output = a and b and (c or d)

# bill_amount = 1000
# has_cash = True
# cash_amount = 900
# has_card = False
# can_pay_via_cash = has_cash and cash_amount >= 1000
# print(can_pay)

# NOT 
# is_sunny = False
# is_raining = not is_sunny
# print(is_raining)

# form_submitted = True
# can_edit_form = not form_submitted
# print(can_edit_form)

# Operator Precendence (Priority)
# temperature = 12
# is_sunny = False
# is_weekend = True
# result = temperature > 20 or is_sunny and is_weekend
# print(result)

# Use parantheses for better understanding of evaluation of multiple conditions.

# age = int(input('Please enter your age: '))
# has_license = True
# knows_driving = True
# can_drive = age >= 18 and has_license and knows_driving
# print(can_drive)

# Python evaluates the expressions from LEFT to RIGHT

# != : NOT EQUAL TO
# username = "deepak"
# password = "deepak"

# is_valid = len(username) >= 5 and len(password) >= 5 and username != password
# print(is_valid)

# else if => Python elif

# is_student = False
# is_mentor = True
# is_ta = False

# role = ""
# if(is_student):
#     role = "student"
# elif is_mentor:
#     role = "mentor"
# elif is_ta:
#     role = "ta"

# print(role)

# username = "deepak" # Python considers empty string as FALSE.

# name = username or "Guest"
# print(name)

# age = 20
# has_license = True
# can_drive = (age >= 18 and has_license) or not has_license
# print(can_drive)