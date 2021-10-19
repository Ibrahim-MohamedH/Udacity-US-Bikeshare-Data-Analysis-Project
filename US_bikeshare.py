import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # HINT: Use a while loop to handle invalid inputs
    while True:
        # get user input for city (chicago, new york city, washington).
        city = input("Which city would you like to see its data? (chicago, new york city, or washington)\n").lower().strip()
        if city not in ["chicago", "new york city", "washington"]:
            print("[-] please enter a valid city! (chicago, new york city, or washington)\n[+] Restarting the program...")
            continue
        # ask user if they want to filter time
        time_filter = input("Would you like to filter both Months and Days?\n(type \"yes\" to choose a specific month and day, or \"no\" to display full data)\n").lower().strip()
        if time_filter == "yes":
            # get user input for month (all, january, february, ... , june)
            month = input("Which month would you like to filter the data according to? (ex: all, january, february, ... , june)\n").lower().strip()
            if month not in ["all", "january", "february", "march", "april", "may", "june"]:
                print("[-] please enter a valid Month! (ex: all, january, february, ... , june)\n[+] Restarting the program...")
                continue
            # get user input for day of week (all, monday, tuesday, ... sunday)
            day = input("Which day would you like to filter the data according to? (ex: all, monday, tuesday, ... sunday)\n").lower().strip()
            if day not in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                print("[-] please enter a valid Day! (ex: all, monday, tuesday, ... sunday)\n[+] Restarting the program...")
                continue
        elif time_filter == "no":
            month = "all"
            day = "all"
        else:
            print("[-] please enter a valid answer! (type \"yes\" to choose a specific month and day, or \"no\" to display all data)\n[+] Restarting the program...")
            continue

        print('-' * 80)
        return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Loading the Data into DataFrames
    df = pd.read_csv(CITY_DATA[city])

    # Convert "Start Time" column to datetime based column
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # Extract Month and Day of week from "Start Time" column to create new columns
    df["Month"] = df["Start Time"].dt.month
    df["Day Of Week"] = df["Start Time"].dt.dayofweek

    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df.loc[(df["Month"] == month)]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = days.index(day.title())
        df = df.loc[(df["Day Of Week"] == day)]

    return df


def twelveH_period(hours):
    """Convert 24 hour period time to 12 hour period time (AM and PM)."""
    if 12 > hours > 1:
        hours = str(hours) + " AM"
    elif hours == 0:
        hours = "12 AM"
    elif hours > 12:
        hours = str(hours - 12) + " PM"
    return hours


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["Month"].mode()[0]
    months = ["January", "February", "March", "April", "May", "June"]
    common_month = months[common_month - 1]
    print("Most Common Month is: {}".format(common_month))

    # display the most common day of week
    common_day = df["Day Of Week"].mode()[0]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    common_day = days[common_day]
    print("Most Common Day of the week is: {}".format(common_day))

    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    twelve_hour_period = twelveH_period(common_hour)
    print("Most common hour of the day is: {} ({})".format(common_hour, twelve_hour_period))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    count_start_station = df["Start Station"].value_counts()[0]
    print("Most used Start Station is: {}\nWith count of: {} Times".format(common_start_station, count_start_station))
    print()

    # display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    count_end_station = df["End Station"].value_counts()[0]
    print("Most used End Station is: {}\nWith count of: {} Times".format(common_end_station, count_end_station))
    print()

    # display most frequent combination of start station and end station trip
    df["Trips"] = df["Start Station"] + " - " + df["End Station"]
    common_trip = df["Trips"].mode()[0]
    count_common_trip = df["Trips"].value_counts()[0]
    print("Most common Trip is: ({})\nWith count of: {} Times".format(common_trip, count_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df["Trip Duration"].sum()
    minutes = int(total_duration // 60)
    hours = minutes // 60
    print("Total Travel time in \n      Seconds: {:.2f}\n      Minutes: {}\n      Hours: {}".format(total_duration, minutes, hours))

    # display mean travel time
    average_duration = df["Trip Duration"].mean()
    minutes = int(average_duration // 60)
    print("Average Trip Duration in \n      Seconds: {:.2f}\n      Minutes: {}".format(average_duration, minutes))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # Display counts of user types
        user_type_count = df["User Type"].value_counts()
        print("Counts for each User Type: \n{}".format(user_type_count))
        print()
    except Exception as e:
        print("[-] No Data for {} in this city".format(e))
    try:
        # Display counts of gender
        count_of_gender = df["Gender"].value_counts()
        print("Counts for each gender: \n{}".format(count_of_gender))
        print()
    except Exception as e:
        print("[-] No Data for {} in this city".format(e))
    try:
        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = int(df["Birth Year"].min())
        most_recent_year = int(df["Birth Year"].max())
        most_common_year = int(df["Birth Year"].mode()[0])
        print("Oldest person birth year is: {}\nYoungest person birth year is: {}\nMost common birth year is: {}".format(earliest_birth_year, most_recent_year, most_common_year))
    except Exception as e:
        print("[-] No Data for {} in this city".format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def raw_data(df):
    """Displays Original raw data to the user."""
    while True:
        # get user input if they want to see the original raw data
        answer = input("Would you like to see the original raw data? (type \"yes\" or \"no\")\n").lower().strip()
        if answer == "yes":
            rows = 0
            while True:
                # if yes, display the first 5 rows
                print(df.iloc[rows: rows + 5, :-4])
                # get user input if they want to see more date
                more_data = input("would you like to see more data? (type \"yes\" or \"no\")\n").lower().strip()
                if more_data == "yes":
                    # if user wants to see more data display next 5 rows
                    rows += 5
                    continue
                elif more_data == "no":
                    break
                else:
                    print("[-] Invalid answer please type \"yes\" or \"no\" ")
                    continue
            break
        elif answer == "no":
            break
        else:
            print("[-] Invalid answer please type \"yes\" or \"no\" ")
            continue



def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        if restart != 'yes':
            break


if __name__ == "__main__":
    main()
