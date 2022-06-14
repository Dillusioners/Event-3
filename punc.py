import string #importing string module

given_string = input("Enter your paragraph or sentence as per your choice") #taking the input 
punc_string = given_string.translate(str.maketrans('','', string.punctuation)) #removing the punctuations using the translate function of the String package

print(punc_string) #printing the result