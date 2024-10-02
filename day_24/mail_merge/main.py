
def get_names():
    with open('input/names/invited_names.txt','r') as name_file:
        contents = name_file.read()
        name = contents.split('\n')
    return name

def get_letter_template():
    with open('input/letters/starting_letter.txt','r') as letter_file:
        letter = letter_file.read()
        lt = letter.split('[name]')
    return lt


names = get_names()
letter_template = get_letter_template()
for name in names:
    with open(f'output/ready_to_send/letter_to_{name}.txt','w') as file:
        file.write(letter_template[0]+name+letter_template[1])





