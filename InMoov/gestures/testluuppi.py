def testluuppi():

  rounds=0
  
  while True:
    rounds+=1

    momotalk2(str(rounds))
  
    if rounds > 10:
      break
  
    sleep(1)
