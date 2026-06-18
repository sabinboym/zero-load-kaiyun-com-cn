import json
import datetime

SITE_DATA = {
    "name": "开云综合站点",
    "url": "https://www.zero-load-kaiyun.com.cn",
    "keywords": ["开云", "零负载", "综合平台", "开源信息"],
    "tags": ["技术", "工具", "开放资源"],
    "description": "一个提供轻量级、零负载开云相关技术资源与信息的综合站点。"
}

def load_site_info(data: dict) -> dict:
    return {
        "site_name": data.get("name", "未命名"),
        "site_url": data.get("url", ""),
        "keywords": data.get("keywords", []),
        "tags": data.get("tags", []),
        "description": data.get("description", "无描述")
    }

def build_keyword_summary(keywords: list) -> str:
    if not keywords:
        return "暂无关键词"
    return ", ".join(keywords)

def build_tag_summary(tags: list) -> str:
    if not tags:
        return "未分类"
    return " | ".join(tags)

def generate_summary(site_info: dict) -> str:
    lines = []
    lines.append("=" * 48)
    lines.append("站点摘要报告")
    lines.append(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 48)
    lines.append(f"站点名称：{site_info['site_name']}")
    lines.append(f"URL：{site_info['site_url']}")
    lines.append(f"关键词：{build_keyword_summary(site_info['keywords'])}")
    lines.append(f"标签：{build_tag_summary(site_info['tags'])}")
    lines.append(f"说明：{site_info['description']}")
    lines.append("=" * 48)
    return "\n".join(lines)

def export_json_summary(site_info: dict) -> str:
    export = {
        "site": site_info["site_name"],
        "url": site_info["site_url"],
        "keywords": site_info["keywords"],
        "tags": site_info["tags"],
        "description": site_info["description"],
        "generated_at": datetime.datetime.now().isoformat()
    }
    return json.dumps(export, ensure_ascii=False, indent=2)

def main():
    info = load_site_info(SITE_DATA)
    print(generate_summary(info))
    print()
    print("JSON 格式输出：")
    print(export_json_summary(info))

if __name__ == "__main__":
    main()