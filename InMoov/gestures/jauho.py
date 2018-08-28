def jauho():
  i01.startedGesture()
  fullspeed()
  rest()

  # open hands
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')

  # right arm up first, goes higher, palm down
  i01.moveHand("right",180,180,180,180,180,155)
  i01.moveArm("right", 75, 73, 160, 129)
  sleep(1)

  # left arm up and palm up
  i01.moveHand("left",180,180,180,180,180,37)
  i01.moveArm("left", 58, 40, 146, 120)

  sleep(4)

  momotalk("jauho")

  sleep(1)

  print commands.getoutput('/bin/echo "950,1000,1000,950,950" | /usr/bin/nc localhost 10000')
  sleep(0.7)
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  sleep(0.7)
  print commands.getoutput('/bin/echo "950,1000,1000,950,950" | /usr/bin/nc localhost 10000')
  sleep(0.7)
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')

  sleep(2)

  rest()

  i01.finishedGesture()
