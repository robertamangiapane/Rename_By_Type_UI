import maya.cmds as cmds

mainWindow = None

def CreateWindow(windowName):
    if cmds.window(windowName, exists=True):
        cmds.deleteUI(windowName)

    global mainWindow
    mainWindow = cmds.window(windowName, title=windowName)

    cmds.showWindow(mainWindow)
    return mainWindow

def RenameByTypeUI():

    editedWindow = CreateWindow("Rename By Type")
    cmds.window(editedWindow, edit=True, title="Rename By Type", widthHeight=(300, 100))
    cmds.rowColumnLayout(nr=2, cat=(1, "both", 10), rs=(1, 10), rat=(1, "both", 10), ral=(1, "center"))
    cmds.text(label="You have to select at least ONE object to rename!")
    cmds.button(label="Rename", width=270, c=GetObjType)


def GetObjType(*args):

    selection = cmds.ls(selection=True, dag=True)
    selection.sort(key=len, reverse=True)

    if len(selection) == 0:
        print "You have to select at least ONE object to rename!"

    for i in selection:

        children = cmds.listRelatives(i, children=True, fullPath=True) or[]

        if len(children) == 1:
            child= children[0]
            typeObj = cmds.objectType(child)
        else:
            typeObj = cmds.objectType(i)


        if typeObj == "mesh":
            suffix = "geo"
        elif typeObj == "joint":
            suffix = "jnt"
        elif typeObj == "camera":
            continue
        elif typeObj == "nurbsCurve":
            suffix = "crv"
        elif typeObj == "directionalLight":
            suffix = "lgt"
        elif typeObj == "ambientLight":
            suffix = "lgt"
        elif typeObj == "pointLight":
            suffix = "lgt"
        elif typeObj == "spotLight":
            suffix = "lgt"
        elif typeObj == "areaLight":
            suffix = "lgt"
        elif typeObj == "nurbsSurface":
            suffix = "surfc"
        else:
            suffix = "grp"

        cmds.rename(i,(i+"_"+suffix))



RenameByTypeUI()

