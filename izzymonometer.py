import datetime

current_time=datetime.datetime.now()

def time_until_lit(current_time):
    seconds_until=60 - current_time.second
    minutes_until=60-current_time.minute
    hours_until = 24-current_time.hour
#july 14th at 24 hours, 0 minutes and 0 seconds will be the time she is freee
    if current_time.month==7:
        days_until=14-current_time.day
    else:
        days_until = (30-current_time.day) + 14
    return('Allie will be getting LIT again in: \n' + str(days_until) + 'days\n' + str(hours_until)+ 'hours,\n' + str(minutes_until) + ' minutes, and\n' + str(seconds_until) + ' seconds\n you\n got\n this\n you\n mono\n beast\n')
#july 15th at 12:01am is when she can drink again

def main():
    print(time_until_lit(current_time))

if __name__ == '__main__':
    main()