import os
import time

WAIT_DURATION = 3
DIM_DURATION = 3
DEFAULT_BRIGHTNESS = 0.7

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
        time.sleep(WAIT_DURATION)
        dim_screen(DIM_DURATION, DEFAULT_BRIGHTNESS)

if __name__ == "__main__":
    main()