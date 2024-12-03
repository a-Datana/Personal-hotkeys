import datetime
import time
import keyboard
import pyperclip
import pyautogui
import random



def perform_pass_keybind():
    from secret import password
    pyautogui.press("backspace", presses=5, interval=0)
    pyperclip.copy(password)  # Copies the text to the clipboard
    time.sleep(0.1)  # Short delay before pasting
    pyautogui.hotkey('ctrl', 'v')  # Pastes the text from the clipboard
    time.sleep(0.5) 
    pyperclip.copy("Are you trying to steal my password? :D")  # Copies a message to the clipboard

def perform_timestamp():
    pyautogui.press("backspace", presses=3, interval=0)
    time.sleep(0.01)
    current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    message = f"{current_time}"
    pyperclip.copy(message)  
    time.sleep(0.1)  # Short delay before pasting
    pyautogui.hotkey('ctrl', 'v')  # Pastes the password from the clipboard


def invalid_argument():
    pyautogui.press("backspace", presses=6, interval=0)
    time.sleep(0.01)

    texts = [
        "Your Argument is Invalid.",
        "I Have Already Depicted",
        "You as The Soyjak & Me As The Chad."
    ]

    for text in texts:
        pyautogui.typewrite(text, interval=0.01)
        keyboard.press_and_release('enter')
        time.sleep(random.uniform(0.2, 0.5))  # Zufälliger Delay zwischen 0.2 und 0.5 Sekunden
        keyboard.press_and_release('enter')
        time.sleep(random.uniform(0.2, 0.5))

def placeholder():
    pass

# Hotkeys definieren
keyboard.add_hotkey('A+E+R+6', perform_pass_keybind)
keyboard.add_hotkey('L+D+T', perform_timestamp)
keyboard.add_hotkey('S+H+I+T', invalid_argument)
keyboard.add_hotkey('M+K+T', placeholder)

def delete_previous_input():
    """
    Delete the previous input by selecting all the text, deleting it,
    and waiting for a short delay before executing any further actions.
    """
    pyautogui.hotkey("ctrl", "a")  # Markiert den aktuellen Text
    time.sleep(0.01)  # Kurze Verzögerung, um sicherzustellen, dass die Markierung abgeschlossen ist
    pyautogui.press("backspace")  # Löscht den markierten Text
    time.sleep(0.01)  # Kurze Verzögerung vor dem Ausführen der benutzerdefinierten Aktion
    



print("keybinds loaded")
print("available Keybinds:")
print("L+D+T: Current Timestamp")
print("S+H+I+T: Used to tell Lol Players that they are wrong")
print("A+S+H+I+T: like S+H+I+T but for all players")

# Endlosschleife, um das Programm am Laufen zu haltenprint("S+H+I+T: Used to tell Lol Players that they are wrong")
try:
    while True:
        # wait for any key pressed
        keyboard.wait()
except KeyboardInterrupt:
    # Programm beenden, wenn Strg+C gedrückt wird
    pass