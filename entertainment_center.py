import fresh_tomatoes
import media

# list of movie objects
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life, \
                         Woody and Buzz Lightyear go out to find Bo Peep and\
                         bring her back",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=msAciPMZdMM")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

jurassic_world = media.Movie("Jurassic World 2015",
                             "A new theme park is built on the original \
                              site of Jurassic Park",
                             "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",  # noqa
                             "https://www.youtube.com/watch?v=RFinNxS5KN4")

hunger_games = media.Movie("Hunger Game: Catching Fire",
                           "Katniss Everdeen and Peeta Mellark become targets \
                            of the Capitol after their victory in the 74th \
                            Hunger Games sparks a rebellion in the Districts \
                            of Panem.",
                           "https://upload.wikimedia.org/wikipedia/en/1/12/Catching-Fire_poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=jyPnQw_Lqds")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "While on a trip to Paris with his fiance's \
                                 family, a nostalgic screenwriter finds \
                                 himself mysteriously going back to the 1920s \
                                 everyday at midnight",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # noqa
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

school_of_rock = media.Movie("School of Rock",
                             "After being kicked out of a rock band, \
                              Dewey Finn becomes a substitute teacher of \
                              a strict elementary private school, only to try \
                              and turn it into a rock band.",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # noqa
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# store movie objects above in a list data structure
movies = [toy_story, avatar, jurassic_world, hunger_games,
          midnight_in_paris, school_of_rock]

# call funtion to build the HTML file to display the website
fresh_tomatoes.open_movies_page(movies)
