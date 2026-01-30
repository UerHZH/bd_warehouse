from build123d import MM
from bd_warehouse.fastener import ButtonHeadScrew
from ocp_vscode import show, Camera, save_screenshot

screw = ButtonHeadScrew("M6-1", 20 * MM, fastener_type='gb70.2')
show(screw, names=["Button Head Screw"], reset_camera=Camera.CENTER)

# 导出零件图片（保存当前视图的截图）
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
save_screenshot(os.path.join(script_dir, "button_head_screw.png"))
