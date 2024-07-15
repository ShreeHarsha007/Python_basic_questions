def convert_days(days):
    years = days // 365
    weeks = (days % 365) // 7
    remaining_days = (days % 365) % 7
    return years, weeks, remaining_days

def main():
    days = int(input("Enter the number of days: "))
    years, weeks, remaining_days = convert_days(days)
    print(f"{days} days is equal to {years} years, {weeks} weeks, and {remaining_days} days.")

if __name__ == "__main__":
    main()
