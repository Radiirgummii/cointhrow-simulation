import random 
import choice
def progress_bar (progress, total):
  percent = 100 / (total / progress)
  bar = "#" * int(percent/2) + "-" * int((100 - percent) / 2)
  print("\r[" + bar + "]" + str(round(percent, 2)) + "%   " + str(progress) + "/" + str(total), end="\r")
  

i = 0
a = 0
print("Bitte Anzahl der Simulationsdurchläufe eingeben")
t = int(input())
kopf = 0
zahl = 0
beides = 0
while i != t:
  if random.choice([True, False]):
    if random.choice([True,False]):
      kopf = kopf + 1
      #print("kopf")
    else:
      beides = beides + 1
      #print("beides")
  else:
    if random.choice([True,False]):
      beides = beides + 1
      #print("beides")
    else:
      zahl = zahl + 1
      #print("zahl")
  i = i + 1 
  progress_bar(i, t)
print("\n\n\nZahl:   " + str(zahl) + "   " + str(100 / (t / zahl)) + "%" + "\nBeides: " + str(beides) + "   " + str(100 / (t / beides)) + "%" + "\nKopf:   " + str(kopf) + "   " + str(100 / (t / kopf)) + "%" )