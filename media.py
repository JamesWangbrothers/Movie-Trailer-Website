import webbrowser

class Movie():
    """This class provides a way to store a movie related information""" # create the documentation
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] #class variable
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): #constructor to instantiate movie objects
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self): #class method
        webbrowser.open(self.trailer_youtube_url)
