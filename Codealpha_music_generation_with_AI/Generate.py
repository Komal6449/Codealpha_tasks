import pickle
import numpy as np

from tensorflow.keras.models import load_model
from music21 import note, chord, stream

model = load_model("music_model.h5")

notes = pickle.load(open("notes.pkl", "rb"))

pitchnames = sorted(set(notes))

note_to_int = dict(
    (note, number)
    for number, note in enumerate(pitchnames)
)

int_to_note = dict(
    (number, note)
    for number, note in enumerate(pitchnames)
)

start = np.random.randint(0, len(notes) - 100)

pattern = notes[start:start + 100]

prediction_output = []

for note_index in range(200):

    prediction_input = [note_to_int[n] for n in pattern]

    prediction_input = np.reshape(
        prediction_input,
        (1, len(prediction_input), 1)
    )

    prediction_input = prediction_input / float(len(pitchnames))

    prediction = model.predict(
        prediction_input,
        verbose=0
    )

    index = np.argmax(prediction)

    result = int_to_note[index]

    prediction_output.append(result)

    pattern.append(result)

    pattern = pattern[1:]

offset = 0
output_notes = []

for pattern in prediction_output:

    try:
        if '.' in pattern:
            notes_in_chord = pattern.split('.')
            chord_notes = []

            for current_note in notes_in_chord:
                new_note = note.Note(int(current_note))
                chord_notes.append(new_note)

            new_chord = chord.Chord(chord_notes)
            new_chord.offset = offset

            output_notes.append(new_chord)

        else:
            new_note = note.Note(pattern)
            new_note.offset = offset

            output_notes.append(new_note)

        offset += 0.5

    except:
        pass

midi_stream = stream.Stream(output_notes)

midi_stream.write(
    'midi',
    fp='generated_music.mid'
)

print("Music Generated Successfully!")
