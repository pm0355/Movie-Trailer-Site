# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"G:\udacity-fsnd\lessons\4(make classes)"

import media
import fresh_tomatoes

toy_story= media.Movie("Toy Story", "A Story of a boy and his toys that come to life.","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=4KPTXpQehio")
avatar= media.Movie("Avatar","A marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock= media.Movie("School of Rock", "Storyline", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille= media.Movie("Ratatouille","Storyline","https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://www.youtube.com/watch?v=c3sBBRxDAqk")
hunger_games=media.Movie("Hunger Games","Storyline","https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg","https://www.youtube.com/watch?v=mfmrPu43DF8")
midnight_in_paris=media.Movie("Midnight in Paris", "Storyline","https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [toy_story,avatar,school_of_rock,ratatouille,hunger_games,midnight_in_paris]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)