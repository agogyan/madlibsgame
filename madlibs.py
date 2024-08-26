import random
# Lists for random choices
measures_of_time = ["days", "hours", "weeks", "months", "years", "seconds"]
parts_of_body = ["arm", "leg", "head", "nose", "finger", "toe", "ear", "eye"]
def madlibsgame1():

    number = input("enter number:")
    measureoftime = random.choice(measures_of_time)  # Randomly choose a measure of time
    modeoftransportation = input("Mode of Transportation:")
    adjective = input("enter an adjective:")
    adjective2 = input("enter an adjective:")
    noun = input("enter a noun:")
    color = input("enter a color:")
    measureoftime = random.choice(measures_of_time)  # Randomly choose a measure of time
    verb = input("enter a verb:")
    number2 = input("enter  number:")
    noun2 = input("enter a noun:")
    noun3 = input("enter a noun:")
    partofthebody2 = random.choice(parts_of_body)  # Randomly choose a part of the body
    noun4 = input("enter a noun:")
    adjective3 = input("enter an adjective:")
    sillyword = input("enter a silly word:")


    print(f'''
        It was about {number} {measureoftime} ago when I arrived at the hospital in a {modeoftransportation}.
        The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here.
        There are nurses here who have {color} {partofthebody}.
        If someone wants to come into my room I told them that they have to {verb} first.
        I have decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {partofthebody2}.
        I heard that all doctors {verb} {noun4} every day for breakfast.
        The most {adjective3} thing about being in the hospital is the {sillyword} {noun} !''')




def madlibsgame2():

    proper_noun=input("enter a person’s name:")
    noun = input("enter a noun:")
    adjective = input("enter feeling:")
    verb = input("enter a verb:")
    adjective2 = input("enter feeling:")
    animal = input("enter an animal:")
    verb2 = input("enter a verb:")
    color = input("enter a color:")
    verb3 = input("enter a verb ending in ing:")
    adverb = input("enter an adverb ending in ly:")
    number = input("enter number:")
    measureoftime = random.choice(measures_of_time)  # Randomly choose a measure of time
    sillyword = input("enter a silly word:")
    noun2 = input("enter a noun:")

    print(f'''
        This weekend I am going camping with {proper_noun}.
        I packed my lantern, sleeping bag, and {noun}.
        I am so {adjective} to {verb} in a tent. 
        I am {adjective2} we might see a(n) {animal}, I hear they’re kind of dangerous. 
        While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb3}.
        Then we will {adverb} hike through the forest for {number} {measureoftime}.
        If I see a {color} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {number} {sillyword} stories and roast {noun2} around the campfire!!
        ''')
       

def madlibsgame3():

    proper_noun=input("a person’s name:")
    adjective = input("enter an adjective:")
    color = input("enter a color:")
    animal = input("enter an animal:")
    place = input("enter a place:")
    adjective2 = input("enter an adjective:")
    magical_creature = input("enter a magical creature(plural):") 
    adjective3 = input("enter an adjective:")
    magical_creature2 = input("enter a magical creature(plural):") 
    room_in_a_house = input("enter a room in a house:")
    noun = input("enter a noun:")
    noun2 = input("enter a noun:")
    plural_noun = input("enter plural noun:")
    adjective4 = input("enter an adjective:")
    plural_noun2 = input("enter plural noun:")
    number = input("enter number:")
    measureoftime = random.choice(measures_of_time)  # Randomly choose a measure of time
    verb = input("enter a verb ending in ing:")
    adjective5 = input("enter an adjective:")
    noun3 = input("enter a noun:")

    print(f'''
     Dear {proper_noun}, I am writing to you from a {adjective} castle in an enchanted forest.
     I found myself here one day after going for a ride on a {color} {animal} in {place}.
     There are {adjective2} {magical_creature} and {adjective3} {magical_creature2} here!
     In the {room_in_a_house} there is a pool full of {noun}.
     I fall asleep each night on a {noun2} of {plural_noun} and dream of {adjective4} {plural_noun2}.
     It feels as though I have lived here for {number} {measureoftime}. 
     I hope one day you can visit, although the only way to get here now is {verb} on a {adjective5} {noun3}!!
       ''') 
        
       
    
templates  = input("input a template 1-3:")
if int(templates) == 1:
    madlibsgame1()
elif int(templates) == 2:
    madlibsgame2()    
elif int(templates) == 3:
    madlibsgame3()
else:
    print("Invalid choice. Please restart the game and choose a valid template.")

