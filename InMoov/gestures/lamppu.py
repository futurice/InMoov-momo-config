def lamppu():
  i01.startedGesture()

  fullspeed()
  rest()

  # right palm down
  i01.moveHand("right",0,0,0,0,0,161)

  # arm up
  i01.moveArm("right", 100, 104, 174, 115)

  # right thumb first
  print commands.getoutput('/bin/echo "1050,50,50,50,50" | /usr/bin/nc localhost 10000')

  sleep(1)

  # right hand fist
  print commands.getoutput('/bin/echo "1050,1000,1000,1000,1000" | /usr/bin/nc localhost 10000')

  sleep(5)

  momotalk("lamppu")

  sleep(1)

  # open hand and move a bit
  i01.moveArm("right", 80, 94, 164, 115)
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')

  sleep(3)

  rest()

  i01.finishedGesture()
