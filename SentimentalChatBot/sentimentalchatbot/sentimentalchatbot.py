if __name__ == "__main__":
    from pattern.en import sentiment, polarity, subjectivity, positive

    name = raw_input("Hello, What's your name?: ")
    
    cadena = raw_input(name +" , tell me about you: ")
    while cadena != "#":
        if(positive(cadena, 0.1)):
           print ("Wow that's fantastic!")
        else:
            print("That's bad")
            
        cadena = raw_input(name +" , tell me about you: ")

    print("Program finished")
        


