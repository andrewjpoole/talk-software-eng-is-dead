- Serena (semantic search, edit, refactor and debugging, 40 languages LSP) much better than grepping
- codebase-memory-mcp (treesitter, indexes code tree into sqllite, 155 languages) read only tools, "120x fewer tokens" vs grepping
- RTK (CLI proxy, intercepts filters and compresses command outputs before reaching LLM) "reduces token consumption 60-90%"
- caveman (reduces output tokens, "why use many token when few do trick") "cuts 75% of output tokens, brain still big, mouth small!"

- Agent = model + harness
- Harness = orchestration loop + tool execution and sandboxing + context management + state & memory persistence + guard rails & safety
