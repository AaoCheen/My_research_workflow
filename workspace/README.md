# 实际工作区

这个目录用于放真实项目和 LLM 对话，**只有本说明文件纳入 Git**。`workspace/<project>/` 默认忽略，因此普通 `git add` 和 `git push` 不会上传这里的具体研究材料。

建议的新项目结构：

```text
workspace/
  my-project/
    PROJECT.md                        # 目标、路径、当前阶段与下一步
    sessions/
      YYYY-MM-DD_topic.md             # 原始对话导出、摘录或标明类型的摘要
    brainstorming/
      paper/
        pdf/
        md/
        metadata/
      idea/
        001-topic/                    # 原稿、版本和 decisions.md
      idea_review/
        001-topic/                    # 版本评审、pilot 计划/结果、交接
    writing/                          # 正文、引用及其他写作产物
    experiments/                      # 需要时使用；已有工程则复用实际工程路径
```

只按当前任务创建目录。已有 TAFFC 或其他研究项目直接在原目录工作，不需要再复制一份到这里；原项目也可以按需要使用 `PROJECT.md` 与 `sessions/` 的约定。

可复制的模板：

- [项目说明](../workflow/templates/PROJECT.md)
- [会话记录](../workflow/templates/session.md)

对话保存需要手动导出，或明确让 LLM 写入摘要；文件夹本身不会自动抓取聊天记录。会话记录帮助恢复上下文，idea 决策、正式稿件和实测日志仍保留各自的依据。

本地工作区没有通过这个仓库备份。删除临时目录前，把需要保留的项目与对话移回自己的长期项目目录。
