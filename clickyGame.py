import tkinter

class Game:
  def addCount(self):
    self.count += 1
    if self.count == 10 or self.win:
      self.win = True
      self.counter.configure(text="YOU WIN!!")
    else:
      self.counter.configure(text="%d" % self.count)

  def createGui(self):
    self.root = tkinter.Tk()
    self.root.geometry("150x150")
    self.counter = tkinter.Label(self.root, text=self.count)
    self.button = tkinter.Button(self.root,text="clicky", command= self.addCount)
    
    self.counter.pack()
    self.button.pack()

  def __init__(self):
    self.count = 0
    self.win = False
    self.createGui()
    self.root.mainloop()
    
game = Game()
