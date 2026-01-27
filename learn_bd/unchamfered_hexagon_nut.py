from bd_warehouse.fastener import UnchamferedHexagonNut
from ocp_vscode import show, Camera

nut = UnchamferedHexagonNut("M6-1", simple=False)
show(nut, names=["Unchamfered Hexagon Nut"], reset_camera=Camera.CENTER)
