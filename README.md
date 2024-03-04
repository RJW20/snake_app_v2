# Snake App v2
A python implementation of the the game Snake using [pygame](https://www.pygame.org/docs/).

![alt text](https://i.imgur.com/KSBw9z2.png "Snake")

## Basic Requirements
1. [Python](https://www.python.org/downloads/).
2. [Poetry](https://python-poetry.org/docs/) for ease of installing the dependencies.

## Getting Started
1. Clone or download the repo `git clone https://github.com/RJW20/snake_app_v2.git`.
2. Set up the virtual environment with `poetry install`.
3. Enter the virtual environment with `poetry shell`.

## Usage
1. Change any settings in `settings.py`:
   - `grid_size` is the number of blocks in x, y directions.
   - `block_width` is the width in pixels of a block.
   - `block_padding` is the number of pixels that make up the gap between blocks.
   - `start_length` is the number of blocks the snake starts with.
   - `speed` is the number of frames per second the game runs at.
2. Run the game with `poetry run main`.
3. Use the arrow keys to change the snake's direction as appropriate.

## Note
This was made with the intention of creating an AI for the game using the genetic algorithm as seen [here](https://github.com/RJW20/snake_ai_genetic_algorithm_v2). Version 2 was created over my [original](https://github.com/RJW20/snake_app) because although the original allows for faster learning by always having the snake be travelling forward from it's perspective, this then also means the resulting AI will behave the same in every direction which is not what the perfect 'solution' to the game is.
