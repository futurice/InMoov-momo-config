def ikiluuppi():

  from random import randint
  
  rounds=0
  
  # rest values: left bicep, left rotate, left shoulder, left omoplate
  
  rlb=8
  rlr=90
  rls=90
  rlo=90
  
  # rest values: right bicep, right rotate, right shoulder, right omoplate
  
  rrb=20
  rrr=90
  rrs=90
  rro=97
  
  # rest values: neck, rothead
  
  rn=60
  rr=90
  
  # rest values: left wrist, right wrist
  
  rlw=50
  rrw=170
  
  # rest value: torso
  rt=102
  
  # was a gesture running the last round?
  lastround=False
  
  while True:

    # if this one hits, a gesture is running, so we will skip a round
    if i01.RobotCanMoveRandom == False:
      lastround=True
      sleep(1)
      continue

    if lastround == True:
      lastround=False
      sleep(3)

    # these need to be here; if a gesture is run in middle, it will reset to fullspeed
    i01.setArmSpeed("right", 0.5, 0.5, 0.5, 0.5);
    i01.setArmSpeed("left", 0.5, 0.5, 0.5, 0.5);
    i01.setHeadSpeed(0.5, 0.5)
    # only the last value matters for hands
    i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.5)
    i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.5)
    # only first value matters for torso
    #i01.setTorsoSpeed(0.5, 0.5, 0.5)

    rounds+=1
  
    if randint(0,1) == 0:
      i01.moveArm("left", rlb + randint(0, 9), rlr + randint(0, 19), rls + randint(0, 9), rlo + randint(0, 6))
  
    if randint(0,1) == 0:
      i01.moveArm("right", rrb + randint(0, 9), rrr + randint(0, 19), rrs + randint(0, 9), rro + randint(0, 6))
  
    if randint(0,1) == 0:
      i01.head.rothead.moveTo(rr + randint(-20, 20))
  
    if randint(0,1) == 0:
      i01.head.neck.moveTo(rn + randint(-20, 20))
  
    if randint(0,1) == 0:
      i01.moveHand("right",180,180,180,180,180,rrw + randint(-3, 3))
  
    if randint(0,1) == 0:
      i01.moveHand("left",180,180,180,180,180,rlw + randint(-3, 3))
  
#   if randint(0,1) == 0:
#     i01.moveTorso(rt + randint(-2, 2),102,102)
  
#    if rounds > 20:
#      rest()
#      sleep(3)
#      break
  
    sleep(3)
