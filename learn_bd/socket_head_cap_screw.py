from build123d import MM
from bd_warehouse.fastener import SocketHeadCapScrew
from ocp_vscode import show, Camera

screw = SocketHeadCapScrew("M6-1", 20 * MM)
show(screw, names=["Socket Head Cap Screw"], reset_camera=Camera.CENTER)
