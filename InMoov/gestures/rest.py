# ##############################################################################
#         ROBOT REST POSITIONS ( minimal )
# ##############################################################################

def rest():
  fullspeed()
  if isRightHandActivated:
    i01.rightHand.rest()
  
  if isLeftHandActivated:
    i01.leftHand.rest()
  
  if isRightArmActivated:
    i01.rightArm.rest()
  
  if isLeftArmActivated:
    i01.leftArm.rest()

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')
    
# ##############################################################################
#         ROBOT REST POSITIONS ( full )
# ##############################################################################    
  
  if isHeadActivated:
    i01.head.rest()
  
  if isTorsoActivated:
    i01.torso.rest()
    
  if isEyeLidsActivated:
    i01.eyelids.rest()
