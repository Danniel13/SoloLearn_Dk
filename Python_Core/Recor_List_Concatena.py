List1 = ['Harry Potter\n', 'The Hunger Games\n', 'Pride and Prejudice\n', 'Gone with the Wind']

#newList = file.readlines()
for line in List1:
    if line[-1] == "\n":
        print(line[0]+str(len(line)-1))
    else:
        print(line[0]+str(len(line)))