# 🔐 Password Manager

A simple and efficient password manager developed with **Python** and **Tkinter**, using **Object-Oriented Programming (OOP)** concepts.

## 📌 Features

- **Secure Password Generator** 🔑  
  - Generates random and secure passwords with letters, numbers, and symbols.
  - Automatically copies the password to the clipboard.
  
- **Password Storage** 💾  
  - Saves passwords in a `data.txt` file along with the associated website and email.

## 🛠️ Technologies Used

- **Python** 🐍  
- **Tkinter** (Graphical Interface) 🎨  
- **pyperclip** (Automatically copies the generated password to the clipboard) 📋  

## 🚀 How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager
   ```

2. **Create a virtual environment (optional, but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the program**  
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
password-manager/
│── password_generator.py  # Class for generating secure passwords
│── data_manager.py        # Class responsible for saving passwords
│── ui.py                  # Application graphical interface
│── main.py                # Main file to run the app
│── data.txt               # File where passwords are saved
│── logo.png               # Application logo
│── requirements.txt       # List of project dependencies
│── README.md              # Project documentation
```

## 📜 License

This project is open source and licensed under the **MIT License**.

