import TI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

BUTTON_PIN = 13

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Waiting for button press...")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("Button Pressed!")
            break
        else:
            print("Button Not Pressed! Yet")
        time.sleep(0.3)

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    GPIO.cleanup()
