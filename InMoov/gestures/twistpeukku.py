def twistpeukku():
  i01.startedGesture()

  fullspeed()

  # close right fist
  print commands.getoutput('/bin/echo "600,1000,1000,1000,1000" | /usr/bin/nc localhost 10000')

  sleep(1)

  # lift right arm and rotate wrist
  i01.moveArm("right", 100, 30, 140, 0)
  i01.moveHand("right",0,0,0,0,0,173)

  sleep(3)

  # extend thumb
  print commands.getoutput('/bin/echo "50,900,900,900,900" | /usr/bin/nc localhost 10000')

  jingle()

  sleep(3)

  # close right fist
  print commands.getoutput('/bin/echo "600,900,900,900,900" | /usr/bin/nc localhost 10000')

  sleep(1)

  rest()

  i01.finishedGesture()
