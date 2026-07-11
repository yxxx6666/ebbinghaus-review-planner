# RELEASE REPORT

Version: v1.4.0
Package output: skill.zip

## 本版完成

1. 将 DOCX 明确为唯一母版，PDF 必须从最终 DOCX 直接转换。
2. 新增 DOCX 空白页、连续分页符、标题样式、页码和字号预检。
3. 新增 DOCX/PDF 正文覆盖率检查，默认不少于 97%。
4. 普通正文最低 10 磅，表格和答案正文最低 9.5 磅。
5. 禁止英文单词、K/Q 编号、题号范围和日期被拆断。
6. 零基础模式覆盖所有 A 级知识点的教学卡。
7. 首页增加 K/Q 编号说明。
8. 每日任务只记录当日最低分，详细评分按每个 K/Q 记录。
9. 自适应间隔改为向上取整。
10. R0 的等待时间和实际练习时间拆开说明。

## Validation targets

- SKILL.md frontmatter only contains name and description.
- Version consistency is v1.4.0.
- All referenced files exist and use UTF-8.
- Study-plan fixtures pass/fail as expected.
- DOCX preflight self-test passes.
- DOCX/PDF pair checker self-test passes.
- No temporary or forbidden paths are packaged.
