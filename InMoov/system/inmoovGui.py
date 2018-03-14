

###############################################################################
#                 inmoov.fr connector
###############################################################################

#service configuration
####################
#inmoovfrUrl="http://inmoov.fr/wp-content/themes/klein/"
#if glob.glob(RuningFolder+'*.key'):
#  key=os.path.basename(glob.glob(RuningFolder+'*.key')[0]).split('.key', 1 )[0]
#  iHaveInmoovFrKey=1

#log function
#################### 
def logIt(file,txt,method):
  with open(file,method) as filelog:
    filelog.write(txt+" \n")
logIt(RuningFolder+"system/inmoov.fr.log","Good evening Dave, ","w")    

#config files update
####################
def getInmoovFrParameter(parameter,output):
  logIt(RuningFolder+"system/inmoov.fr.log","Tried to contact InMoovCloud? No way Jose","a")
