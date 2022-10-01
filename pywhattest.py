# importing the module
import pywhatkit
 
# using Exception Handling to avoid
# unprecedented errors
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+234803xxxxxxx",
                        "This is from VSCode",
                        13, 24)
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")
