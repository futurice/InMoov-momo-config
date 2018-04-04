def karamelli():
  i01.startedGesture()
  fullspeed()

  # make fists
  print commands.getoutput('/bin/echo "1000,1000,1000,1000,1000" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')

  # wrists in position
  i01.moveHand("right",180,180,180,180,180,150)
  i01.moveHand("left",180,180,180,180,180,69)
  sleep(4)

  # right arm up first, goes higher
  i01.moveArm("right", 90, 70, 146, 97)
  sleep(2)

  # left arm up
  i01.moveArm("left", 80, 62, 120, 90)

  sleep(3)
  
  # point the index and middle fingers
  print commands.getoutput('/bin/echo "1000,50,50,1000,1000" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,50,50,900,900" | /usr/bin/nc localhost 10001')
  
  sleep(3)

  # tap right hand against left hand
  i01.moveArm("right", 80, 70, 135, 97)
  sleep(1.5)

  # up
  i01.moveArm("right", 90, 70, 146, 97)
  sleep(1.5)

  # down
  i01.moveArm("right", 80, 70, 137, 97)
  sleep(3)

  # rest, take left hand down first

  i01.moveArm("left", 8, 90, 90, 90)
  sleep(1)

  i01.moveArm("right", 20, 90, 90, 97)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  sleep(2)

  i01.finishedGesture()
