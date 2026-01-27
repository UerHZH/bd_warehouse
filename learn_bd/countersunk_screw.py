from build123d import MM
from bd_warehouse.fastener import CounterSunkScrew
from ocp_vscode import show, Camera

screw = CounterSunkScrew("M6-1", 20 * MM, simple=False)
show(screw, names=["Countersunk Screw"], reset_camera=Camera.CENTER)
