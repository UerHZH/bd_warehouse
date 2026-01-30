from bd_warehouse.fastener import HexNutWithFlange
from ocp_vscode import show, Camera

nut = HexNutWithFlange("M6-1")
show(nut, names=["Hex Nut With Flange"], reset_camera=Camera.CENTER)
