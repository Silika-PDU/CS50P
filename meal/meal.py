def main():
    user_time = input("Enter time (24-H): ")
    what_time = convert(user_time)

    if 7 <= what_time <= 8:
        print("Breakfast Time")
    elif 12 <= what_time <= 13:
        print("Lunch Time")
    elif 18 <= what_time <= 19:
        print("Dinner Time")
    
    


def convert(user_time):
    hour, minute = user_time.split(":")
    hour = int(hour)
    minute = int(minute)
    return hour + minute / 60


if __name__ == "__main__":
    main()