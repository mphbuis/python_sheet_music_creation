import abjad
from random import randrange
import tk
import os
current_directory = os.getcwd()

duration = abjad.Duration(1, 4)
notes = [abjad.Note(pitch, duration) for pitch in range(16)]
staff = abjad.Staff(notes)

print(abjad.persist.as_png(staff, current_directory+'/output/test'))
print(abjad.persist.as_ly(staff, current_directory+'/output/neww'))
print(abjad.persist.as_midi(staff, current_directory+'/output/neww'))
print(abjad.persist.as_pdf(staff, current_directory+'/output/neww'))

# print(abjad.persist.as_midi(midi_block, current_directory+'/output/grah.midi'))

# Now this could be rendered as png using the following:
# abjad.persist(staff).as_png('output/output.png')

# container = abjad.Container("d'16 c'32 e'16 c'16 d'4 ~ d'16")
# abjad.show(container)
# abjad.persist(container).as_png("output.pdf")
