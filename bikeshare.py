import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input("Please select the city for the info between Chicago, New York City or Washington\n").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print('We have no data for the selected city.\n')
        city = input("Please select the city for the info between Chicago, New York City or Washington\n").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please select the month info for the month to filter from January to June or select 'all' for all the months data\n").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print('We have no data for the selected month.\n')
        month = input("Please select the month info for the month to filter from January to June or select 'all' for all the months data\n").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please select the day info for the day to filter from Monday to Sunday or select 'all' for all the days data\n").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print('We have no data for the selected day.\n')
        day = input("Please select the day info for the day to filter from Monday to Sunday or select 'all' for all the days data\n").lower()


    print('-'*40)
    return city, month, day

    # I took the 'load_data' part from exercise question 3.
def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is', most_common_month)


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day is', most_common_day)


    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station is', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station is', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = ('from ' + df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most frequent combination of start station and end station trip are', most_frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_time = df['Trip Duration'].sum()
    print('Total travel time in seconds is: ', total_time,'\n')
    print('This information can also be translated into minutes,hours and days.\n')
    print('Total travel time in minutes is: ', total_time/60)
    print('Total travel time in hours is: ', total_time/3600)
    print('Total travel time in days is: ', total_time/86400)


    mean_time = df['Trip Duration'].mean()
    print('Mean travel time in seconds is: ', mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('Counts of user types are:\n', counts_of_user_types)


    # TO DO: Display counts of gender
    # I used 'an if statement' to check the data of the column has value, as Washington has no gender data. I searched on stack everflow to be sure of the usage.
    # https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas
    if 'Gender' in df.columns:
        count_of_gender = df['Gender'].value_counts()
        print('Counts of gender are:\n', count_of_gender)
    else:
        print('The selected city has no gender data.')
    #We can also change the user_stats function as 'user_stats(df,city) to display the name of the city.'



    if 'Birth Year' in df.columns:
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()
        print('Earliest year of birth is ', int(earliest_year_of_birth))
        print('Most recent year of birth is ', int(most_recent_year_of_birth))
        print('Most common year of birth is ', int(most_common_year_of_birth))
    else:
        print('The selected city has no birth year data.\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: Displaying row data.
    # It shows 5 lines each time. 
def printing_row_data(df):
        row=0
        raw_data =input('Would you like to see 5 raw data lines? Yes or No?\n')
        while True :
            if raw_data.lower() == 'yes':
                print(df.iloc[row : row + 5])
                row += 5
                raw_data = input('Would you like to see another 5 raw data lines? Yes or No?\n')

            else:
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        printing_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
