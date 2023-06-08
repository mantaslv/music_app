# Music Player

Music Player is a Python-based application that allows you to listen to your favorite tunes. It uses `pipenv` for package management, and `unittest` for testing. This README provides instructions on how to install, use, and contribute to the project.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Linting](#linting)

## Installation

Music Player uses `pipenv` to manage dependencies. To install `pipenv` and the dependencies of the project, you can follow the steps below:

1. Clone the repository to your local machine using `git clone https://github.com/mantaslv/music_app.git`.
2. Navigate to the project directory using `cd music_app`.
3. If `pipenv` is not installed on your system, install it using `pip install pipenv`.
4. Install the dependencies of the project using `pipenv install`.

## Usage

After installing the dependencies, you can use the following commands:

- To activate the project's virtual environment, use `pipenv shell`.
- To run the application, use `python -m ui`.

Once the application is running, you can:

- add a track
- play a track
- delete a track
- list your tracks
- search your tracks
- summarise your top artists

## Testing

This project uses `unittest` for testing. To run the tests, you can use the following command: `python -m unittest`.

## Linting

The project uses `flake8` for linting. To lint the code, use the command: `flake8`.