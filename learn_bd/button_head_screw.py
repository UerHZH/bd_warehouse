from build123d import MM
from bd_warehouse.fastener import ButtonHeadScrew
from ocp_vscode import show, Camera

screw = ButtonHeadScrew("M6-1", 20 * MM, simple=False)
show(screw, names=["Button Head Screw"], reset_camera=Camera.CENTER)
