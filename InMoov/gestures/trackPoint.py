def trackPoint():
  if (i01.RobotIsOpenCvCapturing()):
    i01.opencv.removeFilter("Gray")
    i01.opencv.removeFilter("PyramidDown")
    i01.opencv.removeFilter("FaceRecognizer")
  i01.startHeadTracking("leftPort",12,13)
  #i01.startEyesTracking("leftPort",22,24)
  #i01.eyesTracking.pid.setPID("x",eyeXPidKp,eyeXPidKi,eyeXPidKd)
  #i01.eyesTracking.pid.setPID("y",eyeYPidKp,eyeYPidKi,eyeYPidKd)
  i01.headTracking.pid.setPID("x",rotheadPidKp,rotheadPidKi,rotheadPidKd)
  i01.headTracking.pid.setPID("y",neckPidKp,neckPidKi,neckPidKd)
  sleep(1)
  i01.headTracking.startLKTracking()
  #i01.eyesTracking.startLKTracking()
  i01.setHeadVelocity(80, -1)
  i01.head.rollNeck.setOverrideAutoDisable(True)
  i01.head.rollNeck.moveToBlocking(90)
  sleep(1)
  fullspeed()
