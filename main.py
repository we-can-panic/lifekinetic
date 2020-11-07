# lifekineticに着想した体の動きを交えた脳トレ
from sub import *


def main():
  # DANCE
  # 一回onetime秒で指定された動きをし、それをalltime秒繰り返す
  alltime = 300
  onetime = 3
  dance = Dance()
  dance.move(alltime, onetime)


if __name__ == '__main__':
  main()
