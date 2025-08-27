def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).upper()
    true = 0
    love = 0
    for letter in combined_name:
        if 'T' in letter or 'R' in letter or 'U' in letter or 'E' in letter :
            true += 1 
    for letter2 in combined_name:
        if 'L' in letter2 or 'O' in letter2 or 'V' in letter2 or 'E' in letter2:
            love += 1            

    true_love = str(true)+ str(love)
    print(true_love)

calculate_love_score("Kanye West", "Kim Kardashian")