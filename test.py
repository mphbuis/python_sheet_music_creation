import abjad



duration = abjad.Duration(1, 4)
notes = [abjad.Note(pitch, duration) for pitch in range(16)]
staff = abjad.Staff(notes)

# creates lilypond file object
lilypond_file = abjad.LilyPondFile.new(staff)

# notes title
lilypond_file.header_block.title = abjad.Markup('best song ever')

# save pdf file at a custom location
abjad.persist.as_pdf(lilypond_file, './output/test.pdf')
