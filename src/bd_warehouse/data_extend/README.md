# 紧固件扩展标准参数文件说明

## 概述

`data_extend` 目录包含了扩展的紧固件参数数据，涵盖了全球主要的紧固件标准体系，包括：

- **ISO** - 国际标准化组织 (International Organization for Standardization)
- **GB** - 中国国家标准 (Chinese National Standard)
- **DIN** - 德国工业标准 (German Industrial Standard)
- **JIS** - 日本工业标准 (Japanese Industrial Standard)
- **ANSI/ASME** - 美国国家标准/美国机械工程师协会标准 (American National Standards Institute / American Society of Mechanical Engineers)

## 文件列表

### 1. 六角螺母 (Hex Nuts)
**文件**: `hex_nut_parameters_extended.csv`

包含标准：
- **ISO 4032** - 六角螺母，1型（普通型）
- **ISO 4033** - 六角螺母，2型（加厚型）
- **ISO 4035** - 六角薄螺母
- **GB 6170** - 1型六角螺母
- **GB 6172** - 六角薄螺母
- **DIN 934** - 六角螺母
- **DIN 439** - 六角薄螺母
- **JIS B1181** - 六角螺母
- **ANSI B18.2.2** - 美制六角螺母

参数说明：
- `m` - 螺母高度 (Nut height)
- `s` - 对边宽度 (Width across flats)

### 2. 六角螺栓 (Hex Head Bolts)
**文件**: `hex_head_bolt_parameters_extended.csv`

包含标准：
- **ISO 4014** - 六角头螺栓，半螺纹（部分螺纹）
- **ISO 4017** - 六角头螺栓，全螺纹
- **GB 5782** - 六角头螺栓，半螺纹
- **GB 5783** - 六角头螺栓，全螺纹
- **DIN 931** - 六角头螺栓，半螺纹
- **DIN 933** - 六角头螺栓，全螺纹
- **JIS B1180** - 六角头螺栓
- **ANSI B18.2.1** - 美制六角头螺栓

参数说明：
- `k` - 头部高度 (Head height)
- `s` - 对边宽度 (Width across flats)
- `short` - 最短长度 (Minimum length)
- `long` - 最长长度 (Maximum length)

### 3. 内六角圆柱头螺钉 (Socket Head Cap Screws)
**文件**: `socket_head_cap_screw_parameters_extended.csv`

包含标准：
- **ISO 4762** - 内六角圆柱头螺钉
- **GB 70.1** - 内六角圆柱头螺钉
- **DIN 912** - 内六角圆柱头螺钉
- **JIS B1176** - 内六角螺钉
- **ASME B18.3** - 美制内六角螺钉

参数说明：
- `dk` - 头部直径 (Head diameter)
- `k` - 头部高度 (Head height)
- `s` - 内六角宽度 (Socket size across flats)
- `t` - 内六角深度 (Socket depth)
- `short` - 最短长度
- `long` - 最长长度

### 4. 内六角半圆头螺钉 (Button Head Screws)
**文件**: `button_head_screw_parameters_extended.csv`

包含标准：
- **ISO 7380-1** - 内六角半圆头螺钉
- **GB 70.2** - 内六角盘头螺钉
- **DIN 7380** - 内六角半圆头螺钉

参数说明：
- `dk` - 头部直径
- `k` - 头部高度
- `rf` - 法兰直径 (Flange diameter)
- `s` - 内六角宽度
- `t` - 内六角深度

### 5. 内六角沉头螺钉 (Countersunk Head Screws)
**文件**: `countersunk_head_screw_parameters_extended.csv`

包含标准：
- **ISO 10642** - 内六角沉头螺钉
- **GB 70.3** - 内六角沉头螺钉
- **DIN 7991** - 内六角沉头螺钉

参数说明：
- `dk` - 头部直径
- `k` - 头部高度
- `s` - 内六角宽度
- `t` - 内六角深度

### 6. 十字槽盘头螺钉 (Pan Head Screws)
**文件**: `pan_head_screw_parameters_extended.csv`

包含标准：
- **ISO 14583** - 十字槽盘头螺钉（H型槽）
- **ISO 1580** - 一字槽盘头螺钉
- **GB 818** - 十字槽盘头螺钉
- **DIN 7985** - 十字槽盘头螺钉
- **JIS B1111** - 十字槽盘头螺钉
- **ASME B18.6.3** - 美制十字槽盘头螺钉

参数说明：
- `dk` - 头部直径
- `k` - 头部高度
- `recess` - 槽型 (Recess type, 如 T6, T8 等)
- `n` - 槽宽 (Slot width)
- `t` - 槽深 (Slot depth)

### 7. 紧定螺钉 (Set Screws)
**文件**: `setscrew_parameters_extended.csv`

包含标准：
- **ISO 4026** - 内六角平端紧定螺钉
- **GB 77** - 内六角平端紧定螺钉
- **DIN 913** - 内六角平端紧定螺钉
- **JIS B1177** - 内六角紧定螺钉

参数说明：
- `s` - 内六角宽度
- `t` - 内六角深度

### 8. 平垫圈 (Plain Washers)

#### 8.1 标准平垫圈
**文件**: `plain_washer_parameters_extended.csv`

包含标准：
- **ISO 7089** - 平垫圈，A级
- **GB 97.1** - 平垫圈，A级
- **DIN 125-A** - 平垫圈，A型
- **JIS B1256** - 平垫圈
- **ANSI B18.22.1** - 美制平垫圈

#### 8.2 大平垫圈
**文件**: `large_plain_washer_parameters_extended.csv`

包含标准：
- **ISO 7093** - 大平垫圈
- **GB 96.1** - 大垫圈
- **DIN 9021** - 大垫圈

#### 8.3 小平垫圈
**文件**: `small_plain_washer_parameters_extended.csv`

包含标准：
- **ISO 7092** - 小平垫圈
- **GB 848** - 小垫圈
- **DIN 433** - 小垫圈

参数说明：
- `d1` - 内径 (Inner diameter)
- `d2` - 外径 (Outer diameter)
- `h` - 厚度 (Thickness)

### 9. 弹簧垫圈 (Spring Lock Washers)
**文件**: `spring_lock_washer_parameters_extended.csv`

包含标准：
- **ISO 7090** - 弹簧垫圈
- **ISO 7091** - 弹簧垫圈，重型
- **GB 93** - 弹簧垫圈
- **DIN 127** - 弹簧垫圈
- **DIN 7980** - 弹簧垫圈

参数说明：
- `d1` - 内径
- `d2` - 外径
- `h` - 厚度

```

### 示例：创建 GB 标准的六角螺母

```python
from bd_warehouse.fastener import HexNut
from build123d import MM

# 使用 GB 6170 标准创建 M6 六角螺母
nut = HexNut(size="M6-1", fastener_type="gb6170")
```

### 示例：创建 DIN 标准的内六角螺钉

```python
from bd_warehouse.fastener import SocketHeadCapScrew
from build123d import MM

# 使用 DIN 912 标准创建 M8x20 内六角螺钉
screw = SocketHeadCapScrew(size="M8-1.25", length=20*MM, fastener_type="din912")
```

## 尺寸规格说明

### 公制螺纹 (Metric Thread)
格式：`M<直径>-<螺距>`
- 示例：`M6-1` 表示 M6 螺纹，螺距 1mm
- 常用尺寸：M2, M3, M4, M5, M6, M8, M10, M12, M14, M16, M20, M24, M30, M36

### 美制螺纹 (Imperial/Unified Thread)
格式：`<直径>-<每英寸螺纹数>`
- 示例：`1/4-20` 表示 1/4 英寸直径，每英寸 20 牙
- 编号规格：`#0`, `#1`, `#2`, `#3`, `#4`, `#5`, `#6`, `#8`, `#10`, `#12`
- 分数规格：`1/4`, `5/16`, `3/8`, `7/16`, `1/2`, `5/8`, `3/4`, `7/8`, `1`

## 标准对照表

### 六角螺母标准对照
| ISO | GB | DIN | JIS | 描述 |
|-----|-----|-----|-----|------|
| ISO 4032 | GB 6170 | DIN 934 | JIS B1181 | 普通六角螺母 |
| ISO 4035 | GB 6172 | DIN 439 | - | 薄型六角螺母 |
| ISO 4033 | - | - | - | 加厚六角螺母 |

### 六角螺栓标准对照
| ISO | GB | DIN | JIS | 描述 |
|-----|-----|-----|-----|------|
| ISO 4014 | GB 5782 | DIN 931 | JIS B1180 | 半螺纹六角螺栓 |
| ISO 4017 | GB 5783 | DIN 933 | - | 全螺纹六角螺栓 |

### 内六角螺钉标准对照
| ISO | GB | DIN | JIS | ASME | 描述 |
|-----|-----|-----|-----|------|------|
| ISO 4762 | GB 70.1 | DIN 912 | JIS B1176 | ASME B18.3 | 圆柱头 |
| ISO 7380-1 | GB 70.2 | DIN 7380 | - | - | 半圆头 |
| ISO 10642 | GB 70.3 | DIN 7991 | - | - | 沉头 |

### 平垫圈标准对照
| ISO | GB | DIN | JIS | ANSI | 描述 |
|-----|-----|-----|-----|------|------|
| ISO 7089 | GB 97.1 | DIN 125-A | JIS B1256 | ANSI B18.22.1 | 标准平垫圈 |
| ISO 7093 | GB 96.1 | DIN 9021 | - | - | 大平垫圈 |
| ISO 7092 | GB 848 | DIN 433 | - | - | 小平垫圈 |

## 参数单位

- 所有公制参数单位均为**毫米 (mm)**
- 美制参数单位为**英寸 (inch)**
- 在 build123d 代码中使用时需要添加单位：
  - 公制：使用 `MM` 或直接数值
  - 英制：使用 `IN`

## 数据来源

参数数据基于以下标准文档：
- ISO 标准手册
- 中国国家标准 (GB)
- 德国工业标准 (DIN)
- 日本工业标准 (JIS)
- ASME/ANSI 标准手册

## 注意事项

1. **标准等效性**：不同地区的标准虽然相似，但细节上可能有差异，使用时请确认是否符合实际需求
2. **公差等级**：本数据文件提供的是基本尺寸，实际加工时需考虑公差等级
3. **材料与强度**：不同标准对材料和机械性能要求可能不同
4. **单位转换**：公制与美制之间不能直接替换使用

## 扩展与贡献

如需添加新的标准或补充现有参数：

1. 参照现有 CSV 文件格式
2. 遵循命名规范：`<标准名小写>:<参数名>`
3. 确保数据准确性
4. 更新本说明文档

