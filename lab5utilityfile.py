# COMPUTING I Lab 5 Utility File

# Dictionary to map user's choice to the movie name.
choice_to_movie = {
    '1': 'Interstellar',
    '2': 'Inception',
    '3': 'Tenet',
    '4': 'The Dark Knight',
    '5': 'Oppenheimer',
}

def display_movies():
    print(""); # blank space
    print(" 1) Interstellar"); # number one option is Interstellar
    print(" 2) Inception"); # number two option is Inception
    print(" 3) Tenet"); # number three option is Tenet
    print(" 4) The Dark Knight"); # number four option is The Dark Knight
    print(" 5) Oppenheimer"); # number five option is Oppenheimer

def validateget_movie(selectedchoice): # define validateget_movie with the selectedchoice paramater
    if int(selectedchoice)>5 or int(selectedchoice)<1: # if the integer of the selected choice is greater than 5 OR less than 1
        return "None" # then return none
    else: # otherwise
        return choice_to_movie[str(selectedchoice)]; # return the string value of the selected movie

def find_movie(movie_list, movie_to_search): # define find_movie with the movie_list and movie_to_search paramater
    for movie in movie_list: # for loop for if the movie in the movie list
        if movie[0] == movie_to_search: # is equal to 0 (in the array value), it is equal to movie_to_search
            return movie; # return movie value

def calculate_total_revenue(movie_list): # define the calculate_total_revenue function with the movie_list paramater
    return sum(int(movie[2]) for movie in movie_list); # return that the sum for the integer of movie [2] (2 is the value in the array) for the movie in the movie list
