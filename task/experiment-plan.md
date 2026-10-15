# 实验计划

> 以下保留最初的实验设计与提示词草案。2026-10-15 已完成雨声、敲桌、发芽声首轮生成，实际采用的提示词经后续项目讨论调整，见[生成记录](generation-log-20261015.md)。试听、编辑与音乐实验尚未开展，进度见[实验记录表](experiment-records.md)。

## 1. 规模与共同规则

| 编号 | 内容 | 首轮计划样本 | 状态 |
| --- | --- | --- | --- |
| E01 | 温室雨声 | 3 个候选，每个约 20 秒 | 实际生成 4 条，待循环试听 |
| E02 | 水滴、敲桌、发芽 | 每类 3 个候选，共 9 个 | 敲桌、发芽各生成 4 条，待试听；水滴未生成 |
| E03 | 完整音乐生成后整理 | 2 个候选，各取约 20 秒；选 1 个深入整理 | 未开展 |
| E04 | MIDI／谱面优先 | 1 份固定谱面、2 个生成候选；选 1 个深入整理 | 未开展 |

按实际账户权限和额度执行，每次尝试均编号，失败样本也保留记录。工具一次输出多个候选时记录实际数量与筛选依据。

后续每组提示词提供英文与中文对照，实际只提交英文。生成阶段先在网页查看候选，Codex 完成后通知我，不自动下载。本计划涉及本地剪辑、文件归档和游戏验证的步骤，待我安排后再执行。首轮已提交的三组提示词及中文释义见[生成记录](generation-log-20261015.md)。

每次记录日期、工具／模型、账户方案、完整提示词、参数、输入来源、原始输出、处理后输出、生成等待时间、人工处理时间及试听观察。等待时间和编辑时间分别统计，不把官方说明写成实测结果。

## 2. E01：雨声生成与循环适配

**问题：** 雨声能否持续循环，并与音乐、操作提示叠加？

**候选工具及条件：** ElevenLabs Sound Effects；约 20 秒，启用实际提供的循环选项。同一提示词与设置取得 3 个候选，观察重复生成差异。

提示词草案：

```text
Gentle steady rain heard from inside a small glass greenhouse. Soft rain on glass, a calm intimate atmosphere, consistent texture and level. Seamless ambient loop. No music, no voices, no thunder, no isolated loud drips.
```

步骤：

1. 保存实际参数与全部原始输出。
2. 每个片段重复播放 5 次，记录接缝突变、停顿、多余事件和明显周期感。
3. 选 1 个候选，按需裁剪、交叉淡化及调整电平；保留处理版本与耗时。
4. 编辑后同样重复 5 次，再与固定的音乐、水滴和敲桌素材叠加试听，注明对照素材来源。

评价：接缝可察觉程度，是否掩盖音乐与提示，编辑前后差异和人工处理时间。

## 3. E02：单次音效与交互适配

**问题：** 生成声音能否成为清晰、可重复触发的操作或事件反馈？

**候选工具：** ElevenLabs Sound Effects。水滴、敲桌各拟生成约 1 秒，发芽约 2 秒；每类同一设置取得 3 个候选。

提示词草案：

```text
Water drop: A single small water drop striking glass, delicate and bright, with a clear immediate attack and a short decay. Isolated one-shot, dry recording, no background ambience, no music, no repeated drops.

Table tap: A single gentle fingertip tap on a wooden tabletop, warm and rounded, with a clear immediate attack and a short decay. Isolated one-shot, dry recording, no background ambience, no music, no repeated taps.

Seed sprout: A tiny seed cracking open and sprouting, a soft organic crackle followed by a brief delicate airy shimmer. Gentle storybook game feedback, isolated one-shot, no voices, no background ambience, no musical phrase.
```

步骤：

1. 保存所有输出，检查多次事件、背景音乐、前置静音、长尾音及语义偏差。
2. 每类选 1 个，裁剪前置静音、保留合适尾音并调整电平，保存处理前后文件和编辑耗时。
3. 水滴、敲桌分别按 96 BPM 四分音符和八分音符间隔播放，再按“水滴提示—敲桌回应”交替试听。
4. 发芽声单次触发，与雨声及音乐叠加试听；没有对应动画时不填写动画同步评价。

评价：起音、尾音、密集触发时的混浊、两类节奏声音的可辨识度，以及与场景其他声音叠加后的表现。

## 4. 音乐实验共同条件

拟定测试条件为 **96 BPM、4/4 拍、C 大调、8 小节，约 20 秒，另留尾音**，以柔和、安静的纯器乐为目标。这是实验条件，不代表最终选曲决定。

两条路线均以“独立旋律、节奏、和声，MIDI／谱面与可即时触发的旋律音源”为整理目标，尽量使用同一生成工具与后期工具。

E04 使用固定的 8 小节单声部 MIDI／谱面，记录音高、拍位、时值与来源。E03 若支持，可使用同一旋律作为参考；若采用纯文本生成，应将结果解释为两种实际工作流程的比较，不能声称是同一旋律的严格对照。

现有本地程序合成原型可作为流程对照，使用前核对文件与谱面版本；此类素材标为“程序合成”，不计入 AIGC 样本。

## 5. E03：先生成完整音乐，再拆分整理

**问题：** 从完整音乐出发，能否整理出独立声部与可靠音符数据？

**候选工具：** Suno，分轨与 MIDI 功能以账户实际可用情况为准。

提示词草案：

```text
Instrumental music for a quiet storybook game set inside a rainy greenhouse. 96 BPM, 4/4, C major. A simple memorable monophonic lead melody, sparse warm accompaniment, and a restrained clear percussion pattern. Soft flute-like lead with light mallet accents. A short eight-bar phrase with a gentle ending. No vocals, no rain sound effects, no dramatic tempo changes.
```

步骤：

1. 取得 2 个候选，各取连续约 20 秒，记录实际速度、结构与提示符合情况。
2. 按旋律清晰度和风格匹配度选 1 个，记录筛选依据。
3. 尝试分离旋律、节奏、和声；保存实际获得的声部，记录不支持或无法分开的情况。
4. 尝试获取旋律 MIDI，对照音频检查漏音、多余音符、音高、起音与时值，保存修正前后版本。
5. 整理可触发的旋律音源，记录采用切片、采样器或其他方法，以及与原音色的差异。
6. 按统一方式验证交互，统计人工处理步骤和时间。

评价：节拍稳定性、声部串音、转写错误、整理成本与交互可用性。某次无法导出不用于推断其他工具的能力。

## 6. E04：先确定 MIDI／谱面，再制作声音

**问题：** 已有明确音乐结构，能否减少游戏适配中的修正？

**候选工具：** Suno Studio 的 MIDI 输入与生成功能。支持上传不等于能准确保留旋律，保留程度需实测。

步骤：

1. 保存固定的 8 小节 MIDI／谱面，记录来源、速度、音高、拍位与时值。
2. 尝试上传 MIDI，沿用 E03 风格描述，补充“保留输入旋律音高与节奏、提供柔和音色与稀疏伴奏”的要求，保存实际操作与完整提示词。
3. 取得 2 个候选，对照固定谱面检查旋律、节奏是否被改写，声部能否独立使用。
4. 选 1 个整理为独立声部与触发音源，记录重生成、剪辑或人工重建等实际操作。
5. 按统一方式验证交互，记录处理时间，与 E03 比较。

账户无法使用对应功能时，本项保持未开展。若改为固定 MIDI 配合常规音源，再让 AI 生成独立伴奏或音色素材，另行记录方案变更，明确常规音源渲染为非 AIGC 环节。

评价：输入旋律保留程度、伴奏对齐、独立控制能力和人工处理时间；记录与 E03 在音色或输入方式上的差异及比较限制。

## 7. 统一交互验证

采用同一试听环境、相近感知响度及同一事件序列，分别测试整理后的两组音乐素材：

1. 完整演奏乐句，检查声部对齐。
2. 分别开关旋律、节奏与和声，检查分层控制。
3. 按实际触发时刻播放音符，测试连续收集、漏音与长停顿；未触发的音符保持空白。
4. 植物回放记录的音符，玩家敲桌仅在操作时发声，检查两者独立控制。

在浏览器原型验证时记录改动、输入方式与录屏；仅做离线事件序列试听时，标为“离线模拟”，不填写已接入游戏或输入延迟结论。

## 8. 文件保存与比较方式

有实际材料时再创建 `assets/experiments/E01/` 等目录，分别使用 `raw/`、`edited/`，E04 另设 `input/`。采用 `E01_take01_raw`、`E01_take01_loop` 等文件名并保留原始扩展名，记录表用相对路径链接文件。

最终比较可用数量、循环与触发表现、音乐结构、分轨和音符问题、生成次数、等待时间、人工处理时间与复用程度。只根据本次样本、工具版本和测试条件得出结论，注明素材来源及公开分享条件。
