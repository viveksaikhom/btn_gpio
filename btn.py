import TI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

BUTTON_PIN = 13

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(BUTTON_PIN, GPIO.BOTH, bouncetime=200)

print("Waiting for button presses...")

try:
    while True:
        if GPIO.event_detected(BUTTON_PIN):
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                print("Button Pressed!")
            else:
                print("Button Released!")
        time.sleep(0.1)


except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    GPIO.cleanup()
