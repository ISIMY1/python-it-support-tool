# # IT Helpdesk Ticket with Access Checker 

username = input("Enter your username: ")
department = input("Enter your department: ")
device = input("Enter your device model or name: ")
description = input("Please describe the issue you are experiencing: ")
time = int(input("How long has this issue been occurring? (in minutes): "))
account_active = input("Is your account active? (yes/no): ").lower()
multiple_users = input("Are there multiple users experiencing this issue? (yes/no): ").lower()

High = time >= 60 and multiple_users == "yes"
Medium = time >= 30 and multiple_users == "yes"
Low = not High and not Medium
no_access = account_active == "no"

print(""""
=========================
TICKET SUMMARY:
=========================
""")
print("Name: " + username)
print("Department: " + department)
print("Device: " + device)
print("Description: " + description)
print("Multiple Users: " + multiple_users)
if time >= 60 and multiple_users == "yes":
    print("Priority: High")
elif time >= 30 and multiple_users == "yes":
    print("Priority: Medium")
else:
    print("Priority: Low")

if account_active == "no":
    print("Account access needs to be checked.")
print("""
=========================
TICKET SUMMARY:
=========================
""")
