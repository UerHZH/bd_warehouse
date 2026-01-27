from build123d import MM
from bd_warehouse.fastener import LowProfileScrew
from ocp_vscode import show, Camera

screw = LowProfileScrew("M5-0.8", 20 * MM, simple=False)
show(screw, names=["Low Profile Screw"], reset_camera=Camera.CENTER)
