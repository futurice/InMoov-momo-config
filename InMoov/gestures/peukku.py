def peukku():
  i01.startedGesture()

  fullspeed()

  # close right fist
  print commands.getoutput('/bin/echo "600,900,900,900,900" | /usr/bin/nc localhost 10000')  

  sleep(1)

  # lift right arm
  i01.moveArm("right", 180, 90, 90, 25)

  sleep(3)

  # extend thumb
  print commands.getoutput('/bin/echo "50,900,900,900,900" | /usr/bin/nc localhost 10000')
  
  sleep(5)

  # lower right arm
  i01.moveArm("right", 0, 90, 0, 0)

  sleep(2)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')

  sleep(2)

  i01.finishedGesture()
