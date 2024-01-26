import pickle
import time

# Load existing notes from a file or create an empty list if the file doesn't exist
def load_notes(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except (IOError, EOFError):
        print("No default notebook was found, created one.")
        return []

# Save notes to a file using pickle
def save_notes(filename, notes):
    with open(filename, 'wb') as file:
        pickle.dump(notes, file)

# Add a new note with a timestamp
def add_note(notes):
    note = input("Write a new note: ")
    timestamp = time.strftime("%X %x")
    notes.append(f"{note}:::{timestamp}")

# Edit an existing note
def edit_note(notes):
    if not notes:
        print("No notes to edit.")
        return
    for idx, note in enumerate(notes):
        print(f"{idx}: {note}")
    index = int(input("Which of them will be changed?: "))
    if 0 <= index < len(notes):
        new_note = input("Give the new note: ")
        timestamp = time.strftime("%X %x")
        notes[index] = f"{new_note}:::{timestamp}"
    else:
        print("Invalid note number.")

# Delete an existing note
def delete_note(notes):
    if not notes:
        print("No notes to delete.")
        return
    for idx, note in enumerate(notes):
        print(f"{idx}: {note}")
    index = int(input("Which of them will be deleted?: "))
    if 0 <= index < len(notes):
        print(f"Deleted note {notes.pop(index)}")
    else:
        print("Invalid note number.")

# Main program loop
def main():
    filename = "notebook.dat"
    notes = load_notes(filename)

    while True:
        print("\n(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit")
        choice = input("Please select one: ")

        if choice == '1':
            for note in notes:
                print(note)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            edit_note(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            save_notes(filename, notes)
            print("Notebook shutting down, thank you.")
            break

if __name__ == "__main__":
    main()
