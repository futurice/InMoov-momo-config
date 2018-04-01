def hiihto():
  i01.startedGesture()

# i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)
# i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)

# i01.setArmSpeed("left", 0.75, 0.75, 0.75, 0.75)
# i01.setArmSpeed("right", 0.75, 0.75, 0.75, 0.75)

  fullspeed()

  i01.moveHand("left",180,180,180,180,180,90)
  i01.moveHand("right",180,180,180,180,180,90)
  
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')  
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')  

  sleep(2)

  i01.moveArm("left", 180, 90, 105, 25)
  i01.moveArm("right", 180, 90, 105, 25)

  sleep(2)

  i01.moveArm("left", 0, 90, 55, 25)
  i01.moveArm("right", 0, 90, 55, 25)

  sleep(2)

  i01.moveArm("left", 180, 90, 105, 25)
  i01.moveArm("right", 180, 90, 105, 25)

  sleep(2)

  i01.moveArm("left", 0, 90, 55, 25)
  i01.moveArm("right", 0, 90, 55, 25)

  sleep(2)

  i01.moveArm("left", 0, 90, 0, 0)
  i01.moveArm("right", 0, 90, 0, 0) 

  sleep(2)

#  i01.moveHand("left",0,0,0,0,0)
#  i01.moveHand("right",0,0,0,0,0)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.finishedGesture()
