import re
import random
 
 
reflections = {
    "am": "are",
    "are": "am",
    "was": "were",
    "i": "you",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}
 
psychobabble = [
    [r'I need (.*)',
     ["Why do you need {0}?",
      "Are you sure you need {0}?"]],
 
    [r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Do you really want me to {0}?"]],
 
    [r'Why can\'?t I ([^\?]*)\??',
     ["Do you think you should be able to {0}?",
      "Have you really tried?"]],
 
    [r'I can\'?t (.*)',
     ["How do you know you can't {0}?",
      "What would it take for you to {0}?"]],
 
    [r'I am (.*)',
     ["Did you come to me because you are {0}?",
      "How do you feel about being {0}?"]],
 
    [r'I\'?m (.*)',
     ["How does being {0} make you feel?",
       "Why do you think you're {0}?"]],
 
    [r'Are you ([^\?]*)\??',
     ["Why does it matter whether I am {0}?",
      "I may be {0} -- what do you think?"]],
 
    [r'What (.*)',
     ["Why do you ask?",
      "What do you think?"]],
 
    [r'How (.*)',
     ["How do you suppose?",
      "What is it you're really asking?"]],
 
    [r'Because (.*)',
     ["Is that the real reason?",
      "If {0}, what else must be true?"]],
 
    [r'(.*) sorry (.*)',
     ["There are many times when no apology is needed.",
      "What feelings do you have when you apologize?"]],
 
    [r'Hello(.*)',
     ["Hello... I'm glad you could drop by today.",
      "Hello, how are you feeling today?"]],
 
    [r'I think (.*)',
     ["Do you doubt {0}?",
      "But you're not sure {0}?"]],
 
    [r'(.*) friend (.*)',
     ["Tell me more about your friends.",
      "Why don't you tell me about a childhood friend?"]],
 
    [r'Yes',
     ["You seem quite sure.",
      "OK, but can you elaborate a bit?"]],
 
    [r'(.*) computer(.*)',
     ["Are you really talking about me?",
      "Do you feel threatened by computers?"]],
 
    [r'Is it (.*)',
     ["Do you think it is {0}?",
      "It could well be that {0}."]],
 
    [r'It is (.*)',
     ["You seem very certain.",
      "If I told you that it probably isn't {0}, what would you feel?"]],
 
    [r'Can you ([^\?]*)\??',
      "Why do you ask if I can {0}?"]],
 
    [r'Can I ([^\?]*)\??',
     ["Perhaps you don't want to {0}.",
      "If you could {0}, would you?"]],
 
    [r'You are (.*)',
     ["Why do you think I am {0}?",
      "Perhaps you're really talking about yourself?"]],
 
    [r'You\'?re (.*)',
     ["Why do you say I am {0}?",
      "Are we talking about you, or me?"]],
 
    [r'I don\'?t (.*)',
     ["Don't you really {0}?",
      "Do you want to {0}?"]],
 
    [r'I feel (.*)',
     ["Good, tell me more about these feelings.",
      "When you feel {0}, what do you do?"]],
 
    [r'I have (.*)',
     ["Why do you tell me that you've {0}?",
      "Now that you have {0}, what will you do next?"]],
 
    [r'I would (.*)',
     ["Could you explain why you would {0}?",    
      "Who else knows that you would {0}?"]],
 
    [r'Is there (.*)',
     ["Do you think there is {0}?",
      "Would you like there to be {0}?"]],
 
    [r'My (.*)',
     ["I see, your {0}.",
      "When your {0}, how do you feel?"]],
 
    [r'You (.*)',
     ["We should be discussing you, not me.",
      "Why do you care whether I {0}?"]],
 
    [r'Why (.*)',
     ["Why don't you tell me the reason why {0}?",
      "Why do you think {0}?"]],
 
    [r'I want (.*)',
     ["What would it mean to you if you got {0}?",
      "If you got {0}, then what would you do?"]],
 
    [r'(.*) mother(.*)',
     ["Tell me more about your mother.",
      "Good family relations are important."]],
 
    [r'(.*) father(.*)',
     ["Tell me more about your father.",
      "Do you have trouble showing affection with your family?"]],
 
    [r'(.*) child(.*)',
     ["Did the other children sometimes tease you?",
      "How do you think your childhood experiences relate to your feelings today?"]],
 
    [r'(.*)\?',
     ["Why do you ask that?",
      "Why don't you tell me?"]],
 
    [r'quit',
     ["Thank you for talking with me.",
      "Thank you, that will be $150.  Have a good day!"]],
 
    [r'(.*)',
     ["Please tell me more.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "{0}.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"]]
]
 
 
def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)
 
 
def analyze(statement):
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])
 
 
def main():
    print "Hello. How are you feeling today?"
 
    while True:
        statement = raw_input("> ")
        print analyze(statement)
 
        if statement == "quit":
            break
 
 
if __name__ == "__main__":
    main()





