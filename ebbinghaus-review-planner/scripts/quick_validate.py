#!/usr/bin/env python3
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.2.0"
errors = []

required = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/review-schedules.md",
    "references/output-templates.md",
    "references/knowledge-card-types.md",
    "references/platform-adapters.md",
    "references/quality-checklist.md",
    "references/a4-print-workflow.md",
    "scripts/check_a4_pdf.py",
]

for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing runtime file: {rel}")

skill_path = ROOT / "SKILL.md"
skill = skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""
match = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
if not match:
    errors.append("SKILL.md has invalid YAML frontmatter")
else:
    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        errors.append(f"invalid YAML frontmatter: {exc}")
        frontmatter = {}
    if not isinstance(frontmatter, dict):
        errors.append("frontmatter must be a mapping")
        frontmatter = {}
    if set(frontmatter) != {"name", "description"}:
        errors.append("frontmatter must contain only name and description")
    if frontmatter.get("name") != "ebbinghaus-review-planner":
        errors.append("frontmatter name mismatch")
    description = frontmatter.get("description", "")
    if not isinstance(description, str) or not description.strip():
        errors.append("description is empty")
    if description != description.lower():
        errors.append("description must be lowercase")
    for phrase in ["explicitly wants", "do not invoke for summarization-only"]:
        if phrase not in description:
            errors.append(f"description missing trigger boundary: {phrase}")

for term in [
    VERSION,
    "快速版",
    "标准版",
    "完整版",
    "0-4",
    "最长间隔 90 天",
    "R0 与当天晚间任务间隔不足 2 小时时合并",
    "A4 竖版 PDF",
    "逐页审核",
    "题目区与答案区必须分开",
]:
    if term not in skill:
        errors.append(f"SKILL.md missing required rule: {term}")

for ref in re.findall(r"`(references/[^`]+\.md)`", skill):
    if not (ROOT / ref).is_file():
        errors.append(f"broken reference from SKILL.md: {ref}")

for rel in ["SKILL.md", "README.md", "VERSION.md", "CHANGELOG.md", "RELEASE_REPORT.md"]:
    path = ROOT / rel
    if path.exists() and VERSION not in path.read_text(encoding="utf-8"):
        errors.append(f"{rel} missing {VERSION}")

agent_path = ROOT / "agents/openai.yaml"
if agent_path.exists():
    try:
        agent = yaml.safe_load(agent_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"invalid agents/openai.yaml: {exc}")
        agent = {}
    interface = agent.get("interface", {}) if isinstance(agent, dict) else {}
    for key in ["display_name", "short_description", "default_prompt"]:
        if not interface.get(key):
            errors.append(f"agents/openai.yaml missing interface.{key}")

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if any(part in {".git", "__MACOSX", "__pycache__"} for part in path.parts) or path.name == ".DS_Store":
        errors.append(f"forbidden temporary path: {path.relative_to(ROOT)}")
    try:
        path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"non-UTF-8 file: {path.relative_to(ROOT)}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDATION PASSED")
print(f"Root: {ROOT}")
print(f"Version: {VERSION}")
print(f"Runtime files: {len(required)}")
