from bd_warehouse.fastener import HeatSetNut
from ocp_vscode import show, Camera

nut = HeatSetNut("M5-0.8-Standard")
show(nut, names=["Heat Set Nut"], reset_camera=Camera.CENTER)
