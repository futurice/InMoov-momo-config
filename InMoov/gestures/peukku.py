def peukku():
  i01.startedGesture()

  fullspeed()

  # close right fist
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')  

  sleep(2)

  # lift right arm
  i01.moveArm("right", 180, 90, 105, 25)

  sleep(2)

  # extend thumb
  print commands.getoutput('/bin/echo "50,900,900,900,900" | /usr/bin/nc localhost 10000')
  
  sleep(5)

  # lower right arm
  i01.moveArm("right", 0, 90, 55, 25)

  sleep(2)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')

  sleep(2)

  i01.finishedGesture()
