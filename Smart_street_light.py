import time
import random
from datetime import datetime

# LDR threshold
# Lower LDR value = dark
LDR_THRESHOLD = 500


def read_ldr():
    """
    Simulate an LDR sensor reading.

    In a real project, replace this function with
    an actual LDR sensor reading from Raspberry Pi,
    ESP32, or another microcontroller.
    """
    return random.randint(0, 1023)


def turn_light_on():
    print("💡 Street Light: ON")


def turn_light_off():
    print("🌙 Street Light: OFF")


def main():
    print("=" * 50)
    print("       SMART STREET LIGHT USING LDR")
    print("=" * 50)

    try:
        while True:

            ldr_value = read_ldr()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"\nTime      : {timestamp}")
            print(f"LDR Value : {ldr_value}")

            if ldr_value < LDR_THRESHOLD:
                turn_light_on()
            else:
                turn_light_off()

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nSmart street light system stopped.")


if __name__ == "__main__":
    main()
