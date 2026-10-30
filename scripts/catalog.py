#!/usr/bin/env python3
"""Read the skill's local catalog. No network or account access."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="列出品牌或产品的完整执行卡")
    parser.add_argument("--brand", help="品牌 ID；不填则先介绍十个品牌")
    parser.add_argument("--product", help="精确产品 ID")
    parser.add_argument("--json", action="store_true", help="输出结构化 JSON")
    args = parser.parse_args()
    data = json.loads((Path(__file__).resolve().parents[1] / "references/catalog.json").read_text(encoding="utf-8"))
    brands = data["brands"]
    if args.brand:
        brands = [b for b in brands if b["id"] == args.brand]
        if not brands:
            parser.error("品牌 ID 不存在；不填参数可查看十个品牌")
    if args.product:
        products = [dict(p, brand=b["id"]) for b in brands for p in b["products"] if p["id"] == args.product]
        if not products:
            parser.error("产品 ID 不存在或不属于所选品牌")
        print(json.dumps(products[0], ensure_ascii=False, indent=2))
    elif args.json:
        print(json.dumps(brands if args.brand else [{k: b[k] for k in ("id", "name", "summary")} for b in brands], ensure_ascii=False, indent=2))
    else:
        for index, b in enumerate(brands, 1):
            print(f"{index}. {b['name']} [{b['id']}]：{b['summary']}")
            if args.brand:
                for p in b["products"]:
                    print(f"   {p['id']} | {p['name']} | {'/'.join(p['routes'])} | {p['purpose']}")


if __name__ == "__main__":
    main()
