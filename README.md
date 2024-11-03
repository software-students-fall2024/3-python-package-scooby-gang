# Python Package Exercise
![build](https://github.com/software-students-fall2024/3-python-package-scooby-gang/actions/workflows/build.yaml/badge.svg) <br>
## Contributors
[Lucia Song](https://github.com/lys7942) <br>
[Chelsea Hodgson](https://github.com/Chelsea-Hodgson) <br>
[Yeshni Savadatti](https://github.com/yeshnii) <br>
[Alan Zhao](https://github.com/Alan3562) <br>

## Description
Get your fortune for Python!

## Usage
This project allows users to receive randomly generated fortunes, either good or bad, by running commands in the terminal or by importing and using it as a module within a Python project. Users can create custom fortunes, purchase a batch of fortunes, or retrieve fortunes with a single function call.

### Command Line
To use the fortune generator from the command line, navigate to the project’s root directory and use the following command:

> $python -m src.fortune.FortuneCookie

This will prompt you to choose between generating a custom fortune or purchasing random fortunes. You will receive fortunes directly in the terminal based on your input.

Here’s a breakdown of the options:

**Custom Fortune (c)**: When prompted, type c to enter a custom fortune. You’ll then be asked to enter the custom fortune text, which will appear in a fortune cookie image.

**Purchase Fortunes (p)**: When prompted, type p to select a number of fortunes. You’ll then be asked how many fortunes you’d like (up to a maximum of 10). If you select more than 5 fortunes, the program will ask you to enter a valid amount.

### Import into Project
To use the fortune generator as a module within your Python project, import specific functions from FortuneCookie.py in your code:

> from src.fortune.FortuneCookie import quoteGetter, customFortuneCookie, addQuote, fortuneCookie, randomFortuneCookie, cookieScript

Here’s a brief description of each function and how to use it:

quoteGetter(fortuneAmount): Retrieves and prints a specified number of random good or bad fortunes. Returns a list of generated fortunes.
customFortuneCookie(userQuote): Prints a fortune cookie image with a custom fortune message passed as userQuote.
addQuote(userQuote, quoteType): Adds a custom fortune to either the good or bad fortune file. Specify quoteType as 'g' for good and 'b' for bad.
fortuneCookie(): Prints a blank fortune cookie image.
randomFortuneCookie(fortuneAmount): Prints a specified number of random fortunes from both good and bad files.
cookieScript(fortuneCustom): Simulates a process of creating or purchasing fortunes. Use 'c' for custom fortune and 'p' for purchasing multiple fortunes.

## Contributing
We welcome contributions! Here’s how you can help:
1. **Fork the Repository**: Start by forking the repository and cloning your fork to your local machine.
2. **Install Dependencies**: Make sure you have the necessary dependencies installed. You can install any required packages using:
   > $pip install -r requirements.txt
3. **Create a New Branch**: Create a branch for your feature or bug fix.
4. **Make Changes and Write Tests**: Make your changes, ensuring that you add or update tests as needed in the tests directory.
5. **Commit and Push Your Changes**: After finishing your work on local machine, commit and push your changes to git.
6. **Create a Pull Request**: Go to the original repository and create a pull request for your changes.

Please ensure your codes come with meaningful commit messages and follow the PEP 8 standard, which can be found in detail [here](https://peps.python.org/pep-0008/).
