from time import sleep
# import RPi.GPIO as GPIO

PUL = 17  # Stepper Drive Pulses
DIR = 27  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
ENA = 22  # Controller Enable Bit (High to Enable / LOW to Disable).

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

print('PUL = GPIO 17 - RPi 3B-Pin #11')
print('DIR = GPIO 27 - RPi 3B-Pin #13')
print('ENA = GPIO 22 - RPi 3B-Pin #15')

print('Initialization Completed')

delay = 0.0000001  # Delay between PUL pulses - effectively sets the motor rotation speed
print(f'Speed set to {delay}')

cycles = -1  # Infinite loop
degree_per_step = float(input('Enter the number of degrees per step: '))

def move_motor(direction, steps, message):
    GPIO.output(ENA, GPIO.HIGH)
    print('ENA set to HIGH - Controller Enabled')

    sleep(0.5)  # Pause for a possible change in direction
    GPIO.output(DIR, direction)
    print(f'DIR set to {direction} - {message} at {delay}')
    print('Controller PUL being driven.')

    for _ in range(steps):
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)

    GPIO.output(ENA, GPIO.LOW)
    print('ENA set to LOW - Controller Disabled')
    sleep(0.5)  # Pause for a possible change in direction


try:
    while True:
        direction_input = input('Enter direction (f for forward, b for backward, q to quit): ')
        
        if direction_input.lower() == 'q':
            break
        
        if direction_input.lower() == 'f':
            steps = int(input('Enter the number of steps for forward direction: '))
            move_motor(GPIO.LOW, steps, 'Moving Forward')
        
        elif direction_input.lower() == 'b':
            steps = int(input('Enter the number of steps for backward direction: '))
            move_motor(GPIO.HIGH, steps, 'Moving Backward')
        
        else:
            print('Invalid input. Enter "f" for forward, "b" for backward, or "q" to quit.')

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    print('Program Ended')
