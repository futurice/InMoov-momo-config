def auto():
  i01.startedGesture()

  fullspeed()

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')

  sleep(1)

  i01.moveArm("right", 180, 95, 85, 0)
  i01.moveArm("left", 180, 95, 85, 0)

  sleep(2)

  i01.moveArm("left", 120, 80, 100, 0)
  i01.moveArm("right", 130, 110, 70, 0)
  i01.moveHand("left", 0, 0, 0, 0, 0, 75)
  i01.moveHand("right", 0, 0, 0, 0, 0, 152)
    
  sleep(2)

  i01.moveArm("left", 80, 110, 70, 0)
  i01.moveArm("right", 180, 80, 100, 0)
  i01.moveHand("left", 0, 0, 0, 0, 0, 65)
  i01.moveHand("right", 0, 0, 0, 0, 0, 142)

  sleep(2)

  i01.moveArm("left", 120, 80, 100, 0)
  i01.moveArm("right", 130, 110, 70, 0)
  i01.moveHand("left", 0, 0, 0, 0, 0, 75)
  i01.moveHand("right", 0, 0, 0, 0, 0, 152)

  sleep(2)

  i01.moveArm("left", 80, 110, 70, 0)
  i01.moveArm("right", 180, 80, 100, 0)
  i01.moveHand("left", 0, 0, 0, 0, 0, 65)
  i01.moveHand("right", 0, 0, 0, 0, 0, 142)


  sleep(1)

  # rest
  
  i01.moveArm("left", 0, 90, 0, 0)
  i01.moveArm("right", 0, 90, 0, 0)

  i01.moveHand("left", 0, 0, 0, 0, 0, 70)
  i01.moveHand("right", 0, 0, 0, 0, 0, 147)

  sleep(2)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.finishedGesture()
