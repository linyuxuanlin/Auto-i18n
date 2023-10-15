# Auto-i18n

Auto translate Markdown files to multi languages using ChatGPT | 使用 ChatGPT 自动将 Markdown 文件批量翻译为多语言

程序执行的逻辑：

1. 程序会默认翻译 dir_to_translate 下的所有 Markdown 文件，如果有不需要翻译的文件，请加进 exclude_list 变量中
2. 经程序处理过的文件，文件名会被加进自动生成的 `processed_list.txt` 中，下次默认不进行处理。
3. 原本就用英文撰写的文章，不会被重新翻译为英文，也不会翻译回中文，会翻译为其他语言。需要在文章中添加字段 `> This post was originally written in English.`（注意上下需各留一个空行），以便程序识别。
4. 如果某篇文章需要重新翻译（例如翻译结果不完备，或文章内容有修改），可在文章中加入字段 `[translate]`（注意上下需各留一个空行）。这个操作将不理会 exclude_list 与 processed_list 规则，仅遵守规则3（如果原本为英文，则不会被重新翻译为英语），进行翻译处理

待解决的问题：

1. 如果 Markdown 文件包含 Front Matter，可能也会被翻译而造成问题。我的解决方法是不适用 Front Matter，直接用一级标题作为文章标题。
2. 如果文章不完整，可能会出现 ChatGPT 帮你翻译并续写的情况，需要手动验证
3. 在某些特殊的情况下，可能会出现翻译不正确或某些字段没有翻译的情况，需进行验证并手动调整
