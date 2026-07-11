# 艾宾浩斯复习计划表

`ebbinghaus-review-planner` 是一个面向 ChatGPT / Codex 的学习与复习规划 Skill。它会把用户明确希望学习、记忆、复习、备考或长期掌握的资料，整理成知识地图、主动回忆题、自适应复习日期、每日唯一学习任务，以及经过内容与逐页视觉审核的 A4 可打印学习手册。

当前版本：`1.3.0`

## 这个仓库是什么

这是 `艾宾浩斯复习计划表` Skill 的 GitHub 一键安装仓库。

仓库根目录提供项目介绍、安装说明、目录结构和版本信息；内层 `ebbinghaus-review-planner/` 是真正可被 `npx skills add` 识别和安装的 Skill 文件夹。

## 适合谁用

- 学生与考证人群：把课程、讲义、教材和考试资料变成可执行复习计划。
- 职场学习者：学习企业培训、产品知识、SOP、销售话术和专业资料。
- 阅读与研究者：把书籍、论文和长文整理成知识地图与主动回忆题。
- 培训负责人：制作可打印的练习册、复习手册和每日打卡计划。
- Skill 作者：参考包含自适应复习规则、A4 成品工作流、零基础教学流程和计划完整性检查脚本的完整 Skill。

## 示例预览

### 示例图（聊天结果 + PDF 预览）

![示例图](docs/example-output-chat-and-pdf.jpg)

## 会产出什么

Skill 会先理解资料，再生成一套可以真正执行的学习系统：

- 学习总览：学习目标、资料类型、预计学习量和优先级。
- 知识地图：主题、知识点、重要程度、难度、类型和原文位置。
- 零基础教学卡：大白话解释、正例、反例、拆解步骤和引导练习。
- 主动回忆题：问答、填空、判断、流程复述、场景应用和实操任务。
- 每日唯一任务：具体日期、学习范围、复习题号、应用任务、时间预算和完成标准。
- 自适应调整：根据 0–4 分掌握反馈动态安排下一次复习。
- A4 学习手册：默认生成可编辑 DOCX 和可打印 PDF。
- 双重审核：内容审核后排版，排版后逐页渲染检查并修正。

支持三种输出规模：

- 快速版：重要知识点、主动回忆题和首个 7 天计划。
- 标准版：完整知识地图、零基础导学、练习区、复习日历、自评区和独立答案区。
- 完整版：覆盖全部重要章节和 A/B 级知识点，长资料自动分册。

## v1.3.0 核心升级

- 新增“完全不会”模式，先教会再测试。
- 新增零基础教学卡：大白话解释、正例、反例、分步拆解、引导练习和迁移应用。
- 新增“每日唯一任务”，同一天的新学、复习、测试和应用自动合并，避免重复计算时间。
- 新增学习范围完整性检查，标明精读、略读、选读与暂不学习，避免跳页无说明。
- A/B 级知识点真正参与调度排序，优先复习重要且薄弱的内容。
- 新增可落表的自适应记录：当前间隔、得分、新间隔、下次日期、错误原因和纠错动作。
- 新增 `references/zero-base-teaching-workflow.md`。
- 新增 `references/study-plan-integrity.md`。
- 新增 `scripts/check_study_plan.py` 及有效/无效计划样例。

## 一键安装

```bash
npx skills add https://github.com/yxxx6666/ebbinghaus-review-planner --skill ebbinghaus-review-planner
```

## 怎么用

安装后，在 ChatGPT / Codex 中调用：

```text
$ebbinghaus-review-planner
我完全不会这份资料，请帮我从零开始学习，生成知识地图、教学卡、主动回忆题、具体复习日期，并制作成可以打印的 A4 学习手册。
```

考试冲刺场景：

```text
$ebbinghaus-review-planner
我 14 天后考试，每天能学习 40 分钟。请按考试优先级整理这份讲义，生成每日任务、复习题和 A4 打印版。
```

工作培训场景：

```text
$ebbinghaus-review-planner
请把这份产品培训资料变成新员工可以学习和检测的复习系统，重点覆盖流程、话术、易错点和场景应用。
```

## 工作流程

1. 判断资料类型、学习目标、开始日、截止日和每日预算。
2. 选择快速版、标准版或完整版。
3. 建立知识地图并标记重要程度、难度和知识类型。
4. 遇到“完全不会”时先生成零基础导学与教学卡。
5. 按知识类型生成主动回忆题和检测标准。
6. 计算具体复习日期，并合并成每日唯一任务。
7. 根据 0–4 分掌握反馈动态调整复习间隔。
8. 检查学习范围覆盖、页码范围、日期冲突和时间预算。
9. 制作 A4 竖版 DOCX 母版并转换为 PDF。
10. 渲染并逐页检查裁切、重叠、乱码、断表、空白页和编号错位。
11. 修正后交付最终 PDF、DOCX 和用户要求的附加导出格式。

## 目录结构

```text
ebbinghaus-review-planner/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   └── example-output-chat-and-pdf.jpg
└── ebbinghaus-review-planner/
    ├── SKILL.md
    ├── README.md
    ├── CHANGELOG.md
    ├── VERSION.md
    ├── RELEASE_REPORT.md
    ├── agents/
    │   └── openai.yaml
    ├── examples/
    ├── references/
    └── scripts/
```

实际安装入口是内层目录：

```text
ebbinghaus-review-planner/
```

安装时请使用：

```bash
--skill ebbinghaus-review-planner
```

## 自适应评分

| 评分 | 掌握状态 | 下一次复习 |
|---|---|---|
| 0 | 完全不会 | 1 天，并重新学习 |
| 1 | 模糊，需要明显提示 | 当前间隔 × 0.5 |
| 2 | 能答出主要内容但不稳定 | 当前间隔 × 1.2 |
| 3 | 能独立准确回答 | 当前间隔 × 2 |
| 4 | 能在新场景中应用 | 当前间隔 × 3 |

复习间隔最短 1 天，最长 90 天。连续低分会退回重新学习，连续高分会进入长期维护。

## 版本

- Skill ID：`ebbinghaus-review-planner`
- 中文显示名：`艾宾浩斯复习计划表`
- 当前版本：`1.3.0`
- Release tag：`v1.3.0`
- 入口文件：`ebbinghaus-review-planner/SKILL.md`

## 验证

验证 Skill 结构与业务规则：

```bash
python ebbinghaus-review-planner/scripts/quick_validate.py ebbinghaus-review-planner
```

检查生成的 PDF 是否符合 A4 页面要求：

```bash
python ebbinghaus-review-planner/scripts/check_a4_pdf.py path/to/output.pdf
```

检查学习计划是否存在页码跳跃、同日重复、超预算等问题：

```bash
python ebbinghaus-review-planner/scripts/check_study_plan.py path/to/study-plan.json
```

## 设计目标

- 先忠实理解资料，再规划学习，不补写资料中没有的事实。
- 先教会，再测试；先理解，再记忆；先练习，再长期复习。
- 用主动回忆和应用检测替代反复阅读。
- 让每个复习任务有具体日期、时间预算和完成标准。
- 让学习者可以根据真实掌握情况持续调整计划。
- 最终产出不只是聊天文本，而是一份可以直接使用和打印的学习手册。
- 所有成品在交付前经过内容审核和逐页视觉审核。

## License

MIT
