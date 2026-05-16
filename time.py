from datetime import timedelta
import random
import time

print("\nsample different given stop time")
def  get_raw_time(sec):
    # create a timedelta ond convert it to string
    td_str = str(timedelta(seconds=sec))
    print(f'time in seconds {sec}')
    
    # string into individual components
    time_div = td_str.split(':')
    print(f'\ntime in hh:mm:ss >> {time_div[0]} hours, {time_div[1]} minutes, {time_div[2]} seconds')
    
    return time_div
    
get_raw_time(3691)


print("\nsample different: time count down")
t = 36912
def triple_time_dec():
    # converts to hh:mm:ss format
    given_time = get_raw_time(t)
    i = 0
    time_val = 0
    while i < len(given_time):
        if i == 0:
            time_val += int(given_time[i]) * 3600
        if i == 1:
            time_val += int(given_time[i]) * 60
        if i == 2:
            time_val += int(given_time[i]) * 1
        i += 1
    
    print(f'proper time?? >> {time_val}')
    
triple_time_dec()

# anHour = 3600
# the_time = random.randint(1, 9000)
# if the_time < anHour:
#     print("setting a timer for (TV_Length) without the time for end credits")
#     print(f"proper time {the_time}")
#     time.sleep(the_time - 60)
# elif the_time > anHour:
#     print("setting a timer for (Movie_Length) without the time for end credits")
#     print(f"proper time {the_time}")
#     time.sleep(the_time - 420)