from histogram import Dictogram
from wordsegment import segment
from parsemarkov import generate_random_start,generate_random_sentence
from markov import make_higher_order_markov_model,make_markov_model
import random
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

if __name__=='__main__':
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=API(auth)

    model=dict()

    followers={}

    with open('gotcorpus.txt') as f:
        for line in f:
            if len(line)>2:
                words=line.lower().split()
                if(len(words)>0):
                    window=('end','') 
                    if window in model:
                        model[window].update([words[0]])
                    else:
                        model[window]=Dictogram([words[0]])
                    #print(line)
                    #print(words[0])
                    #print(words[1])
                    if(len(words)>1):
                        if words[0] in followers:
                            followers[words[0]].append(words[1])
                        else:
                            followers[words[0]]=[words[1],]

                    model=make_higher_order_markov_model(model,words,2)

# Now markov model is ready

#for i in start_words:
   #print(i)

    def generate_tweet(model,followers):
        tweet=''
        while len(tweet)<=140:
            temp=generate_random_sentence(10,model,followers) # Quotes contain average of 10 words and each word on average 5 letters therefore 50letters+10spaces=60 characters
            if len(tweet+temp)<=140:
                tweet+=temp
            else:
                break


        return tweet

    tweet=generate_tweet(model,followers)
    print(tweet+'\n')
    api.update_status(tweet)











