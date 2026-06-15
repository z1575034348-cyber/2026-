# 世界杯球队关系星图 ⚽

> 2026 美加墨世界杯 16 支热门球队的**关系可视化交互图谱**

在线吃瓜，深挖足球队内的内讧、矛盾、派系与默契——所有数据基于真实新闻事件。

## 🎯 功能特色

- **16 支球队**：比利时、法国、英格兰、葡萄牙、阿根廷、巴西、西班牙、德国、荷兰、意大利、美国、韩国、墨西哥、喀麦隆、塞尔维亚、乌拉圭
- **暗黑星空主题**：力导向关系图 + 星空粒子背景
- **真实头像**：Wikipedia API 自动获取球员高清头像
- **八卦红线**：点击红色连线弹出"吃瓜大讲堂"，含完整事件详情和媒体来源
- **关系分类**：🔴矛盾/🟡黄金搭档/🟢密友/⚪普通
- **搜索 + 筛选**：搜索球员、按位置分组、只看大瓜模式
- **聚焦高亮**：点击节点淡化无关元素
- **移动端适配**：手机端底部抽屉式信息面板
- **零外网依赖**：Vis.js 本地加载

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/你的用户名/worldcup-star-map.git
cd worldcup-star-map

# 2. 启动服务
python run_server.py

# 3. 浏览器打开
# http://localhost:8080
```

## 📁 项目结构

```
├── index.html              # 主页面（暗黑星图）
├── run_server.py           # 本地服务器（自动端口检测）
├── vis-network.min.js      # Vis.js 库（本地离线）
├── teams.json              # 16 队注册表
├── data/                   # 球队数据文件
│   ├── belgium_data.json   # 比利时（27人完整版）
│   ├── france_data.json    # 法国
│   └── ...                 # 共 16 个
├── scripts/                # 数据生成与维护脚本
└── README.md
```

## 🔧 添加新球队

1. 创建球队数据 JSON（参考 `data/belgium_data.json` 格式）
2. 在 `teams.json` 中注册新球队
3. 刷新页面，下拉框自动出现

## 📊 数据格式

```json
{
  "teamName": "某国国家队",
  "totalNodes": 27,
  "nodes": [
    {
      "id": 1,
      "label": "球员名\n(EnglishName)",
      "wiki": "Wikipedia_Page_Name",
      "title": "简介：...\n薪资：...\n现役：...",
      "group": "goalkeeper|defender|midfielder|forward|coach",
      "value": 20,
      "isMain": true
    }
  ],
  "edges": [
    {
      "from": 1, "to": 2,
      "label": "友妻门",
      "color": "#ff4d4f",
      "width": 4,
      "relationType": "red",
      "summary": "一句话概述",
      "details": "<b>【标题】</b><br><br>八卦详情..."
    }
  ]
}
```

## 🛠 技术栈

- **前端**：HTML5 + CSS3 + 原生 JavaScript
- **图谱引擎**：Vis.js Network（力导向图）
- **图片源**：Wikipedia REST API
- **服务端**：Python http.server

## 📝 免责声明

本项目仅供学习和娱乐目的。所有球员关系数据基于公开媒体报道整理，不代表客观事实。数据可能包含推测和演绎成分，请理性看待。

## 📄 License

MIT License
