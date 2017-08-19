#converting the given string into meaningfull string by using the given hint
#written by tmanikanta in python 3.6.1



python_dictionary = {
                      'a': 'c' ,
                      'b': 'd',
                      'c' :'e',
                      'd' :'f',
                      'e' :'g',
                      'f' :'h',
                      'g' :'i',
                      'h' :'j',
                      'i' :'k',
                      'j' :'l',
                      'k' :'m',
                      'l' :'n',
                      'm' :'o',
                      'n' :'p',
                      'o' :'q',
                      'p' :'r',
                      'q' :'s',
                      'r' :'t',
                      's' :'u',
                      't' :'v',
                      'u' :'w',
                      'v' :'x',
                      'w' :'y',
                      'x' :'z',
                      'y' : 'a',
                      'z' :'b',
                      ' ' : ' ',
                      '.' : '.',
                      '\'' : '\'',
                      '(' : '(',
                      ')' : ')'
                    }
                    

def go_ahead(input_string) :
  empty_string = ""
  for i in input_string :
    empty_string += python_dictionary[i]
  
  return empty_string

string = input("Enter the string :")

print(go_ahead(string))
