"""
Advanced Fastener Assembly Example - Bracket with Fastened Connections

This example demonstrates how to create a practical mechanical assembly with:
- A mounting bracket
- Multiple fastened connections using different fastener types
- Proper alignment and positioning of fasteners
"""

import timeit
from ocp_vscode import show, Camera
from build123d import *
from bd_warehouse.fastener import (
    SocketHeadCapScrew,
    HexNut,
    PlainWasher,
    CounterSunkScrew,
)

print("=" * 70)
print("ADVANCED FASTENER ASSEMBLY - MOUNTING BRACKET")
print("=" * 70)

# ============================================================================
# 1. CREATE THE BASE BRACKET
# ============================================================================
print("\n1. Creating mounting bracket...")
starttime = timeit.default_timer()

bracket = Box(100 * MM, 80 * MM, 10 * MM)

# Create mounting holes
hole_positions = [
    (20 * MM, 20 * MM, 0),
    (80 * MM, 20 * MM, 0),
    (50 * MM, 60 * MM, 0),
]

with BuildPart() as fastener_holes:
    add(bracket)
    for x, y, z in hole_positions:
        with Locations((x, y, z)):
            Hole(5.5 * MM, depth=10 * MM)

bracket = fastener_holes.part
elapsed = timeit.default_timer() - starttime
print(f"   Bracket created: {elapsed:.3f}s")
print(f"   - Dimensions: 100 x 80 x 10 mm")
print(f"   - 3 mounting holes (M6 clearance holes)")

# ============================================================================
# 2. CREATE FASTENED ASSEMBLY
# ============================================================================
print("\n2. Creating fastened assembly...")

# Socket Head Cap Screws at positions 1 and 2
screw1 = SocketHeadCapScrew("M6-1", 25 * MM, simple=False).move(Location((20 * MM, 20 * MM, -10 * MM)))
screw2 = SocketHeadCapScrew("M6-1", 25 * MM, simple=False).move(Location((80 * MM, 20 * MM, -10 * MM)))

# Countersunk screw at position 3
screw3 = CounterSunkScrew("M5-0.8", 20 * MM, simple=False).move(Location((50 * MM, 60 * MM, 10 * MM)))

# Washers for socket head cap screws
washer1 = PlainWasher("M6", "iso7089").move(Location((20 * MM, 20 * MM, -10.1 * MM)))
washer2 = PlainWasher("M6", "iso7089").move(Location((80 * MM, 20 * MM, -10.1 * MM)))

# Nuts for socket head cap screws
nut1 = HexNut("M6-1", simple=False).move(Location((20 * MM, 20 * MM, -15 * MM)))
nut2 = HexNut("M6-1", simple=False).move(Location((80 * MM, 20 * MM, -15 * MM)))

elapsed = timeit.default_timer() - starttime
print(f"   Assembly created: {elapsed:.3f}s")

# ============================================================================
# 3. COMBINE COMPONENTS
# ============================================================================
print("\n3. Combining components into complete assembly...")
starttime = timeit.default_timer()

# Assemble all components
assembly = bracket + screw1 + screw2 + screw3 + washer1 + washer2 + nut1 + nut2

elapsed = timeit.default_timer() - starttime
print(f"   Assembly combined: {elapsed:.3f}s")
print(f"   Total components: 1 bracket + 3 screws + 2 washers + 2 nuts")

# ============================================================================
# 4. DISPLAY INFORMATION
# ============================================================================
print("\n" + "=" * 70)
print("ASSEMBLY DETAILS")
print("=" * 70)

print("\nFastening Points:")
print("  1. Position (20, 20): M6 Socket Head Cap Screw + Washer + Nut")
print("  2. Position (80, 20): M6 Socket Head Cap Screw + Washer + Nut")
print("  3. Position (50, 60): M5 Countersunk Screw (flush mount)")

print("\nMaterial Properties:")
print("  Bracket: Aluminum")
print("  Fasteners: Steel (zinc-plated)")
print("  Washers: Steel")

print("\nClamping Load Distribution:")
print("  - Socket Head Cap Screws (2): Distributed with washers")
print("  - Countersunk Screw (1): Direct mounting")

print("\n" + "=" * 70)
print("ASSEMBLY COMPLETE")
print("=" * 70)
print("\nThis assembly demonstrates:")
print("  ✓ Multiple fastener types (socket head, countersunk)")
print("  ✓ Washers for load distribution")
print("  ✓ Proper hole alignment")
print("  ✓ Practical mechanical design")
print("\nYou can now export this assembly to STEP or STL format!")
print("=" * 70)

show(
    bracket,
    screw1,
    screw2,
    screw3,
    washer1,
    washer2,
    nut1,
    nut2,
    names=[
        "bracket",
        "screw1",
        "screw2",
        "screw3",
        "washer1",
        "washer2",
        "nut1",
        "nut2",
    ],
    collapse="1",
    reset_camera=Camera.CENTER,
)
