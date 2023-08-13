from textblob import TextBlob

word = input("Enter Word: ")
print("Original text: "+ str(word))

correct_word = TextBlob(word).correct()
print("Corrected Word: "+str(correct_word))
