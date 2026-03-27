# Gold-Analyzer Skill - 独立版本

## 📋 Skill说明

这是一个**完全独立**的黄金市场分析skill,无需外部项目依赖。

## 🚀 快速开始

### 1. 安装依赖

```bash
cd ~/.claude/skills/gold-analyzer
pip install -r lib/requirements.txt
```

### 2. 测试数据获取

```bash
python fetch_gold_data.py
```

### 3. 在Claude Code中使用

直接提问:
- "分析当前黄金市场"
- "金价走势如何"
- "现在适合买黄金吗"

## 📁 目录结构

```
gold-analyzer/
├── SKILL.md                    # Skill配置文件
├── fetch_gold_data.py          # 数据获取脚本 ⭐
├── README_SKILL.md             # 本文档
└── lib/
    ├── gold_data_api.py        # 独立API客户端
    └── requirements.txt        # 依赖包
```

## 🎯 核心特性

- ✅ **完全独立**: 无需golddata项目
- ✅ **即插即用**: 复制skill目录即可使用
- ✅ **自动获取**: 自动调用脚本获取最新数据
- ✅ **多数据源**: 国际金价、上海金交所、央行储备
- ✅ **十维度分析**: 地缘、经济、技术面全面分析

## 📊 数据获取流程

```
用户提问
    ↓
运行 fetch_gold_data.py
    ↓
调用 lib/gold_data_api.py
    ↓
获取网络数据 + akshare数据
    ↓
返回JSON格式数据
    ↓
基于十维度模型分析
    ↓
生成投资建议
```

## 🔧 依赖说明

### 必需依赖
- `requests`: HTTP请求
- `akshare`: 中国金融数据(上海金交所、央行储备)

### 可选依赖
- 无!这就是全部依赖

## 📈 数据来源

| 数据类型 | 数据源 | 更新频率 |
|---------|--------|---------|
| 国际金价 | metals.live API | 实时 |
| 国内金价 | akshare (上海金交所) | 交易时段实时 |
| 央行储备 | akshare (央行官网) | 每月 |
| 宏观经济 | 网络搜索 | 实时 |

## ⚠️ 注意事项

1. **首次使用**: 需要安装依赖 `pip install -r lib/requirements.txt`
2. **网络要求**: 需要能访问外网API
3. **akshare**: 用于获取国内数据,如失败会提示安装
4. **数据时效**: 建议每次分析前运行fetch脚本

## 🔄 与项目版本的区别

| 特性 | 独立版本(skill内) | 项目版本(golddata/) |
|------|------------------|-------------------|
| 位置 | `~/.claude/skills/` | `/path/to/golddata/` |
| 依赖 | requests+akshare | 完整项目环境 |
| ETF数据 | ❌ | ✅ |
| 历史数据 | ❌ | ✅ |
| 独立性 | ✅ 完全独立 | ❌ 依赖项目 |
| 适用场景 | 通用skill | 开发/完整分析 |

## 🛠 故障排除

### 问题1: akshare未安装
```bash
pip install akshare
```

### 问题2: 网络API失败
- 检查网络连接
- 脚本会使用fallback数据

### 问题3: 导入错误
```bash
# 确保在skill目录运行
cd ~/.claude/skills/gold-analyzer
python fetch_gold_data.py
```

## 📝 更新日志

### v2.0 (2026-03-27)
- ✅ 完全重构为独立版本
- ✅ 移除项目依赖
- ✅ 添加独立API客户端
- ✅ 简化部署流程

### v1.0 (2026-03-21)
- 初始版本,依赖golddata项目

## 🎓 使用示例

### 示例1: 快速分析
```
用户: 分析当前黄金市场

Claude:
[运行 fetch_gold_data.py 获取数据]
→ 国际金价: $4,395/盎司
→ 国内金价: ¥705.8/克
→ 央行储备: 7,422万盎司

[基于十维度模型分析]
→ 投资信号: 持有观望
→ 风险提示: ...
```

### 示例2: 价格查询
```
用户: 现在金价多少?

Claude:
[运行 fetch_gold_data.py]
→ 国际: $4,395/盎司
→ 国内: ¥705.8/克 (Au99.99)
→ 更新时间: 2026-03-27 09:00
```

## 📧 技术支持

如遇问题:
1. 检查依赖是否安装
2. 查看错误日志
3. 确认网络连接
4. 查看SKILL.md了解详细用法

---

**总结**: 这是一个完全独立的skill,无需任何外部项目,开箱即用! 🎉
