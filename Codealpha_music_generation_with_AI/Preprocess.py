from music21 import converter, note, chord
import glob
import pickle

notes = []

for file in glob.glob("dataset/*.mid"):
    print("Reading:", file)

    try:
        midi = converter.parse(file)

        for element in midi.flatten().notes:

            if isinstance(element, note.Note):
                notes.append(str(element.pitch))

            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

    except:
        print("Skipped:", file)

with open("notes.pkl", "wb") as f:
    pickle.dump(notes, f)

print("Total notes extracted:", len(notes))
