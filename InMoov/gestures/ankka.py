def ankka():

  i01.startedGesture()

  fullspeed()

  # make fists

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')

  # palms down
  
  i01.moveHand("right",180,180,180,180,180,157)
  i01.moveHand("left",180,180,180,180,180,60)

  # arms up

  i01.moveArm("left", 80, 84, 130, 90)
  i01.moveArm("right", 90, 90, 140, 97)

  sleep(4)

  momotalk("ankka")

  sleep(1)

  # do the shake

  i01.moveArm("left", 65, 84, 120, 90)
  i01.moveArm("right", 90, 90, 140, 97)


  sleep(0.5)

  i01.moveArm("left", 80, 84, 130, 90)
  i01.moveArm("right", 75, 90, 130, 97)

  sleep(0.5)

  i01.moveArm("left", 65, 84, 120, 90)
  i01.moveArm("right", 90, 90, 140, 97)

  sleep(0.5)

  i01.moveArm("left", 80, 84, 130, 90)
  i01.moveArm("right", 75, 90, 130, 97)

  sleep(0.5)

  i01.moveArm("left", 65, 84, 120, 90)
  i01.moveArm("right", 90, 90, 140, 97)

  sleep(2)

  # rest

  i01.moveArm("left", 8, 90, 90, 90)
  i01.moveArm("right", 20, 90, 90, 97)

  i01.moveHand("right",180,180,180,180,180,167)
  i01.moveHand("left",180,180,180,180,180,50)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')

  sleep(2)

  i01.finishedGesture()
