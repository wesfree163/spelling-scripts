
# function that takes names and separates them where the comma&space is at
def func():
    print("what we watchin?")
    lineup = str(input('> example: Atlanta, Fargo, Bleach, Blade, ...\n\n$>'))
    list_shows = lineup.split(', ')
    # print(list_shows)
    return list_shows
    
for val in func():
    print(f"{val} length is {len(val)}")
    
# some thowaway time code
print("Time modules\n\n")
sec = 6000
print(f"time in seconds, {sec}")

td = timedelta(seconds=sec)
print(f'\ntime in hh:mm:ss, {td}')

# use the below code if you want it in a string
print(f'\nstringified time: {str(timedelta(seconds=sec))} >> original type: {type(timedelta(seconds=sec))}')
