import tkinter as tk 
from pydub import AudioSegment
from pydub.playback import play 
import math
import random 

class ChordRecognizer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.go = tk.Button(self, text='Start', command = lambda: self.ChordSelector())
        self.go.pack()

    def ChordSelector(self):
        chord_possibilities = {1: 'a', 2: 'a#', 3: 'b', 4: 'c', 5: 'c#', 6: 'd', 7: 'd#', 8: 'e', 9: 'e', 10: 'f', 11: 'f#', 12: 'g', 13: 'g#'} 
        random_choice = random.randint(1, 13)
        chord_choice = chord_possibilities[random_choice]
        random_wrong_list = [] 
        while len(random_wrong_list) <= 5:
            random_wrong_choice = random.randint(1,13)
            if random_wrong_choice != random_choice:
                if chord_possibilities[random_wrong_choice] not in random_wrong_list:
                    random_wrong_list.append(chord_possibilities[random_wrong_choice])
        random_positiion = random.randint(0, 5)
        random_wrong_list.insert(random_positiion, chord_choice)
        
        Button = tk.Button(self, text='Play Sound', command = lambda: self.playSound())
        Button.pack()
        for chord in random_wrong_list:
            Button = tk.Button(self, text=chord)
            Button.pack()

        return chord_choice, random_wrong_list

root = tk.Tk()
ChordRecognizer(root).pack(side='top',expand=True)
root.mainloop()