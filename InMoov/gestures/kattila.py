def kattila():

  i01.startedGesture()

  fullspeed()
  rest()

  # make fists

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 20000')

  # palms a bit up

  i01.moveHand("right",180,180,180,180,180,163)
  i01.moveHand("left",180,180,180,180,180,51)

  # arms up

  i01.moveArm("left", 80, 84, 130, 90)
  i01.moveArm("right", 90, 90, 140, 97)

  sleep(5)
  
  momotalk("kattila")

  sleep(1.5)

  # do the shake

  i01.moveArm("left", 65, 84, 120, 90)
  i01.moveArm("right", 75, 90, 130, 97)

  sleep(0.5)

  i01.moveArm("left", 80, 84, 130, 90)
  i01.moveArm("right", 90, 90, 140, 97)

  sleep(0.5)

  i01.moveArm("left", 65, 84, 120, 90)
  i01.moveArm("right", 75, 90, 130, 97)

  sleep(0.5)

  i01.moveArm("left", 80, 84, 130, 90)
  i01.moveArm("right", 90, 90, 140, 97)

  sleep(0.5)

  i01.moveArm("left", 65, 84, 120, 90)
  i01.moveArm("right", 75, 90, 130, 97)

  sleep(2)

  rest()

  i01.finishedGesture()
