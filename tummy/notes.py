import json
from time import strftime


class Notepad:
    def __init__(self, notes_path):
        self.file = notes_path
        self.notes = self.get_notes()


    def write_changes(self):
        with open(self.file, "w") as f:
            json.dump(self.notes, f, indent=4)


    def get_notes(self):
        try:
            f = open(self.file)
        except FileNotFoundError:
            temp_obj = {"notes": []}
            f = open(self.file, 'w+')
            json.dump(temp_obj, f, indent=4)
            rv = temp_obj
            f.close()
        else:
            rv = json.load(f)
            f.close()
        finally:
            return rv
            


    def show_notes(self):
        print("\n    Your notes:")
        if len(self.notes['notes']) == 0:
            print("\tYou have no notes!\n")
            return
        for n, note in enumerate(self.notes['notes'], start=1):
            print(f"\t{n}: {note}")
        print()


    def add_note(self, note):
        self.notes['notes'].append(f"{strftime('%D')} | {note}")
        self.write_changes()

    
    def remove_note(self, note_number):
        temp_obj = {"notes": []}
        for n, note in enumerate(self.notes['notes'], start=1):
            if n != note_number:
                temp_obj['notes'].append(note)
        self.notes = temp_obj
        self.write_changes()


    def clear_notes(self):
        self.notes = {"notes": []}
        self.write_changes()


def parse_note_args(subcommand, args, notepad):
    if subcommand == "add":
        if args:
            notepad.add_note(" ".join(args))
        else:
            print("    Please provide a note to add.")
    elif subcommand == "remove":
        if args:
            try:
                to_remove = int(args[0])
            except ValueError:
                print("    Please provide a number to remove.")
            else:
                notepad.remove_note(to_remove)
        else:
            print("    Please provide a note number to remove.")
    elif subcommand == "clear":
        yorn = input("\n    Are you sure you want to clear your notes? [Y/N]\n\t-> ").lower()
        print()
        if yorn == "y":
            notepad.clear_notes()
    elif subcommand == "show" or args == None:
        notepad.show_notes()