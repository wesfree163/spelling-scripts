def get_shows():
    print('What shows are we going to watch?')
    lineup = str(input("> example: Atlanta, Rick and Morty, Fargo, Blade, ...\n\n$> "))
    watchList = lineup.split(',')
    print(f"{watchList}")

get_shows()