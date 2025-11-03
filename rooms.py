class Room:
    def __init__(self, name):
        self.name = name
        self.next_room = {}
        self.completed = False

    def enter(self):
        return self.story_dict["enter"]

    def look_around(self):
        return self.story_dict["look_around"]

    # def get_details(self):
    #     details = f"{self.name}\n"
    #     details += f"{self.description}\n"
    #     for direction, room in self.connected_rooms.items():
    #         details += f"The {room.name} is to the {direction}.\n"
    #     return details


class TheCell(Room):
    def __init__(self):
        super().__init__("A putrid cellar")

        self.actions = ["look_around", "search_corps", "inspect_door", "whisper_words"]

        # on corps when searched
        self.room_items = {
            "tattered note: 'Backwards is the way to salvation.' - Alucard"
        }

        self.story_dict = {
            "enter": """
As you open your eyes, a throbbing pain pulses through your head. 'Where am I?' you wonder. 
'What happened?' you mutter to yourself. As your senses slowly return, you find yourself in a dimly lit
what seems to be a cell. 'Ugh the stench...' you gag as you cover your nose.
The air is thick with a putrid smell of mold and rotting flesh.
            """,
            "look_around": """
You see a small, dark cellar with stone walls covered in moss and slimy brown fungus.
In the corner, there's a rotting corps slumped against the wall. You can tell the corps has been there for quite some time.
You also notice a heavy iron door with what seems to be claw marks etched into its surface.
'Poor bastard... Tried to claw his way out.' you whisper as you glance back at the corps.
            """,
            "search_corps": """
'Ugh...' you gag as you approach the corps. The stench is overwhelming, but you steel yourself and begin to search through the remains.
As you move aside decayed clothing and brittle bones, you see maggots feasting on the rotting eyes. You shudder but press on.
Buried deep within the entrails you find a bloody tattered note. You wipe off bits of flesh, maggots, and blood and read it:

'Backwards is the way to salvation.' - Alucard.

'Hmmm...' you ponder the meaning of the note as you carefully pocket it.
            """,
            "inspect_door": """
You step closer to the heavy iron door, its surface cold and rough to the touch.
There are deep claw marks etched into the metal, evidence of a desperate attempt to escape.
More than likely from the poor soul whose corps lies slumped in the corner.
There seems to be slight erie energy emanating from the door. A feeling of dread washes over you as you stand before it.
Youve felt this type of energy before. 'Dark magic... Fuck.' you whisper to yourself.
'What the fuck happend.... How did I end up in this shit hole?!'.
            """,
            "door_opens": """
As you whisper the words 'Dracula' the door begins to glow brighter!
The dark energy bursts from the door and passes throught you! 
You feel as if your soul was torn from your body for just a split second.
Dazed by the blast you stumble back. Slowly you re-gain your senses as the dark energy disapates from your body.
As the glow begins to fade from the iron door you hear a 'click' and the door opens.
'Well that was interesting... I need to get out of this hell hole.' you whisper as you head for the exit.
You glance back at the poor bastard rotting in the croner as you exit the cell.
                """,
        }

    def search_corps(self, player):
        tattered_note = "tattered note: 'Backwards is the way to salvation.' - Alucard"
        if tattered_note in self.room_items:
            self.room_items.remove(tattered_note)
            player.inventory.append(tattered_note)
            return self.story_dict["search_corps"]
        else:
            return "'I,m not searching that again...' you mutter as you step away from the corps."

    def inspect_door(self):
        return self.story_dict["inspect_door"]

    def whisper_words(self):
        words = input("What will you whisper?")
        if words == "dracula":
            print("You whisper 'Dracula'.")
            print(self.story_dict["door_opens"])
            self.completed = True
        else:
            print(f"You whisper '{words}', but nothing happens.")
            print("'Now what? I need to get out of here...' you mutter.")


## TEST CODE
class Player:
    def __init__(self):
        self.inventory = []


player = Player()
room = TheCell()
print(room.enter())
print(room.look_around())
print(room.search_corps(player))
print("Player Inventory:", player.inventory)
