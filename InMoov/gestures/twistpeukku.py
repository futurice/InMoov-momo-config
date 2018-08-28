def twistpeukku():
  i01.startedGesture()

  fullspeed()

  # close right fist
  print commands.getoutput('/bin/echo "600,1000,1000,1000,1000" | /usr/bin/nc localhost 10000')

  # lift right arm and rotate wrist
  i01.moveArm("right", 100, 30, 140, 0)
  i01.moveHand("right",0,0,0,0,0,173)

  sleep(3)

  # extend thumb
  print commands.getoutput('/bin/echo "50,900,900,900,900" | /usr/bin/nc localhost 10000')

  # jingle()

  sleep(2)

  # close right fist
  print commands.getoutput('/bin/echo "600,900,900,900,900" | /usr/bin/nc localhost 10000')

  i01.moveHand("right",180,180,180,180,180,158)
  i01.moveHand("left",180,180,180,180,180,50)

  i01.moveArm("right", 20, 98, 90, 94)
  i01.moveArm("left", 8, 90, 90, 97)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')

  i01.finishedGesture()
