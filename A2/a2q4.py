# Glenn Raphael De Los Reyes
# 11189672
# gld141


def get_user_info():
  '''
  Ask and store user name and date of birth
  Returns: username and date of birth
  '''
  username = input("What is your desired account name? ")
  dob = input("What is your date of birth (MM/DD/YYYY)? ")
  return username, dob


def format_name(original_name):
  '''
  Formats username by truncating it to 10 characters (if applciable), converts to lowercase, and replace spaces with underscores
  Input:
    original_name: the username to be formatted
  Returns: the formatted username
  '''
  result = original_name
  result = result[:10] # slice notation will not raise error if result length is less than 10, so no need for if statement
  result = result.lower()
  result = result.replace(" ", "_")
  return result


def finalize_account_name(formatted_name, dob):
  '''
  Concatenate formatted name with last 2 digits of birth year
  Inputs:
    formatted_name: output of the format_name() function -> 10 characters or less, lowercase, and no spaces
    dob: date of birth in format of MM/DD/YYYY
  Returns: finalized account name - formatted name with last 2 digits of birth year
  '''
  final_name = formatted_name + dob[-2:]
  return final_name


# --- Main execution --- # 


[name, dob] = get_user_info()
formatted = format_name(name)
finalized_name = finalize_account_name(formatted, dob)

print("\nYour account has been created.")
print("Your account handle is", finalized_name)