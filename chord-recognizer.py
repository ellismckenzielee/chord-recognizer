import tkinter as tk 
from pydub import AudioSegment
from pydub.playback import play 
import math
import random 

class ChordRecognizer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.gamecount = 1
        self.go = tk.Button(self, text='Start', command = lambda: self.ChordSelector())
        self.go.pack()
        self.no_of_games = 10
        
    def ChordSelector(self):
        self.go.pack_forget()
        chord_possibilities = {1: 'a', 2: 'a#', 3: 'b', 4: 'c', 5: 'c#', 6: 'd', 7: 'd#', 8: 'e', 9: 'e', 10: 'f', 11: 'f#', 12: 'g', 13: 'g#'} 
        random_choice = random.randint(1, 13)
        chord_choice = chord_possibilities[random_choice]
        random_wrong_list = [] 
        print(chord_choice)
        
        while len(random_wrong_list) <= 5:
            random_wrong_choice = random.randint(1,13)
            if random_wrong_choice != random_choice:
                if chord_possibilities[random_wrong_choice] not in random_wrong_list:
                    random_wrong_list.append(chord_possibilities[random_wrong_choice])
        
        random_positiion = random.randint(0, 5)
        random_wrong_list.insert(random_positiion, chord_choice)
        
        Button = tk.Button(self, text='Play Sound', command = lambda: self.playSound())
        Button.pack()

        chord_position = 0
        for chord in random_wrong_list:
            Button = tk.Button(self, text=chord, command = lambda chord = random_wrong_list[chord_position]: self.SelectionChecker(chord, chord_choice))
            Button.pack()
            chord_position = chord_position + 1
        print(random_wrong_list)
        return chord_choice, random_wrong_list

    def SelectionChecker(self, value, chord_choice):
        print(self.gamecount)
        '''Checks the user input and continues with the appropriate action'''
        print(value)
        end_of_game = self.endGameChecker()

        if value == chord_choice:
            print('Correct')
            ScoreCounter.addScore()
        self.addGame()
        for widget in self.winfo_children():
            widget.destroy()
        if end_of_game == True:
            self.endGame()
        else: 
            self.ChordSelector()
  
    def addGame(self):
        self.gamecount = self.gamecount + 1

    def endGameChecker(self):
        if self.gamecount == self.no_of_games:
            return True
        else:
            return False

    def endGame(self):
        for widget in self.winfo_children():
            widget.destroy()
        Label = tk.Label(self, text='Thanks for playing')
        Label.pack()
        Score = tk.Label(self, text = 'You scored {} out of {}! '.format(ScoreCounter.score, self.no_of_games))
        Score.pack()
        self.go = tk.Button(self, text='Play Again?', command = lambda: self.ChordSelector())
        self.go.pack()
        ScoreCounter.resetScore()
        self.gamecount = 1

class ScoreCounter():
    def __init__(self):
        self.score = 0 

    def addScore(self):
        self.score = self.score + 1
        print(self.score)

    def resetScore(self):
        self.score = 0

        
root = tk.Tk()
root.minsize(250,500)
ScoreCounter = ScoreCounter()
ChordRecognizer(root).pack(side='top',expand=True)
root.mainloop()