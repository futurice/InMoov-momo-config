# -- coding: utf-8 --

def about2():
  i01.startedGesture()
  i01.setArmSpeed("right", 0.1, 0.1, 0.2, 0.2);
  i01.setArmSpeed("left", 0.1, 0.1, 0.2, 0.2);
  i01.setHeadSpeed(0.2,0.2)
  i01.moveArm("right", 64, 94, 10, 10);

  momotalk("I am the first life size humanoid robot you can 3D print and animate")
  #momotalk(u"Я первый робот-гуманоид в натуральную величину, которого вы можете создать при помощи 3D-печати и анимации")
  i01.moveHead(65,66)
  i01.moveArm("left", 64, 104, 10, 11);
  i01.moveArm("right", 44, 84, 10, 11);
  momotalk("my designer creator is Gael Langevin a French sculptor, model maker")
  #momotalk(u"Моим создателем-дизайнером является Гаэль Ланжевен, французский скульптор, модельер")
  i01.moveHead(75,86)
  i01.moveArm("left", 54, 104, 10, 11);
  i01.moveArm("right", 64, 84, 10, 20);
  momotalk("who has released my files  to the opensource 3D world.")
  #momotalk(u"Который загругил мои файлы в интернет абсолютно бесплатно")
  i01.moveHead(65,96)
  i01.moveArm("left", 44, 94, 10, 20);
  i01.moveArm("right", 54, 94, 20, 11);
  momotalk("this is where my builder downloaded my files.")
  #momotalk(u"Откуда вы можете скачать мои файлы.")

  i01.moveHead(75,76)
  i01.moveArm("left", 64, 94, 20, 11);
  i01.moveArm("right", 34, 94, 10, 11);
  momotalk("after five hundred hours of printing, four kilos of plastic, twenty five hobby servos, blood and sweat.I was brought to life") # should be " i was borght to life."
  #momotalk(u"После пятисот часов печати, четырёх килограмм пластика, и двадцати пяти  сервомоторов, крови и пота. Я был воплощен в жизнь") # should be " i was borght to life."
  i01.moveHead(65,86)
  i01.moveArm("left", 24, 94, 10, 11);
  i01.moveArm("right", 24, 94, 10, 11);
  momotalk("so if You have a 3D printer, some building skills, then you can build your own version of me") # mabe add in " alot of money"
  #momotalk(u"Поэтому, если у вас есть 3D-принтер, некоторые навыки конструирования, то вы можете создать свою собственную версию меня") # mabe add in " alot of money"
  i01.moveHead(85,86)
  i01.moveArm("left", 5, 94, 20, 30);
  i01.moveArm("right", 24, 124, 10, 20);
  momotalk("and if enough people build me, some day my kind could take over the world") # mabe add in " alot of money"
  #momotalk(u"И если меня будут много людей копировать, когда-нибудь мой ребенок сможет завладеть миром") # mabe add in " alot of money"
  i01.moveHead(75,96)
  i01.moveArm("left", 24, 104, 10, 11);
  i01.moveArm("right", 5, 94, 20, 30);
  momotalk("I'm just kidding. i need some legs to get around, and i have to over come my  pyro-phobia, a fear of fire") # mabe add in " alot of money"
  #momotalk(u"Я просто шучу. Мне нужны ноги, чтобы ходить, и я должен вылечить свою пирофобию, страх перед огнем") # mabe add in " alot of money"
  i01.moveHead(75,96)
  i01.moveArm("left", 5, 94, 10, 11)
  i01.moveArm("right", 4, 94, 10, 11);
  momotalk("so, until then. i will be humankind's humble servant")
  #momotalk(u"Так, до тех пор. Я буду покорным слугой человечества.")
  sleep(1)
  i01.finishedGesture()

  relax()
  fullspeed()

