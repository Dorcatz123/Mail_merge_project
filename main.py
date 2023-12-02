##****Birthday party invitation letter creator****


#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
invited_names = open("./Input/Names/invited_names.txt", "r")
invited_list = invited_names.read().split('\n')
starting_letter = open("./Input/Letters/starting_letter.txt", "r")
letter = starting_letter.read()
#print(letter)
letter_list = letter.split('\n')
letter_content = letter_list[1:]
for invitee in invited_list:
    new_letter = [f'Dear {invitee},']
    new_letter.extend(letter_content)
    finished_letter = '\n'.join(new_letter)
    new_invitee = open(f"letter_for_{invitee}.txt", "w" )
    new_invitee.write(finished_letter)


