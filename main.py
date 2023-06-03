from flask import Flask, jsonify, request
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/get_upcoming', methods=['GET'])
def get_upcoming():
    # Retrieve the 'api_key' query parameter from the request
    api_key = request.args.get('api_key')

    # Get the current date and time
    current_date = datetime.now()

    def fetch_data(url):
        # Function to make a GET request to the provided URL and return the JSON response
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    # Construct the base URL for the movie database API with the provided 'api_key'
    base_url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}'

    # Format the current date components to two digits
    current_day = str(current_date.day).zfill(2)
    current_month = str(current_date.month).zfill(2)
    current_year = current_date.year

    # Calculate the next month and year, considering the special case for December
    next_month = int(current_month) + 2 if current_month != '12' else '01'
    next_month = str(next_month).zfill(2)
    next_year = current_year if current_month != '12' else str(current_date.year + 1)

    # Construct the conditions strings for the API requests
    conditions = f"&primary_release_date.gte={current_year}-{current_month}-{current_day}" \
                   f"&primary_release_date.lte={next_year}-{next_month}-31"

    # Fetch data using the first conditions
    url = base_url + conditions
    upcoming_data = fetch_data(url)


    if upcoming_data is not None :
        movie_ids = [movie['id'] for movie in upcoming_data['results']]
        results = []

        # Second API call to retrieve images for each movie
        images_base_url = f'https://api.themoviedb.org/3/movie/{{}}/images?api_key={api_key}'

        for movie_id in movie_ids:
            images_url = images_base_url.format(movie_id)
            images_data = fetch_data(images_url)
            if images_data is not None and 'logos' in images_data:
                # Finding the first filepath that ends with '.png' in the 'logos' field
                filepath = next(
                    (logo['file_path'] for logo in images_data['logos'] if logo['file_path'].endswith('.png')), None)
            else:
                filepath = None
            # Extracting the month and day from the 'release_date'
            release_date = upcoming_data['results'][movie_ids.index(movie_id)]['release_date']
            release_date_obj = datetime.strptime(release_date, '%Y-%m-%d')
            month = release_date_obj.strftime('%b').upper()
            day = release_date_obj.strftime('%d')

            # Third API call to retrieve site and key
            videos_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}"
            videos_data = fetch_data(videos_url)

            if videos_data is not None and 'results' in videos_data:
                trailer_videos = [video for video in videos_data['results'] if
                                  video['type'] in ['Trailer', 'Teaser'] and video['site'].lower() == 'youtube']

                if trailer_videos:
                    # Append 'https://youtu.be/' to the key
                    key = 'https://youtu.be/' + trailer_videos[0]['key']
                    site = 'YouTube'
                else:
                    key = None
                    site = None
            else:
                key = None
                site = None

            if filepath is not None and upcoming_data['results'][movie_ids.index(movie_id)][
                'backdrop_path'] is not None:
                # Prepare movie data with file paths and separate keys for month and day
                movie_data = {
                    'id': movie_id,
                    'original_title': upcoming_data['results'][movie_ids.index(movie_id)]['original_title'],
                    'overview': upcoming_data['results'][movie_ids.index(movie_id)]['overview'],
                    'release_date': release_date,
                    'month': month,
                    'day': day,
                    'title': upcoming_data['results'][movie_ids.index(movie_id)]['title'],
                    'logo_path': filepath,
                    'backdrop_path': upcoming_data['results'][movie_ids.index(movie_id)]['backdrop_path'],
                    'site': site,
                    'key': key
                }
                results.append(movie_data)
        response_data = {'results': results}
    else:
        response_data = {'results': []}

    return jsonify(response_data)


@app.route('/get_popular', methods=['GET'])
def get_popular():
    # Retrieve the API key from the request parameters
    api_key = request.args.get('api_key')

    # Function to fetch the data from a given URL
    def fetch_data(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    # API call to retrieve popular movies
    popular_url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'
    popular_data = fetch_data(popular_url)

    if popular_data is not None:
        # Extracting the movie IDs from the JSON response
        movie_ids = [movie['id'] for movie in popular_data['results']]
        results = []

        for movie_id in movie_ids:
            # Second API call to retrieve images for each movie
            images_url = f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={api_key}'
            images_data = fetch_data(images_url)

            if images_data is not None and 'logos' in images_data:
                # Finding the first logo filepath that ends with '.png'
                logo_filepath = next(
                    (logo['file_path'] for logo in images_data['logos'] if logo['file_path'].endswith('.png')),
                    None)
            else:
                logo_filepath = None

            # Third API call to retrieve site and key
            videos_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}"
            videos_data = fetch_data(videos_url)

            if videos_data is not None and 'results' in videos_data:
                trailer_videos = [video for video in videos_data['results'] if
                                  video['type'] in ['Trailer', 'Teaser'] and video['site'].lower() == 'youtube']

                if trailer_videos:
                    # Append 'https://youtu.be/' to the key
                    key = 'https://youtu.be/' + trailer_videos[0]['key']
                    site = 'YouTube'
                else:
                    key = None
                    site = None
            else:
                key = None
                site = None

            # Prepare movie data
            movie_data = {
                'id': movie_id,
                'original_title': popular_data['results'][movie_ids.index(movie_id)]['original_title'],
                'overview': popular_data['results'][movie_ids.index(movie_id)]['overview'],
                'release_date': popular_data['results'][movie_ids.index(movie_id)]['release_date'],
                'title': popular_data['results'][movie_ids.index(movie_id)]['title'],
                'poster_path': popular_data['results'][movie_ids.index(movie_id)]['poster_path'],
                'site': site,
                'key': key,
                'logo_path': logo_filepath,
                'backdrop_path': popular_data['results'][movie_ids.index(movie_id)]['backdrop_path'],
            }
            results.append(movie_data)

        response_data = {'results': results}
    else:
        response_data = {'results': []}

    return jsonify(response_data)


if __name__ == '__main__':
    app.run()
