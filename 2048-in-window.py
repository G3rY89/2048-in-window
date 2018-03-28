import random
import tkinter as tk
import colored
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E, N, S, LEFT, RIGHT
from colored import bg, attr
import datetime
import os
os.system('cls' if os.name == 'nt' else 'clear')


table = {
    '11':  '-',
    '21': '-',
    '31': '-',
    '41': '-',
    '12': '-',
    '22': '-',
    '32': '-',
    '42': '-',
    '13': '-',
    '23': '-',
    '33': '-',
    '43': '-',
    '14': '-',
    '24': '-',
    '34': '-',
    '44': '-'
    }

class game_2048():
    def __init__(self, master):
        self.master = master
        master.title("2048 by Dewsy and Geri")

        self.color_code = {
            '-': 0,
            2: 1,
            4: 2,
            8: 3,
            16: 4,
            32: 5,
            64: 6,
            128: 7,
            256: 8,
            512: 9,
            1024: 10,
            2048: 11
            }

        self.user_name = None
        self.steps = 0

        self.up_button = Button(master, text="↑", command=lambda:[self.up(), self.printtable(), self.span2(), self.step_Counter()])
        self.down_button = Button(master, text="↓", command=lambda:[self.down(), self.printtable(), self.span2(), self.step_Counter()])
        self.left_button = Button(master, text="←", command=lambda:[self.left(), self.printtable(), self.span2(), self.step_Counter()])
        self.right_button = Button(master, text="→", command=lambda:[self.right(), self.printtable(), self.span2(), self.step_Counter()])
        self.usrname_button = Button(master, text="Enter", command=lambda:self.store_userName()) 
        self.usrname = Label(master, text="Player name: ")
        self.entry = Entry(master, validate="none",)
        self.steps_made = StringVar()
        self.counter = Label(master, text="Steps: ")
        self.made_steps = Label(master, textvariable=self.steps_made)
        self.greetings = Label(master, text="Welcome on board!")
        
        self.usrname.grid(row=0 , column=0, sticky=W+E)
        self.usrname_button.grid(row=0 , column=2, sticky=W+E)
        self.entry.grid(row=0 , column=1, sticky=W+E) 
        self.up_button.grid(row=1 , column=4, sticky=W+E)
        self.left_button.grid(row=2 , column=3, sticky=W+E)  
        self.down_button.grid(row=2 , column=4, sticky=W+E) 
        self.right_button.grid(row=2 , column=5, sticky=W+E) 
        self.counter.grid(row=2, column=0)
        self.made_steps.grid(row=2, column=1)
        self.greetings.grid(row=3 , column=1, sticky=W+E+N+S)
       
        self.span2()
        self.span2()
        self.printtable()

    def savegame(self):
        with open('savegame.csv', 'w') as f:
            t = []
            for k, v in table.items():
                t.append('{key}: {value}'.format(key=str(k), value=(v)))
            f.write(','.join(t))
    print('Saved!')


    def loadgame(self):

        def isint(x):
            try:
                int(x)
                return int(x)
            except ValueError:
                return str(x)

        with open('savegame.csv', 'r') as f:
            global table
            table = {}
            t = f.read().split(',')
            for i in t:
                values = i.split(': ')
                table[values[0]] = isint(values[1])

    def step_Counter(self):
        self.steps += 1
        self.steps_made.set(self.steps)
        return(self.steps)
          
    def store_userName(self):   
        self.user_name = self.entry.get()
        if self.user_name != None:
            self.entry.delete(0, 'end')
        return(self.user_name)
       
    def color(self, x):
        return bg(self.color_code[table[x]])
  
    def printtable(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        score = []
        for k, v in table.items():
            score.append(v)
        score = filter(lambda x: type(x) == int, score)
        print('\n')
        print("Score: ", sum(score))
        print('\n')
        print(
            '{background} {:^4}'.format(table['11'], background=bg(self.color_code[table['11']])),
            '{background} {:^4}'.format(table['21'], background=bg(self.color_code[table['21']])),
            '{background} {:^4}'.format(table['31'], background=bg(self.color_code[table['31']])),
            '{background} {:^4}'.format(table['41'], background=bg(self.color_code[table['41']])))
        print(
            '{background} {:^4}'.format(table['12'], background=bg(self.color_code[table['12']])),
            '{background} {:^4}'.format(table['22'], background=bg(self.color_code[table['22']])),
            '{background} {:^4}'.format(table['32'], background=bg(self.color_code[table['32']])),
            '{background} {:^4}'.format(table['42'], background=bg(self.color_code[table['42']])))
        print(
            '{background} {:^4}'.format(table['13'], background=bg(self.color_code[table['13']])),
            '{background} {:^4}'.format(table['23'], background=bg(self.color_code[table['23']])),
            '{background} {:^4}'.format(table['33'], background=bg(self.color_code[table['33']])),
            '{background} {:^4}'.format(table['43'], background=bg(self.color_code[table['43']])))
        print(
            '{background} {:^4}'.format(table['14'], background=bg(self.color_code[table['14']])),
            '{background} {:^4}'.format(table['24'], background=bg(self.color_code[table['24']])),
            '{background} {:^4}'.format(table['34'], background=bg(self.color_code[table['34']])),
            '{background} {:^4}'.format(table['44'], background=bg(self.color_code[table['44']])))
        print(bg(0))

    def span2(self):
        table[random.choice(list([i for i, j in table.items() if j == '-']))] = 2

    def upCollumn(self, x):
            for self.y in range(3):
                z = 0
                for self.b in range(3):
                    z = z + 1
                    if table[str(x) + str(z)] == '-':
                        table[str(x) + str(z)] = table[str(x) + str(z + 1)]
                        table[str(x) + str(z + 1)] = '-'
            for self.y in range(3):
                z = 0
                for self.b in range(3):
                    z = z + 1
                    if table[str(x) + str(z)] != '-' and table[str(x) + str(z)] == table[str(x) + str(z + 1)]:
                        table[str(x) + str(z)] = table[str(x) + str(z)] * 2
                        table[str(x) + str(z + 1)] = '-'     

    def downCollumn(self, x):
        for self.y in range(3):
            z = 5
            for self.b in range(3):
                z = z - 1
                if table[str(x) + str(z)] == '-':
                    table[str(x) + str(z)] = table[str(x) + str(z - 1)]
                    table[str(x) + str(z - 1)] = '-'
        for self.y in range(3):
            z = 5
            for self.b in range(3):
                z = z - 1
                if table[str(x) + str(z)] != '-' and table[str(x) + str(z)] == table[str(x) + str(z - 1)]:
                    table[str(x) + str(z)] = table[str(x) + str(z)] * 2
                    table[str(x) + str(z - 1)] = '-'


    def leftRow(self, x):
        for y in range(3):
            z = 0
            for b in range(3):
                z = z + 1
                if table[str(z) + str(x)] == '-':
                    table[str(z) + str(x)] = table[str(z + 1) + str(x)]
                    table[str(z + 1) + str(x)] = '-'
        for y in range(3):
            z = 0
            for b in range(3):
                z = z + 1
                if table[str(z) + str(x)] != '-' and table[str(z) + str(x)] == table[str(z + 1) + str(x)]:
                    table[str(z) + str(x)] = table[str(z + 1) + str(x)] * 2
                    table[str(z + 1) + str(x)] = '-'


    def rightRow(self, x):
        for y in range(3):
            z = 5
            for b in range(3):
                z = z - 1
                if table[str(z) + str(x)] == '-':
                    table[str(z) + str(x)] = table[str(z - 1) + str(x)]
                    table[str(z - 1) + str(x)] = '-'
        for y in range(3):
            z = 5
            for b in range(3):
                z = z - 1
                if table[str(z) + str(x)] != '-' and table[str(z) + str(x)] == table[str(z - 1) + str(x)]:
                    table[str(z) + str(x)] = table[str(z - 1) + str(x)] * 2
                    table[str(z - 1) + str(x)] = '-'   

    def up(self):
            for z in range(3):
                z = 0
                for self.w in range(4):
                    self.upCollumn(z + 1)
                    z = z + 1

    def down(self):
        for z in range(3):
            z = 0
            for w in range(4):
                self.downCollumn(z + 1)
                z = z + 1


    def left(self):
        for z in range(3):
            z = 0
            for w in range(4):
                self.leftRow(z + 1)
                z = z + 1


    def right(self):
        for z in range(3):
            z = 0
            for w in range(4):
                self.rightRow(z + 1)
                z = z + 1
    

root = Tk()
my_gui = game_2048(root)
root.mainloop()