import time
import random

Hair = ["two long golden blades", "curly brown hair", "black wavy hair"]
Girl_hair = random.choice(Hair)
strange = ["a strange man", "a little boy", "a talking wolf"]
stranger = random.choice(strange)


def print_pause(s):
    print(s)
    time.sleep(2)


def valid_input(promot, option1, option2):
    while True:
        response = input(promot).lower()
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_pause("Sorry, I do not understand.")
    return response


def intro():
    print_pause(f"Once upon a time a little girl with {Girl_hair}"
                " and a yellow spotted dress was told from her parents not to"
                " go inside the dark forest as she was still very young to"
                " inside and live that experince.")
    print_pause("But she was very curious and could not hold herself back"
                " so she stepped in the dark forest , first it seems quite"
                " all of a sudden, a huge fence made up of trees grew fast"
                " and surround all the forest , now she is trapped inside"
                " ,all what she has to do is to live the experience and "
                " find her way out.")


def Tree_path():
    response = valid_input("There are trees from both side , it is dark and"
                           " scary but she keeps on moving, unfortunatly she"
                           " is tired, Should she sleep anywhere in the tree"
                           " path or wait till she find a safe place?\n"
                           "1.sleep anywhere.\n"
                           "2.find safe place.\n"
                           "Please enter '1' or '2'\n", "1", "2")
    if response == "1":
        print_pause("She wakes up finding herself hanging"
                    " upside down from her feet from a bunch"
                    " of monkeys.")
        print_pause("She fights them and was able to escape"
                    " till the end of the forest.")
    elif response == "2":
        print_pause("She keeps moving till she find a huge flower"
                    " like a tree and slept under it ")
        print_pause("next morning she keep moving till she reach the"
                    " end of the forest.")


def strangeman():
    response = valid_input("At the end of the river bank, There is "
                           f"{stranger} should she trust him?"
                           "Please say yes or no.\n", "yes", "no")
    if response == "yes":
        print_pause("He cuts her hair and trapped her"
                    " in a cage , now she will never get out"
                    " of the forest.")
        print_pause("you lose!!!")
    elif response == "no":
        print_pause("He follow her by his eyes but she did not"
                    " look him back , so He did not hurt her.")
        print_pause("She keep moving till she reach the Tree path.")
        Tree_path()


def stop_play():
    response = valid_input("Do you want to play again?\n"
                           "PLease say yes or no\n", "yes", "no")
    if response == "yes":
        print_pause("Ok, let's play again")
        intro()
        river_bank_and_tree_path()
        huge_fence()
    elif response == "no":
        print_pause("Ok, Good bye!!!")
        quit()


def river_bank_and_tree_path():
    response = valid_input("she looked infront of her there are two"
                           " way to go:\n"
                           " 1.The river bank way.\n"
                           " 2.The tree path.\n"
                           "Please enter '1' or '2'\n", "1", "2")
    if response == "1":
        print_pause("There are a lot of crocodiles she has to"
                    " run fast or she will be eatten.")
        strangeman()
        stop_play()
    elif response == "2":
        Tree_path()


def huge_fence():
    print_pause("A huge fence infront of her.")
    response = valid_input("What should she do?\n"
                           "1.Climp the fence.\n"
                           "2.Hit it with a branch of"
                           " a tree.\n", "1", "2")
    if response == "1":
        print_pause("She gets out of the forest safely")
        print_pause("You won!!")
        stop_play()
    elif response == "2":
        print_pause("she made lots of noise so the forest"
                    " creatures surround her and she has"
                    " to escape from them inside the forest"
                    " again!!")
        print_pause("You lose, Do you want to play again?")
        stop_play()


def play_game():
    intro()
    river_bank_and_tree_path()
    huge_fence()


play_game()
