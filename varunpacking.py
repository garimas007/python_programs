"""
using variable unpacking in practical scenarios
"""

def get_user_info(usrid):
    name = "abc"
    email = "abc@gmail.com"
    age = 30

    return name, email, age

u_name, u_email, u_age = get_user_info(107)
print(f"name : {u_name}")
print(f"email : {u_email}")
print(f"age : {u_age}")