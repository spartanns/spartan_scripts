import time
import os


def display_clock():
    """Display a real-time clock in ASCII art."""
    while True:
        # Clear the screen
        os.system("cls" if os.name == "nt" else "clear")

        # Get current time
        current_time = time.strftime("%H:%M:%S")

        # Create a stylish clock
        print(f"""
        ╔════════════════════╗
        ║   CURRENT TIME     ║
        ╠════════════════════╣
        ║      {current_time}      ║
        ╚════════════════════╝
        """)
        time.sleep(1)


# Run the clock
display_clock()
