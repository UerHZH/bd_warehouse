from build123d import MM
from bd_warehouse.fastener import PanHeadScrew
from ocp_vscode import show, Camera

screw = PanHeadScrew("M6-1", 20 * MM, simple=False)
show(screw, names=["Pan Head Screw"], reset_camera=Camera.CENTER)
