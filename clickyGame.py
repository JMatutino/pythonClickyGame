import tkinter, random

class Game:
  def setCounter(self):
    if self.win:
      self.counter.configure(text="YOU WIN!!")
    else:
      self.counter.configure(text="%d" % self.count)            

  def addCount(self):
    self.count += 1
    if self.count == 10 or self.win:
      self.win = True
    self.setCounter()
      
  def subtractCount(self):
    randNum = random.randrange(1,3)
    print(randNum)
    if self.count - randNum <= 0:
      self.count = 0
    else:
      self.count -= randNum
    self.setCounter() 
    if not self.win:
      self.root.after( 1000, self.subtractCount )
      
   
  def createGui(self):
    self.root = tkinter.Tk()
    self.root.geometry("150x150")
    
    self.counter = tkinter.Label(self.root, text=self.count)
    self.root.after( 1000, self.subtractCount )
    
    self.button = tkinter.Button(self.root,text="clicky", command= self.addCount)
    
    self.counter.pack()
    self.button.pack()

  def __init__(self):
    self.count = 0
    self.win = False
    self.createGui()
    self.root.mainloop()
    
game = Game()
