import random
#printing the list in good lookin way
def outoflist(l):
    for i in l:
        print(i, end=" ")
    print("\n")   
#a simple func to replace a value by index for lists
def re_place(l,i,v):
    l.insert(i,v)
    l.pop(i+1)
    return l
#the difficulity phase of game
def game_times():
    level = input("choose a hardness level : \n (a) easy \n (b) normal \n (c) hard \n")
    if level == "a":
        times = len(word) + 5
        print("you have chosen the easy difficulity , you have ",times," guess")
    if level == "b":
        times = len(word) + 3
        print("you have chosen the normal difficulity , you have ",times," guess")
    if level == "c":
        times = len(word) + 1        
        print("you have chosen the hard difficulity , you have ",times," guess")
    return times 
#reading a random word from the file 
def words_file():
    word_file = open("words.txt","r")
    list_words = word_file.readlines()
    j =random.randint(0,len(list_words)-1)
    word = list_words[j]
    word = word[:-1]
    return word
#the vars and list 
wlist_full = []
wlist = []
s = 0 
word = words_file()
times = game_times()
print("\n------------------------------------------------------\n")
#put the word into a list
for i in range(len(word)):
    wlist.append(" - ")
    wlist_full.append(word[i])
#the main loop of the game     
while s != times:
    print("Guess : ")
    n = input()
    s += 1
    #checking if the input is letter or word : LETTER
    if len(n) == 1:
        if n in word:
            print("that was correct ! good job")
            for i in range(len(word)):
                if wlist_full[i] == n:
                    re_place(wlist,i,n)
            outoflist(wlist)                     
        else:
            print("Wrong letter ! please try again")
            outoflist(wlist)
    #checking if the input is letter or word : WORD        
    if len(n)>1:
        if n == word :
            print("goodjob , YOU WIN ! , the word was : ",n)
            s = times
        else :
            print("Wrong word ! please try again ") 
            outoflist(wlist)
    #if user guesses all letters correct
    if wlist == wlist_full :
        print("goodjob , YOU WIN ! , the word was : ")
        outoflist(wlist_full)
        s = times
    if wlist != wlist_full and s == times:
        print("oh you lose :( , the word was " , word)    
    print("\n------------------------------------------------------\n")
