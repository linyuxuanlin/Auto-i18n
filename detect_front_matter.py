import re

markdown_text = """
---
title: "尝试健身"
date: "2023-09-09 12:06:56"
tags:
  - 生活
  - tag2
  - tag3
categories: ["Life is Beautiful", "人间值得"]
featured: true
slug: "20230909"
---
这里是文章的正文内容...
"""

front_matter_pattern = r"---(.*?)---"  # 匹配 front matter 区域
parameter_pattern = r'(\w+):\s*((?:"[^"]*")|(?:\[[^\]]*\])|(?:[^\n\r]+)|(?:true|false))'  # 匹配参数名和参数值

front_matter_match = re.search(front_matter_pattern, markdown_text, re.DOTALL)

if front_matter_match:
    front_matter_content = front_matter_match.group(1)
    parameter_matches = re.findall(parameter_pattern, front_matter_content)

    front_matter_data = {}
    for param_name, param_value in parameter_matches:
        # 去掉引号（如果有）
        if param_value.startswith('"') and param_value.endswith('"'):
            param_value = param_value[1:-1]
        # 如果值是以 "[" 开头，表示这是一个列表
        if param_value.startswith("["):
            param_value = [item.strip(' "[]') for item in param_value.split(',')]
        # 如果值是 "true" 或 "false"，转换为相应的布尔值
        elif param_value == "true":
            param_value = True
        elif param_value == "false":
            param_value = False

        front_matter_data[param_name] = param_value

    print("Front Matter 数据:")
    for key, value in front_matter_data.items():
        print(f"{key}: {value}")
else:
    print("未找到 Front Matter 区域。")

# 你可以将 front_matter_data 存储到变量中，然后使用其中的数据进行后续处理
