from build123d import MM
from bd_warehouse.fastener import RaisedCheeseHeadScrew
from ocp_vscode import show, Camera

screw = RaisedCheeseHeadScrew("M6-1", 20 * MM, simple=False)
show(screw, names=["Raised Cheese Head Screw"], reset_camera=Camera.CENTER)
