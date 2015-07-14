import sys 
import os
import fileinput


temp = sys.stdout 
newpath = r'tweet_output' 
if not os.path.exists(newpath): os.makedirs(newpath)
sys.stdout = open("tweet_output/ft1.txt","w")  #please specify the proper path

wordlist=[]

for line in fileinput.input(['tweet_input/tweets.txt']): #please specify the proper path
    word = line.strip().split(' ')
    wordlist.extend(word)
    
def wordListToFreqDict1(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    a =  dict(zip(wordlist,wordfreq))
    for key, value in sorted(a.items()):
        print("{} : {}".format(key, value))

                    
wordListToFreqDict1(wordlist)
sys.stdout.close() 
sys.stdout = temp
