from bd_warehouse.fastener import DomedCapNut
from ocp_vscode import show, Camera

nut = DomedCapNut("M6-1", simple=False)
show(nut, names=["Domed Cap Nut"], reset_camera=Camera.CENTER)
