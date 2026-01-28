# Fix ThreadedHole AttributeError

## Issue
The error `AttributeError: 'NoneType' object has no attribute 'locations'` occurs in `ThreadedHole.__init__` at line 3563:
`self.thread_locations = LocationList._get_context().locations`

This happens because `ThreadedHole` assumes it is being created inside a context (like `with BuildPart() ...` or `with Locations() ...`). When used in isolation as in the example script `learn_bd/threaded_hole.py`, `LocationList._get_context()` returns `None`, causing the crash.

## Solution
We need to modify `learn_bd/threaded_hole.py` (and similar scripts) to wrap the hole creation in a `BuildPart` context, OR modify `src/bd_warehouse/fastener.py` to handle the case where there is no active context.

Given the traceback implies a bug/limitation in how `ThreadedHole` handles standalone instantiation (it tries to access context locations blindly), the most robust fix for the library would be to patch `fastener.py`. However, as a user of the library, the immediate fix is to use the library as it expects: within a context.

BUT, I have permission to edit the codebase. The `fastener.py` logic seems flawed for standalone usage. It should check if the context exists before accessing `.locations`.

**Plan A: Patch `src/bd_warehouse/fastener.py`**
Modify line 3563 to default to a single location (identity) if no context is present.

```python
# Current
self.thread_locations = LocationList._get_context().locations

# Proposed
context = LocationList._get_context()
self.thread_locations = context.locations if context else [Location()]
```

**Plan B: Patch `learn_bd/threaded_hole.py`**
Wrap the creation in a context. This is less invasive but doesn't fix the underlying fragility of the library.

I will proceed with **Plan A** to make the library more robust, as `ThreadedHole` inherits from `BasePartObject` which is typically usable standalone.

## Steps
1.  Read `src/bd_warehouse/fastener.py` around line 3563.
2.  Apply the fix to safely access locations.
3.  Run `learn_bd/threaded_hole.py` (simulated check).

## Additional Check
I should also check if other hole types have similar issues. `ClearanceHole` and others seem to use `_make_fastener_hole` and standard `BasePartObject` init which usually handles context gracefully. `ThreadedHole` has this extra logic for `self.thread_locations`.

Wait, looking at `ThreadedHole` source read previously:
```python
03562|         self.thread = None if simple else thread
03563|         self.thread_locations = LocationList._get_context().locations
```
This line is indeed the culprit.

## Execution
I will edit `src/bd_warehouse/fastener.py`.
