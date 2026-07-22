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
