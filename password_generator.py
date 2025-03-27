from random import choice, randint, shuffle
import pyperclip

class PasswordGenerator:
    @staticmethod
    def generate():
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '!#$%&()*+'

        password_list = (
            [choice(letters) for _ in range(randint(8, 10))] +
            [choice(symbols) for _ in range(randint(2, 4))] +
            [choice(numbers) for _ in range(randint(2, 4))]
        )

        shuffle(password_list)
        password = "".join(password_list)
        pyperclip.copy(password)
        return password