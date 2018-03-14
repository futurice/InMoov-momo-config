# -- coding: utf-8 --

def shakehand():
  rest()
  i01.startedGesture()
  ##move arm and hand
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(39,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  sleep(3)
  ##set hand up
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(90,90)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,60,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  i01.moveHand("right",80,70,70,50,50,77)
  ##ask chatbot to say something
  chatBot.getResponse("SYSTEM_SHAKE_HAND_GET_CLOSER")
   ##optional, detect if there is a human ( waiting finger sensor, we use ultrasonic distance as test )
  if ultraSonicSensorActivated:
    distance=200
    timeout=0
    timeoutGetCloser=0
    while (not distance or distance > 100): 
      timeout+=1
      timeoutGetCloser+=1
      distance=i01.getUltrasonicSensorDistance()
      print distance
      if timeout > 20:
        chatBot.getResponse("SYSTEM_SHAKE_HAND_NOHUMAN")
        sleep(2)
        shakehandFinish()
        break
      # ask GET CLOSER
      if timeoutGetCloser>6:
        chatBot.getResponse("SYSTEM_SHAKE_HAND_GET_CLOSER")
        timeoutGetCloser=0
        sleep(2)
      sleep(0.5)
      # great, human detected
    if distance<=100:shakehandAnimation()
  else:
    sleep(3)
    shakehandAnimation()

def shakehandAnimation():
  chatBot.getResponse("SYSTEM_SHAKE_HAND")
  ##close the hand
  i01.moveHand("right",180,125,135,145,168,77)
  sleep(1)
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.75, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(39,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,48,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,125,135,145,168,77)
  i01.moveTorso(95,95,90)
  sleep(3)
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.75, 0.75)
  i01.setTorsoSpeed(0.65, 0.55, 1.0)
  i01.moveHead(70,53)
  sleep(0.5)
  i01.moveHead(39,70)
  sleep(0.5)
  i01.moveHead(70,53)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,48,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,125,135,145,168,77)
  i01.moveTorso(95,95,90)
  sleep(1.5)
  ##shake hand up
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.65, 0.55, 1.0)
  i01.moveHead(80,53)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,60,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,125,135,145,168,77)
  i01.moveTorso(95,95,90)
  sleep(1)
  ##shake hand down
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.65, 0.55, 1.0)
  i01.moveHead(80,88)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,48,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,125,135,145,168,77)
  i01.moveTorso(95,95,90)
  sleep(1.5)
  ##shake hand up
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.65, 0.55, 1.0)
  i01.moveHead(80,53)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,60,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,125,135,145,168,77)
  i01.moveTorso(95,95,90)
  sleep(1)
  ##shake hand down
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(0.85, 0.85)
  i01.setTorsoSpeed(0.65, 0.55, 1.0)
  i01.moveHead(80,88)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,48,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,125,135,145,168,77)
  i01.moveTorso(95,95,90)
  sleep(1.5)
  ## release hand  
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.95, 0.95, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.65, 0.55, 1.0)
  i01.moveHead(39,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,45,16)
  i01.moveHand("left",50,50,40,20,20,77)
  i01.moveHand("right",20,30,30,20,20,90)
  i01.moveTorso(95,95,90)
  sleep(1)
  shakehandFinish()

def shakehandFinish():
  i01.finishedGesture()
  rest()
  relax()