# Pablo's Flashcard Simulator

Welcome to Pablo's Flashcard Simulator (Alpha 0.09)! This simple command-line tool is designed to help you study and test your knowledge using flashcards. It's a lightweight, Python-based application that allows you to create, manage, and test yourself with custom flashcards, all within your terminal.

## What's Special?

- **Minimalistic Design**: The simulator operates directly in the command line, making it easy to use without any additional dependencies.
- **Customizable Flashcards**: You can create, edit, and delete flashcards, allowing for personalized study sessions.
- **Persistent Storage**: Your flashcards are saved and loaded using Python's `pickle` module, ensuring that your study progress is never lost.
- **Interactive Learning**: The tool provides an interactive way to test your knowledge by displaying the front of the card and asking you to recall the answer.

## How to Use

1. **Run the Simulator**:
   Start the program by running the `Main.py` file. You'll be greeted with a welcome message and a list of available commands.

   ```bash
   python Main.py
   ```

2. **Commands**:
   - `help`: Display a list of available commands.
   - `load`: Load a specific set of flashcards from a file.
   - `ls`: List all your current flashcards.
   - `saveas`: Save your flashcards to a file.
   - `start`: Begin a flashcard round to test your knowledge.
   - `clear`: Clear the terminal screen.
   - `rmcard`: Delete a specific flashcard.
   - `mkcard`: Create a new flashcard.

3. **Creating Flashcards**:
   Use the `mkcard` command to create a new flashcard. You'll be prompted to enter the front and back content of the card.

4. **Testing Yourself**:
   Use the `start` command to begin a flashcard round. You'll be shown the front of each card and asked to recall the answer. Afterward, you can mark whether you got the answer right or wrong.

5. **Save Your Progress**:
   Use the `saveas` command to save your flashcards to a file, so you can continue your study sessions later.

## Requirements

- Python 3.x

## Installation

1. Clone or download the repository.
2. Ensure Python is installed on your system.
3. Run the `Main.py` file to start the flashcard simulator.

## Future Improvements

- Adding support for more complex flashcard sets.
- Implementing a graphical interface for easier use.
- Enhancing feedback mechanisms for incorrect answers.
