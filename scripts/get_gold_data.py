#!/usr/bin/env python3
"""
黄金价格和ETF数据获取脚本
获取伦敦现货黄金、Au9999、黄金ETF等实时数据
"""

import yfinance as yf
import requests
import json
from datetime import datetime

def get_london_gold_price():
    """获取伦敦现货黄金价格"""
    try:
        gold = yf.Ticker("GC=F")  # 黄金期货
        data = gold.history(period="1d")
        if not data.empty:
            price = data['Close'].iloc[-1]
            return {
                "name": "伦敦现货黄金(期货)",
                "price": round(price, 2),
                "unit": "美元/盎司",
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "source": "Yahoo Finance"
            }
    except Exception as e:
        return {"error": f"获取伦敦金价失败: {str(e)}"}

def get_au9999_price():
    """获取Au9999价格"""
    try:
        # 使用东方财富API
        url = "https://api.finance.eastmoney.com/API/ChinaStockData/GetChinaStockData"
        params = {
            "code": "AU9999",
            "market": "SHFE"
        }
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "name": "黄金9999",
                "price": data.get("price", "N/A"),
                "unit": "元/克",
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "source": "东方财富"
            }
    except Exception as e:
        return {"error": f"获取Au9999价格失败: {str(e)}"}

def get_spdr_gld_holdings():
    """获取SPDR黄金ETF持仓量"""
    try:
        url = "https://www.spdrgoldshares.com/us/api/holdings.json"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "name": "SPDR黄金ETF (GLD)",
                "holdings": data.get("holdings", "N/A"),
                "unit": "吨",
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "source": "SPDR官方"
            }
    except Exception as e:
        return {"error": f"获取SPDR持仓失败: {str(e)}"}

def get_huaan_etf_data():
    """获取华安黄金ETF数据"""
    try:
        etf = yf.Ticker("518880.SS")  # 华安黄金ETF
        data = etf.history(period="5d")
        if not data.empty:
            latest = data.iloc[-1]
            return {
                "name": "华安黄金ETF (518880)",
                "price": round(latest['Close'], 3),
                "volume": int(latest['Volume']),
                "change_percent": round((latest['Close'] - latest['Open']) / latest['Open'] * 100, 2),
                "unit": "元",
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "source": "Yahoo Finance"
            }
    except Exception as e:
        return {"error": f"获取华安ETF数据失败: {str(e)}"}

def get_gold_minis():
    """获取小型黄金期货数据"""
    try:
        gold = yf.Ticker("MGC=F")  # 小型黄金期货
        data = gold.history(period="1d")
        if not data.empty:
            return {
                "name": "小型黄金期货",
                "price": round(data['Close'].iloc[-1], 2),
                "unit": "美元/盎司",
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "source": "Yahoo Finance"
            }
    except Exception as e:
        return {"error": f"获取小型期货失败: {str(e)}"}

def main():
    """主函数:获取所有黄金相关数据"""
    print("=" * 60)
    print("黄金市场数据")
    print("=" * 60)
    print(f"更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 伦敦现货黄金
    print("【价格数据】")
    london = get_london_gold_price()
    if "error" not in london:
        print(f"{london['name']}: {london['price']} {london['unit']}")
        print(f"  来源: {london['source']}")
    else:
        print(london["error"])

    # Au9999
    au9999 = get_au9999_price()
    if "error" not in au9999:
        print(f"{au9999['name']}: {au9999['price']} {au9999['unit']}")
        print(f"  来源: {au9999['source']}")
    else:
        print(au9999["error"])

    print()

    # ETF数据
    print("【ETF数据】")
    spdr = get_spdr_gld_holdings()
    if "error" not in spdr:
        print(f"{spdr['name']}: {spdr['holdings']} {spdr['unit']}")
        print(f"  来源: {spdr['source']}")
    else:
        print(spdr["error"])

    huaan = get_huaan_etf_data()
    if "error" not in huaan:
        print(f"{huaan['name']}: {huaan['price']} {huaan['unit']}")
        print(f"  涨跌幅: {huaan['change_percent']}%")
        print(f"  成交量: {huaan['volume']}")
        print(f"  来源: {huaan['source']}")
    else:
        print(huaan["error"])

    print()
    print("=" * 60)

if __name__ == "__main__":
    main()
