from bd_warehouse.fastener import HexNut
from ocp_vscode import show, Camera

nut = HexNut("M5-0.8", simple=False)
show(nut, names=["Hex Nut"], reset_camera=Camera.CENTER)