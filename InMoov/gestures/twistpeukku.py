def twistpeukku():
  i01.startedGesture()

  fullspeed()

  # close right fist
  print commands.getoutput('/bin/echo "600,900,900,900,900" | /usr/bin/nc localhost 10000')

  sleep(1)

  # lift right arm and rotate wrist
  i01.moveArm("right", 180, 29, 94, 0)
  i01.moveHand("right",0,0,0,0,0,153)

  sleep(3)

  # extend thumb
  print commands.getoutput('/bin/echo "50,900,900,900,900" | /usr/bin/nc localhost 10000')

  sleep(3)

  # close right fist
  print commands.getoutput('/bin/echo "600,900,900,900,900" | /usr/bin/nc localhost 10000')

  # lower right arm
  i01.moveArm("right", 0, 90, 0, 0)
  i01.moveHand("right",0,0,0,0,0,147)
  sleep(2)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')

  i01.finishedGesture()
