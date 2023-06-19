# Python Mafia Game Simulation

This is a console-based simulation of the popular social deduction game, Mafia, written in Python. The simulation includes different roles such as Townsfolk, Detectives, Doctors, and Mafia members. The simulation also includes a chatbot narrator that uses OpenAI's GPT-3 model to generate text based on the game's events.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- OpenAI Python library

### Installing

- Install the required Python version if you haven't done so already. You can download Python from the [official website](https://www.python.org/downloads/).

- Navigate to the directory in which you would like this program to be installed. Run the following command in your terminal:

```bash
git clone https://github.com/dwood-97/Mafia
```

- Install the required libraries navigate to the "Mafia" directory. Run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Running the Simulation

To run the simulation, navigate to the directory containing the project files in your terminal and run the following command:

```bash
python3 main.py
```

## Running the Tests

This project includes some basic tests. You can run them using the following commands:

```bash
python -m unittest test_game.py
python -m unittest test_roles.py
```

## Built with

- Python
- OpenAI GPT-3

## Contributing

We welcome contributions from the community. If you'd like to contribute, please fork the repository and make your changes, then open a pull request to propose your changes.

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.
