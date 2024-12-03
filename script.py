import os
import time

WAIT_DURATION = 1200
DIM_DURATION = 30
DEFAULT_BRIGHTNESS = 10 / 16

def set_brightness(level):
    """
    Set screen brightness using the 'brightness' command-line tool.
    """
    try:
        os.system(f"brightness {level}")

    except Exception as e:
        print(f"Error setting brightness: {e}")

def dim_screen(duration, default_brightness):
    """
    Dim the screen brightness to 0 for 20 seconds and then restore.
    """
    try:
        set_brightness(0.0)
        time.sleep(duration)
        set_brightness(default_brightness)
        
    except Exception as e:
        print(f"Error dimming screen: {e}")

def main():
    """
    Main loop to dim the screen every 20 minutes.
    """
    while True:
        print("Waiting for 20 minutes...")
        time.sleep(WAIT_DURATION)
        print("Dimming screen...")
        dim_screen(DIM_DURATION, DEFAULT_BRIGHTNESS)

if __name__ == "__main__":
    main()