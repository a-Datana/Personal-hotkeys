import datetime
import time
import keyboard
import pyperclip
import pyautogui


def perform_pass_keybind():
    from secret import password
    pyautogui.press("backspace", presses=5, interval=0)
    pyperclip.copy(password)  # Copies the text to the clipboard
    time.sleep(0.1)  # Short delay before pasting
    pyautogui.hotkey('ctrl', 'v')  # Pastes the text from the clipboard
    pyperclip.copy("Are you trying to steal my password? :D")  # Copies a message to the clipboard

def perform_timestamp():
    pyautogui.press("backspace", presses=3, interval=0)
    time.sleep(0.01)
    current_time = datetime.datetime.now().strftime("%d:%m:%Y %H:%M:%S:%f")
    message = f"By LDR at {current_time}"
    pyperclip.copy(message)  
    time.sleep(0.1)  # Short delay before pasting
    pyautogui.hotkey('ctrl', 'v')  # Pastes the password from the clipboard
    
def placeholder():
    pass

# Hotkeys definieren
keyboard.add_hotkey('A+E+R+H+6', perform_pass_keybind)
keyboard.add_hotkey('L+D+T', perform_timestamp)
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
print("M+K+T: Ununsed")

# Endlosschleife, um das Programm am Laufen zu halten
try:
    while True:
        # wait for any key pressed
        keyboard.wait()
except KeyboardInterrupt:
    # Programm beenden, wenn Strg+C gedrückt wird
    pass