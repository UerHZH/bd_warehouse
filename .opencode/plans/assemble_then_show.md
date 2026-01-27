# Assemble First, Then Show

## Objective
The user wants to separate the "assembly" logic from the "show" logic in `learn_bd/assembly.py`. Currently, the components are moved *inside* the `show()` call. The goal is to perform the movements and assignments first, creating final "placed" objects, and then simply pass those objects to `show()`.

## Plan

1.  **Modify `learn_bd/assembly.py`**:
    *   Keep the component creation as is (`screw`, `washer`, `nut`).
    *   Define the locations (`washer_loc`, `nut_loc`) as they are.
    *   **Crucial Step**: Create new variables for the *placed* components.
        *   `washer_placed = washer.move(washer_loc)`
        *   `nut_placed = nut.move(nut_loc)`
    *   Update the `show()` call to use these new variables (`screw`, `washer_placed`, `nut_placed`).

## Verification
*   The script should run without errors.
*   The visualization in OCP CAD Viewer should be identical to the previous version (screw, washer, and nut correctly aligned).

## Example Code Structure

```python
# 1. Create
screw = ...
washer = ...
nut = ...

# 2. Assemble (Move)
washer_loc = Location(...)
nut_loc = Location(...)

# Create new "placed" objects
washer_placed = washer.move(washer_loc)
nut_placed = nut.move(nut_loc)

# 3. Show
show(screw, washer_placed, nut_placed, ...)
```
