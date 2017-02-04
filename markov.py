from histogram import Dictogram
# Do you know about Hidden Markov Chains ??  
# Markov chains are cool ...  :) :) :) 

def make_markov_model(data):
    markov_model=dict()

    for i in range(0,len(data)-1):
        if data[i] in markov_model:
            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]]=Dictogram([data[i+1]])


    return markov_model

# Hail Markov 

def make_higher_order_markov_model(markov_model,data,order):
    
    for i in range(0,len(data)-order):
        # Create the window
        window=tuple(data[i:i+order])
        # Add to the dictionary
        if window in markov_model:
            markov_model[window].update([data[i+order]])
        else:
            markov_model[window]=Dictogram([data[i+order]])

    return markov_model