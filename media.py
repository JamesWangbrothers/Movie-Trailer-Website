import webbrowser


class Movie:

    """This class provides a way to store \
       a movie related information"""  # create the documentation

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # class variable

    # constructor to instantiate movie objects
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):  # class method

        """This method provides a way to play the trailer"""
        webbrowser.open(self.trailer_youtube_url)
