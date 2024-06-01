import pywhatkit

def wb(phone_number):
    message = "I'm the only one"
    hour = 16
    minute =33
    
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
    
# Example usage:
phone_number = input("Enter the phone number: ")
wb(phone_number)