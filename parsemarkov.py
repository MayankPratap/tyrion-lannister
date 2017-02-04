from histogram import Dictogram
import random

def generate_random_start(model,followers):
    tup=('end','')

    if tup in model:
        seed_tup=tup

        while seed_tup==tup:
            seed_word=model[seed_tup].return_weighted_random_word()
            num=random.randint(0,len(followers[seed_word]))
            if num<len(followers[seed_word]):
                follower=followers[seed_word][num]
                seed_tup=(seed_word,follower)

        return seed_tup
        
    return random.choice(model.keys())


def generate_random_sentence(length,markov_model,followers):
    current_tup=generate_random_start(markov_model,followers)
    sentence=[]
    sentence.extend(current_tup)

    for i in range(0,length):
        #print(current_tup[0]+" "+current_tup[1])
        # Last two words of sentences are not captured
        # For example :- "lovely girl"
        if current_tup in markov_model:
            current_dicto=markov_model[current_tup]
            random_weighted_word=current_dicto.return_weighted_random_word();
            current_word=random_weighted_word
            sentence.append(current_word)
            current_tup=(current_tup[1],current_word)

    sentence[0]=sentence[0].capitalize()
    return ' '.join(sentence)+'.'
    return sentence 




