import random

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадаю число от 1 до 100, а ты постараешься угадать.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Введи число: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Моё число больше!")
            elif guess > number_to_guess:
                print("Моё число меньше!")
            else:
                print(f"Поздравляю! Ты угадал число {number_to_guess} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, вводи только числа!")

if __name__ == "__main__":
    guess_the_number()