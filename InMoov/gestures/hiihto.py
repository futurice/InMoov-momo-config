def hiihto():
  i01.startedGesture()

  fullspeed()

  # wrists to rest

  i01.moveHand("left",180,180,180,180,180,70)
  i01.moveHand("right",180,180,180,180,180,147)

  # make fists

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')

  sleep(2)

  # arms up

  i01.moveArm("left", 80, 84, 145, 115)
  i01.moveArm("right", 90, 90, 155, 122)

  sleep(2)

  # pump arms down

  i01.moveArm("left", 10, 84, 90, 100)
  i01.moveArm("right", 20, 90, 90, 105)

  sleep(2)

  # up

  i01.moveArm("left", 80, 84, 145, 115)
  i01.moveArm("right", 90, 90, 155, 122)

  sleep(2)

  # down
  
  i01.moveArm("left", 10, 84, 90, 100)
  i01.moveArm("right", 20, 90, 90, 105)

  sleep(2)

  # rest

  i01.moveArm("left", 8, 90, 90, 90)
  i01.moveArm("right", 20, 90, 90, 97)

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.finishedGesture()
