import sys 
import os
temp = sys.stdout 
newpath = r'tweet_output' 
if not os.path.exists(newpath): os.makedirs(newpath)
sys.stdout = open("tweet_output/ft2.txt","a") 
import fileinput
sortlist=[]
for line in fileinput.input(['tweet_input/tweets.txt']):
    stripped = line.strip()
    split_words = stripped.split(' ')
    countlist = list(set(split_words))
    sortlist.append(len(countlist))
input_list = sortlist


def median(input_list):

    if len(input_list) % 2 == 1:
        b =  float(input_list[len(input_list)/2])
        print b
    else:
        b = float((input_list[len(input_list)/2]+input_list[len(input_list)/2 -1])/2.0)
        print b 
    

         
median(input_list)

sys.stdout.close() 
sys.stdout = temp
