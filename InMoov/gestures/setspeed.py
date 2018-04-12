def setspeed():
  i01.startedGesture()
# slow down some movements
  i01.head.jaw.setVelocity(100)
  i01.head.rothead.setVelocity(40)
  i01.head.neck.setVelocity(40)
  i01.finishedGesture()
