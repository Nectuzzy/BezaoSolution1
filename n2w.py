from num2words import num2words as n2w
from word2number import w2n

print("\n")

def number_to_words(): 
    username = input("Input your name: ").title()
    print("\n")

    while True:

        choice_1 = input(username + ", do you want to change numbers to words, yes/no: ").lower()
        print("\n")
        
        if choice_1 == "no":
            choice_2 = input(username + ", do you want to change words to numbers, yes/no: ").lower()
            print("\n")
            
            if choice_2 == "no":
                print(username + ", " +"Thanks for your time. \n\n")
                break
            elif choice_2 == "yes":
                word_con = input("Write in words: ")
                new_num = w2n.word_to_num(word_con)
                print("\n")
                print("Your words in numerics is: " + str(new_num) + "\n")
                print(username + ", " +"Thanks for your time. \n\n")
                break
        
        elif choice_1 == "yes":
            num_con = int(input("Write a number: "))
            print("\n")
            new_word = n2w(num_con)
            print("Your number in words is: " + new_word + "\n")
            print(username + ", " +"Thanks for your time. \n\n")
            break
    return


number_to_words()