from num2words import num2words as n2w
from word2number import w2n

print("\n")

def number_to_words(): 
    username = input("Input your name: ").title()
    print("\n")

    while True:

        choice_1 = input(username + ", if you want to change numbers to words, enter 1; \nElse if you want to change words to numbers, enter 2: ")
        print("\n")
        
        if choice_1 == "1":
            
            num_con = int(input("Write a number: "))
            print("\n")
            new_word = n2w(num_con)
            print("Your number in words is: " + new_word + "\n")
            try_again = input("Do you want to try again? (yes/no): ").lower()
            print("\n")

            if try_again == "yes":
                number_to_words()
            elif try_again == "no":
                print(username + ", " +"Thanks for your time. \n\n")      
                break

        elif choice_1 == "2":

            word_con = input("Write in words: ")
            new_num = w2n.word_to_num(word_con)
            print("\n")
            print("Your words in numerics is: " + str(new_num) + "\n")
            try_again = input("Do you want to try again? (yes/no): ").lower()
            print("\n")
            
            if try_again == "yes":
                number_to_words()
            elif try_again == "no":
                print(username + ", " +"Thanks for your time. \n\n")      
                break
        break
    return


number_to_words()