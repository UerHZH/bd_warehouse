# Visualization Update Plan for Fasteners Examples

## Objective
Modify `examples/fasteners_demo.py` and `examples/fasteners_assembly.py` to enable visualization using `ocp-vscode` instead of text-only output or failing imports.

## Files to Modify

### 1. `examples/fasteners_assembly.py`

**Current State:**
- Imports `build123d`.
- Creates a `bracket` and several fasteners.
- Combines them into `assembly`.
- Has a `try...except ImportError` block at the end attempting to `show(assembly)`.

**Proposed Changes:**
1.  **Import**: Add `from ocp_vscode import show, Camera`.
2.  **Visualization**: Replace the existing `try...except` block with a robust `show()` command.
3.  **Hierarchy**: Display individual components (`bracket`, `screw1`, `screw2`, `screw3`, `washer1`, `washer2`, `nut1`, `nut2`) instead of the fused assembly.
4.  **Naming**: Provide explicit names for the component tree.
5.  **Camera**: Reset camera to center.

### 2. `examples/fasteners_demo.py`

**Current State:**
- Imports `build123d`.
- Creates ~20 different fastener instances.
- Prints details to console.
- Ends with an incorrect `show_object(HexNut)` call.

**Proposed Changes:**
1.  **Import**: Add `from ocp_vscode import show, Camera`.
2.  **Collection**: Gather all created fastener instances into a list.
3.  **Layout**: Implement a grid layout algorithm (e.g., 5 columns, 50mm spacing) to arrange the components so they don't overlap at the origin.
4.  **Visualization**: Use `show()` to display the arranged components with clear names.

## Execution Strategy

I will apply these changes by editing the files directly.

## Validation
- Review the modified files to ensure correct syntax.
- Ensure all necessary objects are included in the visualization call.
