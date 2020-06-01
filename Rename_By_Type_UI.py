import maya.cmds as cmds

mainWindow = None


def create_window(window_name):
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)

    global mainWindow
    mainWindow = cmds.window(window_name, title=window_name)

    cmds.showWindow(mainWindow)
    return mainWindow


def rename_by_type_window():

    edited_window = create_window("Rename_By_Type")
    cmds.window(edited_window, edit=True, title="Rename_By_Type", widthHeight=(300, 100))
    cmds.rowColumnLayout(nr=2, cat=(1, "both", 10), rs=(1, 10), rat=(1, "both", 10), ral=(1, "center"))
    cmds.text(label="You have to select at least ONE object to rename!")
    cmds.button(label="Rename", width=270, c=rename_obj_type)


def rename_obj_type(*args):

    selection = cmds.ls(selection=True, dag=True)
    selection.sort(key=len, reverse=True)

    if len(selection) == 0:
        print("You have to select at least ONE object to rename!")

    else:
        for i in selection:

            children = cmds.listRelatives(i, children=True, fullPath=True) or[]

            if len(children) == 1:
                child = children[0]
                type_obj = cmds.objectType(child)
            else:
                type_obj = cmds.objectType(i)

            suffix = get_suffix(type_obj)
            cmds.rename(i, (i + "_" + suffix))

    global mainWindow
    cmds.deleteUI(mainWindow)


rename_by_type_window()


def get_suffix(obj):

    switcher = {
        "mesh": "geo",
        "joint": "jnt",
        "nurbsCurve": "crv",
        "nurbsSurface": "surf",
        "directionalLight": "lgt",
        "ambientLight": "lgt",
        "pointLight": "lgt",
        "spotLight": "lgt",
        "areaLight": "lgt",
        "camera": "camera"
    }
    return switcher.get(obj, "grp")

