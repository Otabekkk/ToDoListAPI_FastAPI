import random

def rock_paper_scissors():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("Для выбора введи: 'камень', 'ножницы' или 'бумага'. Напиши 'выход', чтобы завершить игру.")
    
    choices = ["камень", "ножницы", "бумага"]
    
    while True:
        player_choice = input("Твой выбор: ").lower()
        
        if player_choice == "выход":
            print("Спасибо за игру! До встречи!")
            break
        
        if player_choice not in choices:
            print("Неверный выбор. Попробуй снова.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Компьютер выбрал: {computer_choice}")
        
        if player_choice == computer_choice:
            print("Ничья!")
        elif (
            (player_choice == "камень" and computer_choice == "ножницы") or
            (player_choice == "ножницы" and computer_choice == "бумага") or
            (player_choice == "бумага" and computer_choice == "камень")
        ):
            print("Ты выиграл!")
        else:
            print("Компьютер выиграл!")
        
        print()  # Пустая строка для удобства

if __name__ == "__main__":
    rock_paper_scissors()