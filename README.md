# pairwise-denoiser-history-reset

## 领域

游戏、图形与多媒体

## 主题

降噪历史重置

## 说明

运动量钳制历史长度、重投影失败回退与 NaN 收敛。

初始状态下 `render/denoiser_history_reset.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
