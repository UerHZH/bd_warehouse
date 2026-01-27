from build123d import MM, Location
from bd_warehouse.fastener import SocketHeadCapScrew, PlainWasher, HexNut
from ocp_vscode import show, Camera

# 1. Create components
# simple=False generates threads for realistic visualization
screw = SocketHeadCapScrew("M6-1", 30 * MM, simple=False)
washer = PlainWasher("M6", "iso7089")
nut = HexNut("M6-1", simple=False)

# 2. Position components
# Move washer to the end of the screw (approximate position)
washer_loc = Location((0, 0, -25 * MM))
# Move nut below the washer
nut_loc = Location((0, 0, -28 * MM))

nut = nut.move(nut_loc)
nut_z_max = nut.bounding_box().max.Z

washer_loc = Location((0, 0, nut_z_max))
washer = washer.move(washer_loc)
# 3. Show
show(
    screw, 
    washer, 
    nut, 
    names=["Screw", "Washer", "Nut"], 
    reset_camera=Camera.CENTER
)
