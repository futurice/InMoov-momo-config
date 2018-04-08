def lamppu():
  i01.startedGesture()

  fullspeed()

  # right palm down

  i01.moveHand("right",0,0,0,0,0,140)


  # right thumb first
  print commands.getoutput('/bin/echo "1050,50,50,50,50" | /usr/bin/nc localhost 10000')

  sleep(1)

  # right hand fist
  print commands.getoutput('/bin/echo "1050,1000,1000,1000,1000" | /usr/bin/nc localhost 10000')

  # arm up
  i01.moveArm("right", 100, 104, 174, 115)

  sleep(7)

  # open hand
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')

  sleep(3)

  #rest
  i01.moveArm("right", 0, 90, 0, 0)
  i01.moveArm("left", 0, 90, 0, 0)

  sleep(1)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.moveHand("right",0,0,0,0,0,147)

  i01.finishedGesture()
