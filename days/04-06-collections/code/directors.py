import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = "movie_metadata.csv"
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)"""
    movies_by_director = defaultdict(list)
    with open(MOVIE_DATA, encoding="utf-8") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            try:
                year = int(row["title_year"])
            except ValueError:
                continue
            if year < MIN_YEAR:
                continue
            movies_by_director[row["director_name"]].append(
                Movie(row["movie_title"].strip(), year, float(row["imdb_score"]))
            )
    return movies_by_director


def get_average_scores(directors):
    """Filter directors with < MIN_MOVIES and calculate averge score"""
    scores = {
        (director, _calc_mean(movies)): movies
        for director, movies in directors.items()
        if len(movies) >= MIN_MOVIES
    }
    return scores


def _calc_mean(movies):
    """Helper method to calculate mean of list of Movie namedtuples"""
    return round(sum(movie.score for movie in movies) / len(movies), 1)


def print_results(directors):
    """Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output"""
    fmt_director_entry = "{counter}. {director:<52} {avg}"
    fmt_movie_entry = "{year}] {title:<50} {score}"
    sep_line = "-" * 60
    directors = sorted(directors.items(), key=lambda x: x[0][1], reverse=True)
    for i, ((director, avg), movies) in enumerate(directors, start=1):
        print(fmt_director_entry.format(counter=i, director=director, avg=avg))
        print(sep_line)
        for movie in movies:
            print(
                fmt_movie_entry.format(
                    year=movie.year, title=movie.title, score=movie.score
                )
            )
        if i <= 20:
            print()
        else:
            break


def main():
    """This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py"""
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == "__main__":
    main()
