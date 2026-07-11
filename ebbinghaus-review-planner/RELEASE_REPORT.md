# RELEASE REPORT

Version: v1.2.0
Package output: skill.zip

## 本版完成

1. 将 A4 可打印文件设为默认最终交付，而不是可选导出。
2. 默认同时生成 PDF 打印版和 DOCX 可编辑版。
3. 新增排版前内容审核和排版后逐页视觉审核。
4. 新增 A4 页面、页边距、字号、颜色、表格和书写空间规范。
5. 新增题目区与答案区分离，保护主动回忆效果。
6. 新增封面、说明、练习、计划、记录和答案的完整手册结构。
7. 新增 PDF A4 尺寸与近空白页自动预检脚本。
8. 新增分册规则，避免超长资料形成不可打印的大文件。

## Validation targets

- SKILL.md frontmatter only contains name and description.
- Version consistency is v1.2.0.
- All referenced files exist.
- Required files are UTF-8.
- A4 PDF preflight script runs successfully on a valid sample.
- No temporary or forbidden paths are packaged.
- Official skill validator passes before packaging.
