#!/usr/bin/python

import sys
import os
import time
import datetime
import random
import ConfigParser

def note_sum(note,interval):
#funcion clave para hacer todo relativo
    if note == 'C':
	if (interval % 12) == 1: new_note = 'Db'
	if (interval % 12) == 2: new_note = 'D'
	if (interval % 12) == 3: new_note = 'Eb'
	if (interval % 12) == 4: new_note = 'E'
	if (interval % 12) == 5: new_note = 'F'
	if (interval % 12) == 6: new_note = 'Gb'
	if (interval % 12) == 7: new_note = 'G'
	if (interval % 12) == 8: new_note = 'Ab'
	if (interval % 12) == 9: new_note = 'A'
	if (interval % 12) == 10: new_note = 'Bb'
	if (interval % 12) == 11: new_note = 'B'
	if (interval % 12) == 0: new_note = 'C'

    if note == 'Db':
	if (interval % 12) == 1: new_note = 'D'
	if (interval % 12) == 2: new_note = 'Eb'
	if (interval % 12) == 3: new_note = 'E'
	if (interval % 12) == 4: new_note = 'F'
	if (interval % 12) == 5: new_note = 'Gb'
	if (interval % 12) == 6: new_note = 'G'
	if (interval % 12) == 7: new_note = 'Gb'
	if (interval % 12) == 8: new_note = 'A'
	if (interval % 12) == 9: new_note = 'Bb'
	if (interval % 12) == 10: new_note = 'B'
	if (interval % 12) == 11: new_note = 'C'
	if (interval % 12) == 0: new_note = 'Db'

    if note == 'D':
	if (interval % 12) == 1: new_note = 'Eb'
	if (interval % 12) == 2: new_note = 'E'
	if (interval % 12) == 3: new_note = 'F'
	if (interval % 12) == 4: new_note = 'Gb'
	if (interval % 12) == 5: new_note = 'G'
	if (interval % 12) == 6: new_note = 'Ab'
	if (interval % 12) == 7: new_note = 'A'
	if (interval % 12) == 8: new_note = 'Bb'
	if (interval % 12) == 9: new_note = 'B'
	if (interval % 12) == 10: new_note = 'C'
	if (interval % 12) == 11: new_note = 'Db'
	if (interval % 12) == 0: new_note = 'D'

    if note == 'Eb':
	if (interval % 12) == 1: new_note = 'E'
	if (interval % 12) == 2: new_note = 'F'
	if (interval % 12) == 3: new_note = 'Gb'
	if (interval % 12) == 4: new_note = 'G'
	if (interval % 12) == 5: new_note = 'Ab'
	if (interval % 12) == 6: new_note = 'A'
	if (interval % 12) == 7: new_note = 'Bb'
	if (interval % 12) == 8: new_note = 'B'
	if (interval % 12) == 9: new_note = 'C'
	if (interval % 12) == 10: new_note = 'Db'
	if (interval % 12) == 11: new_note = 'D'
	if (interval % 12) == 0: new_note = 'Eb'

    if note == 'E':
	if (interval % 12) == 1: new_note = 'F'
	if (interval % 12) == 2: new_note = 'Gb'
	if (interval % 12) == 3: new_note = 'G'
	if (interval % 12) == 4: new_note = 'Ab'
	if (interval % 12) == 5: new_note = 'A'
	if (interval % 12) == 6: new_note = 'Bb'
	if (interval % 12) == 7: new_note = 'B'
	if (interval % 12) == 8: new_note = 'C'
	if (interval % 12) == 9: new_note = 'Db'
	if (interval % 12) == 10: new_note = 'D'
	if (interval % 12) == 11: new_note = 'Eb'
	if (interval % 12) == 0: new_note = 'E'

    if note == 'F':
	if (interval % 12) == 1: new_note = 'Gb'
	if (interval % 12) == 2: new_note = 'G'
	if (interval % 12) == 3: new_note = 'Ab'
	if (interval % 12) == 4: new_note = 'A'
	if (interval % 12) == 5: new_note = 'Bb'
	if (interval % 12) == 6: new_note = 'B'
	if (interval % 12) == 7: new_note = 'C'
	if (interval % 12) == 8: new_note = 'Db'
	if (interval % 12) == 9: new_note = 'D'
	if (interval % 12) == 10: new_note = 'Eb'
	if (interval % 12) == 11: new_note = 'E'
	if (interval % 12) == 0: new_note = 'F'

    if note == 'Gb':
	if (interval % 12) == 1: new_note = 'G'
	if (interval % 12) == 2: new_note = 'Ab'
	if (interval % 12) == 3: new_note = 'A'
	if (interval % 12) == 4: new_note = 'Bb'
	if (interval % 12) == 5: new_note = 'B'
	if (interval % 12) == 6: new_note = 'C'
	if (interval % 12) == 7: new_note = 'Db'
	if (interval % 12) == 8: new_note = 'D'
	if (interval % 12) == 9: new_note = 'Eb'
	if (interval % 12) == 10: new_note = 'E'
	if (interval % 12) == 11: new_note = 'F'
	if (interval % 12) == 0: new_note = 'Gb'

    if note == 'G':
	if (interval % 12) == 1: new_note = 'Ab'
	if (interval % 12) == 2: new_note = 'A'
	if (interval % 12) == 3: new_note = 'Bb'
	if (interval % 12) == 4: new_note = 'B'
	if (interval % 12) == 5: new_note = 'C'
	if (interval % 12) == 6: new_note = 'Db'
	if (interval % 12) == 7: new_note = 'D'
	if (interval % 12) == 8: new_note = 'Eb'
	if (interval % 12) == 9: new_note = 'E'
	if (interval % 12) == 10: new_note = 'F'
	if (interval % 12) == 11: new_note = 'Gb'
	if (interval % 12) == 0: new_note = 'G'

    if note == 'Ab':
	if (interval % 12) == 1: new_note = 'A'
	if (interval % 12) == 2: new_note = 'Bb'
	if (interval % 12) == 3: new_note = 'B'
	if (interval % 12) == 4: new_note = 'C'
	if (interval % 12) == 5: new_note = 'Db'
	if (interval % 12) == 6: new_note = 'D'
	if (interval % 12) == 7: new_note = 'Eb'
	if (interval % 12) == 8: new_note = 'E'
	if (interval % 12) == 9: new_note = 'F'
	if (interval % 12) == 10: new_note = 'Gb'
	if (interval % 12) == 11: new_note = 'G'
	if (interval % 12) == 0: new_note = 'Ab'

    if note == 'A':
	if (interval % 12) == 1: new_note = 'Bb'
	if (interval % 12) == 2: new_note = 'B'
	if (interval % 12) == 3: new_note = 'C'
	if (interval % 12) == 4: new_note = 'Db'
	if (interval % 12) == 5: new_note = 'D'
	if (interval % 12) == 6: new_note = 'Eb'
	if (interval % 12) == 7: new_note = 'E'
	if (interval % 12) == 8: new_note = 'F'
	if (interval % 12) == 9: new_note = 'Gb'
	if (interval % 12) == 10: new_note = 'G'
	if (interval % 12) == 11: new_note = 'Ab'
	if (interval % 12) == 0: new_note = 'A'

    if note == 'Bb':
	if (interval % 12) == 1: new_note = 'B'
	if (interval % 12) == 2: new_note = 'C'
	if (interval % 12) == 3: new_note = 'Db'
	if (interval % 12) == 4: new_note = 'D'
	if (interval % 12) == 5: new_note = 'Eb'
	if (interval % 12) == 6: new_note = 'E'
	if (interval % 12) == 7: new_note = 'F'
	if (interval % 12) == 8: new_note = 'Gb'
	if (interval % 12) == 9: new_note = 'G'
	if (interval % 12) == 10: new_note = 'Ab'
	if (interval % 12) == 11: new_note = 'A'
	if (interval % 12) == 0: new_note = 'Bb'

    if note == 'B':
	if (interval % 12) == 1: new_note = 'C'
	if (interval % 12) == 2: new_note = 'Db'
	if (interval % 12) == 3: new_note = 'D'
	if (interval % 12) == 4: new_note = 'Eb'
	if (interval % 12) == 5: new_note = 'E'
	if (interval % 12) == 6: new_note = 'F'
	if (interval % 12) == 7: new_note = 'Gb'
	if (interval % 12) == 8: new_note = 'G'
	if (interval % 12) == 9: new_note = 'Ab'
	if (interval % 12) == 10: new_note = 'A'
	if (interval % 12) == 11: new_note = 'Bb'
	if (interval % 12) == 0: new_note = 'B'
 
    return new_note

#read configuration file
config = ConfigParser.ConfigParser()
if len(sys.argv) > 1:
    config_file = sys.argv[1]
else:
    config_file = "configuration.ini"

if os.path.isfile(config_file):
    config.read(config_file)
    baseOctave = int(config.get('General', 'baseOctave'))
    baseNote = config.get('General', 'baseNote')
    #load melodic dictation configuration
    melodic_dictation_length = config.get('Melodic Dictation', 'length')
#melodic_dictation_names
    for i in range(11):
        melodic_dictation_intervals = [int(inter) for inter in config.get('Melodic Dictation', 'level'+str(i+1)).split()]
        melodic_dictation_level = [note_sum(baseNote,inter) for inter in perfect_levels_intervals]
        melodic_dictation_rep = [int(inter) for inter in config.get('Melodic Dictation', 'repetitions'+str(i+1)).split()]
        perfect_levels_notes[i]= melodic_dictation_level
        melodic_dictation_reps[i]= perfect_levels_rep
    print perfect_levels_notes
    print perfect_levels_reps
    #load perfect pitch configuration
    for i in range(11):
        perfect_levels_intervals = [int(inter) for inter in config.get('Perfect Pitch', 'level'+str(i+1)).split()]
        perfect_level = [note_sum(baseNote,inter) for inter in perfect_levels_intervals]
        perfect_levels_rep = [int(inter) for inter in config.get('Perfect Pitch', 'repetitions'+str(i+1)).split()]
        perfect_levels_notes[i]= perfect_level
        perfect_levels_reps[i]= perfect_levels_rep

else:
    print "\nWarning: No configuration file, using built-in configuration\n"
