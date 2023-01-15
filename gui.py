import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from tensorflow.keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))



def bow(sentence, words, show_details=True):

    sentence_words = clean_up_sentence(sentence)

    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 

                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):

    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def clean_up_sentence(sentence):

    sentence_words = nltk.word_tokenize(sentence)

    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

import tkinter as tk

class ChatApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chat Pet")
        
        # Set the background color of the window
        self.root.configure(bg='#3f51b5')
        
        self.messages_frame = tk.Frame(self.root, bg='#3f51b5')
        self.scrollbar = tk.Scrollbar(self.messages_frame, bg='#3f51b5')
        
        # Create a canvas to display the chat logs
        self.canvas = tk.Canvas(self.messages_frame, height=200, width=500, yscrollcommand=self.scrollbar.set, bg='#ffffff')
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH)
        self.canvas.pack()
        
        self.messages_frame.pack()
        
        # Create an input field to type in messages
        self.entry_field = tk.Entry(self.root, width=50, bg='#ffffff', fg='#000000', font=('Helvetica', 12))
        self.entry_field.pack()
        
        # Create a send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, bg='#ffffff', fg='#000000', font=('Helvetica', 12))
        self.send_button.pack()
        
        # Create a dictionary to store the chat logs
        self.chat_logs = {}
        
        # Create a variable to store the y-coordinate of the last message
        self.last_y = 0
        
    def send_message(self):
        # Get the message from the input field
        message = self.entry_field.get()
        # Clear the input field
        self.entry_field.delete(0, 'end')
        
        # Add the message to the chat logs dictionary
        self.chat_logs[self.last_y] = ('user', message)
        
        # Display the message on the canvas
        self.display_message(self.last_y, 'user', message)
        
        # Increment the y-coordinate of the last message
        self.last_y += 20
        
        # Wait for a response from the bot
        response = self.get_response_from_bot(message)
        
        # Add the response to the chat logs dictionary
        self.chat_logs[self.last_y] = ('bot', response)
        
        # Display the response on the canvas
        self.display_message(self.last_y, 'bot', response)
        
        # Increment the y-coordinate of the last message
        self.last_y += 20
        
    def get_response_from_bot(self, message):
        resp = chatbot_response(message)
        return resp
    
    def display_message(self, y, sender, message):
        if sender == 'user':
            color = '#ff5722'
        elif sender == 'bot':
            color = '#2196f3'
        
        # Create a rectangle as the background of the message
        self.canvas.create_rectangle(0, y+30, 2000, y, fill=color, outline=color)
        
        # Create a text object to display the message
        self.canvas.create_text(5, y, anchor='nw', fill='#ffffff', font=('Helvetica', 12), text=message)
    
if __name__ == "__main__":
    app = ChatApp()
    app.root.mainloop()



