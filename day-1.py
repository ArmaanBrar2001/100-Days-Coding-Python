# Take an input character from the user and check whether the given input is a vowel or consonant.

a = input('Enter a character: ')
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
alpha = []

if a is a.isalpha():
    if a in vowels:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Invalid input')


