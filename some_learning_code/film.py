# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import defaultdict

user_movie_rating = defaultdict(lambda :defaultdict(int))

user_movie_rating["Alice"]["LOR1"] = 4
user_movie_rating["Alice"]["LOR2"] = 5
user_movie_rating["Alice"]["LOR3"] = 3
user_movie_rating["Alice"]["SW1"] = 5
user_movie_rating["Alice"]["SW2"] = 3

user_movie_rating["Huntsman"]["LOR1"] = 1
user_movie_rating["Huntsman"]["LOR2"] = 2
user_movie_rating["Huntsman"]["LOR3"] = 1
user_movie_rating["Huntsman"]["SW1"] = 4
user_movie_rating["Huntsman"]["SW2"] = 4

user_movie_rating["Snipe"]["LOR1"] = 3
user_movie_rating["Snipe"]["LOR2"] = 4
user_movie_rating["Snipe"]["LOR3"] = 4
user_movie_rating["Snipe"]["SW1"] = 2
user_movie_rating["Snipe"]["SW2"] = 1


print(user_movie_rating)