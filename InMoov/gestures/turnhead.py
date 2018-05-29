def turnhead(coords):
  i01.startedGesture()

  lcoords = coords.split('/')
  x = lcoords[0]
  y = lcoords[1]

  talk("x on "+str(x))
  talk("y on "+str(y))

  rothead = int(x) + 40;
  neck = int(y) + 10;

  if neck < 25 :
    neck = 25

  if neck > 115 :
    neck = 115

  talk("neck on " + str(neck))
  talk("rot on " + str(rothead))

  i01.finishedGesture()
