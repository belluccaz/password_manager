# Password Manager

A simple password manager built with Python and Tkinter. This application allows you to generate strong passwords and save them securely in a local text file.

## Features

- Generate random strong passwords.
- Store website credentials (website, email/username, and password).
- Copy generated passwords to the clipboard automatically.
- Simple and user-friendly interface using Tkinter.

## Installation

### Prerequisites

- Python 3.x installed
- Required dependencies: `tkinter`, `pyperclip`

### Install Dependencies

Ensure you have `pyperclip` installed. You can install it using:

```bash
pip install pyperclip
```

On Linux, you may also need to install `xclip` or `xsel` for clipboard functionality:

```bash
sudo apt-get install xclip
```

## Usage

Run the script:

```bash
python main.py
```

## Project Structure

```
Password-Manager/
│── password_manager.py
│── ui.py
│── password_generator.py
│── data_manager.py
│── README.md
│── logo.png
```

- `ui.py` - Handles the graphical interface.
- `password_generator.py` - Generates secure passwords.
- `data_manager.py` - Saves and manages credentials.
- `main.py` - Runs the application.

## License

This project is open-source and available under the MIT License.
