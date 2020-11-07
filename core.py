import tkinter as tk


class mWindow(tk.Frame):
  def __init__(self):
    master = tk.Tk()
    master.title("Software Title")
    master.geometry("400x300")
    super().__init__(master)
    self.master = master
    self.pack()
    # self.create_widgets()

  def create_widgets(self):
    self.hi_there = tk.Button(self)
    self.hi_there["text"] = "Hello World\n(click me)"
    self.hi_there["command"] = self.say_hi
    self.hi_there.pack(side="top")

    self.quit = tk.Button(self, text="QUIT", fg="red",
                          command=self.master.destroy)
    self.quit.pack(side="bottom")

  def say_hi(self):
    print("hi there, everyone!")

  def clear(self):
    for child in self.winfo_children():
      child.destroy()

  def pushstr(self, txt):
    tk.Label(self.master, text=txt).pack()

  def color(self, code):
    print(code)

def main():
  app = mWindow()
  app.mainloop()

if __name__ == '__main__':
  main()
