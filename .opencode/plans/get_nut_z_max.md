# Get Max Z Coordinate of Nut

## Objective
The user wants to obtain the maximum Z coordinate of the `nut` object in `learn_bd/assembly.py` after it has been positioned.

## Approach
To do this correctly, we must ensure the object is moved to its final position *before* we query its coordinates.

1.  **Consolidate Transformations**:
    *   Currently, the code has `nut = nut.move(nut_loc)` but also tries to move it again in `show()`.
    *   I will finalize the positions for both `washer` and `nut` by assigning them to variables (e.g., `washer = washer.move(washer_loc)`).

2.  **Calculate Max Z**:
    *   Use the `.bounding_box()` method on the positioned `nut` object.
    *   Access `.max.Z` from the bounding box.
    *   Code: `nut_z_max = nut.bounding_box().max.Z`

3.  **Print Result**:
    *   Add a print statement to display the value.

4.  **Update Visualization**:
    *   Pass the already-moved objects to `show()` to avoid applying the transformation twice.

## Proposed Code Changes for `learn_bd/assembly.py`

```python
from build123d import MM, Location
from bd_warehouse.fastener import SocketHeadCapScrew, PlainWasher, HexNut
from ocp_vscode import show, Camera

# 1. Create components
screw = SocketHeadCapScrew("M6-1", 30 * MM, simple=False)
washer = PlainWasher("M6", "iso7089")
nut = HexNut("M6-1", simple=False)

# 2. Position components
washer_loc = Location((0, 0, -25 * MM))
nut_loc = Location((0, 0, -28 * MM))

# Apply movement
washer = washer.move(washer_loc)
nut = nut.move(nut_loc)

# 3. Get Z Max
# bounding_box() returns the axis-aligned bounding box of the object
# .max returns the corner with maximum X, Y, and Z values
nut_max_z = nut.bounding_box().max.Z
print(f"Nut max Z position: {nut_max_z}")

# 4. Show
show(
    screw, 
    washer, 
    nut, 
    names=["Screw", "Washer", "Nut"], 
    reset_camera=Camera.CENTER
)
```
