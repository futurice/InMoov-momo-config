def vasara():
  i01.startedGesture()

  fullspeed()

  # wrists to rest

  i01.moveHand("right",0,0,0,0,0,147)
  i01.moveHand("left",0,0,0,0,0,70)

  # right thumb first
  print commands.getoutput('/bin/echo "1050,50,50,50,50" | /usr/bin/nc localhost 10000')

  sleep(1)

  # right hand fist
  print commands.getoutput('/bin/echo "1050,1000,1000,1000,1000" | /usr/bin/nc localhost 10000')

  # hammer up
  i01.moveArm("right", 100, 110, 160, 0)

  sleep(4)

  momotalk("vasara")

  sleep(1)

  # hammer down
  i01.moveArm("right", 20, 110, 140, 0)

  sleep(0.7)

  # dup
  i01.moveArm("right", 100, 110, 160, 0)

  sleep(0.7)

  # down
  i01.moveArm("right", 20, 110, 140, 0)

  sleep(0.7)

  i01.moveArm("right", 55, 110, 140, 0)

  sleep(2)

  #rest
  i01.moveArm("right", 0, 90, 0, 0)
  i01.moveArm("left", 0, 90, 0, 0)

  sleep(1)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.finishedGesture()
