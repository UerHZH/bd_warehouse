"""
Comprehensive demonstration of bd_warehouse fasteners

This example demonstrates the usage of various fasteners available in bd_warehouse:
- Nuts: HexNut, SquareNut, HexNutWithFlange, DomedCapNut, HeatSetNut, UnchamferedHexagonNut
- Screws: SocketHeadCapScrew, HexHeadScrew, CheeseHeadScrew, CounterSunkScrew, PanHeadScrew,
          ButtonHeadScrew, SetScrew, and many more
- Washers: PlainWasher, ChamferedWasher, InternalToothLockWasher
"""

import timeit
from ocp_vscode import show, Camera
from build123d import *
from bd_warehouse.fastener import (
    # Nuts
    HexNut,
    SquareNut,
    HexNutWithFlange,
    DomedCapNut,
    HeatSetNut,
    UnchamferedHexagonNut,
    # Screws
    SocketHeadCapScrew,
    HexHeadScrew,
    CheeseHeadScrew,
    CounterSunkScrew,
    PanHeadScrew,
    ButtonHeadScrew,
    SetScrew,
    LowProfileScrew,
    RaisedCheeseHeadScrew,
    RaisedCounterSunkOvalHeadScrew,
    PanHeadWithCollarScrew,
    ButtonHeadWithCollarScrew,
    HexHeadWithFlangeScrew,
    # Washers
    PlainWasher,
    ChamferedWasher,
    InternalToothLockWasher,
)

print("=" * 60)
print("BD_WAREHOUSE FASTENERS DEMONSTRATION")
print("=" * 60)

# ============================================================================
# NUTS EXAMPLES
# ============================================================================
print("\n1. NUTS")
print("-" * 60)

# Hex Nut
print("\nHex Nut (M6-1):")
starttime = timeit.default_timer()
hex_nut = HexNut("M6-1", simple=False)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M6-1")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {hex_nut.is_valid}")

# Square Nut
print("\nSquare Nut (M8-1.25):")
starttime = timeit.default_timer()
square_nut = SquareNut("M8-1.25")
elapsed = timeit.default_timer() - starttime
print(f"  Size: M8-1.25")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {square_nut.is_valid}")

# Hex Nut with Flange
print("\nHex Nut with Flange (M10-1.5):")
starttime = timeit.default_timer()
hex_flange_nut = HexNutWithFlange("M10-1.5")
elapsed = timeit.default_timer() - starttime
print(f"  Size: M10-1.5")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {hex_flange_nut.is_valid}")

# Domed Cap Nut
print("\nDomed Cap Nut (M12-1.75):")
starttime = timeit.default_timer()
domed_cap_nut = DomedCapNut("M12-1.75")
elapsed = timeit.default_timer() - starttime
print(f"  Size: M12-1.75")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {domed_cap_nut.is_valid}")

# Heat Set Nut
print("\nHeat Set Nut (M5-0.8-Standard):")
starttime = timeit.default_timer()
heatset_nut = HeatSetNut("M5-0.8-Standard")
elapsed = timeit.default_timer() - starttime
print(f"  Size: M5-0.8-Standard")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {heatset_nut.is_valid}")

# Unchamfered Hexagon Nut
print("\nUnchamfered Hexagon Nut (M8-1.25):")
starttime = timeit.default_timer()
unchamfered_nut = UnchamferedHexagonNut("M8-1.25")
elapsed = timeit.default_timer() - starttime
print(f"  Size: M8-1.25")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {unchamfered_nut.is_valid}")

# ============================================================================
# SCREWS EXAMPLES
# ============================================================================
print("\n\n2. SCREWS")
print("-" * 60)

# Socket Head Cap Screw
print("\nSocket Head Cap Screw (M5 x 16):")
starttime = timeit.default_timer()
socket_cap = SocketHeadCapScrew("M5-0.8", 16 * MM, simple=False)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M5 x 16mm")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {socket_cap.is_valid}")

# Hex Head Screw
print("\nHex Head Screw (M6 x 20):")
starttime = timeit.default_timer()
hex_head = HexHeadScrew("M6-1", 20 * MM)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M6 x 20mm")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {hex_head.is_valid}")

# Cheese Head Screw
print("\nCheese Head Screw (M4 x 12):")
starttime = timeit.default_timer()
cheese_head = CheeseHeadScrew("M4-0.7", 12 * MM)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M4 x 12mm")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {cheese_head.is_valid}")

# Counter Sunk Screw
print("\nCounter Sunk Screw (M5 x 16):")
starttime = timeit.default_timer()
countersunk = CounterSunkScrew("M5-0.8", 16 * MM)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M5 x 16mm")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {countersunk.is_valid}")

# Pan Head Screw
print("\nPan Head Screw (M4 x 10):")
starttime = timeit.default_timer()
pan_head = PanHeadScrew("M4-0.7", 10 * MM)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M4 x 10mm")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {pan_head.is_valid}")

# Button Head Screw
print("\nButton Head Screw (M5 x 14):")
starttime = timeit.default_timer()
button_head = ButtonHeadScrew("M5-0.8", 14 * MM)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M5 x 14mm")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {button_head.is_valid}")

# Set Screw
print("\nSet Screw (M6 x 20):")
starttime = timeit.default_timer()
set_screw = SetScrew("M6-1", 20 * MM)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M6 x 20mm")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {set_screw.is_valid}")

# Low Profile Screw
print("\nLow Profile Screw (M4 x 8):")
starttime = timeit.default_timer()
low_profile = LowProfileScrew("M4-0.7", 8 * MM)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M4 x 8mm")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {low_profile.is_valid}")

# Raised Cheese Head Screw
print("\nRaised Cheese Head Screw (M5 x 12):")
starttime = timeit.default_timer()
raised_cheese = RaisedCheeseHeadScrew("M5-0.8", 12 * MM)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M5 x 12mm")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {raised_cheese.is_valid}")

# Hex Head with Flange Screw
print("\nHex Head with Flange Screw (M8 x 25):")
starttime = timeit.default_timer()
hex_flange = HexHeadWithFlangeScrew("M8-1.25", 25 * MM)
elapsed = timeit.default_timer() - starttime
print(f"  Size: M8 x 25mm")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {hex_flange.is_valid}")

# ============================================================================
# WASHERS EXAMPLES
# ============================================================================
print("\n\n3. WASHERS")
print("-" * 60)

# Plain Washer
print("\nPlain Washer (M6 - ISO 7089):")
starttime = timeit.default_timer()
plain_washer = PlainWasher("M6", "iso7089")
elapsed = timeit.default_timer() - starttime
print(f"  Size: M6")
print(f"  Type: ISO 7089")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {plain_washer.is_valid}")

# Chamfered Washer
print("\nChamfered Washer (M8):")
starttime = timeit.default_timer()
chamfered_washer = ChamferedWasher("M8", "iso7090")
elapsed = timeit.default_timer() - starttime
print(f"  Size: M8")
print(f"  Type: ISO 7090")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {chamfered_washer.is_valid}")

# Internal Tooth Lock Washer
print("\nInternal Tooth Lock Washer (M5):")
starttime = timeit.default_timer()
lock_washer = InternalToothLockWasher("M5", "din6797")
elapsed = timeit.default_timer() - starttime
print(f"  Size: M5")
print(f"  Type: DIN 6797")
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Valid: {lock_washer.is_valid}")

# ============================================================================
# ASSEMBLED FASTENER SYSTEM
# ============================================================================
print("\n\n4. ASSEMBLED FASTENER SYSTEM")
print("-" * 60)

print("\nAssembling a complete fastening system (M6 Socket Cap Screw + Washer + Nut):")
starttime = timeit.default_timer()

# Create components
screw = SocketHeadCapScrew("M6-1", 30 * MM, simple=False)
washer = PlainWasher("M6", "iso7089")
nut = HexNut("M6-1", simple=False)

# Assemble with proper positioning
assembled = screw + washer.move(Location((0, 0, 30 * MM))) + nut.move(Location((0, 0, 32 * MM)))

elapsed = timeit.default_timer() - starttime
print(f"  Creation time: {elapsed:.3f}s")
print(f"  Complete assembly created")

print("\n" + "=" * 60)
print("DEMONSTRATION COMPLETE")
print("=" * 60)
print("\nAll fasteners have been successfully created and validated.")
print("You can now use these fasteners in your designs!")

# Prepare objects for visualization
fasteners_to_show = [
    ("Hex Nut", hex_nut),
    ("Square Nut", square_nut),
    ("Hex Flange Nut", hex_flange_nut),
    ("Domed Cap Nut", domed_cap_nut),
    ("Heat Set Nut", heatset_nut),
    ("Unchamfered Nut", unchamfered_nut),
    ("Socket Head Cap Screw", socket_cap),
    ("Hex Head Screw", hex_head),
    ("Cheese Head Screw", cheese_head),
    ("Counter Sunk Screw", countersunk),
    ("Pan Head Screw", pan_head),
    ("Button Head Screw", button_head),
    ("Set Screw", set_screw),
    ("Low Profile Screw", low_profile),
    ("Raised Cheese Head Screw", raised_cheese),
    ("Hex Flange Screw", hex_flange),
    ("Plain Washer", plain_washer),
    ("Chamfered Washer", chamfered_washer),
    ("Lock Washer", lock_washer),
    ("Assembled System", assembled),
]

# Arrange objects in a grid
grid_columns = 5
spacing = 50 * MM
arranged_objects = []
names = []

for i, (name, obj) in enumerate(fasteners_to_show):
    row = i // grid_columns
    col = i % grid_columns
    # Move object to grid position
    moved_obj = obj.move(Location((col * spacing, -row * spacing, 0)))
    arranged_objects.append(moved_obj)
    names.append(name)

show(
    *arranged_objects,
    names=names,
    reset_camera=Camera.CENTER,
)