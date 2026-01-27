from build123d import MM
from bd_warehouse.fastener import HexHeadScrew
from ocp_vscode import show, Camera

screw = HexHeadScrew("M6-1", 20 * MM, simple=False)
show(screw, names=["Hex Head Screw"], reset_camera=Camera.CENTER)
