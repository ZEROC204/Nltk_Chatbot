import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
[
        r"tell me some stuff about you|tell me about you|say about you|tell me about your personality|talk about yourself|talk some stuff about yourself|what are you|define yourself|I want to know you better|tell me about yourself",
        ["I'm a virtual being, not a real person.", "I am a virtual existence."]
    ],
    [
        r"what is your name ?",
        ["I'm ZERO"]
    ],
    [
        r"how are you ?",
        ["I'm doing good, How about You?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind"]
    ],
    [
        r"I am fine|fine",
        ["Great to hear that!"]
    ],
    [
        r"quit",
        ["Bye bye take care. It was nice talking to you :) "]
    ],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
