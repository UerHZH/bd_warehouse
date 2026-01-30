from build123d import MM
from bd_warehouse.fastener import RaisedCounterSunkOvalHeadScrew
from ocp_vscode import show, Camera

screw = RaisedCounterSunkOvalHeadScrew("M6-1", 20 * MM)
show(screw, names=["Raised CounterSunk Oval Head Screw"], reset_camera=Camera.CENTER)
