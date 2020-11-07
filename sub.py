from time import sleep
from random import shuffle, sample, randint

from core import mWindow

class Dance:
  def __init__(self):
    """
    levelによってmove, vec, cmdの数が変わる
    move: 動かす部位
    vec : 動かす方向
    cmd : 対応する指令
    """
    self.place = [["body"], ["arm"], ["leg"]]
    self.vec  = ["↑", "↓", "←", "→"]
    self.cmd  = [["#ff0000", "#00ff00", "#0000ff", "#ffff00"],
                  ["1", "2", "3", "4"]]
    self.cmd=[[i[j] for i in self.cmd] for j in range(len(self.cmd))]
    # 描画
    self.window = mWindow()
    #self.window.mainloop()

  def move(self, alltime=300, onetime=1):
    self._shuffle()
    self.show_cmd()
    for i in range(int(alltime/onetime)):
      self.window.clear()
      p = sample(self.place, 1)[0]
      vcc = sample(self.iter, 1)[0]
      v, c = vcc[0], sample(vcc[1], 1)[0]
      self.window.pushstr(p)
      if c.startswith("#"):
        self.window.color(c)
      else:
        self.window.pushstr(c)
      sleep(onetime)

  def show_cmd(self):
    for v, c in self.iter:
      self.window.pushstr("{0}: {1[0]} or {1[1]}".format(v, c))
    #sleep(5)


  def _shuffle(self):
    shuffle(self.vec)
    shuffle(self.cmd)
    self.iter = [[i,j] for i,j in zip(self.vec, self.cmd)]



if __name__ == '__main__':
  Dance().move()
