def auto():
  i01.startedGesture()

  fullspeed()

  print commands.getoutput('/bin/echo "1000,1000,1000,1000,1000" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "1000,1000,1000,1000,1000" | /usr/bin/nc localhost 10001')

  sleep(1)

  i01.moveArm("right", 80, 85, 135, 90)
  i01.moveArm("left", 80, 70, 120, 97)

  sleep(4)

  i01.moveArm("right", 100, 85, 135, 90)
  i01.moveHand("right", 0, 0, 0, 0, 0, 142)

  i01.moveArm("left", 60, 70, 120, 97)
  i01.moveHand("left", 0, 0, 0, 0, 0, 65)

  sleep(1.5)

  i01.moveArm("right", 60, 85, 135, 0)
  i01.moveHand("right", 0, 0, 0, 0, 0, 149)

  i01.moveArm("left", 100, 70, 120, 0)
  i01.moveHand("left", 0, 0, 0, 0, 0, 75)

  sleep(1.5)

    
  i01.moveArm("right", 100, 85, 135, 90)
  i01.moveHand("right", 0, 0, 0, 0, 0, 142)

  i01.moveArm("left", 60, 70, 120, 97)
  i01.moveHand("left", 0, 0, 0, 0, 0, 65)


  sleep(1.5)

  i01.moveArm("right", 60, 85, 135, 0)
  i01.moveHand("right", 0, 0, 0, 0, 0, 149)

  i01.moveArm("left", 100, 70, 120, 0)
  i01.moveHand("left", 0, 0, 0, 0, 0, 75)

  sleep(1.5)

  # rest

  i01.moveArm("left", 8, 90, 90, 90)
  i01.moveArm("right", 20, 90, 90, 97)

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.finishedGesture()
