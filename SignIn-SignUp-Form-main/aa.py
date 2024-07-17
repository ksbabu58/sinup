import pyautogui as pg
import time

# Delay to run the program (optional)
print("Program will run after 5 seconds")
time.sleep(5)

# Loop to send messages
for i in range(100):
    # Replace with the desired message
    message = "Hello, World!"
    
    # Simulate typing and sending the message
    pg.typewrite(message)
    pg.press('enter')
    time.sleep(1)  # Add a delay between messages (optional)
