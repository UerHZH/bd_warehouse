from build123d import *
from build123d import MM, Location
from bd_warehouse.fastener import ThreadedHole, SocketHeadCapScrew
from ocp_vscode import show, Camera

# 1. Create a base plate
plate = Box(30 * MM, 30 * MM, 20 * MM)

# 2. Create the fastener reference
fastener = SocketHeadCapScrew("M6-1", 20 * MM)

# 3. Create the hole cutter
# ThreadedHole creates a hole with internal threads
# simple=False ensures the threads are actually modeled (not simplified)
hole_cutter = ThreadedHole(fastener, depth=15 * MM, simple=False)

# 4. Subtract the hole from the plate
# Position the hole at the center of the top face
hole_loc = Location((0, 0, 10 * MM))
part_with_hole = plate - hole_cutter.move(hole_loc)

# 5. Show the result
show(part_with_hole, names=["Plate with Threaded Hole"], reset_camera=Camera.CENTER)
