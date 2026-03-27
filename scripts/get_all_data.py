#!/usr/bin/env python3
"""
完整环境背景数据获取脚本
获取十维度分析所需的全部数据并生成评分
"""

import subprocess
import json
from datetime import datetime

def run_script(script_name):
    """运行数据获取脚本"""
    try:
        result = subprocess.run(
            ["python", f"/Users/liuhuihui/.claude/skills/gold-analyzer/scripts/{script_name}"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Exception: {str(e)}"

def get_environment_score():
    """
    环境背景十维度评分模型
    返回各维度评分和分析结论
    """

    scores = {
        "① 地缘风险": {"score": 0.5, "weight": 0.10, "analysis": "需要最新地缘政治新闻分析"},
        "② 股市波动": {"score": 0.5, "weight": 0.10, "analysis": "需要VIX和股市数据"},
        "③ 期货持仓": {"score": 0.5, "weight": 0.10, "analysis": "需要CFTC和ETF持仓数据"},
        "④ 技术面": {"score": 0.5, "weight": 0.10, "analysis": "需要黄金价格和技术指标"},
        "⑤ 实际利率": {"score": 0.5, "weight": 0.15, "analysis": "需要美债收益率和通胀数据"},
        "⑥ 通胀": {"score": 0.5, "weight": 0.15, "analysis": "需要CPI/PCE数据"},
        "⑦ 就业": {"score": 0.5, "weight": 0.10, "analysis": "需要非农和失业率数据"},
        "⑧ 人民币汇率": {"score": 0.5, "weight": 0.08, "analysis": "需要USDCNH汇率数据"},
        "⑨ 美债赤字": {"score": 0.5, "weight": 0.06, "analysis": "需要美债规模数据"},
        "⑩ 央行购金": {"score": 0.5, "weight": 0.06, "analysis": "需要全球央行购金数据"}
    }

    # 计算加权总分
    total_score = sum(item["score"] * item["weight"] for item in scores.values())

    return scores, total_score

def generate_signal(total_score):
    """根据总分生成投资信号"""

    if total_score >= 0.7:
        signal = "强烈买入"
        strength = "强"
        advice = "市场环境高度利好黄金,建议增加黄金配置"
    elif total_score >= 0.5:
        signal = "买入/增持"
        strength = "中"
        advice = "市场环境利好黄金,建议维持或增加配置"
    elif total_score >= 0.4:
        signal = "持有观望"
        strength = "中"
        advice = "市场环境中性,建议持有现有仓位"
    elif total_score >= 0.3:
        signal = "减持/谨慎"
        strength = "中"
        advice = "市场环境偏空,建议谨慎操作或减持"
    else:
        signal = "卖出/规避"
        strength = "强"
        advice = "市场环境不利黄金,建议减少或规避黄金投资"

    return signal, strength, advice

def main():
    """主函数:生成完整环境背景分析报告"""

    print("=" * 80)
    print("黄金市场环境背景分析报告")
    print("=" * 80)
    print(f"报告时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 获取数据
    print("正在获取市场数据...")
    print()

    gold_data = run_script("get_gold_data.py")
    print(gold_data)
    print()

    macro_data = run_script("get_macro_data.py")
    print(macro_data)
    print()

    # 生成评分
    print("=" * 80)
    print("环境背景十维度分析")
    print("=" * 80)
    print()

    scores, total_score = get_environment_score()

    # 短期交易属性
    print("【短期交易属性】(1-3个月周期)")
    for i in range(1, 5):
        key = f"0{i} " + list(scores.keys())[i-1].split(" ", 1)[1]
        item = list(scores.values())[i-1]
        score_level = "利好" if item["score"] == 1 else "中性" if item["score"] == 0.5 else "利空"
        print(f"{key}: {score_level} (权重{item['weight']*100:.0f}%)")
        print(f"  分析: {item['analysis']}")
    print()

    # 中期金融属性
    print("【中期金融属性】(4-6个月周期)")
    for i in range(4, 7):
        key = f"0{i} " + list(scores.keys())[i-1].split(" ", 1)[1]
        item = list(scores.values())[i-1]
        score_level = "利好" if item["score"] == 1 else "中性" if item["score"] == 0.5 else "利空"
        print(f"{key}: {score_level} (权重{item['weight']*100:.0f}%)")
        print(f"  分析: {item['analysis']}")
    print()

    # 长期货币属性
    print("【长期货币属性】(6个月以上周期)")
    for i in range(7, 10):
        key = f"0{i} " + list(scores.keys())[i-1].split(" ", 1)[1]
        item = list(scores.values())[i-1]
        score_level = "利好" if item["score"] == 1 else "中性" if item["score"] == 0.5 else "利空"
        print(f"{key}: {score_level} (权重{item['weight']*100:.0f}%)")
        print(f"  分析: {item['analysis']}")
    print()

    # 总分和信号
    print("=" * 80)
    print("投资信号")
    print("=" * 80)
    print()

    signal, strength, advice = generate_signal(total_score)

    print(f"综合评分: {total_score:.2f}/1.00")
    print(f"投资信号: {signal}")
    print(f"信号强度: {strength}")
    print(f"操作建议: {advice}")
    print()

    # 输出JSON格式
    report = {
        "timestamp": datetime.now().isoformat(),
        "scores": {k: v["score"] for k, v in scores.items()},
        "total_score": round(total_score, 3),
        "signal": signal,
        "strength": strength,
        "advice": advice
    }

    # 保存到文件
    with open("/Users/liuhuihui/.claude/skills/gold-analyzer/latest_report.json", "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print("=" * 80)
    print("报告已保存到: latest_report.json")
    print("=" * 80)

if __name__ == "__main__":
    main()
