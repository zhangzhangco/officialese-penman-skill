# 正式文稿开篇写作 Skill

这是一个面向中文正式写作的可复用 Skill，适合生成和修改：

- 专著序言、前言
- 研究报告导言
- 项目申报背景
- 项目总结与验收报告开篇
- 行业白皮书
- 技术方案
- 标准解读
- 教材导言
- 成果发布词

## 使用方法

将整个文件夹放入支持 Skill 的工具目录中，入口文件为 `SKILL.md`。

也可以直接把 `SKILL.md` 和所需模板提供给模型，并给出类似指令：

> 使用 formal-preface-writing Skill，根据以下材料写一篇 1500 字的研究报告前言。

## 推荐读取顺序

1. `SKILL.md`
2. `references/intake_fields.md`
3. 选择一个 `templates/` 中的模板
4. 根据需要读取 `references/scene_adaptations.md`
5. 完成后按 `references/quality_checklist.md` 检查

## 文件结构

```text
formal-preface-writing-skill/
├── SKILL.md
├── README.md
├── manifest.txt
├── templates/
├── references/
├── examples/
└── scripts/
```

## AI Agent 导入说明 (AI Agent Integration)

本 Skill 遵循开源的 `SKILL.md` 规范，可以被直接导入到兼容该规范的 AI Agent 平台（如 Antigravity IDE、Cursor、Claude Code 等）。

### 1. 本地安装到 Antigravity IDE / CLI
将本项目克隆到您的自定义插件/Skill 目录下：
```bash
cd ~/.gemini/config/plugins/
git clone https://github.com/zhangzhangco/formal-preface-writing-skill.git
```

### 2. 在其他 AI 助手（如 Claude / ChatGPT）中使用
直接将 [SKILL.md](SKILL.md) 的内容拷贝作为 Prompt（提示词）提供给 AI，并执行类似指令：
> “使用 formal-preface-writing Skill，根据以下材料写一篇 1500 字的研究报告前言。”

---

## 自动自检工具 (Automated Verification)

项目内置了占位符自检脚本，在文稿生成后，可确保不遗留任何类似 `[项目名称]` 或 `〔待补全〕` 的方括号占位符：
```bash
python3 scripts/check_placeholders.py <您的文稿文件.md>
```

