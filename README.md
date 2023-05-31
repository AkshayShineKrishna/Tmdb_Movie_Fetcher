# Tmdb_Movie_Fetcher
This repository contains a Flask application that retrieves and processes movie details from the [The Movie Database (TMDb)](https://developer.themoviedb.org/docs) API. The application provides two endpoints: /get_upcoming and /get_popular, which return upcoming and popular movie details, respectively.

## Prerequisites
You need an API key from TMDb to access their API.

### Generating TMDB API Key
1. Visit the TMDB website at [https://www.themoviedb.org/](https://www.themoviedb.org/) and create an account if you don't have one already.
2. Once logged in, navigate to your account settings.
3. In the account settings, select the "API" section.
4. Click on the "Request an API key" button.
5. Provide the necessary information and follow the instructions to generate your API key.

## Setup

1. Clone the repository to your local machine.
```
git clone https://github.com/AkshayShineKrishna/Tmdb_Movie_Fetcher.git
```
2. Create a virtual environment using [venv](https://docs.python.org/3/library/venv.html) or [virtualenv](https://pypi.org/project/virtualenv/). Here's an example using `venv`:
  - Run the command to create a virtual environment named `env` : 
```
python3 -m venv env
```
3. Activate the virtual environment:
- For Windows : 
```
.\env\Scripts\activate
```
- For Unix/macOS: 
```
source env/bin/activate
```
4. Install the required dependencies by running the command: 
```
pip install -r requirements.txt
```
5. Run the `main.py` file

## Usage

### Get Upcoming Movies

Endpoint: `/get_upcoming`

This endpoint retrieves upcoming movie details, including titles, release dates, overviews, posters, backdrops, video links, and logos. The application combines data from the themoviedb.org API and incorporates additional details not directly available from the API.

To use this endpoint, send a GET request to `/get_upcoming` with the `api_key` query parameter set to your themoviedb.org API key.

Example: 
```
http://localhost:5000/get_upcoming?api_key=<YOUR_API_KEY>
```

### Get Popular Movies

Endpoint: `/get_popular`

This endpoint retrieves popular movie details, including titles, release dates, overviews, posters, backdrops, video links, and logos. Similar to the `/get_upcoming` endpoint, the application combines data from the themoviedb.org API and incorporates additional details not directly available from the API.

To use this endpoint, send a GET request to `/get_popular` with the `api_key` query parameter set to your themoviedb.org API key.

Example: 
```
http://localhost:5000/get_popular?api_key=<YOUR_API_KEY>
``` 

For more information, refer to the Flask application code in `main.py`.
