import pyfirmata2
import time

comport = 'COM5'

try:
    board = pyfirmata2.Arduino(comport)
    print(f"Connected to Arduino on {comport}")
except Exception as e:
    print(f"Error: Could not connect to Arduino on {comport}. {e}")
    exit()

# Define LED pins using the correct syntax
led_pins = {
    1: board.get_pin('d:8:o'),
    2: board.get_pin('d:9:o'),
    3: board.get_pin('d:10:o'),
    4: board.get_pin('d:11:o'),
    5: board.get_pin('d:12:o')
}

def led(fingerUp):
    """
    Control LEDs based on the fingerUp list.

    Parameters:
    fingerUp (list): A list indicating which fingers are up (1) or down (0).
    """
    led_states = {
        (0, 0, 0, 0, 0): [0, 0, 0, 0, 0],
        (0, 1, 0, 0, 0): [1, 0, 0, 0, 0],
        (0, 1, 1, 0, 0): [1, 1, 0, 0, 0],
        (0, 1, 1, 1, 0): [1, 1, 1, 0, 0],
        (0, 1, 1, 1, 1): [1, 1, 1, 1, 0],
        (1, 1, 1, 1, 1): [1, 1, 1, 1, 1]
    }

    # Get the corresponding LED state
    states = led_states.get(tuple(fingerUp), [0, 0, 0, 0, 0])

    # Set LED states
    for idx, state in enumerate(states, start=1):
        led_pins[idx].write(state)

time.sleep(2)  # Wait for 2 seconds to establish connection
