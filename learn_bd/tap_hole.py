from build123d import *
from bd_warehouse.fastener import TapHole, SocketHeadCapScrew
from ocp_vscode import show, Camera

# 1. Create a base plate
plate = Box(30 * MM, 30 * MM, 20 * MM)

# 2. Create the fastener reference
fastener = SocketHeadCapScrew("M6-1", 20 * MM)

# 3. Create the hole cutter
# TapHole creates a hole sized for tapping (smaller than the nominal diameter)
hole_cutter = TapHole(fastener, material="Soft", depth=15 * MM)

# 4. Subtract the hole from the plate
# Position the hole at the center of the top face
part_with_hole = plate - hole_cutter.move(Location((0, 0, 10 * MM)))

# 5. Show the result
show(part_with_hole, names=["Plate with Tap Hole"], reset_camera=Camera.CENTER)
