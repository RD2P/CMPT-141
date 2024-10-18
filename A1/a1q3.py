# Glenn Raphael De Los Reyes
# 11189672
# gld141


# Inputs
payment = int(input("Enter the payment for the case : "))
number_staff = int(input("Enter the number of staff : "))

# Calculations
phoenix_share = payment / 4
staff_share = payment - phoenix_share
individual_staff_share = staff_share / number_staff

# Outputs
print("Phoenix Wright’s 25% share : $" + str(phoenix_share))
print("The staff’s 75% share of the fee : $" + str(staff_share))
print("Each staff member takes home : $" + str(individual_staff_share))
