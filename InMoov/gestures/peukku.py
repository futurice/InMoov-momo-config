def peukku():
  i01.startedGesture()

  fullspeed()

  # close right fist
  print commands.getoutput('/bin/echo "600,1000,1000,1000,1000" | /usr/bin/nc localhost 10000')

  sleep(1)

  # lift right arm
  i01.moveArm("right", 100, 85, 115, 90)
  i01.moveHand("right",180,180,180,180,180,150)

  i01.setArmVelocity("right", 50, -1, -1, -1)
  
  sleep(3)

  # extend thumb
  print commands.getoutput('/bin/echo "50,1000,1000,1000,1000" | /usr/bin/nc localhost 10000')
  i01.moveArm("right", 40, 80, 165, 0)

  sleep(5)

  print commands.getoutput('/bin/echo "1000,1000,1000,1000,1000" | /usr/bin/nc localhost 10000')

  sleep(1)
  # rest

  i01.moveArm("left", 8, 90, 90, 90)
  i01.moveArm("right", 20, 90, 90, 97)

  sleep(1)

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.finishedGesture()
