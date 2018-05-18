def momotalk(line):
#  i01.startedGesture()
  # open mouth
  i01.head.jaw.moveTo(90)
  # start talking
  talk("[[rate 150; pbas -8]]"+line)
  # calculate how many seconds we keep the mouth open while the robot talks
  wait=len(line)/10.0  
  sleep(wait)
  # close mouth
  i01.head.jaw.moveTo(0)
#  i01.finishedGesture()
