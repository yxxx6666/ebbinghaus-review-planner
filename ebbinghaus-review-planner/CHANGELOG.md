# Changelog

## v1.4.0 - DOCX/PDF Consistency and Print Quality

### Added

- 新增 `references/docx-pdf-consistency.md`，规定 DOCX 唯一母版、直接转换 PDF、空白页、断词和双格式一致性。
- 新增 `scripts/check_docx_workbook.py`，检查连续分页符、空白页风险、标题样式、动态页码和直接设置的过小字号。
- 新增 `scripts/check_output_pair.py`，比较 DOCX 与 PDF 的正文覆盖率。
- 新增首页 K/Q 编号解释和每日最低分记录口径。

### Changed

- 普通正文最低字号从 9 磅提高到 10 磅；表格和答案正文最低 9.5 磅。
- 零基础模式要求所有 A 级知识点都有教学卡。
- PDF 必须由最终 DOCX 直接转换，禁止独立生成两套版式。
- 自适应间隔统一使用向上取整。
- R0 改为“等待约 20 分钟，再用 3-5 分钟闭卷回忆”。
- 每日任务表不再使用含义不清的总评分，改为记录当日最低分。
- 禁止英文单词、K/Q 编号、题号范围和日期在字符中间断裂。

## v1.3.0 - Zero-Base Teaching and Plan Integrity

### Added

- 新增 `references/zero-base-teaching-workflow.md`：完全不会/零基础时强制先教后练。
- 新增教学卡结构：大白话解释、为什么重要、正例、反例、拆解、引导练习、独立练习、迁移应用。
- 新增 `references/study-plan-integrity.md`：检查阅读范围、同日任务合并、预算和分级调度。
- 新增 `scripts/check_study_plan.py`，自动检查范围缺口、重复日期、预算超限和非法状态。
- 新增计划 JSON 的有效与无效示例。
- 新增知识点—题号映射和 A/B 级调度优先级。
- 新增当前间隔、新间隔和具体下次日期的自适应记录表。
- PDF 预检脚本新增可选页码检测。

### Changed

- “完全不会”不再从知识点表直接进入大量闭卷题。
- 7 天学习计划与 30 天复习节点合并为“每日唯一任务”，R0 计入当天预算。
- 声称覆盖某页码或章节时，必须标记精读、略读、选读或暂不读，禁止无说明跳页。
- 当前章节尚未完整覆盖时，不再正式学习下一章；只允许明确标注的轻量预览。
- A/B 级标签必须参与题目覆盖和每日调度，而不是只用于展示。
- A4 手册增加零基础导学、教学卡、范围覆盖表和结业挑战。
- 页脚必须包含实际页码；答案页过密时拆页，不能缩小字体硬塞。

## v1.2.0 - Printable A4 Workbook Delivery

### Added

- 默认将学习系统制作成 A4 竖版 PDF 和可编辑 DOCX。
- 新增内容审核 -> A4 排版 -> DOCX 渲染 -> PDF 转换 -> PDF 渲染 -> 修正的强制闭环。
- 新增 `references/a4-print-workflow.md`，规定页边距、字号、色彩、表格、书写区和文件命名。
- 新增题目区与答案区分离规则，避免打印练习时直接看到答案。
- 新增 `scripts/check_a4_pdf.py`，检查 A4 页面尺寸、方向、可打开性和近空白页。

## v1.1.0 - Precision and Adaptive Planning

- 收窄触发条件，增加三种输出规模、自适应算法、日期边界和平台适配。

## v1.0.0 - Initial Release

- 首次发布知识地图、主动回忆题和间隔复习规划能力。
