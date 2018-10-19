import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
                 'washington': 'washington.csv' }


def input_print(input_elem, enterable_list):
    while True:
        ret = input(input_elem).lower()
        if ret in enterable_list:
            return ret         

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_print("\nWhich city would you like to analysis:\n",
                      ['chicago', 'new york city', 'washington'])
       
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input_print("\nWhich month would you like to analysis:\n",
                      ['all', 'january', 'february', 'march', 'april', 'may', 'june'])
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_print("\nWhich day would you like to analysis:\n",
                      ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])


    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] =  df['Start Time'].dt.month
    df['day'] =  df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]

    
    return df 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The popular month: {} ".format(popular_month))

    # TO DO: display the most common day of week
    popular_day_of_week = df['day'].mode()[0]
    print("The popular day of week: {} ".format(popular_day_of_week))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The popular hour: {} ".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].value_counts()
    print("The most start station:{} ".format(most_start_station))

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].value_counts()
    print("The most end station:{} ".format(most_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    combination_station_trip = df.groupby(["Start Station", "End Station"])
    most_ination_station_trip = combination_station_trip.size().idxmax()
    print("The most ination station trip:\n {} to {} ".format(most_ination_station_trip[0],most_ination_station_trip[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time: {}".format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time: {}".format(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The User Type:{}".format(user_types))

    # TO DO: Display counts of gender
    try:
        user_types = df['Gender'].value_counts()
        print("The counts of gender: {}".format(user_types))
    except:
        print("Sorry,data does not exise.")

    # TO DO: Display earliest, most recent, and most common year of birth    
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        most_resent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()
        print("\nThe earliest year of birth:{},\nmost resent year of birth:{},\nmost common year of birth:{}.".format(earliest_year_of_birth,most_common_year_of_birth,most_common_year_of_birth))
    except:
        print("Sorry,data does not exise.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

