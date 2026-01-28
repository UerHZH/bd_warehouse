from build123d import *
from bd_warehouse.fastener import InsertHole, HeatSetNut
from ocp_vscode import show, Camera

# 1. Create a base plate
plate = Box(30 * MM, 30 * MM, 20 * MM)

# 2. Create the fastener reference
fastener = HeatSetNut("M5-0.8-Standard")

# 3. Create the hole cutter
# InsertHole creates a hole sized for a heat-set insert (slightly tapered usually)
hole_cutter = InsertHole(fastener, depth=10 * MM)

# 4. Subtract the hole from the plate
# Position the hole at the center of the top face
part_with_hole = plate - hole_cutter.move(Location((0, 0, 10 * MM)))

# 5. Show the result
show(part_with_hole, names=["Plate with Insert Hole"], reset_camera=Camera.CENTER)
