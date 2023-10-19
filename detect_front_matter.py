import re
import yaml

markdown_text = """
---
title: "文章标题"
date: "2023-09-09 12:06:56"
tags: 
  - 标签1
  - 标签2
categories: ["分类1", "分类2"]
featured: true
slug: "文章摘要"
---
正文
"""

# 使用正则表达式来匹配front matter
front_matter_match = re.search(r'---\n(.*?)\n---', markdown_text, re.DOTALL)

if front_matter_match:
    front_matter_text = front_matter_match.group(1)
    # 使用PyYAML加载YAML格式的数据
    front_matter_data = yaml.safe_load(front_matter_text)

    # 打印front matter的参数与对应的值
    print("Front Matter 数据:")
    for key, value in front_matter_data.items():
        if isinstance(value, bool):
            print(f"{key}: {value}")
        else:
            if isinstance(value, list):
                value_str = ', '.join([str(v) for v in value])
            else:
                value_str = str(value)
            print(f'{key}: "{value_str}"')
