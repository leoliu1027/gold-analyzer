#!/usr/bin/env python3
"""
宏观经济数据获取脚本
获取美国CPI、PCE、就业、利率、汇率等关键经济指标
"""

import pandas as pd
import requests
from datetime import datetime, timedelta

class FredDataFetcher:
    """FRED经济数据库获取器"""

    def __init__(self):
        self.base_url = "https://api.stlouisfed.org/fred/series/observations"
        # 需要申请FRED API key
        self.api_key = "your_api_key_here"  # 替换为你的API key

    def get_series(self, series_id, start_date=None):
        """获取FRED数据序列"""
        if not start_date:
            start_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")

        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json",
            "observation_start": start_date
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                observations = data.get("observations", [])
                if observations:
                    latest = observations[-1]
                    return {
                        "series_id": series_id,
                        "value": latest.get("value"),
                        "date": latest.get("date"),
                        "real_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "source": "FRED (Federal Reserve Economic Data)"
                    }
        except Exception as e:
            return {"error": f"获取{series_id}失败: {str(e)}"}

def get_treasury_yields():
    """获取美债收益率"""
    fred = FredDataFetcher()

    print("【美债收益率】")
    yields_data = {
        "2年期国债": "DGS2",
        "10年期国债": "DGS10",
        "30年期国债": "DGS30"
    }

    for name, series_id in yields_data.items():
        data = fred.get_series(series_id)
        if "error" not in data and data.get("value"):
            print(f"{name}: {data['value']}% (截至{data['date']})")
        else:
            print(f"{name}: 数据获取失败")
    print()

def get_inflation_data():
    """获取通胀数据"""
    fred = FredDataFetcher()

    print("【通胀数据】")
    inflation_data = {
        "CPI同比": "CPIAUCSL",
        "核心CPI": "CPILFESL",
        "PCE物价指数": "PCEPI",
        "核心PCE": "DPCCRVGJ"
    }

    for name, series_id in inflation_data.items():
        data = fred.get_series(series_id)
        if "error" not in data and data.get("value"):
            print(f"{name}: {data['value']} (截至{data['date']})")
        else:
            print(f"{name}: 数据获取失败")
    print()

def get_employment_data():
    """获取就业数据"""
    fred = FredDataFetcher()

    print("【就业数据】")
    employment_data = {
        "失业率": "UNRATE",
        "非农就业人口": "PAYEMS",
        "劳动参与率": "CIVPART"
    }

    for name, series_id in employment_data.items():
        data = fred.get_series(series_id)
        if "error" not in data and data.get("value"):
            print(f"{name}: {data['value']} (截至{data['date']})")
        else:
            print(f"{name}: 数据获取失败")
    print()

def get_dollar_index():
    """获取美元指数"""
    import yfinance as yf

    try:
        dxy = yf.Ticker("DX-Y.NYB")  # 美元指数
        data = dxy.history(period="5d")
        if not data.empty:
            latest = data.iloc[-1]
            print(f"【美元指数(DXY)】")
            print(f"最新值: {round(latest['Close'], 2)}")
            print(f"涨跌幅: {round((latest['Close'] - latest['Open']) / latest['Open'] * 100, 2)}%")
            print()
    except Exception as e:
        print(f"获取美元指数失败: {str(e)}")

def get_exchange_rate():
    """获取人民币汇率"""
    import yfinance as yf

    try:
        # 离岸人民币
        usdcnh = yf.Ticker("USDCNH=X")
        data = usdcnh.history(period="5d")
        if not data.empty:
            latest = data.iloc[-1]
            print(f"【人民币汇率】")
            print(f"美元/离岸人民币: {round(latest['Close'], 4)}")
            print(f"涨跌幅: {round((latest['Close'] - latest['Open']) / latest['Open'] * 100, 2)}%")
            print()
    except Exception as e:
        print(f"获取汇率失败: {str(e)}")

def get_vix_index():
    """获取VIX恐慌指数"""
    import yfinance as yf

    try:
        vix = yf.Ticker("^VIX")
        data = vix.history(period="5d")
        if not data.empty:
            latest = data.iloc[-1]
            print(f"【VIX恐慌指数】")
            print(f"最新值: {round(latest['Close'], 2)}")
            print(f"涨跌幅: {round((latest['Close'] - latest['Open']) / latest['Open'] * 100, 2)}%")
            print()
    except Exception as e:
        print(f"获取VIX失败: {str(e)}")

def main():
    """主函数:获取所有宏观经济数据"""
    print("=" * 60)
    print("宏观经济数据")
    print("=" * 60)
    print(f"更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 美债收益率
    get_treasury_yields()

    # 通胀数据
    get_inflation_data()

    # 就业数据
    get_employment_data()

    # 美元指数
    get_dollar_index()

    # 人民币汇率
    get_exchange_rate()

    # VIX指数
    get_vix_index()

    print("=" * 60)
    print("\n注意: 部分数据需要FRED API key才能获取")
    print("申请地址: https://fred.stlouisfed.org/docs/api/api_key.html")

if __name__ == "__main__":
    main()
