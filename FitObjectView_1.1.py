import maya.cmds as cmds
jobNum = cmds.scriptJob( ct = ["SomethingSelected","cmds.viewFit(an = True),cmds.viewFit(c = True),cmds.viewFit( f=0.5 )"]),cmds.scriptJob( e= ["SelectionChanged","cmds.select( clear=True ),cmds.undo()"])
cmds.optionVar( fv=('totalAnimateRollTime', 0.4) )

##cmds.scriptJob(kill=jobNum)