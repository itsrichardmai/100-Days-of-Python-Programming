PLACEHOLDER = "[Name]"

def main():

    with open('./Names/names.txt') as names_file:
        names = names_file.readlines()
        # print(names)

    with open("./Letters/starting_letter.txt") as letter_file:
        letter_contents = letter_file.read()
        for name in names:
            clean_name = name.strip()
            new_letter = letter_contents.replace(PLACEHOLDER, clean_name)
            with open(f'./Output/ReadyToSend/LetterTo{clean_name}.txt', "w") as output_file:
                output_file.write(new_letter)

if __name__ == "__main__":
    main()