# Raphael De Los Reyes
# 11189672
# gld141

email_address = input("Enter email address: ")

idx_at = email_address.find("@")
idx_dot = email_address.find(".", idx_at) # search for dot after @

print("Username:", email_address[:idx_at]) # grab everything before the @
print("Domain:", email_address[idx_at + 1:idx_dot]) # grab everything after the @ and before the first dot