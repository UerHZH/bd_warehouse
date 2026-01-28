# Enable Threads in Fastener Examples

## Objective
The user cannot see threads in the OCP CAD Viewer because the fasteners are created with `simple=True` by default, which simplifies the geometry for performance. To fix this, I will modify the example scripts to explicitly set `simple=False` for relevant fasteners.

## Files to Modify

### 1. `examples/fasteners_assembly.py`

**Current State:**
- Creates `SocketHeadCapScrew`, `CounterSunkScrew`, and `HexNut` using default parameters (`simple=True`).

**Proposed Changes:**
- Update all fastener instantiations to include `simple=False`.

**Details:**
- `screw1 = SocketHeadCapScrew("M6-1", 25 * MM, simple=False)`
- `screw2 = SocketHeadCapScrew("M6-1", 25 * MM, simple=False)`
- `screw3 = CounterSunkScrew("M5-0.8", 20 * MM, simple=False)`
- `nut1 = HexNut("M6-1", simple=False)`
- `nut2 = HexNut("M6-1", simple=False)`

### 2. `examples/fasteners_demo.py`

**Current State:**
- Creates ~20 fasteners using default parameters (`simple=True`).

**Proposed Changes:**
- Update specific examples to `simple=False` to demonstrate threads without significantly impacting script runtime (generating threads is computationally expensive).
- Update the final assembly section to use threaded components.

**Details:**
- Update first `HexNut` example: `hex_nut = HexNut("M6-1", simple=False)`
- Update first `SocketHeadCapScrew` example: `socket_cap = SocketHeadCapScrew("M5-0.8", 16 * MM, simple=False)`
- Update final assembly components:
    - `screw = SocketHeadCapScrew("M6-1", 30 * MM, simple=False)`
    - `nut = HexNut("M6-1", simple=False)`

## Verification
- Review the code to ensuring `simple=False` is passed correctly.
- (Implicit) Running the script should now produce detailed threaded models in the viewer.
