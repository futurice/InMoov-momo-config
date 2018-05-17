def hiihto():
  i01.startedGesture()

  fullspeed()

  # wrists to rest

  i01.moveHand("left",180,180,180,180,180,50)
  i01.moveHand("right",180,180,180,180,180,167)

  # make fists

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 20000')

  sleep(2)

  # arms up

  i01.moveArm("left", 80, 84, 145, 115)
  i01.moveArm("right", 90, 90, 155, 122)

  sleep(4)

  momotalk("hiihto")

  sleep(1)

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

  rest()

  i01.finishedGesture()

