# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:24:09 2023

@author: C20441194
"""

# using abc module to create abstract classes and methods
from abc import ABC, abstractmethod
class Person(ABC):
    # Initialise Person object with name and age
    def __init__(self, n, cAge):
        self.name = n
        self.age = cAge
        
    # marking this methods as abstract method 
    @abstractmethod  
    def getName(self):
        pass

    
    
class Actor(Person):
    def __init__(self, name, age, r):
        super().__init__(name, age)
        self.leadRole = r
        
    def setLeadRole(self, lr):
        self.leadRole = lr
        
    # overriding abstract getName from super class
    def getName(self):
        return self.name
    
    # printable string representation
    def __str__(self):
        return "Actor name: " + self.name + "is and the lead Actor: " + str(self.leadRole)
    
    
class Director(Person):
    def __init__(self, name, age, directedMovies):
        super().__init__(name, age)
        self.moviesDirected = directedMovies
        
     # declaring mutator (set) & accessor (get) methods for the instance variables   
    def setNofMoviesDirected(self, nMovD):
        self.moviesDirected = nMovD
        
    def getNofMoviesDirected(self):
        return self.moviesDirected
    
    # overriding abstract getName from super class
    def getName(self):
        return self.name
    
    # eq and lt to compare two directors for equality and if one director has directed more the other
    def __eq__(self, otherDirector):
        return self.moviesDirected == otherDirector.getNofMoviesDirected()
    
    def __lt__(self, otherDirector):
        return self.moviesDirected < otherDirector.getNofMoviesDirected()
    
    # printable string representation
    def __str__(self):
        return "Director name: " + self.name + "; has directed these number of movies: " + str(self.moviesDirected)
    

# # This class show the implemention of aggregation relationship between this class and Person
class Listing:
    def __init__(self,  mtitle, mduration, mrev):
        self.title = mtitle
        self.duration = mduration
        self.revenue = mrev
        self.actors = [] # list to store actors
        self.directors = [] # list to store directors
    
    # adding actors to the list
    def addActorName(self, actorNames):
        if actorNames not in self.actors:
            self.actors.append(actorNames)
            print(f"{actorNames.name} is added to the service.")
    
    # adding directors to the list
    def addDirectorName(self, directorNames):
        self.directors.append(directorNames)
    
    # printable string representation
    def __str__(self):
        return f"{self.title}: {self.duration} mins, Revenue is €{self.revenue}"
    
    
        
# inheriting from the Listing class.
class Movie(Listing):
    def __init__(self, mtitle, mduration, mrev, genre):
        super().__init__(mtitle, mduration, mrev)
        self.genre = genre
    
    def setRevenue(self, mrev):
        # data intergrity check for revenue
        if mrev < 0:
            self.revenue = 0
        else:
            self.revenue = mrev

    def getRevenue(self):
        return self.revenue
    

    def __lt__(self, otherMovie):
        # Compare movies based on their titles
        return self.title < otherMovie.title
    

    # printable string representation
    def __str__(self):
        return f"Movie: {self.title}, {self.duration} mins, Revenue is €{self.revenue}, Genre: {self.genre}"
        
    
        
# inheriting from the Listing class.       
class TvShow(Listing):
    def __init__(self, mtitle, mduration, mrev, season, episodes):
        super().__init__(mtitle, mduration, mrev)
        self.season = season
        self.episodes = episodes
        
    
    # Compare TV shows based on their titles
    def __lt__(self, otherTvShow):
        return self.title < otherTvShow.title
    
    # printable string representation
    def __str__(self):
        return f"Tv Show: {self.title}, {self.duration} mins per episode, Revenue is {self.revenue}, {self.season} season, {self.episodes} episodes per season"
    
    
class ListingService:
    def __init__(self, service_name):
        self.serviceName = service_name
        self.listings = [] # store the movie and tvshow
        #self.tv_shows = []
        
    # Add movies and tv show to the service
    def addListing(self, listing):
        if listing not in self.listings:
            self.listings.append(listing)
            print(f"{listing.title} is added to the service.")
   
    # remove movies or tv show
    def removeListing(self, listing):
        if listing in self.listings:
            self.listings.remove(listing)
            print(f"{listing.title} is removed from the service.")
        else:
            print(f"{listing.title} is not in the service.")
            
    # search for movies or tv show
    def searchListing(self, listing):
        # exception handling for any attribute error
        try:
            if listing in self.listings:
                print(f"{listing.title} is available")
            else:
                print(f"{listing.title} is not available")
        except AttributeError as err:
            print(f"An error occured: {err}")

    # sort the list on default ordering
    def sortListing(self):
        self.listings.sort()
    
    # return a new sorted list based on the default ordering
    def sortedListing(self):
        return sorted(self.listings)
    
    # this will sort the listings based on title
    def sortByNameListing(self):
        self.listings.sort(key=lambda listing: listing.title)
        # self.tv_shows.sort(key=lambda tvshow: tvshow.title)
    
    # return new sorted listing based on the tite
    def sortedByNameListing(self):
        return sorted(self.listings, key=lambda listing: listing.getlistingName())

    # Using filter to iterate through each listing in the 'listings' list
    def filteredType(self, list_type):
        return list(filter(lambda listing: (list_type == 'Movie' and type(listing) is Movie) or 
                           (list_type == 'tvshow' and type(listing) is TvShow), self.listings))
    
    # printable string representation
    def __str__(self):
        returnString = ''
        
        for listing in self.listings:
            returnString += str(listing.title) + '; '
        return self.serviceName  + "\n" + " The result are: " + returnString + "\n"

    

    
def main():
    
    # Create instance for actor and director
    actor1 = Actor("Denzel Washington", 68, "Main Actor")
    print(f"Actor Name: {actor1.name} \nAge:  {actor1.age} \nRole: {actor1.leadRole}")
    
    
    actor2 = Actor("Leonardo DiCaprio", 47, "Lead Actor")
    print(f"Actor Name: {actor2.name} \nAge:  {actor2.age} \nRole: {actor2.leadRole}")
    
    print("___________________________________________________")
    
    director1 = Director("Jordan Peele", 60, 9)
    print(f"Director name: {director1.name} \nAge: {director1.age} \nMovies Directed {director1.moviesDirected}")
    
    director2 = Director("Christopher Nolan", 50, 10)
    print(f"Director name: {director2.name} \nAge: {director2.age} \nMovies Directed: {director2.moviesDirected}")
    
    # comparing the directors
    print("\n Comparing two director nof movies")
    print("Director 1 has same number movies as Drirector 2: ", director1 == director2)  # False
    print("Director 1 number movies is less than Drirector 2: ", director1 < director2)   # True
    
    
    print("___________________________________________________")
    
    # Creating instance for movie and tv show
    movie1 = Movie("The Equaliser", 112, 192000000, "Action, Sci-fi")
    print(f"Movie 1: {movie1.title}, {movie1.duration} mins, Revenue is €{movie1.revenue}, Genre: {movie1.genre}, Actors: {actor1.name}, Director: {director1.name}")
    
    movie2 = Movie("Inception", 148, 829895144, "Action, Adventure, Sci-Fi")
    print(f"Movie 2: {movie2.title}, {movie2.duration} mins, Revenue is €{movie2.revenue}, Genre: {movie2.genre}, Actors: {actor2.name}, Director: {director2.name}")
    
    movie3 = Movie("Get Out", 104, 255407969, "Horror, Mystery, Thriller")
    print(f"Movie 3: {movie3.title}, {movie3.duration} mins, Revenue is €{movie3.revenue}, Genre: {movie3.genre}, Actors: {actor1.name}, Director: {director1.name}")
    print("___________________________________________________")
    
    tvshow1 = TvShow("Snowfall", 45, "Unknown", 5, 10)
    print(f"1. Tv Show: {tvshow1.title}, {tvshow1.duration} mins per episodes, Revenue is {tvshow1.revenue}, {tvshow1.season} season, {tvshow1.episodes} per season")
    
    tvshow2 = TvShow("Breaking Bad", 50, "Drama", 5, 13)
    print(f"\n2. Tv Show: {tvshow2.title}, {tvshow2.duration} mins per episode, Revenue is {tvshow1.revenue}, {tvshow2.season} season, {tvshow2.episodes} episodes per season")
    
    tvshow3 = TvShow("Atlanta", 30, "Drama", 3, 10)
    print(f"\n3. Tv Show: {tvshow3.title}, {tvshow3.duration} mins per episode, Revenue is {tvshow3.revenue}, {tvshow3.season} season, {tvshow3.episodes} episodes per season")
    
    print("\n ________________New Tv Show and Movie added___________________")
    # This will add the movies into database list created
    listing = ListingService("Netflix")
    
    # adding the movies and tv show to the list "listings"
    listing.addListing(movie1)
    listing.addListing(movie2)
    listing.addListing(movie3)
    listing.addListing(tvshow1)
    listing.addListing(tvshow2)
    listing.addListing(tvshow3)
    print("\nPrinting result!!!!")
    print(listing)

    # this will remove movie in database
    listing.removeListing(movie1)
    print("Printing updated result!!!!")
    print(listing)
    
    # Searching for a movie in the database
    listing.searchListing(movie1)
    listing.searchListing(tvshow1)
    # print("\nSearch result\n")
    # print(listing)
    
    # sort and sorted builtin module
    listing.sortListing()
    print("Sorted by default")
    print(listing)
    
    listing.sortByNameListing()
    print("Sorted by name ascending order:")
    print(listing)
    
    
    listing.sortByNameListing()
    print(listing)
    
    
   # Filter movies and print
    movies = listing.filteredType('Movie')
    print("\nFiltered Movies:")
    for movie in movies:
        print(movie)

    # Filter TV shows and print
    tv_shows = listing.filteredType("tvshow")
    print("\nFiltered TV Shows:")
    for tv_show in tv_shows:
        print(tv_show)

    
if __name__ == '__main__':
    main()
    
    
    
   