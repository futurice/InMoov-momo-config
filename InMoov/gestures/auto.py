def auto():
  i01.startedGesture()

# i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)
# i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)

# i01.setArmSpeed("left", 0.75, 0.75, 0.75, 0.75)
# i01.setArmSpeed("right", 0.75, 0.75, 0.75, 0.75)

  fullspeed()

  i01.moveHand("left",180,180,180,180,180)
  i01.moveHand("right",180,180,180,180,180)

  sleep(2)

  i01.moveArm("left", 180, 80, 110, 25)
  i01.moveArm("right", 180, 110, 60, 25)

  sleep(3)

  i01.moveArm("left", 180, 110, 60, 25)
  i01.moveArm("right", 180, 80, 110, 25)

  sleep(1)

  i01.moveArm("left", 180, 80, 110, 25)
  i01.moveArm("right", 180, 110, 60, 25)

  sleep(1)

  i01.moveArm("left", 180, 110, 60, 25)
  i01.moveArm("right", 180, 80, 110, 25)

  sleep(1)

  i01.moveArm("left", 0, 90, 0, 0)
  i01.moveArm("right", 0, 90, 0, 0) 

  sleep(3)

  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",0,0,0,0,0)

  i01.finishedGesture()
