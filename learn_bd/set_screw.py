from build123d import MM
from bd_warehouse.fastener import SetScrew
from ocp_vscode import show, Camera

screw = SetScrew("M6-1", 20 * MM)
show(screw, names=["Set Screw"], reset_camera=Camera.CENTER)
