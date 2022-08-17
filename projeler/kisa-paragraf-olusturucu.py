def main():
    while True:
        name = input("Enter a name: ").title()
        color = input("Enter a color: ")
        adjective = input("Enter an adjective: ")
        animal = input("Enter an animal in plural: ")
        verb = input("Enter an action word: ")

        text = ' '.join((f"Hello I'm {name}! Today I went around",
                         f"in search of some {color} flowers for",
                         f"my {adjective} friend, who loves to",
                         f"see the {animal} {verb} every morning."))

        print("\nHere's a little story:\n")
        print(text)
        seguir = input("\nDo you want to try again? [y/n] ")
        if seguir.lower() == 'n':
            print("\nHave a nice day!... Goodbye!")
            break

if __name__ == "__main__":
    main()