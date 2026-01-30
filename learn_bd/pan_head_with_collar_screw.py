from build123d import MM
from bd_warehouse.fastener import PanHeadWithCollarScrew
from ocp_vscode import show, Camera

screw = PanHeadWithCollarScrew("M6-1", 20 * MM)
show(screw, names=["Pan Head With Collar Screw"], reset_camera=Camera.CENTER)
