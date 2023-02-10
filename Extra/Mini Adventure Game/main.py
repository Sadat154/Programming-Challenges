from room import Room
from item import Item
from Character import Character

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")


Bob = Character("Bob")
Bob.set_description("The builder")
Bob.set_response("Wanna go for a pint of lager? ")

Dave = Character("Dave")
Dave.set_description(("The florist"))

book = Item("Book")
book.set_description("A big fat book")
dining_hall.set_item(book)

wand = Item("Magic Wand")
wand.set_description("Cast your spells with this magical wand")
ballroom.set_item(book)
current_room = kitchen

dining_hall.set_character(Dave)
ballroom.set_character(Bob)

while True:
    print("\n")
    current_room.display_room()
    i = current_room.get_item()
    j = current_room.get_character()
    if i is not None:
        i.display_item()
    if j is not None:
        j.display_character()
        talk_choice = input("Would you like to speak to him? (Y/N): ").lower()
        if talk_choice == "y":
            j.display_response()


    command = input("\nEnter direction: ")
    current_room = current_room.move(command)