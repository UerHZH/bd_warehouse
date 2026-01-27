from bd_warehouse.fastener import SquareNut
from ocp_vscode import show, Camera

nut = SquareNut("M6-1", simple=False)
show(nut, names=["Square Nut"], reset_camera=Camera.CENTER)
