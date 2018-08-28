def palmsup():
  i01.startedGesture()

  fullspeed()

  i01.moveHand("right",180,180,180,180,180,168)
  i01.moveHand("left",180,180,180,180,180,45)

  i01.setArmSpeed("right", 0.85, 0.85, 0.85, 0.85);
  i01.setArmSpeed("left", 0.85, 0.85, 0.85, 0.85);

  i01.moveArm("right", 100, 98, 90, 94)
  i01.moveArm("left", 90, 90, 90, 97)

  sleep(3)

  i01.setArmSpeed("right", 0.7, 0.7, 0.7, 0.7);
  i01.setArmSpeed("left", 0.7, 0.7, 0.7, 0.7);

  i01.moveHand("right",180,180,180,180,180,158)
  i01.moveHand("left",180,180,180,180,180,50)

  i01.moveArm("right", 20, 98, 90, 94)
  i01.moveArm("left", 8, 90, 90, 97)

  sleep(2)

  i01.finishedGesture()
