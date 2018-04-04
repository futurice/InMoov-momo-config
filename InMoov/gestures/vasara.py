def vasara():
  i01.startedGesture()

  fullspeed()

  # wrists to rest
  
  i01.moveHand("right",0,0,0,0,0,147)
  i01.moveHand("left",0,0,0,0,0,70)

  # right hand fist
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')

  # hammer up
  i01.moveArm("right", 140, 110, 120, 0)

  sleep(3)

  # hammer down
  i01.moveArm("right", 40, 110, 120, 0)

  sleep(1)

  # dup
  i01.moveArm("right", 140, 110, 120, 0)

  sleep(1)

  # down
  i01.moveArm("right", 40, 110, 120, 0)

  sleep(1)

  #rest
  i01.moveArm("right", 0, 90, 0, 0)
  i01.moveArm("left", 0, 90, 0, 0)

  sleep(1)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.finishedGesture()
