def letter_count():
    sentence = input("enter a sentence").lower()
    letter = []
    number = []

    for i in sentence:
        if i not in letter:
            letter.append(i)   
            number.append(sentence.count(i))
        
        
    return dict(zip(letter,number))

print(letter_count())