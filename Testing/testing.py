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

def key_pressed(interval):
    #define what note is pressed,note rel_interval semitones above baseNote
    octave_rel = interval / 12
    octave = str(octave_rel+baseOctave)
    note = note_sum(baseNote,interval)+octave
    current_state.notes_pressed.append(note)
    sound = pygame.mixer.Sound(path_key_notes+note+sformat)
    sound.play()
    if current_state.playing: 
        check_note(note) 
    else:
        display_pressed.set('Played '+note)
    return

def value_solve(): 
    n_played = "Played"
    for note in current_state.notes_played:    
        n_played += " "+note
    solution.set(n_played)
    return

def value_save():
    #save hiscores
    now = datetime.datetime.now()
    date = str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"/"+str(now.hour)+":"+str(now.minute).zfill(2)
    fout1=open("Hiscores_Melodic"+".txt",'a')
    fout2=open("Hiscores_Perfect"+".txt",'a')
    fout3=open("Hiscores_Intervals"+".txt",'a')
    fout4=open("Hiscores_Dictation"+".txt",'a')
    fout1.write(date+" = "+str(melodic_hiscores)+"\n")
    fout2.write(date+" = "+str(perfect_hiscores)+"\n")
    fout3.write(date+" = "+str(intervals_hiscores)+"\n")
    fout4.write(date+" = "+str(dictation_hiscores)+"\n")
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
    fout4=open("Hiscores_Dictation"+".txt",'a')
    fout1.write(date+" = "+str(melodic_hiscores)+"\n")
    fout2.write(date+" = "+str(perfect_hiscores)+"\n")
    fout3.write(date+" = "+str(intervals_hiscores)+"\n")
    fout4.write(date+" = "+str(dictation_hiscores)+"\n")
    fout1.close()
    fout2.close()
    fout3.close()
    fout4.close()
    quit()
    return

def value_reset():
    #reset state
    current_state.playing=False   
    current_state.game=-1          
    current_state.level=1        
    current_state.level_rep=0   
    current_state.repetitions_guessed=0    
    current_state.guessed=False   
    current_state.failed=False   
    current_state.notes_played=[]
    current_state.notes_pressed=[] 
    current_state.last=[]         
    current_state.next=False 
    return

def value_test():
    #for testing
    if debug:
        print "esta en true"
    else:
        print "esta en false"
    return

def message_display_pressed(notes_pressed):
    #message to show in the pressed notes display
    display_message = "Pressed"
    if len(notes_pressed) > 1:
        for n in notes_pressed:
            display_message += ' '+n
    else:
            display_message += ' '+notes_pressed[0]
    display_pressed.set(display_message)
    return


def clear_notes_played():
    current_state.notes_played[:] = []
    return

def clear_notes_pressed():
    current_state.notes_pressed[:] = []
    return

def random_melody(notes,length):
    melody=[]
    octaves=(baseOctave,baseOctave+1)
    for i in range(length):
        melody.append(random.choice(notes)+str(random.choice(octaves)))
    return melody

def random_dictation(intervals,length):
    #choose base note and then generate a correct dictation
    base_notes = (0,1,2,3,4,5,6,7,8,9,10,11)
    octaves = (0,12)
    dictation = []
    #select base note, tonal note  
    sel_base_note = random.choice(base_notes) + random.choice(octaves)
    note = note_sum(baseNote, sel_base_note)
    octave = sel_base_note / 12
    dictation.append(note+str(octave+baseOctave))
    #select notes, must exist
    while True:
        sel_rel_octave = random.choice(octaves)
        sel_inter_note = random.choice(intervals)
        print sel_base_note, sel_rel_octave, sel_inter_note 
        rel_interval = sel_base_note + sel_rel_octave + sel_inter_note 
        #the notes can be between 0 a 24 semitones from baseOctave
        if (rel_interval > 24) or (rel_interval < 0): continue
        note = note_sum(baseNote, rel_interval)
        octave = rel_interval / 12
        dictation.append(note+str(octave+baseOctave))
        if len(dictation) == length: break
    return dictation

def random_interval(interval):
    interval_notes=[]
    base_notes = (0,1,2,3,4,5,6,7,8,9,10,11)
    octaves = (0,12)
    sel_interval = random.choice(interval)  
    #the lower and upper note must exit, loop until accomplished
    while True:
        sel_base_octave = random.choice(octaves)
        sel_base_note = random.choice(base_notes) + sel_base_octave
        if sel_base_note + sel_interval > 24:
            sel_base_note -= 12
        if sel_base_note + sel_interval < -24:
            sel_base_note += 12
        sel_next_note = sel_base_note + sel_interval
        if sel_base_note >= 0 and sel_base_note <=24:
            if sel_next_note >= 0 and sel_next_note <=24: break         
    base_note_octave_rel = sel_base_note / 12
    base_note_octave = str(base_note_octave_rel+baseOctave)
    base_note = note_sum(baseNote,sel_base_note)+base_note_octave
    next_note_octave_rel = sel_next_note / 12
    next_note_octave = str(next_note_octave_rel+baseOctave)
    next_note = note_sum(baseNote,sel_next_note)+next_note_octave
    interval_notes.append(base_note)
    interval_notes.append(next_note)
    return interval_notes


def value_melodic_dictation():
    #melodic dictation code
    if  current_state.game == -1:
        current_state.playing = True
        current_state.game = 0
        current_state.repetitions_guessed = 0
    elif current_state.game != 0:
        current_state.game = 0
        current_state.repetitions_guessed = 0
        current_state.level = 1
    display_checking.set("Try!")   
    intensity=('.ff.','.ff.')
    force=random.choice(intensity)
    #check level
    if current_state.level > 20: current_state.level = 20
    level_notes = melodic_dictation_notes[current_state.level-1]
    level_name = melodic_dictation_names[current_state.level-1]
    current_state.level_rep = melodic_dictation_reps[current_state.level-1]
    display_game.set(level_name)
    #play new melody, repeat if repetition not guessed ot failed
    display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
    if current_state.guessed or len(current_state.notes_played) == 0 and not current_state.failed:
        if debug: print "new note melodic",melodic_dictation_length,current_state.notes_played
        melody=random_melody(level_notes,melodic_dictation_length)  
        clear_notes_played()
        clear_notes_pressed()
        if debug: print melody
        for note in melody:
            current_state.notes_played.append(note)
            force=random.choice(intensity)
            if debug: print path+force+note+".wav"
            sound = pygame.mixer.Sound(path+force+note+sformat)
            sound.play()
            #os.system("mplayer "+path+force+note+sformat)
        current_state.guessed = False
    else:
        if debug: print "new note melodic REPITE"
        for note in current_state.notes_played:
            sound = pygame.mixer.Sound(path+force+note+sformat)
            sound.play()

    return

def value_perfect_pitch():
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
        current_state.level = 1
    display_checking.set("Try!")   
    intensity=('.ff.','.ff.')
    force=random.choice(intensity)
    #check level
    if current_state.level > 11: current_state.level = 11
    level = perfect_levels_notes[current_state.level-1]
    current_state.level_rep = perfect_levels_reps[current_state.level-1]
    level_notes=""
    for n in level:
            level_notes+=n+" "
    display_game.set("Level "+str(current_state.level)+" "+level_notes)

    #play new note, repeat if not repetitions_guessed ot failed
    display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
    if current_state.guessed or len(current_state.notes_played) == 0 and not current_state.failed:
        if debug: print "new note"
        clear_notes_played()
        clear_notes_pressed()
        current_state.failed = False
    #solo la nota base esta en 3. Generamos una nota diferente a la anterior
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
        if debug: print absolute_note
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

def value_interval_recognition():
    #interval code
    if  current_state.game == -1:
        current_state.playing = True
        current_state.game = 2
        current_state.repetitions_guessed = 0
    elif current_state.game != 2:
        current_state.game = 2
        current_state.repetitions_guessed = 0
        current_state.level = 1
    display_checking.set("Try!")   
    intensity=('.ff.','.ff.')
    force=random.choice(intensity)
    #check level
    if current_state.level > 42: current_state.level = 42
    level_name = interval_recognition_names[current_state.level-1]
    current_state.level_rep = interval_recognition_reps[current_state.level-1]
    level_intervals = interval_level_intervals[current_state.level-1]
    display_game.set(level_name)
    #play new melody, repeat if repetition not guessed ot failed
    display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
    if current_state.guessed or len(current_state.notes_played) == 0 and not current_state.failed:
        if debug: print "new note interval recognition",current_state.notes_played
        interval=random_interval(level_intervals) 
        if debug: print interval 
        clear_notes_played()
        clear_notes_pressed()
        for note in interval:
            current_state.notes_played.append(note)
            force=random.choice(intensity)
            if debug: print path+force+note+".wav"
            sound = pygame.mixer.Sound(path+force+note+sformat)
            sound.play()
            #os.system("mplayer "+path+force+note+sformat)
        current_state.guessed = False
    else:
#
        if debug: print "interval recognition REPITE"
        for note in current_state.notes_played:
            sound = pygame.mixer.Sound(path+force+note+sformat)
            sound.play()

    return

def value_dictation():
    #dictation code
    if  current_state.game == -1:
        current_state.playing = True
        current_state.game = 3
        current_state.repetitions_guessed = 0
    elif current_state.game != 3:
        current_state.game = 3
        current_state.repetitions_guessed = 0
        current_state.level = 1
    display_checking.set("Try!")   
    intensity=('.ff.','.ff.')
    force=random.choice(intensity)
    #check level
    if current_state.level > 20: current_state.level = 20
    level_intervals = dictation_level_intervals[current_state.level-1]
    level_name = dictation_names[current_state.level-1]
    current_state.level_rep = dictation_reps[current_state.level-1]
    display_game.set(level_name)
    #play new dictation, repeat if repetition not guessed ot failed
    display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
    if current_state.guessed or len(current_state.notes_played) == 0 and not current_state.failed:
        if debug: print "new note dictation",dictation_length,current_state.notes_played
        dictation=random_dictation(level_intervals,dictation_length)  
        clear_notes_played()
        clear_notes_pressed()
        if debug: print dictation
        for note in dictation:
            current_state.notes_played.append(note)
            force=random.choice(intensity)
            if debug: print path+force+note+".wav"
            sound = pygame.mixer.Sound(path+force+note+sformat)
            sound.play()
            #os.system("mplayer "+path+force+note+sformat)
        current_state.guessed = False
    else:
        if debug: print "new note dictation REPITE"
        for note in current_state.notes_played:
            sound = pygame.mixer.Sound(path+force+note+sformat)
            sound.play()

    return


def check_note(note):
    #show notes pressed notes and check if the notes are correct 
    message_display_pressed(current_state.notes_pressed)
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
                    display_checking.set("Correct!!")
                    display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
                    if (current_state.repetitions_guessed >= melodic_hiscores[current_state.level-1]): 
                        melodic_hiscores[current_state.level-1] = current_state.repetitions_guessed
               else:
                    if debug: print "Melodic dictation failed"
                    if not current_state.guessed: 
                        current_state.repetitions_guessed = 0
                        display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
                        current_state.failed = True
                        clear_notes_pressed()                      
            #if level accomplished
            if current_state.repetitions_guessed >= current_state.level_rep: 
                current_state.level += 1
                current_state.repetitions_guessed = 0

    #perfect pitch code 
    if current_state.game == 1:
        #if level not finished continue
        if current_state.repetitions_guessed < current_state.level_rep:
            #if repetitions_guessed
            if current_state.notes_played[0] == note:
                if debug: print "Perfect pith repetitions_guessed"
                if not current_state.failed and not current_state.guessed: current_state.repetitions_guessed += 1
                current_state.guessed = True
                display_checking.set("Correct!!")
                display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
                if (current_state.repetitions_guessed >= perfect_hiscores[current_state.level-1]): 
                    perfect_hiscores[current_state.level-1] = current_state.repetitions_guessed
            else:
                if debug: print "Perfect pith failed"
                if not current_state.guessed: 
                    current_state.repetitions_guessed = 0
                    display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
                    current_state.failed = True
                    clear_notes_pressed()
        #if level accomplished
        if current_state.repetitions_guessed >= current_state.level_rep: 
            current_state.level += 1
            current_state.repetitions_guessed = 0

    #interval recognition code
    if current_state.game == 2:
        #if phrase not enough continue
        if len(current_state.notes_pressed) == 2: 
        #if level not finished continue
                   if current_state.repetitions_guessed < current_state.level_rep:
            #if repetitions_guessed
               if current_state.notes_played == current_state.notes_pressed:
                    if debug: print "Interval recognition guessed"
                    if not current_state.failed and not current_state.guessed: current_state.repetitions_guessed += 1
                    current_state.guessed = True
                    current_state.failed = False
                    clear_notes_pressed()
                    clear_notes_played()
                    display_checking.set("Correct!!")
                    display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
                    if (current_state.repetitions_guessed >= intervals_hiscores[current_state.level-1]): 
                        intervals_hiscores[current_state.level-1] = current_state.repetitions_guessed
               else:
                    if debug: print "Interval recognition failed"
                    if not current_state.guessed: 
                        current_state.repetitions_guessed = 0
                        display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
                            display_checking.set("Incorrect!!")
                        current_state.failed = True
                        clear_notes_pressed()                      
            #if level accomplished
            if current_state.repetitions_guessed >= current_state.level_rep: 
                current_state.level += 1
                current_state.repetitions_guessed = 0 

    #dictation code
    if current_state.game == 3:
        #if phrase not enough continue
        if len(current_state.notes_pressed) == dictation_length: 
        #if level not finished continue
                   if current_state.repetitions_guessed < current_state.level_rep:
            #if repetitions_guessed
               if current_state.notes_played == current_state.notes_pressed:
                    if debug: print "Dictation guessed"
                    if not current_state.failed and not current_state.guessed: current_state.repetitions_guessed += 1
                    current_state.guessed = True
                    current_state.failed = False
                    clear_notes_pressed()
                    clear_notes_played()
                    display_checking.set("Correct!!")
                    display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
                    if (current_state.repetitions_guessed >= intervals_hiscores[current_state.level-1]): 
                        dictation_hiscores[current_state.level-1] = current_state.repetitions_guessed
               else:
                    if debug: print "Dictation failed"
                    if not current_state.guessed: 
                        current_state.repetitions_guessed = 0
                        display_hiscore.set("Hiscore "+str(current_state.repetitions_guessed)+" / "+str(current_state.level_rep))
                            display_checking.set("Incorrect!!")
                        current_state.failed = True
                        clear_notes_pressed()                      
            #if level accomplished
            if current_state.repetitions_guessed >= current_state.level_rep: 
                current_state.level += 1
                current_state.repetitions_guessed = 0 

    return

def value_level_up():
    current_state.level += 1
    display_game.set("Level "+str(current_state.level))
    display_hiscore.set("Hiscore ")
    current_state.repetitions_guessed = 0
    if debug: print current_state.level
    return

def value_level_down():
    if current_state.level > 1: current_state.level -= 1
    display_game.set("Level "+str(current_state.level))
    display_hiscore.set("Hiscore ")
    current_state.repetitions_guessed = 0
    if debug: print current_state.level
    return

def clear():
    display_checking.set("Try!")

def value_0():
    #note rel_interval semitones above baseNote
    rel_interval = 0
    key_pressed(rel_interval)
    return

def value_1():
    #note rel_interval semitones above baseNote
    rel_interval = 1
    key_pressed(rel_interval)
    return

def value_2():
    #note rel_interval semitones above baseNote
    rel_interval = 2
    key_pressed(rel_interval)
    return

def value_3():
    #note rel_interval semitones above baseNote
    rel_interval = 3
    key_pressed(rel_interval)
    return

def value_4():
    #note rel_interval semitones above baseNote
    rel_interval = 4
    key_pressed(rel_interval)
    return

def value_5():
    #note rel_interval semitones above baseNote
    rel_interval = 5
    key_pressed(rel_interval)
    return

def value_6():
    #note rel_interval semitones above baseNote
    rel_interval = 6
    key_pressed(rel_interval)
    return

def value_7():
    #note rel_interval semitones above baseNote
    rel_interval = 7
    key_pressed(rel_interval)

def value_8():
    #note rel_interval semitones above baseNote
    rel_interval = 8
    key_pressed(rel_interval)
    return

def value_9():
    #note rel_interval semitones above baseNote
    rel_interval = 9
    key_pressed(rel_interval)
    return

def value_10():
    #note rel_interval semitones above baseNote
    rel_interval = 10
    key_pressed(rel_interval)
    return

def value_11():
    #note rel_interval semitones above baseNote
    rel_interval = 11
    key_pressed(rel_interval)
    return

def value_12():
    #note rel_interval semitones above baseNote
    rel_interval = 12
    key_pressed(rel_interval)

def value_13():
    #note rel_interval semitones above baseNote
    rel_interval = 13
    key_pressed(rel_interval)
    return

def value_14():
    #note rel_interval semitones above baseNote
    rel_interval = 14
    key_pressed(rel_interval)
    return

def value_15():
    #note rel_interval semitones above baseNote
    rel_interval = 15
    key_pressed(rel_interval)
    return

def value_16():
    #note rel_interval semitones above baseNote
    rel_interval = 16
    key_pressed(rel_interval)
    return

def value_17():
    #note rel_interval semitones above baseNote
    rel_interval = 17
    key_pressed(rel_interval)
    return

def value_18():
    #note rel_interval semitones above baseNote
    rel_interval = 18
    key_pressed(rel_interval)
    return

def value_19():
    #note rel_interval semitones above baseNote
    rel_interval = 19
    key_pressed(rel_interval)
    return

def value_20():
    #note rel_interval semitones above baseNote
    rel_interval = 20
    key_pressed(rel_interval)
    return

def value_21():
    #note rel_interval semitones above baseNote
    rel_interval = 21
    key_pressed(rel_interval)
    return

def value_22():
    #note rel_interval semitones above baseNote
    rel_interval = 22
    key_pressed(rel_interval)
    return

def value_23():
    #note rel_interval semitones above baseNote
    rel_interval = 23
    key_pressed(rel_interval)
    return

def value_24():
    #note rel_interval semitones above baseNote
    rel_interval = 24
    key_pressed(rel_interval)
    return


#save state
#TODO HARMONIC DICTATION
class State():
    playing=False    #playing
    game=-1          #-1 mo game, 0 melody dictation, 1 perfect pitch, 2 intervals recognition, 3 dictation
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
melodic_hiscores = [0] * 20
perfect_hiscores = [0] * 11
intervals_hiscores = [0] * 42
dictation_hiscores = [0] * 20

#CONFIGURATIONS
#default configuration
#debugging
debug = True
#path to sounds folder, files and format
path="./sounds/piano/Piano"
path_key_notes="./sounds/piano/Piano.ff."
sformat=".wav"
#base octave
baseOctave = 2
#base note
baseNote = 'C'

melodic_dictation_length = 5
melodic_dictation_names = ["Major 1,3,5","Minor 1,3,5","Major 1,3,4,5","Minor 1,3,4,5","Major 1-5","Minor 1-5","Major Pentatonic","Minor Pentatonic", "Major 1-6","Minor 1-6","Blues","Major","Minor","Harmonic Minor","Melodic Minor","Minor, 1 accidental", "Minor, 2 accidental","Minor, 3 accidental","Minor, 4 accidental", "Chromatic"]
melodic_dictation_notes = [('C', 'E', 'G'),('C', 'Eb', 'G'),('C', 'E', 'F','G'),('C', 'Eb', 'F', 'G'),('C', 'D','E', 'F','G'),('C', 'D', 'Eb', 'F', 'G'),('C','D','E', 'G','A'),('C', 'Eb', 'G', 'Ab', 'Bb'),('C', 'D','E', 'F','G','A'),('C', 'D', 'Eb', 'F', 'G','Ab'),('C','Eb', 'F', 'Gb','G','Bb'),('C', 'D','E', 'F','G','B'),('C', 'D', 'Eb', 'F', 'G','Ab','Bb'),('C', 'D', 'Eb', 'F', 'G','Ab','B'),('C', 'D', 'Eb', 'F', 'G','A','B'),('C','D', 'Eb','F', 'G','A','Bb','B'),('C','D', 'Eb','F', 'G','Ab','A','Bb','B'),('C','D', 'Eb','F','Gb', 'G','Bb','A','Bb','B'),('C','D', 'Eb', 'E','F','Gb', 'G','Bb','A','Bb','B'),('C','Db','D', 'Eb', 'E','F','Gb', 'G','Ab','A','Bb','B')]
melodic_dictation_reps = [5,5,5,5,5,7,7,7,7,7,10,10,10,10,10,15,15,15,15,15]


perfect_levels_reps = [20,20,20,20,25,25,25,25,30,30,30]
perfect_levels_notes = [None] * 11
perfect_levels_notes[0] = (note_sum(baseNote,3),note_sum(baseNote,6))
perfect_levels_notes[1] = (note_sum(baseNote,0),note_sum(baseNote,3),note_sum(baseNote,6))
perfect_levels_notes[2] = (note_sum(baseNote,0),note_sum(baseNote,3),note_sum(baseNote,6),note_sum(baseNote,9))
perfect_levels_notes[3] = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,3),note_sum(baseNote,6),note_sum(baseNote,9))
perfect_levels_notes[4] = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,6),note_sum(baseNote,9))
perfect_levels_notes[5] = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,9))
perfect_levels_notes[6] = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,9),note_sum(baseNote,10))
perfect_levels_notes[7] = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,2),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,9),note_sum(baseNote,10))
perfect_levels_notes[8] = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,2),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,5),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,9),note_sum(baseNote,10))
perfect_levels_notes[9] = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,2),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,5),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,9),note_sum(baseNote,10),note_sum(baseNote,11))
perfect_levels_notes[10] = (note_sum(baseNote,0),note_sum(baseNote,1),note_sum(baseNote,2),note_sum(baseNote,3),note_sum(baseNote,4),note_sum(baseNote,5),note_sum(baseNote,6),note_sum(baseNote,7),note_sum(baseNote,8),note_sum(baseNote,9),note_sum(baseNote,10),note_sum(baseNote,11))

interval_recognition_names = ["Ascending seconds","Descending seconds","Seconds","Ascending thirds","Descending thirds","Thirds","Ascending fourths and fifths","Descending fourths and fifths","Fourths and fifths","Ascending sixths","Descending sixths","Sixths","Ascending sevenths","Descending sevenths","Sevenths","Ascending ninths","Descending ninths","Ninths","Ascending sevenths and tritones","Descending sevenths and tritones","Sevenths and tritones","Ascending fourths, fifths and octaves","Descending fourths, fifths and octaves","Fourths, fifths and octaves","Ascending seconds and thirds","Descending seconds and thirds","Seconds and thirds","Ascending sixths and sevenths ","Descending sixths and sevenths","Sixths and sevenths", "Ascending sevenths and ninths","Descending sevenths and ninths","Sevenths and ninths", "Ascending seconds to octave","Descending seconds to octave","Seconds to octave","Ascending seconds to tenth","Descending seconds to tenth","Seconds to tenth","Ascending seconds to 15th","Descending seconds to 15th","Seconds to 15th"]
interval_level_intervals = [None] * 42
#TODO completar interval_level_intervals
interval_recognition_reps = [15,15,25,15,15,25,20,20,30,15,15,25,15,15,25,20,20,30,20,20,30,20,20,30,20,20,30,20,20,30,20,20,30,30,30,50,40,40,60,50,50,70]

dictation_length = 5
dictation_names = ["Major 1,3,5","Minor 1,3,5","Major 1,3,4,5","Minor 1,3,4,5","Major 1-5","Minor 1-5","Major Pentatonic","Minor Pentatonic", "Major 1-6","Minor 1-6","Blues","Major","Minor","Harmonic Minor","Melodic Minor","Minor, 1 accidental", "Minor, 2 accidental","Minor, 3 accidental","Minor, 4 accidental", "Chromatic"]
dictation_notes = [('C', 'E', 'G'),('C', 'Eb', 'G'),('C', 'E', 'F','G'),('C', 'Eb', 'F', 'G'),('C', 'D','E', 'F','G'),('C', 'D', 'Eb', 'F', 'G'),('C','D','E', 'G','A'),('C', 'Eb', 'G', 'Ab', 'Bb'),('C', 'D','E', 'F','G','A'),('C', 'D', 'Eb', 'F', 'G','Ab'),('C','Eb', 'F', 'Gb','G','Bb'),('C', 'D','E', 'F','G','B'),('C', 'D', 'Eb', 'F', 'G','Ab','Bb'),('C', 'D', 'Eb', 'F', 'G','Ab','B'),('C', 'D', 'Eb', 'F', 'G','A','B'),('C','D', 'Eb','F', 'G','A','Bb','B'),('C','D', 'Eb','F', 'G','Ab','A','Bb','B'),('C','D', 'Eb','F','Gb', 'G','Bb','A','Bb','B'),('C','D', 'Eb', 'E','F','Gb', 'G','Bb','A','Bb','B'),('C','Db','D', 'Eb', 'E','F','Gb', 'G','Ab','A','Bb','B')]
dictation_level_intervals = [None] * 42
dictation_level_intervals[0] = (0,4,7)
dictation_level_intervals[1] = (0,3,7)
dictation_level_intervals[2] = (0,4,5,7)
dictation_level_intervals[3] = (0,3,5,7)
dictation_reps = [5,5,5,5,5,7,7,7,7,7,10,10,10,10,10,15,15,15,15,15]

#read configuration file
config = ConfigParser.ConfigParser()
if len(sys.argv) > 1:
    config_file = sys.argv[1]
else:
    config_file = "configuration.ini"

if os.path.isfile(config_file):
    #read configuration from configuration file
    #TODO protection against void fields
    print "\nReading configuration from " + config_file
    config.read(config_file)
    baseOctave = int(config.get('General', 'baseOctave'))
    baseNote = config.get('General', 'baseNote')
    path = config.get('General', 'pathSounds')
    sformat = config.get('General', 'soundsFormat')
    debug = config.getboolean('General', 'debug')
    #load melodic dictation configuration
    melodic_dictation_length = int(config.get('Melodic Dictation', 'length'))
    for i in range(20):
        melodic_dictation_names[i] = config.get('Melodic Dictation', 'name'+str(i+1))
        melodic_dictation_intervals = [int(inter) for inter in config.get('Melodic Dictation', 'level'+str(i+1)).split()]
        melodic_dictation_level = [note_sum(baseNote,inter) for inter in melodic_dictation_intervals]
        melodic_dictation_notes[i]= melodic_dictation_level
        melodic_dictation_rep = [int(inter) for inter in config.get('Melodic Dictation', 'repetitions'+str(i+1)).split()]
        melodic_dictation_reps[i]= melodic_dictation_rep[0]
    #load perfect pitch configuration
    for i in range(11):
        perfect_levels_intervals = [int(inter) for inter in config.get('Perfect Pitch', 'level'+str(i+1)).split()]
        perfect_level = [note_sum(baseNote,inter) for inter in perfect_levels_intervals]
        perfect_levels_notes[i]= perfect_level
        perfect_levels_rep = [int(inter) for inter in config.get('Perfect Pitch', 'repetitions'+str(i+1)).split()]
        perfect_levels_reps[i]= perfect_levels_rep[0]
    #load intervals recognition configuration
    for i in range(42):
        interval_recognition_names[i] = config.get('Intervals recognition', 'name'+str(i+1))
        interval_recognition_reps[i]= int(config.get('Intervals recognition', 'repetitions'+str(i+1)))
        interval_level_intervals[i] = [int(inter) for inter in config.get('Intervals recognition', 'level'+str(i+1)).split()]
        #interval_level_level = [note_sum(baseNote,inter) for inter in interval_level_intervals]
        #print config.get('Intervals recognition', 'level'+str(i+1)), interval_level_level
        #interval_recognition_notes[i]= interval_level_level
else:
    print "\nWarning: No configuration file, using built-in configuration\n"

root = Tk()
root.title('PIANO FROM '+baseNote+str(baseOctave))

frame_disp0 = Frame(root)
frame_disp0.pack(side = TOP)

#game key pressed, correct o no, hiscore respectively
display_game=StringVar()
display_pressed=StringVar()
display_checking=StringVar()
display_hiscore=StringVar()

display_game.set("GAME SELECTED")
display_pressed.set("NOTES PRESSED")
display_checking.set("CHECKING")
display_hiscore.set("HISCORE")

txtDisplay0=Entry(frame_disp0, textvariable = display_game, bd=5, insertwidth=1, font=30, justify='center',width=40)
txtDisplay0.pack(side=LEFT)
txtDisplay1=Entry(frame_disp0, textvariable = display_hiscore, bd=10, insertwidth=1, font=30, justify='center',width=14)
txtDisplay1.pack(side=LEFT)

frame_disp1 = Frame(root)
frame_disp1.pack(side = TOP)

txtDisplay2=Entry(frame_disp1, textvariable = display_pressed, bd=10, insertwidth=1, font=30, justify='center',width=30)
txtDisplay2.pack(side=LEFT)
txtDisplay3=Entry(frame_disp1, textvariable = display_checking, bd=15, insertwidth=1, font=30, justify='center',width=14)
txtDisplay3.pack(side=LEFT)

topframe = Frame(root)
topframe.pack(side = TOP)
button_play = Button(topframe, width=16, height=4, text="PLAY MELODY", fg="black",command=value_melodic_dictation)
button_play.pack(side=LEFT)
buttonXX = Button(topframe, state=DISABLED, height=4, width=1, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_perfect = Button(topframe, width=16, height=4, text="PLAY NOTE", fg="black",command=value_perfect_pitch)
button_perfect.pack(side=LEFT)
buttonXX = Button(topframe, state=DISABLED, height=4, width=1, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_interval = Button(topframe, width=16, height=4, text="PLAY INTERVAL", fg="black",command=value_interval_recognition)
button_interval.pack(side=LEFT)
buttonXX = Button(topframe, state=DISABLED, height=4, width=1, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_dictation = Button(topframe, width=16, height=4, text="PLAY DICTATION", fg="black",command=value_dictation)
button_dictation.pack(side=LEFT)

frame0 = Frame(root)
frame0.pack(side=TOP)

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

solution=StringVar()

solution.set("NOTES PLAYED")

button_solve = Button(frame1, width=8, height=4, text="SOLUTION", fg="black",command=value_solve)
button_solve.pack(side=LEFT)
solution_display = Entry(frame1, textvariable = solution, bd=15, insertwidth=1, font=30, justify='center',width=34)
solution_display.pack(side=LEFT)
button_repeat = Button(frame1, width=8, height=4, text="LEVEL UP", fg="black",command=value_level_up)
button_repeat.pack(side=LEFT)
buttonXX = Button(frame1, state=DISABLED, height=4, width=2, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_repeat = Button(frame1, width=8, height=4, text="LEVEL DOWN", fg="black",command=value_level_down)
button_repeat.pack(side=LEFT)
buttonXX = Button(frame1, state=DISABLED, height=4, width=2, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_repeat = Button(frame1, width=4, height=4, text="SAVE", fg="black",command=value_save)
button_repeat.pack(side=LEFT)
buttonXX = Button(frame1, state=DISABLED, height=4, width=2, padx=0, pady=0, relief=RIDGE)
buttonXX.pack(side=LEFT)
button_reset = Button(frame1, width=4, height=4, text="RESET", fg="black",command=value_reset)
button_reset.pack(side=LEFT)
button_quit = Button(frame1, width=4, height=4, text="QUIT", fg="black",command=value_quit)
button_quit.pack(side=LEFT)

if debug:
    button_test = Button(frame1, width=4, height=4, text="TEST", fg="black",command=value_test)
    button_test.pack(side=LEFT)

root.mainloop()








