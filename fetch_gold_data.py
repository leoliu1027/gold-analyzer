#!/usr/bin/env python3
"""
数据获取脚本 - 独立版本
为gold-analyzer skill提供数据支持

使用方法:
    python fetch_gold_data.py
"""
import sys
import os
import json

# 添加lib目录到路径
skill_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(skill_dir, 'lib')
if lib_dir not in sys.path:
    sys.path.insert(0, lib_dir)

from gold_data_api import GoldDataAPI

def main():
    """主函数"""
    from datetime import datetime

    print("=" * 60)
    print("黄金数据获取工具 (独立版本)")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()

    api = GoldDataAPI()
    result = api.get_all_data()

    # 打印关键信息
    print("数据摘要:")
    print("-" * 60)

    if 'spot' in result['data']:
        spot = result['data']['spot']
        print(f"✓ 国际金价: ${spot['price_usd']:.2f}/盎司")

    if 'sge' in result['data']:
        sge = result['data']['sge']
        print(f"✓ 国内金价: ¥{sge['price_cny']:.2f}/克 ({sge['product_id']})")

    if 'reserves' in result['data']:
        reserves = result['data']['reserves']
        print(f"✓ 央行储备: {reserves['gold_reserves']:.0f}万盎司 ({reserves['month']})")

    if result['warnings']:
        print()
        print("⚠ 警告:")
        for warning in result['warnings']:
            print(f"  - {warning}")

    if result['errors']:
        print()
        print("✗ 错误:")
        for error in result['errors']:
            print(f"  - {error}")

    print()
    print("=" * 60)
    print("完整JSON数据:")
    print("=" * 60)
    print(json.dumps(result, indent=2, ensure_ascii=False))

    return 0 if result['data'] else 1

if __name__ == '__main__':
    sys.exit(main())
