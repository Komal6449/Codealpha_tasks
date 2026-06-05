from music21 import stream, note

melody = stream.Stream()

notes = ['C4','D4','E4','F4','G4','A4','B4','C5']

for n in notes:
    melody.append(note.Note(n))

melody.write('midi', fp='dataset/song1.mid')

print("MIDI File Created")