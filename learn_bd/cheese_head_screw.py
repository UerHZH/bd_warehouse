from build123d import MM
from bd_warehouse.fastener import CheeseHeadScrew
from ocp_vscode import show, Camera

screw = CheeseHeadScrew("M6-1", 20 * MM, fastener_type='gb65')
show(screw, names=["Cheese Head Screw"], reset_camera=Camera.CENTER)
