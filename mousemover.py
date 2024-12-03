import pyautogui
import time

def mouse_mover(interval=60):
    while True:
        # Bewege die Maus um 1 Pixel nach rechts und zurück
        pyautogui.move(1, 0)
        pyautogui.move(-1, 0)
        time.sleep(interval)  # Wartezeit zwischen den Bewegungen

# Starte das Skript mit einem Intervall von 60 Sekunden
mouse_mover(interval=60)
