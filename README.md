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

## Sample json Response
```
{
  "results": [
    {
      "id": 667538,
      "original_title": "Original movie title",
      "overview": "Movie Overview",
      "release_date": "2023-06-06",
      "month": "JUN",
      "day": "06",
      "title": "Movie title",
      "poster_path": "/path/to/poster.png",
      "site": "YouTube",
      "key": "https://youtu.be/key",
      "logo_path": "/path/to/logo.png",
      "backdrop_path": "/rH3jY9JN9krUyE0Q3WLNtujMs8.jpg"
    },
    ...
  ]
}
```
## Hosting
For hosting Python scripts, you can consider the following free hosting solutions:

1. PythonAnywhere : [PythonAnywhere](https://www.pythonanywhere.com/) provides free hosting for Python scripts. It offers a web-based Python development environment and allows you to run Python scripts, schedule tasks, and even host web applications using Flask or Django.

2. Replit : [Replit](https://replit.com/) is an online coding platform that supports various programming languages, including Python. It allows you to write, run, and host Python scripts directly in the browser. Replit offers a free tier with limited resources.

3. Glitch : [Glitch](https://glitch.com/) is a collaborative coding platform that allows you to host and run web applications, including Python scripts. It provides a web-based development environment and offers free hosting with limited resources.

4. Google Colab : [Google Colab](https://colab.research.google.com/) is a cloud-based Jupyter notebook platform that provides free access to GPUs and TPUs for running Python scripts. While primarily designed for data science and machine learning tasks, it can also be used for general-purpose Python script hosting.

5. AWS Free Tier : [Amazon Web Services (AWS)](https://aws.amazon.com/free/) offers a Free Tier that allows you to host Python scripts using services like AWS Lambda and AWS EC2. You can run serverless functions or deploy virtual servers and take advantage of the free usage limits for a specified period.

6. Microsoft Azure Free Account : [Microsoft Azure](https://azure.microsoft.com/free/) provides a Free Account that includes a limited amount of free resources. You can leverage Azure Functions or Azure Virtual Machines to host and run Python scripts.

Please note that the free tiers of these hosting solutions may have limitations on resources, such as compute power, storage, or bandwidth. It's important to review their documentation and terms to ensure they meet your specific hosting requirements.

## Incorporate Tmdb_Movie_Fetcher in Your Applications
Feel free to use the Tmdb_Movie_Fetcher API in your applications and contribute to its enhancement. Integrate the API to retrieve movie details and leverage additional information like video links and logos.

## Contribution
We welcome contributions to enhance the Tmdb_Movie_Fetcher API and make it even more useful. If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue in the [GitHub repository](https://github.com/AkshayShineKrishna/Tmdb_Movie_Fetcher)
By contributing to Tmdb_Movie_Fetcher, you help create a better API for retrieving and processing movie details. Your contributions can benefit developers and movie enthusiasts alike.

Please make sure to review and follow the [contribution guidelines](https://github.com/AkshayShineKrishna/Tmdb_Movie_Fetcher/blob/master/CONTRIBUTING.md) before submitting your contribution.
