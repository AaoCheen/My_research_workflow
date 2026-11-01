---
name: marker-pdf-to-md
description: 使用本机已配置的 Marker 将单篇或一批 PDF 转成带图片的 Markdown，检查产物与页数；用于论文阅读库，不用于论文改写或工具安装。
---

# Marker PDF → Markdown

使用我已配置好的 Marker 环境。这里只记录调用和验收方法；工具、模型、缓存和辅助脚本保留在 `/data0/ca/datasets/marker/`，不复制进研究项目或本仓库。

## 转换

先确认本轮要转换的 PDF 和输出位置。以下绝对路径入口会加载本机专用环境，避免误用其他环境中的 `marker`。输入、输出参数也可以使用相对于当前工作目录的路径。

批量转换：

```bash
bash /data0/ca/datasets/marker/source/local_tools/convert_papers_marker.sh \
  /absolute/project/brainstorming/paper/pdf \
  /absolute/project/brainstorming/paper/md
```

单篇转换：

```bash
bash /data0/ca/datasets/marker/source/local_tools/convert_papers_marker.sh \
  /absolute/project/brainstorming/paper/pdf/paper.pdf \
  /absolute/project/brainstorming/paper/md
```

入口根据输入类型选择 `marker` 或 `marker_single`，默认使用 CPU、`--mode fast --disable_ocr`，不调用远程付费 LLM。目录模式使用两个 worker、跳过已有结果，且输入目录的普通文件必须都是 PDF，子目录会被忽略。单篇模式会重新生成该篇输出，重跑前先确认是否需要保留已有结果。

每篇输出在 `md/<PDF主文件名>/` 下，包含同名 `.md`、`<PDF主文件名>_meta.json` 及可能提取的图片。移动、阅读或交付 Markdown 时，一起保留其图片与 metadata；不要把其他解析器的纯文本提取称为 Marker 转换结果。

其余 Marker 参数可以追加在命令末尾，先查看入口说明或当前 CLI 支持的选项：

```bash
bash /data0/ca/datasets/marker/source/local_tools/convert_papers_marker.sh --help
```

## 验收

对本轮已转换的 PDF 目录运行：

```bash
/data0/ca/datasets/marker/venv/bin/python \
  /data0/ca/datasets/marker/source/local_tools/validate_marker_outputs.py \
  --pdf-dir /absolute/project/brainstorming/paper/pdf \
  --md-dir /absolute/project/brainstorming/paper/md \
  --manifest /absolute/project/brainstorming/paper/metadata/marker_conversion_manifest.json \
  --path-root /absolute/project
```

验收脚本检查指定 PDF 目录中的所有 PDF：Markdown 必须非空，`_meta.json` 的页数须与原 PDF 一致；存在缺失或不匹配时返回非零。只转换了单篇时，要注意同目录其他 PDF 也会进入验收范围。

清单使用 `--path-root` 尽可能保存项目相对路径。清单中的 mode、OCR 和 device 字段描述辅助脚本的默认配置，不是从已有产物恢复的实际运行参数；版本号属于执行验收的环境。

同时抽查标题、摘要、正文及当前研究关注的表格、公式和图片。页数一致不能证明文字完整或内容正确。该默认配置适合有正常文字层的数字论文；扫描页、图内文字、部分标题、公式和复杂表格可能缺失，应回查 PDF 并记录限制。需要 OCR 时先确认当前 CLI 与已有环境支持的服务和模型，不把默认关闭 OCR 的运行说成完整 OCR 解析。

Marker 可能为复用而启动本地 CPU 布局服务。若本轮要求清理，只停止能确认由本次调用启动的服务，保留已有作业。

## 直接调用原生 CLI

需要自行指定原生参数时：

```bash
source /data0/ca/datasets/marker/source/local_tools/marker_env.sh
marker_single /absolute/paper.pdf \
  --output_dir /absolute/output --mode fast --disable_ocr
```
