from build123d import MM
from bd_warehouse.fastener import HexHeadWithFlangeScrew
from ocp_vscode import show, Camera

screw = HexHeadWithFlangeScrew("M6-1", 20 * MM, simple=False)
show(screw, names=["Hex Head With Flange Screw"], reset_camera=Camera.CENTER)
