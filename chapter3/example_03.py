from sys import exit
cnt = 0
def test():
  try:
    global cnt
    print(cnt)
    cnt += 1
    test()
  except RuntimeError as e:
    print("Caught an RuntimeError and the cnt is:\t%d" %cnt)
    exit(255)
test()
