from build123d import MM, Location
from bd_warehouse.fastener import PlainWasher, ChamferedWasher, InternalToothLockWasher
from ocp_vscode import show, Camera

# Create different types of washers
w1 = PlainWasher("M6", "gb97.1")
w2 = ChamferedWasher("M6", "iso7090").move(Location((20 * MM, 0, 0)))
w3 = InternalToothLockWasher("M6", "gb861.1").move(Location((40 * MM, 0, 0)))

show(
    w1, 
    w2, 
    w3, 
    names=["Plain Washer", "Chamfered Washer", "Lock Washer"], 
    reset_camera=Camera.CENTER
)
