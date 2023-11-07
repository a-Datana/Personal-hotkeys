import time
import keyboard
import pyperclip
import pyautogui

# Funktion, die aufgerufen wird, wenn der Hotkey ausgelöst wird
import pyperclip
import pyautogui
import time

def perform_custom_action():
    delete_previous_input()
    password = "³Ä9·YaÃtÉØ¨×zàØÛ÷ï4²¶ñòÕ¸ø´ë`ÎðNëCñ?zÅ¡.®%T4êeÉíã·Õ©QàüÑ¹#nwHóÁ{ëÜ)Í²5Ç¯ï¥Â*¤vSò,Nc·ÐÖÎbû~D÷X¡¦f#÷/N£¤âæòKv;Q¶î~v)ÅDyÕ´Mé¹ýÝhk{ß=ÐÞñ:ðëþå_ï]Ö¬®oþNtL{õö>¼ij]@àÙZ¥Î½¶Äº¢Zá/Êg{3Ä*ÀÉ%(Î`k_AþïÕaøi4Ö9.äÑÛ~7ýd?÷X#¹*ÜôÌÚD7Ñ·VÔÛû%ÄØ~Ýâ-²è´sæÔUêÍª¦¡þµ:áÅ(Í)å:º<°\"¡´R"
    pyperclip.copy(password)  # Copies the password to the clipboard
    time.sleep(0.1)  # Short delay before pasting
    pyautogui.hotkey('ctrl', 'v')  # Pastes the password from the clipboard
    pyautogui.press('enter')
    pyperclip.copy("Are you trying to steal my password? :D")  # Copies a message to the clipboard

# Hotkey definieren
keyboard.add_hotkey('A+E+R+H+6', perform_custom_action)
def delete_previous_input():
    """
    Delete the previous input by selecting all the text, deleting it,
    and waiting for a short delay before executing any further actions.
    """
    pyautogui.hotkey("ctrl", "a")  # Markiert den aktuellen Text
    time.sleep(0.01)  # Kurze Verzögerung, um sicherzustellen, dass die Markierung abgeschlossen ist
    pyautogui.press("backspace")  # Löscht den markierten Text
    time.sleep(0.01)  # Kurze Verzögerung vor dem Ausführen der benutzerdefinierten Aktion

# Endlosschleife, um das Programm am Laufen zu halten
try:
    while True:
        pass
except KeyboardInterrupt:
    # Programm beenden, wenn Strg+C gedrückt wird
    pass