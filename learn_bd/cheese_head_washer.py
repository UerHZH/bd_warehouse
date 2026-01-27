from bd_warehouse.fastener import CheeseHeadWasher
from ocp_vscode import show, Camera

washer = CheeseHeadWasher("M6", "iso7092")
show(washer, names=["Cheese Head Washer"], reset_camera=Camera.CENTER)
