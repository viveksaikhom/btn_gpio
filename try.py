import TI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

BUTTON_PIN = 13
GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    print(f"Initial state of pin {BUTTON_PIN}: {'HIGH' if GPIO.input(BUTTON_PIN) else 'LOW'}")
finally:
    GPIO.cleanup()
