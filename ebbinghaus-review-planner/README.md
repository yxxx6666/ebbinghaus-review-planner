# 艾宾浩斯复习计划表

`ebbinghaus-review-planner` 把书籍、PDF、课程、讲义、教材和培训资料，转成零基础教学卡、知识地图、主动回忆题、每日唯一任务、自适应复习日期，以及经过逐页审核的 A4 学习手册。

Current version: v1.4.0

## 适用场景

- 完全不会，想从零开始学习一本书或一套教材
- 考试、考证、课程和长期记忆
- 企业培训、产品知识、SOP 和销售话术
- 书籍、论文、讲义与学习笔记
- A4 学习手册、练习册和复习打卡表

## v1.4.0 核心升级

- DOCX 作为唯一母版，PDF 从最终 DOCX 直接转换，避免两套文件内容和版式不一致。
- 新增 DOCX 空白页、连续分页符、标题样式、动态页码和过小字号预检。
- 新增 DOCX/PDF 文本一致性检查，默认覆盖率至少 97%。
- 普通正文不得小于 10 磅，表格和答案正文不得小于 9.5 磅。
- 禁止英文单词、K/Q 编号、题号范围和日期被拆断。
- 零基础模式下，所有 A 级知识点必须先有教学卡，再进入正式练习。
- 首页解释 K = Knowledge、Q = Question。
- 逐题评分；每日任务表只记录当日最低分。
- 自适应间隔统一向上取整。
- R0 明确为学习后等待约 20 分钟，再做 3-5 分钟闭卷回忆。

## 核心输出

- 范围覆盖表：精读、略读、选读、暂不读
- 零基础教学卡：大白话、正例、反例、拆解、引导练习、独立练习、迁移应用
- 知识地图：K001 等知识点与 Q001 等题目映射
- 主动回忆与应用练习
- 每日唯一任务和当日最低分
- 自适应复习记录和下一次具体日期
- A4 DOCX 可编辑版和由同一 DOCX 转换的 PDF 打印版

## 验证脚本

```bash
python scripts/quick_validate.py .
python scripts/check_docx_workbook.py output.docx --require-headings --require-page-numbers
python scripts/check_a4_pdf.py output.pdf --require-page-numbers
python scripts/check_output_pair.py output.docx output.pdf --min-coverage 0.97
```

## 不适用场景

只总结、翻译、润色、提取或转换文件时不应触发，除非用户同时明确要求建立学习或复习系统。
