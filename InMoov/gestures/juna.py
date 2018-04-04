def juna():
  i01.startedGesture()

  fullspeed()

  # make a fist
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')

  # palm up (only the last digit matters)
  i01.moveHand("right",180,180,180,180,180,160)

  # arm up
  i01.moveArm("right", 180, 80, 100, 0)

  sleep(4)

  # fingers to train sign
  print commands.getoutput('/bin/echo "900,400,500,1000,1000" | /usr/bin/nc localhost 10000')

  sleep(2)

  # arm forward
  i01.moveArm("right", 30, 80, 150, 0)

  sleep(2)

  # arm back
  i01.moveArm("right", 180, 80, 100, 0)

  sleep(2)

  # arm forward
  i01.moveArm("right", 30, 80, 150, 0)

  sleep(3)

  #rest
  i01.moveArm("right", 0, 90, 0, 0)
  i01.moveHand("right",180,180,180,180,180,147)
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')

  i01.finishedGesture()
