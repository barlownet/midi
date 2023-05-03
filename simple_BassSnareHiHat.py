# This code creates 80 measures and two tracks of Midi.
# The first track contains bass and snare drum
# The second track contains the high hat

# Note: The instruments assumed are the Drum Kits in GarageBand
# for which
# Note 36 is bass drum, 38 is snare drum, and 42 is high-hat

# This is simple, unoptimized code to get someone started.

# Note that you'll just open this with GarageBand (or other midi players)
# and then choose the proper instrument for each track. GarageBand, for
# example, will always assume Steinway grand piano at first.

import pip

try:
  import mido
except:
  pip.main(['install', mido]) 
  import mido

import random
from mido import MidiFile, MidiTrack, Message

# Constants
tempo = 120  # BPM
ticks_per_beat = 360  # Default ticks per beat (quarter note) for mido
measures = 80
time_signature = (4, 4)

# Calculate ticks per measure
ticks_per_measure = ticks_per_beat * time_signature[0]

# Create a new MIDI file and two tracks
midi = MidiFile(ticks_per_beat=ticks_per_beat)

track1 = MidiTrack()
track2 = MidiTrack()

midi.tracks.append(track1)
midi.tracks.append(track2)

# Set time signature and tempo for two tracks
track1.append(mido.MetaMessage("time_signature", numerator=time_signature[0], denominator=time_signature[1], clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
track1.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(tempo), time=0))

track2.append(mido.MetaMessage("time_signature", numerator=time_signature[0], denominator=time_signature[1], clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
track2.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(tempo), time=0))

# set definitions of where things might happen
bassDrumQuarter = [0]
bassDrumEighth = [2]
snareDrum = [1,3]

# Add notes for each measure
for i in range(measures):
    for j in range(time_signature[0]):

        # Note 36
        if(j in bassDrumQuarter):
            velocity_36 = random.randint(100, 120)
            track1.append(Message("note_on", note=36, velocity=velocity_36, time=0))
            track1.append(Message("note_off", note=36, velocity=velocity_36, time=360))

        if(j in bassDrumEighth):
            velocity_36 = random.randint(110, 120)
            track1.append(Message("note_on", note=36, velocity=velocity_36, time=0))
            track1.append(Message("note_off", note=36, velocity=velocity_36, time=180))
            track1.append(Message("note_on", note=36, velocity=velocity_36, time=0))
            track1.append(Message("note_off", note=36, velocity=velocity_36, time=180))

        # Note 38
        if(j in snareDrum):
            velocity_38 = random.randint(100, 127)
            track1.append(Message("note_on", note=38, velocity=velocity_38, time=0))
            track1.append(Message("note_off", note=38, velocity=velocity_38, time=360))


for i in range(measures):
    for j in range(time_signature[0]):
        # Note 42
        velocity_42 = 127 if j == 0 else 112
        track2.append(Message("note_on", note=42, velocity=velocity_42, time=0))
        track2.append(Message("note_off", note=42, velocity=velocity_42, time=180))
        track2.append(Message("note_on", note=42, velocity=velocity_42, time=0))
        track2.append(Message("note_off", note=42, velocity=velocity_42, time=180))

# Save the MIDI file
midi.save("drumBeat.midi")

