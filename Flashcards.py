class Flashcards():
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash = []
print("Welcome to the flashcard application!")
while(True):
    word = input("Enter the word you want to add to your flashcard:")
    meaning = input("Enter the meaning of your word:")
    flash.append(Flashcards(word,meaning))
    options = int(input("Enter 0 if you want to add a word otherwise, enter 1:"))
    if(options):
        break
print("\nYour flashcard is:")
for i in flash:
    print(">", i)