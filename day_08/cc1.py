from art import logo
print(logo)

def caesar(input_text,shift_amt,encode_or_decode):
    cipher_text = ''
    if encode_or_decode == 'decode':
            shift_amt *= -1
    for letter in input_text:
        if not letter.isalpha():
            cipher_text += letter
            continue
        ind = letters.index(letter)
        actual_shift = (ind+shift_amt)%len(letters)
        cipher_text += letters[actual_shift]
    print(f"Here is the {encode_or_decode}"+f"d result : {cipher_text}")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
restart = None

while(restart != 'no'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n").lower().strip()
    text = input("Type your message : \n").lower().strip()
    shift = int(input("Type the shift number : \n"))
    caesar(input_text = text, shift_amt = shift, encode_or_decode = direction)

    restart = input("\nDo you want to restart the program ? yes/no: ").lower().strip()
    print()
