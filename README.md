# Breakout Clone

A simple clone of the classic Breakout game implemented in Python using the `pygame` library.

## Table of Contents
- [Breakout Clone](#breakout-clone)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Running Tests](#running-tests)
  - [Contributing](#contributing)
  - [License](#license)
  
## Overview

This project is a clone of the classic arcade game Breakout. The objective of the game is to destroy all the bricks by bouncing a ball off a paddle controlled by the player.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lainceline/pybreak.git
   cd pybreak
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install pygame
   ```

## Usage

To run the game, execute the following command:
```bash
python main.py
```

Use the left and right arrow keys to move the paddle and prevent the ball from falling off the screen.

## Running Tests

To run the tests, execute the following command:
```bash
python -m unittest discover
```

The tests cover basic functionalities such as paddle movement, ball collision with walls, paddle, and bricks.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
