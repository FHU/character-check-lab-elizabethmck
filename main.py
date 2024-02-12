#Remove pass and complete the code
def check_character(word, index):
   
   
   if word[index].isalpha():
      return "letter"
   elif word[index].isspace():
      return "white space"
   elif word[index].isdigit():
      return "digit"
   else:
      return "unknown"

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))