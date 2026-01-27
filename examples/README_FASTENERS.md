# BD Warehouse 紧固件编程示例

本目录包含使用 bd_warehouse 库创建各种紧固件的完整示例。

## 📁 文件说明

### 1. **fasteners_demo.py** - 综合演示程序
- 演示所有主要紧固件类型的基本用法
- 包括：螺母、螺钉、垫圈
- 展示每个紧固件的创建时间和有效性检查
- **运行命令**：
  ```bash
  /opt/miniconda3/envs/cq/bin/python examples/fasteners_demo.py
  ```
- **输出**：展示各类紧固件的创建过程和验证结果

### 2. **fasteners_assembly.py** - 高级装配示例
- 创建一个实际的机械装配体：安装支架
- 包含多个紧固点和不同类型的紧固件
- 展示如何在实际设计中使用紧固件库
- **运行命令**：
  ```bash
  /opt/miniconda3/envs/cq/bin/python examples/fasteners_assembly.py
  ```
- **输出**：完整的机械装配说明

### 3. **FASTENERS_GUIDE.md** - 完整使用指南
- 详细的使用文档
- 所有紧固件类型的参数说明
- 实际应用示例
- 常见问题解答
- 性能优化建议

## 🔧 支持的紧固件类型

### 螺母 (Nuts)
- ✅ HexNut - 六角螺母
- ✅ SquareNut - 方形螺母
- ✅ HexNutWithFlange - 带法兰六角螺母
- ✅ DomedCapNut - 穹顶盖螺母
- ✅ HeatSetNut - 热铆螺母
- ✅ UnchamferedHexagonNut - 无倒角六角螺母

### 螺钉 (Screws)
- ✅ SocketHeadCapScrew - 内六角圆柱头螺钉
- ✅ HexHeadScrew - 六角头螺钉
- ✅ CheeseHeadScrew - 盘头螺钉
- ✅ CounterSunkScrew - 沉头螺钉
- ✅ PanHeadScrew - 半圆头螺钉
- ✅ ButtonHeadScrew - 按钮头螺钉
- ✅ SetScrew - 无头螺钉
- ✅ LowProfileScrew - 低矮螺钉
- ✅ RaisedCheeseHeadScrew - 凸起盘头螺钉
- ✅ HexHeadWithFlangeScrew - 带法兰六角头螺钉
- ✅ 及其他多种类型

### 垫圈 (Washers)
- ✅ PlainWasher - 普通垫圈
- ✅ ChamferedWasher - 倒角垫圈
- ✅ InternalToothLockWasher - 内齿锁紧垫圈

## 📊 快速开始

### 最简单的例子

```python
from build123d import *
from bd_warehouse.fastener import HexNut, SocketHeadCapScrew, PlainWasher

# 创建单个紧固件
nut = HexNut("M6-1")
screw = SocketHeadCapScrew("M6-1", 20 * MM)
washer = PlainWasher("M6", "iso7089")

# 组装
assembly = screw + washer + nut
```

### 在你的设计中使用

```python
from build123d import *
from bd_warehouse.fastener import SocketHeadCapScrew

# 创建你的零件
my_part = Box(100 * MM, 80 * MM, 10 * MM)

# 添加螺钉
screw = SocketHeadCapScrew("M5-0.8", 20 * MM)
screw = screw.move(Location((50 * MM, 40 * MM, 0)))

# 组合
design = my_part + screw

# 导出
design.save("my_design.step")
```

## ⚡ 性能数据

根据测试结果：
- 单个螺母创建时间：30-150 ms
- 单个螺钉创建时间：40-150 ms
- 单个垫圈创建时间：1-3 ms
- 完整装配（8个零件）：<200 ms

## 🎯 常用螺纹规格

| 规格 | 螺距 | 用途 |
|------|------|------|
| M4-0.7 | 0.7 mm | 小型装配 |
| M5-0.8 | 0.8 mm | 通用 |
| M6-1 | 1.0 mm | 通用（推荐） |
| M8-1.25 | 1.25 mm | 中型装配 |
| M10-1.5 | 1.5 mm | 大型装配 |
| M12-1.75 | 1.75 mm | 重型装配 |

## 📚 相关资源

- [BD Warehouse GitHub 仓库](https://github.com/gumyr/bd_warehouse)
- [Build123d 官方文档](https://build123d.readthedocs.io/)
- [ISO 标准文档](https://www.iso.org/)
- [OCP Studio 使用指南](https://opencascade.com/)

## ✨ 示例程序输出

### fasteners_demo.py
```
============================================================
BD_WAREHOUSE FASTENERS DEMONSTRATION
============================================================

1. NUTS
Hex Nut (M6-1):
  Size: M6-1
  Creation time: 0.069s
  Valid: True

[更多螺母、螺钉、垫圈的详细信息...]

2. SCREWS
Socket Head Cap Screw (M5 x 16):
  Size: M5 x 16mm
  Creation time: 0.044s
  Valid: True

[更多螺钉类型...]

3. WASHERS
Plain Washer (M6 - ISO 7089):
  Size: M6
  Type: ISO 7089
  Creation time: 0.001s
  Valid: True

4. ASSEMBLED FASTENER SYSTEM
Assembling a complete fastening system...
  Creation time: 0.109s
  Complete assembly created
```

### fasteners_assembly.py
```
======================================================================
ADVANCED FASTENER ASSEMBLY - MOUNTING BRACKET
======================================================================

1. Creating mounting bracket...
   Bracket created: 0.014s
   - Dimensions: 100 x 80 x 10 mm
   - 3 mounting holes (M6 clearance holes)

2. Creating fastened assembly...
   Assembly created: 0.265s

3. Combining components...
   Assembly combined: 0.148s

4. ASSEMBLY DETAILS
Fastening Points:
  1. Position (20, 20): M6 Socket Head Cap Screw + Washer + Nut
  2. Position (80, 20): M6 Socket Head Cap Screw + Washer + Nut
  3. Position (50, 60): M5 Countersunk Screw (flush mount)

✓ Multiple fastener types
✓ Washers for load distribution
✓ Proper hole alignment
✓ Practical mechanical design
```

## 🚀 下一步

1. **修改示例**：编辑 `fasteners_demo.py` 或 `fasteners_assembly.py` 以适应您的需求
2. **创建自己的设计**：基于提供的示例创建新的装配体
3. **导出设计**：使用 `.save()` 方法导出为 STEP、STL 等格式
4. **集成到项目**：将紧固件集成到您的机械设计项目中

## 📝 注意事项

- 所有尺寸规格必须使用字符串格式（如 "M6-1"，而不是 6*MM）
- 垫圈需要指定 `fastener_type` 参数
- 使用 `simple=True` 可以加快大量零件的创建
- 导出前确保所有零件都 `is_valid`

---

**版本**：1.0  
**最后更新**：2026年1月27日  
**环境**：Python 3.11 + build123d + bd_warehouse
