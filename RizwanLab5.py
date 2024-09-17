# This program was developed by Muhammad Ahmad Rizwan on 9/24/2023 as part of the COMPUTING 1 Lab 5 assignment.
# The purpose of this program is to allow users to search for  films directed by Christopher Nolan from a  list and to calculate the total revenue generated by all the movies in the list.
# This project involves splitting and processing string data structures and implementing searches and mathematical operations.

print('   '); # blank space
print('    This is a list of movies directed by Christopher Nolan, through this program, you can find a specific movie, the year it was made'); # description of program
print('    and the revenue generated by it.'); # description of program
print('   '); # blank space

import lab5utilityfile; # import Lab 5 Utility File

def main(): # define main function of the program
    data_string= "Interstellar, 2014, 701700000;Inception, 2010, 839000000;Tenet, 2020, 365300000;The Dark Knight, 2008, 1006000000;Oppenheimer, 2023, 890000000"; # data string including movie, release year, and revenue generated for all Christopher Nolan movies listed
    movieslist= [movie.split(",") for movie in data_string.split(";") if movie]; # movies list array where the movies are split by commas and the indiviual data blocks are split by semicolons
    chrisnolanmovies(movieslist); # chrisnolanmovies being identified with movieslist paramater

def chrisnolanmovies(movieslist): # define chrisnolanmovies function in the program, where the main happenings of the program occur
    print('Which Christopher Nolan movie would you like to know about?'); # print the heading question for the program
    lab5utilityfile.display_movies(); # referring to the utility file for the display movies code

    selectedchoice = input('Enter your choice [1-5]: '); # input choice between 1-5
    movies_to_search = lab5utilityfile.validateget_movie(selectedchoice); # referring to the utility file for the validating movie code
    if  movies_to_search == "None": # if 'None' is chosen for the movies_to_search functin
        print('Invalid choice!'); # Then an invalid choice notice will be printed
        return; # return value
    found_movie = lab5utilityfile.find_movie(movieslist, movies_to_search); # referring to the utility file for the validating found movie code

    if found_movie: # if movie is found
        print(f"{movies_to_search} was released in {found_movie[1]} and has earned ${found_movie[2]}"); # then the the movie name, release data, and revenue will be shown
    else: # otherwise
        print(f"No information found for {movies_to_search}"); # no information will be shown

    selectedchoice2 = input('Would you like to know about the total revenue of all of these movies(Y/N)?: '); # then the second user choice comes in asking if they want to know ALL the revenue for movies combined
    if selectedchoice2 == 'Y': # if Y is selected (or yes)
        total_revenue = lab5utilityfile.calculate_total_revenue(movieslist); # then the total revenue is shown
        print(f"Total revenue from all movies is ${total_revenue}"); # total revenue is shown from all the movies
    else: # otherwise
        print('No worries, have a great day!'); # it will not display anything but this message

main(); # call main function
