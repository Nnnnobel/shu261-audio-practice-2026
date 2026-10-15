# 首轮音效生成记录：雨声、桌面敲击与种子发芽

日期：2026-10-15。

我让 Codex 以正在制作的本地 GameJam 项目为基础，读取剧情、美术规范和较新分镜，并结合温室、水杯、桌面与种子的画面提出声音建议。讨论中，环境雨声与节奏提示被分开，桌面敲击强调清楚的单次起音，发芽声先采用自然的种壳轻裂与嫩芽展开。

这轮由我把控制作方向并决定执行方案，Codex 承担资料梳理、建议转化、平台操作和资产归档的协调工作，在 Chrome 的 ElevenLabs Sound Effects 页面填写提示词、设置参数、提交生成并下载全部候选，随后整理文件和记录。候选声音由 ElevenLabs 生成，试听取舍尚未进行。

## 实际执行

| 内容 | 时长 | 循环 | 提示词影响 | 批次／候选 | 提交前显示的预估积分 |
| --- | --- | --- | --- | --- | --- |
| E01 温室雨声 | 20 秒 | 开启 | 30% | 1 批／4 条 | 268 |
| E02 桌面敲击 | 1 秒 | 关闭 | 60% | 1 批／4 条 | 12 |
| E02 种子发芽 | 2 秒 | 关闭 | 50% | 1 批／4 条 | 28 |

三次均使用手动时长；沿用网页默认开启的「自动优化简短或不清晰的提示词」选项。下文保存的是实际填入、并在历史记录中显示的提示词，未获取工具内部的优化文本。界面没有核验到具体模型名称，不根据 API 文档推定本次模型版本。

原计划每类保留 3 个候选，本次网页每批返回 4 条，全部下载保留，没有额外生成或筛选。积分是提交前显示的预估值，三批合计 308；未记录准确生成等待时间，不作耗时比较。

## 实际提示词

以下英文为本轮实际提交文本；中文为对应释义，供理解与调整，不提交给平台。

### E01 温室雨声

```text
Soft steady rain outside a small glass greenhouse, heard from the quiet interior through a partly open window. Fine rain on glass with a gentle, slightly distant texture and natural variation. Seamless ambient loop. No prominent individual drips, thunder, strong wind, voices, or music.
```

中文对照：从安静的室内，透过一扇半开的窗户，听见小型玻璃温室外柔和、持续的雨声。细雨落在玻璃上，声音轻柔、稍有距离感，并有自然变化。作为首尾无明显接缝的环境声循环。不要突出的单次滴水声、雷声、强风、人声或音乐。

### E02 桌面敲击

```text
One light fingertip tap on a wooden greenhouse worktable. A clear close attack, a small warm woody resonance, and a short dry decay. Gentle touch on a solid surface. Isolated single tap, no repeated knocking, background rain, voices, music, or long reverb.
```

中文对照：用指尖轻轻敲一下温室里的木质工作台。起音清楚、听感距离近，带有少量温暖的木质共鸣，声音短促衰减，保持干声。表现轻触结实桌面的感觉。只要独立的一次敲击，不要反复敲击、背景雨声、人声、音乐或长混响。

### E02 种子发芽

```text
A tiny dry seed shell gently splitting, followed by the delicate rustle of a tender shoot slowly unfolding. A small intimate organic sound, soft and close, with a brief natural decay. One short event. No dramatic cracking, magical chimes, explosion, voices, music, or long reverb.
```

中文对照：一颗细小、干燥的种子外壳轻轻裂开，随后是嫩芽缓慢舒展时细微的窸窣声。声音轻微、贴近，带有自然生长的质感，柔和且近距离，尾音自然、短暂地衰减。只表现一次短事件。不要夸张的爆裂声、魔法钟声、爆炸、人声、音乐或长混响。

这里的 attack 指声音开始时的起音；decay 指声音随时间衰减的过程；dry 指尽量不带明显混响的干声；seamless loop 指首尾衔接时没有明显断点的循环。

## 已完成的检查

- 历史记录中每批均出现 4 条候选，提示词与输入一致。
- 通过每条候选的下载菜单选择 WAV 48 kHz，12 条均已下载。
- 读取本地 WAV 文件头，12 条均为 48 kHz、16 bit、双声道；雨声各 20 秒、敲击各 1 秒、发芽各 2 秒。
- 本地按实验类别与候选编号整理原始文件，复制前后字节一致，并保存 SHA-256 清单。没有剪辑、归一化、采样率转换或位深转换。

原始音频和包含原下载文件名的 `manifest.json` 已在本地归档；本次 GitHub 更新仅包含文字记录，音频尚未上传。生成结果可在本人登录后的 [ElevenLabs 历史记录](https://elevenlabs.io/app/sound-effects/history)查看，该链接不是公开音频分享链接。

## 后续操作约定

本轮下载属于已经完成的操作记录。此后按我的新要求，提示词均提供英文与中文对照，实际仅提交英文；生成后先通知我到 ElevenLabs 网页查看和试听，不自动下载或做本地音频整理。需要编辑或接入游戏时，再根据我的安排处理。

## 待完成

- 雨声连续循环与叠加试听。
- 敲击起音、单次事件、尾音及连续触发测试。
- 发芽声与画面动作的搭配试听。
- 候选筛选、剪辑、使用与公开分享条件记录及游戏接入。
- 水滴单次音效与 E03、E04 音乐实验。

上述文件检查只确认已获得对应格式与时长的音频。声音是否自然、是否符合提示词、是否适合项目，仍待实际试听。

后续已收到我的网页试听反馈，见[第一轮试听反馈与第二轮调整](iteration-02-20261015.md)。本文保留首次生成时的操作事实。
