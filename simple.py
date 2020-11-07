from time import sleep
from random import randint, shuffle


def main():
  vec = ["↑","↓","→","←"]
  num = list(range(1,5))
  shuffle(vec)
  shuffle(num)
  for i,j in zip(vec, num):
    print("{0}: {1}".format(i, j))
  input()
  for i in range(30):
    index = randint(0,3)
    print(num[index])
    sleep(1)
    print(vec[index])
    sleep(2)
    print("\n"*30)


if __name__ == '__main__':
  main()
