class Character:

    def __init__(self, name):
        self.name = name
        self.description = None
        self.response = None


    def set_name(self, npc_name):
        self.name = npc_name

    def get_name(self):
        return self.name

    def set_description(self, npc_desc):
        self.description = npc_desc

    def get_description(self):
        return self.description


    def set_response(self, npc_response):
        self.response = npc_response

    def get_response(self):
        return self.response

    def display_character(self):
        print(f"{self.name} {self.description} is here")

    def display_response(self):
        if self.response == None:
            print(f"{self.name} does not wish to speak to you ")
        else:
            print(f"{self.name} says: {self.response}")
