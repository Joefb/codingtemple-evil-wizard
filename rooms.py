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

        self.actions = ["look_around", "search_corps", "inspect_door", "whisper"]

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

Skeleton in the corner. Skeleton has tattered note.
Rusty iron door that is locked.
            """,
        }

    def search_corps(self, player):
        if (
            "tattered note: 'Backwards is the way to salvation.' - Alucard"
            in self.room_items
        ):
            self.room_items.remove(
                "tattered note: 'Backwards is the way to salvation.' - Alucard"
            )
            player.inventory.append(
                "tattered note: 'Backwards is the way to salvation.' - Alucard"
            )
            return """
You search the corps and find a tattered note. You read it: 'Backwards is the way to salvation.' - Alucard
                   """
        else:
            return "You search the corps again but find nothing of interest."


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
