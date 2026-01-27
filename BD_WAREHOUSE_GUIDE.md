# BD Warehouse 使用指南

BD Warehouse 是一个基于 `build123d` 的参数化标准件库。它提供了包括紧固件、管道、法兰、轴承和齿轮在内的多种机械标准件，并内置了智能装配接口。

## 1. 核心概念

BD Warehouse 的所有零件都是标准的 `build123d.Part` 对象，这意味着它们完全兼容 `build123d` 的所有操作（如 `move`, `rotate`, `mirror`, 布尔运算等）。

此外，BD Warehouse 的零件通常包含预定义的 **接头 (Joints)**，这使得组件之间的对齐和连接变得非常简单。

---

## 2. 紧固件 (Fasteners)

紧固件模块提供了各种螺栓、螺母、垫圈等。

### 基础创建

```python
from build123d import *
from bd_warehouse.fastener import SocketHeadCapScrew, HexNut, PlainWasher

# 创建 M6x20 内六角螺钉
# simple=True (默认) 生成简化模型（无螺纹），速度快
# simple=False 生成精细模型（带螺纹），用于渲染
screw = SocketHeadCapScrew("M6-1", 20 * MM, simple=True)

# 创建 M6 螺母
nut = HexNut("M6-1")

# 创建 M6 垫圈
washer = PlainWasher("M6", "iso7089")
```

### 紧固件装配

紧固件通常使用 `Location` 进行定位。螺钉的原点通常位于头部的底面（即与被紧固件接触的面）。

```python
# 假设我们在 (10, 10, 0) 有一个孔，板厚 10mm
plate_hole_loc = Location((10 * MM, 10 * MM, 10 * MM))

# 将螺钉移动到孔位
# 螺钉头将位于 z=10 平面上，螺杆向下伸入
screw_in_place = screw.move(plate_hole_loc)

# 垫圈和螺母通常安装在背面 (z=0)
nut_loc = Location((10 * MM, 10 * MM, 0))
nut_in_place = nut.move(nut_loc)
```

---

## 3. 管道与法兰 (Pipes & Flanges)

管道系统展示了 BD Warehouse 强大的 **基于接头 (Joint-based)** 的装配能力。

### 关键组件

*   **Pipe (管道)**: 具有 `inlet` (入口) 和 `outlet` (出口) 接头。
*   **Flange (法兰)**: 具有 `pipe` (管道连接端) 和 `face` (法兰盘面) 接头。

### 智能装配示例

使用 `.connect_to()` 方法可以自动对齐和定位零件，无需手动计算坐标。

```python
from build123d import *
from bd_warehouse.pipe import Pipe
from bd_warehouse.flange import WeldNeckFlange, SlipOnFlange
from ocp_vscode import show

# 1. 创建组件
# 创建一段 12英寸 NPS 规格的管道，长度 1000mm
pipe = Pipe(nps="12", length=1000 * MM)

# 创建匹配的法兰
flange_in = WeldNeckFlange(nps="12", flange_class=150)
flange_out = SlipOnFlange(nps="12", flange_class=150)

# 2. 使用接头进行装配
# 将法兰的 "pipe" 接头连接到管道的 "inlet" 接头
flange_in.joints["pipe"].connect_to(pipe.joints["inlet"])

# 将另一个法兰连接到管道出口
flange_out.joints["pipe"].connect_to(pipe.joints["outlet"])

# 3. 显示
show(pipe, flange_in, flange_out)
```

**原理说明**：
*   `pipe.joints["inlet"]` 定义了管道一端的坐标系。
*   `flange.joints["pipe"]` 定义了法兰连接处的坐标系。
*   `connect_to` 会移动 `flange`，使其坐标系与 `pipe` 的坐标系重合，从而实现完美的自动装配。

---

## 4. 轴承与齿轮 (Bearings & Gears)

### 轴承 (Bearing)

```python
from bd_warehouse.bearing import SingleRowDeepGrooveBallBearing

# 创建 608 轴承 (常用于滑板和3D打印机)
bearing = SingleRowDeepGrooveBallBearing(size="608")
# 接头: "a" (一面), "b" (另一面)
```

### 齿轮 (Gear)

提供渐开线齿轮生成。

```python
from bd_warehouse.gear import SpurGear

# 创建模数 1，20 齿的直齿轮
gear = SpurGear(module=1, tooth_count=20, thickness=5 * MM)
```

---

## 5. 装配方法总结

在使用 BD Warehouse 时，主要有两种装配思路：

### 方法 A：相对坐标定位 (Location-based)
适用于简单堆叠或已知坐标的情况。
*   使用 `part.move(Location(...))`
*   适用于：紧固件在孔位上的安装。

### 方法 B：接头连接 (Joint-based)
适用于复杂的机械连接，特别是管道系统或模块化组件。
*   使用 `part1.joints["name"].connect_to(part2.joints["name"])`
*   优点：无需关心具体的 XYZ 坐标，只需关心逻辑连接关系。
*   适用于：管道连接、OpenBuilds 型材连接等。

### 如何查找接头名称？

大多数组件的接头命名遵循以下规律：
*   **管道**: `"inlet"`, `"outlet"`
*   **法兰**: `"pipe"`, `"face"`
*   **螺母**: `"a"` (底面), `"b"` (顶面)
*   **轴承**: `"a"`, `"b"`
*   **通用**: 你可以通过打印 `part.joints.keys()` 来查看对象拥有的所有接头名称。

```python
print(pipe.joints.keys())
# 输出: dict_keys(['inlet', 'outlet'])
```
