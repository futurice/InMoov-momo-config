def karamelli():

  i01.startedGesture()

  fullspeed()

  # make fists

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')

  # wrists in position

  i01.moveHand("right",180,180,180,180,180,115)
  i01.moveHand("left",180,180,180,180,180,90)  

  # right arm up first, goes higher

  i01.moveArm("right", 150, 65, 148, 0)

  sleep(1)

  # left arm up
  
  i01.moveArm("left", 150, 100, 94, 0)

  sleep(4)

  # point the index and middle fingers

  print commands.getoutput('/bin/echo "900,50,50,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,50,50,900,900" | /usr/bin/nc localhost 10001')

  sleep(2)

  # tap right hand against left hand

  i01.moveArm("right", 110, 65, 148, 0)

  sleep(1)

  # up

  i01.moveArm("right", 150, 65, 148, 0)

  sleep(1)

  # down

  i01.moveArm("right", 110, 65, 148, 0)

  sleep(3)  

  # rest, take left hand down first 

  i01.moveArm("left", 0, 90, 0, 0)

  sleep(1)
  
  i01.moveArm("right", 0, 90, 0, 0)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')
 
  i01.moveHand("right",180,180,180,180,180,90)
  i01.moveHand("left",180,180,180,180,180,90)

  sleep(2)

  i01.finishedGesture()
