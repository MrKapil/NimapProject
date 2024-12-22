import time
from datetime import datetime

# Function to display the countdown
def countdown(seconds):
    print("🎉 Countdown starts now! 🎉")
    for i in range(seconds, 0, -1):
        print(f"⏳ Time remaining: {i} seconds", end="\r")
        time.sleep(1)
    print("\nCountdown Complete!")

# Function to display the birthday message
def display_birthday_message():
    # Fixed date and time
    formatted_time = "12:00 AM"
    formatted_date = "1 Dec"
    
    print("\n========================================")
    print("💖 HAPPY BIRTHDAY VIJAYA 💖")
    print(f"✨ It's {formatted_time} on {formatted_date}! ✨")
    print("❤️ 🎂🎁 Wishing you all the happiness in the world! 🎁🎂 ❤️")
    print("========================================")

# Main execution
if __name__ == "__main__":
    countdown(10)
    display_birthday_message()
