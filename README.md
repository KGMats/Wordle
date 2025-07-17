# Python Wordle Clone with AI Solver



https://github.com/user-attachments/assets/4cb26e85-4439-4d9d-9af2-cd0d69be621d



This project is a fully-featured Wordle-style game created with Python and Pygame. It includes a complete graphical user interface, an intelligent AI player designed to solve the puzzle efficiently, and a tournament mode to evaluate the AI's performance. The game supports multiple languages.

This project was developed for the MC102 - Algorithms and Computer Programming course.

## Key Features

- **Graphical User Interface:** A clean and interactive game interface built with Pygame.
- **AI Solver:** An intelligent player that uses an entropy-based strategy to make optimal guesses.
- **Tournament Mode:** A powerful script to simulate thousands of games and evaluate the AI's average performance, including metrics like mean, median, and standard deviation of guesses.
- **Multi-language Support:** Play in English, Portuguese, Spanish, French, or Italian.
- **Classic Wordle Rules:** Follows the classic gameplay loop of guessing a 5-letter word in six attempts with color-coded feedback.

## Requirements

To run this project, you will need Python 3 and the following libraries:
- `pygame` for the game interface.
- `tqdm` for the progress bar in tournament mode.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Install the dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install the required packages
    pip install -r requirements.txt
    ```

## How to Play

### 1. Manual Game

To play the game yourself, run the `game.py` script:

```bash
python game.py
```

-   Type letters to form your guess.
-   Press `Enter` to submit a word.
-   Press `Backspace` to delete a letter.
-   The game will provide feedback:
    -   **Green:** Correct letter in the correct position.
    -   **Yellow:** Correct letter in the wrong position.
    -   **Gray:** Letter is not in the word.

### 2. How to specify the language

By default the game will use the portuguese dictionary, but you can choose the language by passing the --lang flag
```bash
python game.py --lang en
```
### 3. Watch the AI Play

You can also watch the AI solve the puzzle in real-time.

-   Run the game: `python game.py --auto`

### 4. Run an AI Tournament

To evaluate the performance of the AI player over a large number of games, run the `tournament.py` script. It will simulate many games and print the statistics at the end.

```bash
python tournament.py
```
This will output the average number of attempts, median, standard deviation, and other useful metrics.



## Project Structure

```
.
├── game.py             # Main script to run the playable game with Pygame GUI.
├── player.py           # Contains the logic for the AI solver.
├── tournament.py       # Script to run simulations and evaluate the AI's performance.
├── utils.py            # Helper functions for loading words, choosing words, etc.
├── words_en.txt        # English word list.
├── words_fr.txt        # French word list.
├── words_it.txt        # Italian word list.
├── words_pt.txt        # Portuguese word list.
├── words_sp.txt        # Spanish word list.
└── requirements.txt    # A file with the pip dependencies
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add new features (like a new AI strategy or UI enhancements), feel free to fork the repository and submit a pull request.
