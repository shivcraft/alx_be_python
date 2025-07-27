# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # save current datetime
    current_date = datetime.now()
    # print in “YYYY-MM-DD HH:MM:SS” format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # prompt user for days to add
    days_str = input("Enter the number of days to add to the current date: ")
    try:
        days = int(days_str)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # compute future_date
    future_date = datetime.now() + timedelta(days=days)
    # print in “YYYY-MM-DD” format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
