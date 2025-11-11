import pyautogui
from pynput.keyboard import *

delay = 0.001
pause = True
running = True

def on_press(key):
    global pause, running

    if key == Key.f1:
        pause = False
        print("[Resumed]")
    elif key == Key.f2:
        pause = True
        print("[Paused]")
    elif key == Key.esc:
        running = False
        print("[Exit]")

def show_controls():
    print("== AutoClicker ==")
    print(f"Delay: {delay}s")
    print("Controls:")
    print("  F1  Resume")
    print("  F2  Pause")
    print("  ESC Exit")
    print("-------------------")
    print("Waiting for F1...")

def main():
    listener = Listener(on_press=on_press)
    listener.start()
    show_controls()

    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay

    listener.stop()

if __name__ == "__main__":
    main()