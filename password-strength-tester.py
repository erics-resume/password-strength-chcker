import re

import colorama
from colorama import Fore, Style, init
colorama.init(autoreset=True)


# Create new class called PasswordStrengthTester to test password strength
class PasswordStrengthTester:
    # Parameters include
    # password
    # password strength score
    def __init__(self, password, password_strength_score):
        self.password = password
        self.password_strength_score = 0

    # Check/calculate strength of password
    def calculate_password_strength(self):
        self.password_strength_score = 0

        proper_length = len(self.password) >= 12 or len(self.password) <= 20 # length must be greater than 12
        special_characters = "[@_!#$%^&*()<>?/|}{~:]"
        # contains_digits = re.search(r"\d", self.password)  # Detect digits in password
        # contains_uppercase = re.search(r"[A-Z]", self.password)  # Detect uppercase letters in password
        # contains_lowercase = re.search(r"[a-z]", self.password)  # Detect lowercase letters in password
        # contains_special_char = re.search(r"\W", self.password)  # Cannot detect special chars in password

        # Algorithm to calculate strength of password
        # Go through each character one by one possibly
        # check if password contains those specific chars
        # when certain criteria is matched, add/increment to password strength score
        # Calculate password length

        if (proper_length):
            self.password_strength_score += 1


        # Char Diversity Tests
        while True:
            if any(char.isdigit() for char in self.password):
                self.password_strength_score += 1
            if any(char.isupper() for char in self.password):
                self.password_strength_score += 1
            if any(char.islower() for char in self.password):
                self.password_strength_score += 1
            if any(char in special_characters for char in self.password):
                self.password_strength_score += 1
            break

        return self.password_strength_score


    # Display strength of password
    def display_password_strength(self):
        # Conditions
        # Password strength score
        # if password strength score is less than or equal to 2
        if self.password_strength_score <= 2:
            print(Fore.RED + "Password Strength: Weak")
        # else if password strength score is less than or equal to 4
        elif self.password_strength_score <= 4:
            print(Fore.LIGHTYELLOW_EX + "Password Strength: Medium")
        # else if password strength score is less than or equal to 6
        elif self.password_strength_score <= 6:
            print(Fore.YELLOW + "Password Strength: Strong")
        else:
            print(Fore.GREEN + "Password Strength: Very Strong")


if __name__ == "__main__":
    password = input("Enter password you want to test: ")
    password_tester = PasswordStrengthTester(password, 0)
    password_tester.calculate_password_strength()
    password_tester.display_password_strength()