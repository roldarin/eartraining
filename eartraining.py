#!/usr/bin/python

import sys
import os
import time
import datetime
import random
import ConfigParser
import pdb
import pygame
from Tkinter import *

pygame.init()

#para depurar
debug = True

#ruta a las notas
path="./sounds/piano/Piano"
path_key_notes="./sounds/piano/Piano.ff."
sformat=".wav"

#base octave
baseOctave = 2

#base note
baseNote = 'C'

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

def value_save():
    #save hiscores
    now = datetime.datetime.now()
    date = str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"/"+str(now.hour)+":"+str(now.minute).zfill(2)
    fout1=open("Hiscores_Melodic"+".txt",'a')
    fout2=open("Hiscores_Perfect"+".txt",'a')
    fout3=open("Hiscores_Intervals"+".txt",'a')
    fout4=open("Hiscores_Harmonic"+".txt",'a')
    fout1.write(date+" = "+str(melodic_hiscores)+"\n")
    fout2.write(date+" = "+str(perfect_hiscores)+"\n")
    fout3.write(date+" = "+str(intervals_hiscores)+"\n")
    fout4.write(date+" = "+str(harmonic_hiscores)+"\n")
    fout1.close()
    fout2.close()
    fout3.close()
    fout4.close()
    return

def value_quit():
    #save hiscores and quit
    now = datetime.datetime.now()
    date = str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"/"+str(now.hour)+":"+str(now.minute).zfill(2)
    fout1=open("Hiscores_Melodic"+".txt",'a')
    fout2=open("Hiscores_Perfect"+".txt",'a')
    fout3=open("Hiscores_Intervals"+".txt",'a')
    fout4=open("Hiscores_Harmonic"+".txt",'a')
    fout1.write(date+" = "+str(melodic_hiscores)+"\n")
    fout2.write(date+" = "+str(perfect_hiscores)+"\n")
    fout3.write(date+" = "+str(intervals_hiscores)+"\n")
    fout4.write(date+" = "+str(harmonic_hiscores)+"\n")
    fout1.close()
    fout2.close()
    fout3.close()
    fout4.close()
    quit()
    return

def clear_notes_played():
    current_state.notes_played[:] = []
    return

def clear_notes_pressed():
    current_state.notes_pressed[:] = []
    return

def random_melody(notes,length):
    melody=[]
    octaves=(baseOctave,baseOctave)
    for i in range(length):
	melody.append(random.choice(notes)+str(random.choice(octaves)))
    return melody

def random_interval(notes):
    interval=[]
    octaves=(baseOctave,baseOctave)
    for i in range(2):
	interval.append(random.choice(notes)+str(random.choice(octaves)))
    return interval

def value_play_melody():
    #melodic dictation code
    if  current_state.game == -1:
	current_state.playing = True
        current_state.game = 0
	current_state.repetitions_guessed = 0
    elif current_state.game != 0:
        current_state.game = 0
	current_state.repetitions_guessed = 0
	current_state.level
    num2.set("Try!")   
    intensity=('.ff.','.ff.')
    force=random.choice(intensity)
    #check level
    if current_state.level > 20: current_state.level = 20
    level_notes = melodic_dictation_notes[current_state.level-1]
    level_name = melodic_dictation_names[current_state.level-1]
    current_state.level_rep = melodic_dictation_reps[current_state.level-1]
    num0.set(level_name)
    #play new melody, repeat if repetition not guessed ot failed
    num3.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
    if current_state.guessed or len(current_state.notes_played) == 0 and not current_state.failed:
        if debug: print "new note melodic",melodic_dictation_length,current_state.notes_played
        melody=random_melody(level_notes,melodic_dictation_length)  
        clear_notes_played()
	clear_notes_pressed()
	print melody
        for note in melody:
	    current_state.notes_played.append(note)
	    force=random.choice(intensity)
	    print path+force+note+".wav"
	    sound = pygame.mixer.Sound(path+force+note+sformat)
            sound.play()
            #os.system("mplayer "+path+force+note+sformat)
	current_state.guessed = False
    else:
#
        if debug: print "new note melodic REPITE"
	for note in current_state.notes_played:
	    sound = pygame.mixer.Sound(path+force+note+sformat)
	    sound.play()

    return

def value_play_harmony():
    #harmonic dictation code
    if  current_state.game == -1:
	current_state.playing = True
        current_state.game = 3
	current_state.repetitions_guessed = 0
    elif current_state.game != 3:
        current_state.game = 3
	current_state.repetitions_guessed = 0
	current_state.level
    num2.set("Try!")   
    intensity=('.ff.','.ff.')
    force=random.choice(intensity)
    #check level
    if current_state.level > 20: current_state.level = 20
    level_notes = harmonic_dictation_notes[current_state.level-1]
    level_name = harmonic_dictation_names[current_state.level-1]
    current_state.level_rep = harmonic_dictation_reps[current_state.level-1]
    num0.set(level_name)
    #play new harmony, repeat if not repetitions_guessed ot failed
    num3.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
    if current_state.guessed or len(current_state.notes_played) == 0 and not current_state.failed:
#TODO cuidado harmony melody
        if debug: print "new note harmony"
        melody=random_melody(level_notes,harmonic_dictation_length)  
        clear_notes_played()
        for note in melody:
	    current_state.notes_played.append(note)
	    force=random.choice(intensity)
	    print path+force+note+sformat
	    sound = pygame.mixer.Sound(path+force+note+sformat)
            sound.play()
    else:
        if debug: print "repeat note harmonic"
	sound = pygame.mixer.Sound(path+force+current_state.notes_played[0]+sformat)
	sound.play()

    return

def value_play_interval():
    #notas de la escala a usar melody
    #Fifth, Octave
    #interval code
    if  current_state.game == -1:
	current_state.playing = True
        current_state.game = 2
	current_state.repetitions_guessed = 0
    elif current_state.game != 2:
        current_state.game = 2
	current_state.repetitions_guessed = 0
	current_state.level
    num2.set("Try!")   
    intensity=('.ff.','.ff.')
    force=random.choice(intensity)
    #check level
    if current_state.level > 11: current_state.level = 11
    level_notes = melodic_dictation_notes[current_state.level-1]
    level_name = melodic_dictation_names[current_state.level-1]
    current_state.level_rep = melodic_dictation_reps[current_state.level-1]
    num0.set(level_name)
    #play new melody, repeat if repetition not guessed ot failed
    num3.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
    if current_state.guessed or len(current_state.notes_played) == 0 and not current_state.failed:
        if debug: print "new note melodic",melodic_dictation_length,current_state.notes_played
        interval=random_interval(level_notes)  
        clear_notes_played()
	clear_notes_pressed()
	print melody
        for note in interval:
	    current_state.notes_played.append(note)
	    force=random.choice(intensity)
	    print path+force+note+".wav"
	    sound = pygame.mixer.Sound(path+force+note+sformat)
            sound.play()
            #os.system("mplayer "+path+force+note+sformat)
	current_state.guessed = False
    else:
#
        if debug: print "new note melodic REPITE"
	for note in current_state.notes_played:
	    sound = pygame.mixer.Sound(path+force+note+sformat)
	    sound.play()

    return

def value_play_note():
    #pdb.set_trace()
    #perfect pitch code
    #if not playing any mode start
    if  current_state.game == -1:
	current_state.playing = True
        current_state.game = 1
	current_state.repetitions_guessed = 0
    elif current_state.game != 1:
        current_state.game = 1
	current_state.repetitions_guessed = 0
	current_state.level
    num2.set("Try!")   
    intensity=('.ff.','.ff.')
    force=random.choice(intensity)
    #check level
    if current_state.level > 11: current_state.level = 11
    level = perfect_levels_notes[current_state.level-1]
    current_state.level_rep = perfect_levels_reps[current_state.level-1]
    level_notes=""
    for n in level:
            level_notes+=n+" "
    num0.set("Level "+str(current_state.level)+" "+level_notes)

    #play new note, repeat if not repetitions_guessed ot failed
    num3.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
    if current_state.guessed or len(current_state.notes_played) == 0 and not current_state.failed:
        if debug: print "new note"
        current_state.failed = False
#TODO HAY QUE ELEGIR ESCALA, solo la nota base esta en 3. Generamos una nota diferente a la anterior
	while True:
	    note=random.choice(level)
            if note == baseNote:
	        octave_rel = random.choice((0,1,2))
	    else:
	        octave_rel = random.choice((0,1))
	    octave = baseOctave + octave_rel
            absolute_note = note+str(octave)
 	    if absolute_note != current_state.last: break
	current_state.last = absolute_note
	sound = pygame.mixer.Sound(path+force+absolute_note+sformat)
	sound.play()
	if len(current_state.notes_played) == 0: current_state.notes_played.append(absolute_note)
	current_state.notes_played[0]=absolute_note
        current_state.guessed = False
    else:
        if debug: print "repeat note"
	sound = pygame.mixer.Sound(path+force+current_state.notes_played[0]+sformat)
	sound.play()
    print current_state.notes_played[0]
    return

def check_note(note):
    #check if the note is correct 
    #melodic dictation code
    if current_state.game == 0:
	#quit()
        #if phrase not enough continue
	if len(current_state.notes_pressed) == melodic_dictation_length: 
	#if level not finished continue
       	    if current_state.repetitions_guessed < current_state.level_rep:
	    #if repetitions_guessed
	       if current_state.notes_played == current_state.notes_pressed:
		    if debug: print "Melodic dictation guessed",current_state.failed ,current_state.guessed
		    if not current_state.failed and not current_state.guessed: current_state.repetitions_guessed += 1
		    current_state.guessed = True
                    current_state.failed = False
		    clear_notes_pressed()
	            clear_notes_played()
		    num2.set("Correct!!")
                    num3.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
                    if (current_state.repetitions_guessed >= melodic_hiscores[current_state.level-1]): 
		        melodic_hiscores[current_state.level-1] = current_state.repetitions_guessed
	       else:
		    if debug: print "Melodic dictation failed"
		    if not current_state.guessed: 
		        current_state.repetitions_guessed = 0
                        num3.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
		        current_state.failed = True
			clear_notes_pressed()		      
            #if level accomplished
	    if current_state.repetitions_guessed >= current_state.level_rep: 
	        current_state.level += 1
                current_state.repetitions_guessed = 0
	if debug: print current_state.notes_played, current_state.notes_pressed

 
    #perfect pitch code 
    if current_state.game == 1:
	#if level not finished continue
	if current_state.repetitions_guessed < current_state.level_rep:
	    #if repetitions_guessed
	    if current_state.notes_played[0] == note:
		if debug: print "Perfect pith repetitions_guessed"
		if not current_state.failed and not current_state.guessed: current_state.repetitions_guessed += 1
		current_state.guessed = True
		num2.set("Correct!!")
                num3.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
                if (current_state.repetitions_guessed >= perfect_hiscores[current_state.level-1]): 
		    perfect_hiscores[current_state.level-1] = current_state.repetitions_guessed
	    else:
		if debug: print "Perfect pith failed"
		if not current_state.guessed: 
		    current_state.repetitions_guessed = 0
                    num3.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
		    current_state.failed = True
        #if level accomplished
	if current_state.repetitions_guessed >= current_state.level_rep: 
	    current_state.level += 1
            current_state.repetitions_guessed = 0
    return

def value_level_up():
    current_state.level += 1
    num0.set("Level "+str(current_state.level))
    num3.set("Hiscore ")
    current_state.repetitions_guessed = 0
    if debug: print current_state.level
    return

def value_level_down():
    if current_state.level > 1: current_state.level -= 1
    num0.set("Level "+str(current_state.level))
    num3.set("Hiscore ")
    current_state.repetitions_guessed = 0
    if debug: print current_state.level
    return

def clear():
    num2.set("Try!")

def value_0():
    #save note pressed, play it, a check what to do
    interval = 0
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_1():
    #save note pressed, play it, a check what to do
    interval = 1
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_2():
    #save note pressed, play it, a check what to do
    interval = 2
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_3():
    #save note pressed, play it, a check what to do
    interval = 3
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_4():
    #save note pressed, play it, a check what to do
    interval = 4
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_5():
    #save note pressed, play it, a check what to do
    interval = 5
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_6():
    #save note pressed, play it, a check what to do
    interval = 6
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_7():
    #save note pressed, play it, a check what to do
    interval = 7
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_8():
    #save note pressed, play it, a check what to do
    interval = 8
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_9():
    #save note pressed, play it, a check what to do
    interval = 9
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_10():
    #save note pressed, play it, a check what to do
    interval = 10
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_11():
    #save note pressed, play it, a check what to do
    interval = 11
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_12():
    #save note pressed, play it, a check what to do
    interval = 12
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_13():
    #save note pressed, play it, a check what to do
    interval = 13
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_14():
    #save note pressed, play it, a check what to do
    interval = 14
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_15():
    #save note pressed, play it, a check what to do
    interval = 15
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_16():
    #save note pressed, play it, a check what to do
    interval = 16
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_17():
    #save note pressed, play it, a check what to do
    interval = 17
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_18():
    #save note pressed, play it, a check what to do
    interval = 18
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_19():
    #save note pressed, play it, a check what to do
    interval = 19
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_20():
    #save note pressed, play it, a check what to do
    interval = 20
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_21():
    #save note pressed, play it, a check what to do
    interval = 21
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_22():
    #save note pressed, play it, a check what to do
    interval = 22
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_23():
    #save note pressed, play it, a check what to do
    interval = 23
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return

def value_24():
    #save note pressed, play it, a check what to do
    interval = 24
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    num1.set(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: check_note(note) 
    return


root = Tk()
frame = Frame(root)
frame.pack(side = TOP)

root.title('PIANO FROM C '+str(baseOctave))

num0=StringVar()
num1=StringVar()
num2=StringVar()
num3=StringVar()

#save state
class State():
    playing=False    #playing
    game=-1          #-1 mo game, 0 melody, 1 perfect, 2 intervals, 3 harmony
    level=1         #nivel dificultad actual
    level_rep=0     #repetitions required current level
    repetitions_guessed=0       #numero de aciertos
    guessed=False    #if current notes have been guessed
    failed=False     #if current notes have beenfailed
    notes_played=[] #notas que se han tocado
    notes_pressed=[] #notas que se han presionado
    last=[]          #ultima nota tocada, para reducir repeticiones
    next=False  #para ver si se ha acertado, si no se repite

current_state = State()

#Hiscores
melodic_hiscores = [0] * 11
perfect_hiscores = [0] * 11
intervals_hiscores = [0] * 11
harmonic_hiscores = [0] * 11

#CONFIGURATIONS

harmonic_dictation_length = 2
harmonic_dictation_names = ("Major 1,3,5","Minor 1,3,5","Major 1,3,4,5","Minor 1,3,4,5","Major 1-5","Minor 1-5","Major Pentatonic","Minor Pentatonic", "Major 1-6","Minor 1-6","Blues","Major","Minor","Harmonic Minor","Melodic Minor","Minor, 1 accidental", "Minor, 2 accidental","Minor, 3 accidental","Minor, 4 accidental", "Chromatic")
harmonic_dictation_notes = (('C', 'E', 'G'),('C', 'Eb', 'G'),('C', 'E', 'F','G'),('C', 'Eb', 'F', 'G'),('C', 'D','E', 'F','G'),('C', 'D', 'Eb', 'F', 'G'),('C','D','E', 'G','A'),('C', 'Eb', 'G', 'Ab', 'Bb'),('C', 'D','E', 'F','G','A'),('C', 'D', 'Eb', 'F', 'G','Ab'),('C','Eb', 'F', 'Gb','G','Bb'),('C', 'D','E', 'F','G','B'),('C', 'D', 'Eb', 'F', 'G','Ab','Bb'),('C', 'D', 'Eb', 'F', 'G','Ab','B'),('C', 'D', 'Eb', 'F', 'G','A','B'),('C','D', 'Eb','F', 'G','A','Bb','B'),('C','D', 'Eb','F', 'G','Ab','A','Bb','B'),('C','D', 'Eb','F','Gb', 'G','Bb','A','Bb','B'),('C','D', 'Eb', 'E','F','Gb', 'G','Bb','A','Bb','B'),('C','Db','D', 'Eb', 'E','F','Gb', 'G','Ab','A','Bb','B'))
harmonic_dictation_reps = (5,5,5,5,5,7,7,7,7,7,10,10,10,10,10,15,15,15,15,15)

melodic_dictation_length = 2
melodic_dictation_names = ("Major 1,3,5","Minor 1,3,5","Major 1,3,4,5","Minor 1,3,4,5","Major 1-5","Minor 1-5","Major Pentatonic","Minor Pentatonic", "Major 1-6","Minor 1-6","Blues","Major","Minor","Harmonic Minor","Melodic Minor","Minor, 1 accidental", "Minor, 2 accidental","Minor, 3 accidental","Minor, 4 accidental", "Chromatic")
melodic_dictation_notes = (('C', 'E', 'G'),('C', 'Eb', 'G'),('C', 'E', 'F','G'),('C', 'Eb', 'F', 'G'),('C', 'D','E', 'F','G'),('C', 'D', 'Eb', 'F', 'G'),('C','D','E', 'G','A'),('C', 'Eb', 'G', 'Ab', 'Bb'),('C', 'D','E', 'F','G','A'),('C', 'D', 'Eb', 'F', 'G','Ab'),('C','Eb', 'F', 'Gb','G','Bb'),('C', 'D','E', 'F','G','B'),('C', 'D', 'Eb', 'F', 'G','Ab','Bb'),('C', 'D', 'Eb', 'F', 'G','Ab','B'),('C', 'D', 'Eb', 'F', 'G','A','B'),('C','D', 'Eb','F', 'G','A','Bb','B'),('C','D', 'Eb','F', 'G','Ab','A','Bb','B'),('C','D', 'Eb','F','Gb', 'G','Bb','A','Bb','B'),('C','D', 'Eb', 'E','F','Gb', 'G','Bb','A','Bb','B'),('C','Db','D', 'Eb', 'E','F','Gb', 'G','Ab','A','Bb','B'))
melodic_dictation_reps = (5,5,5,5,5,7,7,7,7,7,10,10,10,10,10,15,15,15,15,15)


perfect_levels_reps = (20,20,20,20,25,25,25,25,30,30,30)
perfect_level1 = (note_sum(baseNote,3),note_sum(baseNote,6))
perfect_level2 = (note_sum(baseNote,0),note_sum(baseNote,3),note_sum(baseNote,6))
perfect_level3 = (note_sum(baseNote,0),note_sum(baseNote,3),note_sum(baseNote,6),note_sum(baseNote,9))
perfect_level4 = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,3),note_sum(baseNote,6),note_sum(baseNote,9))
perfect_level5 = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,6),note_sum(baseNote,9))
perfect_level6 = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,9))
perfect_level7 = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,9),note_sum(baseNote,10))
perfect_level8 = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,2),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,9),note_sum(baseNote,10))
perfect_level9 = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,2),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,5),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,9),note_sum(baseNote,10))
perfect_level10 = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,2),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,5),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,9),note_sum(baseNote,10),note_sum(baseNote,11))
perfect_level11 = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,2),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,5),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,8),note_sum(baseNote,9),note_sum(baseNote,10),note_sum(baseNote,11))

print perfect_levels_notes
#TODO hay que hacer los niveles relativos

interval_dictation_names = ("Ascending seconds","Descending seconds","Seconds","Ascending thirds","Descending thirds","Thirds","Ascending fourths and fifths","Descending fourths and fifths","Fourths and fifths","Ascending sixths","Descending sixths","Sixths","Ascending sevenths","Descending sevenths","Sevenths","Ascending ninths","Descending ninths","Ninths","Ascending sevenths and tritones","Descending sevenths and tritones","Sevenths and tritones","Ascending fourths, fifths and octaves","Descending fourths, fifths and octaves","Fourths, fifths and octaves","Ascending seconds and thirds","Descending seconds and thirds","Seconds and thirds","Ascending sixths and sevenths ","Descending sixths and sevenths","Sixths and sevenths", "Ascending sevenths and ninths","Descending sevenths and ninths","Sevenths and ninths", "Ascending seconds to octave","Descending seconds to octave","Seconds to octave","Ascending seconds to tenth","Descending seconds to tenth","Seconds to tenth","Ascending seconds to 15th","Descending seconds to 15th","Seconds to 15th")
interval_levels_notes = ((1, 2),(-1,-2),(-1,-2,1,2))
interval_levels_reps = (15,15,25,15,15,25,20,20,30,15,15,25,15,15,25,20,20,30,20,20,30,20,20,30,20,20,30,20,20,30,20,20,30,30,30,50,40,40,60,50,50,70)

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
#perfect_level1 = (note_sum(baseNote,3),note_sum(baseNote,6))
else:
    print "\nWarning: No configuration file, using built-in configuration\n"

perfect_levels_notes = (perfect_level1,perfect_level2,perfect_level3,perfect_level4,perfect_level5,
perfect_level6,perfect_level7,perfect_level8,perfect_level9,perfect_level10,perfect_level11)

txtDisplay0=Entry(frame, textvariable = num0, bd=5, insertwidth=1, font=30, justify='center',width=40)
txtDisplay0.pack(side=LEFT)
txtDisplay1=Entry(frame, textvariable = num1, bd=10, insertwidth=1, font=30, justify='right',width=4)
txtDisplay1.pack(side=LEFT)
txtDisplay1=Entry(frame, textvariable = num2, bd=10, insertwidth=1, font=30, justify='right',width=6)
txtDisplay1.pack(side=LEFT)
txtDisplay1=Entry(frame, textvariable = num3, bd=15, insertwidth=1, font=30, justify='right',width=14)
txtDisplay1.pack(side=LEFT)

topframe = Frame(root)
topframe.pack(side = TOP)
button_play = Button(topframe, width=16, height=4, text="PLAY MELODY", fg="black",command=value_play_melody)
button_play.pack(side=LEFT)
buttonXX = Button(topframe, state=DISABLED, height=4, width=1, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_play = Button(topframe, width=16, height=4, text="PLAY INTERVALO", fg="black",command=value_play_interval)
button_play.pack(side=LEFT)
buttonXX = Button(topframe, state=DISABLED, height=4, width=1, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_play = Button(topframe, width=16, height=4, text="PLAY NOTE", fg="black",command=value_play_note)
button_play.pack(side=LEFT)
buttonXX = Button(topframe, state=DISABLED, height=4, width=1, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_play = Button(topframe, width=16, height=4, text="PLAY HARMONY", fg="black",command=value_play_note)
button_play.pack(side=LEFT)

frame0 = Frame(root)
frame0.pack(side=TOP)

#button1_0 = Button(frame0, width=4, height=14, text="C", fg="black",command=value_0)
#button1_0.pack(side=LEFT)
#button2_0 = Button(frame0, width=2, height=12, pady=8, bd=8, text="Db", bg="black", fg="white",command=value_1)
#button2_0.pack(side=LEFT)

interval = 0
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button0 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_0)
    button0.pack(side=LEFT)
else:
    button0 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_0)
    button0.pack(side=LEFT)

interval = 1
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button1 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_1)
    button1.pack(side=LEFT)
else:
    button1 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_1)
    button1.pack(side=LEFT)

interval = 2
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button2 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_2)
    button2.pack(side=LEFT)
else:
    button2 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_2)
    button2.pack(side=LEFT)

interval = 3
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button3 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_3)
    button3.pack(side=LEFT)
else:
    button3 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_3)
    button3.pack(side=LEFT)

interval = 4
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button4 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_4)
    button4.pack(side=LEFT)
else:
    button4 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_4)
    button4.pack(side=LEFT)

interval = 5
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button5 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_5)
    button5.pack(side=LEFT)
else:
    button5 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_5)
    button5.pack(side=LEFT)

interval = 6
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button6 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_6)
    button6.pack(side=LEFT)
else:
    button6 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_6)
    button6.pack(side=LEFT)

interval = 7
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button7 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_7)
    button7.pack(side=LEFT)
else:
    button7 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_7)
    button7.pack(side=LEFT)

interval = 8
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button8 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_8)
    button8.pack(side=LEFT)
else:
    button8 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_8)
    button8.pack(side=LEFT)

interval = 9
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button9 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_9)
    button9.pack(side=LEFT)
else:
    button9 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_9)
    button9.pack(side=LEFT)

interval = 10
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button10 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_10)
    button10.pack(side=LEFT)
else:
    button10 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_10)
    button10.pack(side=LEFT)

interval = 11
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button11 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_11)
    button11.pack(side=LEFT)
else:
    button11 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_11)
    button11.pack(side=LEFT)

interval = 12
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button12 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_12)
    button12.pack(side=LEFT)
else:
    button12 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_12)
    button12.pack(side=LEFT)

interval = 13
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button13 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_13)
    button13.pack(side=LEFT)
else:
    button13 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_13)
    button13.pack(side=LEFT)

interval = 14
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button14 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_14)
    button14.pack(side=LEFT)
else:
    button14 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_14)
    button14.pack(side=LEFT)

interval = 15
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button15 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_15)
    button15.pack(side=LEFT)
else:
    button15 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_15)
    button15.pack(side=LEFT)

interval = 16
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button16 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_16)
    button16.pack(side=LEFT)
else:
    button16 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_16)
    button16.pack(side=LEFT)

interval = 17
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button17 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_17)
    button17.pack(side=LEFT)
else:
    button17 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_17)
    button17.pack(side=LEFT)

interval = 18
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button18 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_18)
    button18.pack(side=LEFT)
else:
    button18 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_18)
    button18.pack(side=LEFT)

interval = 19
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button19 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_19)
    button19.pack(side=LEFT)
else:
    button19 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_19)
    button19.pack(side=LEFT)

interval = 20
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button20 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_20)
    button20.pack(side=LEFT)
else:
    button20 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_20)
    button20.pack(side=LEFT)

interval = 21
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button21 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_21)
    button21.pack(side=LEFT)
else:
    button21 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_21)
    button21.pack(side=LEFT)

interval = 22
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button22 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_22)
    button22.pack(side=LEFT)
else:
    button22 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_22)
    button22.pack(side=LEFT)

interval = 23
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button23 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_23)
    button23.pack(side=LEFT)
else:
    button23 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_23)
    button23.pack(side=LEFT)

interval = 24
note = note_sum(baseNote,interval)
if note == 'C' or note == 'D' or note == 'E' or note == 'F' or note == 'G' or note == 'A' or note == 'B':
    button24 = Button(frame0, width=2, height=14, text=note, fg="black",command=value_24)
    button24.pack(side=LEFT)
else:
    button24 = Button(frame0, width=1, height=12, pady=8, bd=8, text=note, bg="black", fg="white",command=value_24)
    button24.pack(side=LEFT)

frame1 = Frame(root)
frame1.pack(side=BOTTOM)

button_repeat = Button(frame1, width=8, height=4, text="LEVEL UP", fg="black",command=value_level_up)
button_repeat.pack(side=LEFT)
buttonXX = Button(frame1, state=DISABLED, height=4, width=2, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_repeat = Button(frame1, width=8, height=4, text="LEVEL DOWN", fg="black",command=value_level_down)
button_repeat.pack(side=LEFT)
buttonXX = Button(frame1, state=DISABLED, height=4, width=2, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_repeat = Button(frame1, width=8, height=4, text="SAVE", fg="black",command=value_save)
button_repeat.pack(side=LEFT)
buttonXX = Button(frame1, state=DISABLED, height=4, width=2, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_quit = Button(frame1, width=4, height=4, text="QUIT", fg="black",command=value_quit)
button_quit.pack(side=LEFT)

root.mainloop()







