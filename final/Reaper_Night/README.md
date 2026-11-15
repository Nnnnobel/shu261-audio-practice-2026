# REAPER 编辑工程

使用 REAPER 7.79 制作。所有工程媒体引用已整理为相对路径，保留本目录结构即可迁移。

- `ChinjuForest_QuietNight.rpp`：五轨、120 秒固定编排混音，使用 `Exports` 内的 WAV。
- `AssetProjects/*.rpp`：九个单素材剪辑工程，使用 `Sources` 内四份录音。
- `Exports`：九条资产与 `ChinjuForest_Final_120s.wav` 混音。
- `Sources`：实际选用的四份 Freesound HQ MP3 预览录音。
- `Evidence`：最终资产格式与 Wwise 参数记录。

| 素材工程 | 源录音片段（秒） | 处理 |
| --- | --- | --- |
| AMB_Stream_Loop | 2–44，衔接片段 44–46 | 2 秒交叉淡化；导出 `AMB_Stream_Loop_42s.wav`，对应 Wwise 的 `AMB_Stream_Loop.wav` |
| AMB_ForestWind_Loop | 25–85，衔接片段 85–87 | 2 秒交叉淡化 |
| AMB_Cicadas_Loop | 1–29，衔接片段 29–31 | 2 秒交叉淡化 |
| BRD_Distant_01 | 2.7–5.0 | 淡入 0.15 秒，淡出 0.25 秒，降低约 25 dB |
| BRD_Distant_02 | 9.0–10.7 | 淡入 0.15 秒，淡出 0.25 秒，降低约 19 dB |
| BRD_Distant_03 | 10.7–12.2 | 淡入 0.15 秒，淡出 0.25 秒，降低约 22 dB |
| LEAF_Rustle_01 | 101–104.5 | 淡入 0.4 秒，淡出 0.8 秒 |
| LEAF_Rustle_02 | 123–127 | 淡入 0.4 秒，淡出 0.8 秒 |
| LEAF_Rustle_03 | 145–148 | 淡入 0.4 秒，淡出 0.8 秒 |

修改后从 REAPER 的 Render 窗口导出，确认采样率 **48000 Hz**、声道 **Stereo**、格式 **WAV / 24 bit PCM**，并选择导出位置。随后在 Wwise 中重新导入对应声音。导出目录与 Wwise 的 `Originals` 各自保留副本。

REAPER 混音使用固定时间线和声像；Wwise 使用实时随机容器及 3D 距离衰减，二者用于不同的试听环节。

素材署名见 [CREDITS.md](../CREDITS.md)，完整制作过程见 [Word 报告](../报告/24122339_郑皓文_基础实践期末报告.docx)。
