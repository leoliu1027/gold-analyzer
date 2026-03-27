# 数据获取说明 - 免费版 vs 完整版

## 📊 当前数据源情况

### ✅ 免费数据(无需API Key)

| 数据类型 | 数据源 | 状态 | 更新频率 |
|---------|--------|------|---------|
| **国际金价** | metals.live API | ✅ 免费开放 | 实时 |
| **国内金价** | akshare (上海金交所) | ✅ 免费开放 | 交易时段 |
| **央行储备** | akshare (央行官网) | ✅ 免费开放 | 每月 |
| **宏观数据** | 公开数据源 | ✅ 历史数据 | 定期更新 |

### ❌ 需要API Key的数据

| 数据类型 | 数据源 | 是否必需 | 获取方式 |
|---------|--------|---------|---------|
| **ETF持仓** | 世界黄金协会 | ❌ 可选 | 需申请 |
| **美联储详细数据** | FRED API | ❌ 可选 | 免费注册 |
| **CFTC持仓** | CFTC官网 | ❌ 可选 | 公开数据 |
| **实时新闻** | 新闻API | ❌ 可选 | 付费服务 |

---

## 🎯 使用建议

### 方案1: 完全免费(当前版本) ⭐推荐

**优点**:
- ✅ 无需任何注册
- ✅ 开箱即用
- ✅ 数据足够分析

**包含**:
- 国际金价实时数据
- 国内金价数据
- 央行储备数据
- 基础宏观数据(历史)

**适合**: 个人投资者、一般分析

### 方案2: 增强版(可选)

**需要申请的API Key**:

#### 1. FRED API (美联储经济数据)
```bash
# 免费注册
https://fred.stlouisfed.org/docs/api/api_key.html

# 获取API Key后,设置环境变量
export FRED_API_KEY="your_api_key_here"
```

**可获得**:
- 详细的美联储利率历史
- 美债收益率曲线
- 经济指标数据

#### 2. Alpha Vantage (综合金融数据)
```bash
# 免费注册
https://www.alphavantage.co/support/#api-key

# 设置环境变量
export ALPHA_VANTAGE_KEY="your_api_key_here"
```

**可获得**:
- 商品期货数据
- 技术指标
- 历史价格数据

#### 3. News API (新闻数据)
```bash
# 免费注册
https://newsapi.org/register

# 设置环境变量
export NEWS_API_KEY="your_api_key_here"
```

**可获得**:
- 实时黄金新闻
- 市场情绪分析
- 新闻情感评分

---

## 💡 实际使用对比

### 免费版分析能力

**十维度分析**:
- ✅ ① 地缘风险: 通过网络搜索
- ✅ ② 股市波动: 通过网络搜索
- ⚠️ ③ 期货持仓: 基础数据或搜索
- ✅ ④ 技术面: 基于价格数据
- ✅ ⑤ 实际利率: 历史数据+搜索
- ✅ ⑥ 通胀: 历史数据+搜索
- ✅ ⑦ 就业: 历史数据+搜索
- ✅ ⑧ 人民币汇率: 历史数据
- ✅ ⑨ 美债赤字: 公开数据
- ✅ ⑩ 央行购金: 完整数据

**结论**: 免费版可以进行**完整的十维度分析**!✅

---

## 🔧 如何升级到增强版

### 步骤1: 申请API Key

```bash
# FRED API (推荐)
访问: https://fred.stlouisfed.org/docs/api/api_key.html
注册 → 获取Key → 复制
```

### 步骤2: 配置环境变量

```bash
# 方式A: 临时设置(当前会话)
export FRED_API_KEY="your_key_here"

# 方式B: 永久设置
echo 'export FRED_API_KEY="your_key_here"' >> ~/.zshrc
source ~/.zshrc

# 方式C: 创建.env文件
echo 'FRED_API_KEY=your_key_here' > ~/.claude/skills/gold-analyzer/.env
```

### 步骤3: 修改代码使用API

在`lib/gold_data_api.py`中添加:

```python
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
FRED_KEY = os.getenv('FRED_API_KEY')

def get_fred_data(self, series_id):
    """从FRED获取数据"""
    url = f"https://api.stlouisfed.org/fred/series/observations"
    params = {
        'series_id': series_id,
        'api_key': FRED_KEY,
        'file_type': 'json'
    }
    response = self.session.get(url, params=params)
    return response.json()
```

---

## 📊 数据质量对比

| 维度 | 免费版 | 增强版 |
|------|--------|--------|
| **实时性** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **准确性** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **完整性** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **历史数据** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **成本** | 💰 免费 | 💰 $0-50/月 |

---

## ✅ 最终建议

### 对于大多数用户:
**使用免费版即可!** ✅
- 核心数据完整
- 分析功能齐全
- 无需配置

### 适合增强版的场景:
- 🏢 专业投资机构
- 📊 量化交易系统
- 📈 需要历史回测
- 🔄 高频数据分析

---

## 🎓 总结

**关键点**:
1. ✅ 免费版已经可以进行完整的十维度分析
2. ✅ 不需要任何API Key即可使用
3. 💡 宏观数据通过公开数据源+网络搜索获取
4. 🚀 API Key是可选增强,不是必需的

**当前实现**:
- 所有核心数据都可以**免费获取**
- 宏观数据使用**公开历史数据+网络搜索**
- 分析功能**不受限制**

---

**结论**: 当前版本**不需要API Key**就能正常使用! 🎉
