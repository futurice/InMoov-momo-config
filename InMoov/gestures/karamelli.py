def karamelli():
  i01.startedGesture()
  fullspeed()

  # make fists
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')

  # wrists in position
  i01.moveHand("right",180,180,180,180,180,150)
  i01.moveHand("left",180,180,180,180,180,69)
  sleep(5)

  # right arm up first, goes higher
  i01.moveArm("right", 125, 64, 152, 0)
  sleep(2)
 
  # left arm up
  i01.moveArm("left", 120, 92, 80, 1)
  sleep(4)

  # point the index and middle fingers
  print commands.getoutput('/bin/echo "900,50,50,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,50,50,900,900" | /usr/bin/nc localhost 10001')
  sleep(5)

  # tap right hand against left hand
  i01.moveArm("right", 104, 57, 148, 0)
  sleep(1)

  # up
  i01.moveArm("right", 125, 64, 152, 0)
  sleep(1)

  # down
  i01.moveArm("right", 104, 57, 148, 0)
  sleep(3)

  # rest, take left hand down first
  
  i01.moveArm("left", 0, 90, 0, 0)
  sleep(1)

  i01.moveArm("right", 0, 90, 0, 0)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  sleep(2)

  i01.finishedGesture()
