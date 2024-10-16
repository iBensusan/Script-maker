
def sentence_maker(phrase):
    interrogatives = ("what", "how", "why", "where", "which", "who", "when")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    

sentences = []

while True:
    sentence = input("Say something: ")
    if sentence == "/end":
        break
    else:
        sentences.append(sentence_maker(sentence))
        
print(" ".join(sentences)) 
    
