# Fix Clearance Hole Visualization

## Issue
The user provided a screenshot showing that `ClearanceHole` generates a solid cylinder (the shape of the hole cutter/negative volume) rather than an actual hole in a part. This is expected behavior because `ClearanceHole` in `bd_warehouse` (and `build123d`) is a tool object designed to be subtracted from another part. When viewed in isolation, it looks like a solid "plug".

## Solution
To demonstrate what a `ClearanceHole` actually does, I need to create a base part (e.g., a simple Box or Plate) and then *subtract* the `ClearanceHole` object from it.

## Plan for `learn_bd/clearance_hole.py`

1.  **Create a Base Part**: Create a `Box` representing a plate.
2.  **Define the Hole**: Create the `ClearanceHole` object as before.
3.  **Apply the Hole**: Subtract the hole from the box using the `-` operator or `mode=Mode.SUBTRACT` within a `BuildPart` context.
4.  **Visualize**: Show the resulting plate with the hole in it.

I will also update the other hole examples (`tap_hole.py`, `threaded_hole.py`, `insert_hole.py`) to follow this pattern, as they all share the same behavior.

## Updated Code Structure

```python
from build123d import *
from bd_warehouse.fastener import ClearanceHole, SocketHeadCapScrew
from ocp_vscode import show, Camera

# 1. Create a base plate
plate = Box(30 * MM, 30 * MM, 10 * MM)

# 2. Create the fastener reference
fastener = SocketHeadCapScrew("M6-1", 20 * MM)

# 3. Create the hole cutter
# Note: In a standalone context, this is just the "negative" shape.
hole_cutter = ClearanceHole(fastener, fit="Normal", depth=20 * MM)

# 4. Subtract the hole from the plate
# Position the hole at the center of the top face
part_with_hole = plate - hole_cutter.move(Location((0, 0, 5 * MM)))

# 5. Show the result
show(part_with_hole, names=["Plate with Clearance Hole"], reset_camera=Camera.CENTER)
```
