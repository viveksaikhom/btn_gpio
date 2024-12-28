import TI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

user = input("Pin number: ")
BUTTON_PIN = user

GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    print(f"Initial state of pin {BUTTON_PIN}: {'HIGH' if GPIO.input(BUTTON_PIN) else 'LOW'}")
finally:
    GPIO.cleanup()
