from build123d import MM
from bd_warehouse.fastener import ButtonHeadWithCollarScrew
from ocp_vscode import show, Camera

screw = ButtonHeadWithCollarScrew("M6-1", 20 * MM, simple=False)
show(screw, names=["Button Head With Collar Screw"], reset_camera=Camera.CENTER)
