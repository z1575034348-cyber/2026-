# 世界杯球队关系星图 — 全流程创建指南

## 一、项目架构总览

```
比利时队_WorldCup_StarMap/          # 项目根目录
├── teams.json                       # ① 球队注册表（所有球队的索引）
├── belgium_data.json                # ② 比利时队数据（27节点 + 25连线）
├── index.html                       # ③ 前端页面（暗黑星图 + 交互）
├── vis-network.min.js               # ④ Vis.js 库（本地离线加载）
├── run_server.py                    # ⑤ 本地服务器（自动端口检测）
├── data_collection.py               # ⑥ 数据生成脚本（可复用于其他球队）
├── test.html                        # ⑦ 诊断页面（排查问题时使用）
└── README_创建指南.md               # ⑧ 本文档
```

**核心设计原则：**
- 数据层与视图层完全分离（JSON 数据 → HTML 渲染）
- 零外网依赖（Vis.js 已下载到本地，头像用 Wikipedia CDN）
- 多球队架构（teams.json 管理球队列表，一键切换）

---

## 二、技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| 数据 | Python 3 | 生成 JSON 数据文件 |
| 前端 | HTML5 + CSS3 + 原生 JS | 单文件纯前端 |
| 图谱 | Vis.js 9.x (Network) | 力导向图引擎 |
| 图片 | Wikipedia REST API | 自动获取球员真实头像 |
| 服务 | Python http.server | 本地预览，解决 CORS |

---

## 三、创建新球队的完整流程

### 步骤 1：收集球队信息

需要准备以下资料：

#### 1.1 球员名单（27人：26球员 + 1主教练）

对每个人员，需要：
- **中文名 + 英文名**（如：德布劳内 / De Bruyne）
- **Wikipedia 页面名**（如：`Kevin_De_Bruyne`）—— 用于自动获取头像
- **场上位置**：`goalkeeper` / `defender` / `midfielder` / `forward` / `coach`
- **三行简介**：
  - 第1行：网梗式特色评价（如"世界第一喂饼大师"）
  - 第2行：预估薪资（如"周薪 £400,000"）
  - 第3行：现效力俱乐部（如"曼彻斯特城"）
- **是否核心人物**：核心球员/教练设 `isMain: true`，头像边框加粗高亮

#### 1.2 关系线（至少 4红 + 5绿 + 若干白/金）

| 类型 | 颜色 | 含义 | 要求 |
|------|------|------|------|
| `red` | `#ff4d4f` 红色 | 矛盾/内讧/八卦 | ≥4条，每条必须有长文 details + 来源 |
| `green` | `#56d364` 绿色 | 默契搭档/密友 | ≥5条 |
| `gold` | `#e3b341` 金色 | 黄金搭档/传奇组合 | 可选 |
| `white`| `#8b949e` 灰色 | 普通战术关系 | 若干 |

**关系数据字段：**
```json
{
    "from": 12,           // 起始节点ID
    "to": 1,              // 目标节点ID
    "label": "友妻门",    // 简短标签（显示在连线上）
    "color": "#ff4d4f",   // 连线颜色
    "width": 4,           // 连线粗细
    "relationType": "red",// 类型：red/green/gold/white
    "summary": "一句话概述",
    "details": "长文详情..."  // 红色线必须有，支持 <b> 粗体 <br> 换行
}
```

#### 1.3 红色八卦的 details 写作规范

- 用 `<b>【标题】</b>` 开头
- 用 `<br><br>` 分段
- 语言生动、戏谑、符合中国互联网"吃瓜"风格
- 用 `<b>加粗</b>` 强调关键爆料
- 结尾加"吃瓜群众辣评"制造互动感
- **必须附加来源背书**：`<br><br><b>📰 实锤来源：</b>` + 引用真实媒体

---

### 步骤 2：生成球队数据文件

#### 2.1 编写数据生成脚本

参考 `data_collection.py` 的结构：

```python
# 1. 定义球员 Wikipedia 页面名映射
PLAYER_WIKI = {
    "球员中文名": "Wikipedia_Page_Name",
    ...
}

# 2. 通过 Wikipedia API 获取头像（自动）
def fetch_wiki_image(wiki_title):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{wiki_title}"
    # ... 请求并解析 thumbnail.source

# 3. 构建节点数据
nodes = [
    {
        "id": 1,                              # 唯一ID（从1开始）
        "label": "中文名\n(EnglishName)",      # \n 分隔中英文
        "image": "头像URL",                    # Wikipedia CDN 直链
        "title": "简介：...\n薪资：...\n现役：...",  # 三行结构
        "group": "goalkeeper",                 # 位置分类
        "value": 25,                           # 节点大小（10-30）
        "isMain": True                         # 核心人物标记（可选）
    },
    ...
]

# 4. 构建连线数据
edges = [
    {
        "from": 12, "to": 1,
        "label": "...", "color": "#ff4d4f",
        "width": 4, "relationType": "red",
        "summary": "...", "details": "..."
    },
    ...
]

# 5. 输出 JSON
output = {
    "teamName": "某国国家队",
    "teamNameEn": "Country National Football Team",
    "totalNodes": len(nodes),
    "totalEdges": len(edges),
    "nodes": nodes,
    "edges": edges
}
```

#### 2.2 运行脚本

```bash
cd 比利时队_WorldCup_StarMap
PYTHONIOENCODING=utf-8 python data_collection.py
```

脚本会：
1. 逐个调用 Wikipedia API 获取球员头像 URL
2. 失败时自动使用预留的备用 URL
3. 输出 `xxx_data.json`（例如 `france_data.json`）

#### 2.3 验证数据

```bash
PYTHONIOENCODING=utf-8 python -c "
import json
with open('france_data.json','r',encoding='utf-8') as f:
    d = json.load(f)
print(f'节点: {d[\"totalNodes\"]}  连线: {d[\"totalEdges\"]}')
# 检查每个节点是否有 image 字段
for n in d['nodes']:
    assert n.get('image','').startswith('http'), f'{n[\"id\"]} 缺头像'
print('验证通过')
"
```

---

### 步骤 3：注册到 teams.json

编辑 `teams.json`，在 `teams` 数组中添加：

```json
{
    "id": "france",
    "name": "法国",
    "nameEn": "France",
    "flag": "🇫🇷",
    "dataFile": "france_data.json",
    "description": "高卢雄鸡的卫冕之路"
}
```

保存后，页面的下拉框会自动出现新球队选项。

**teams.json 完整结构：**
```json
{
    "teams": [
        {
            "id": "belgium",         // 唯一标识（用于 dataFile 命名）
            "name": "比利时",        // 中文名
            "nameEn": "Belgium",     // 英文名
            "flag": "🇧🇪",           // 国旗 emoji
            "dataFile": "belgium_data.json",  // 数据文件名
            "description": "..."     // 一句话描述
        }
    ],
    "default": "belgium"            // 默认显示的球队
}
```

---

### 步骤 4：本地预览测试

```bash
cd 比利时队_WorldCup_StarMap
python run_server.py
```

浏览器打开终端显示的地址（如 `http://localhost:8080`）

#### 测试检查清单

- [ ] 页面正常加载，不再卡在"加载中"
- [ ] 所有 27 个头像正确显示（非灰色占位符）
- [ ] 鼠标悬停头像弹出三行简介卡片
- [ ] 拖拽节点流畅
- [ ] 点击头像 → 底部面板更新 → 关系列表显示
- [ ] 双击头像 → 自动居中放大
- [ ] 点击红色连线 → 弹出吃瓜弹窗 → 包含来源背书
- [ ] 搜索框输入球员名 → 下拉匹配 → 点击跳转
- [ ] 分组筛选按钮（门将/后卫/中场/前锋/教练）正常工作
- [ ] "🔥 只看大瓜" 按钮 → 仅显示红色连线和相关节点
- [ ] 聚焦功能：点击节点 → 无关节点隐藏 → 点击空白取消
- [ ] 浮动按钮（+/-/⟳）正常工作
- [ ] 缩放、拖拽流畅
- [ ] 按 ESC 关闭弹窗/取消聚焦
- [ ] 下拉框切换到其他球队 → 重新加载数据并渲染

---

## 四、页面功能一览

| 功能 | 触发方式 | 效果 |
|------|----------|------|
| 球队切换 | 顶部下拉框 | 切换并加载不同球队数据 |
| 搜索球员 | 搜索框输入 | 实时匹配，点击跳转+聚焦 |
| 分组筛选 | 顶部按钮组 | 按位置筛选节点 |
| 只看大瓜 | 🔥 按钮 | 仅显示红色八卦连线 |
| 悬停卡片 | 鼠标悬停头像 | 三行极简信息卡 |
| 吃瓜弹窗 | 点击红色连线 | 长文八卦 + 来源背书 |
| 聚焦高亮 | 点击头像 | 无关节点隐藏 |
| 取消聚焦 | 点击空白/ESC | 恢复全图 |
| 底部面板 | 点击头像 | 左侧大头像 + 右侧关系列表 |
| 移动端 | 手机访问 | 底部抽屉式卡片 |
| 缩放 | +/- 按钮或滚轮 | 放大缩小 |
| 重置 | ⟳ 按钮 | 恢复默认视角 |

---

## 五、常见问题排查

### Q1: 页面打开黑屏/空白
- 确认通过 `http://localhost:8080` 访问，不是双击 HTML
- 检查 `vis-network.min.js` 是否在项目目录（682KB）
- 打开 F12 控制台查看 JavaScript 报错

### Q2: 一直显示"加载中"
- 打开 `http://localhost:8080/test.html` 逐项诊断
- 检查 `teams.json` 和球队数据文件是否存在且格式正确
- 检查 JSON 文件编码为 UTF-8

### Q3: 头像显示为灰色问号
- Wikipedia 图片 URL 可能过期，重新运行 `data_collection.py` 获取最新 URL
- 或者手动替换为其他可靠图源

### Q4: 服务器端口冲突
- `run_server.py` 已内置自动端口检测（8080-8094）
- 或手动指定：修改脚本中的 PORT 变量

### Q5: 移动端底部面板不显示
- 确认 `<meta name="viewport">` 存在
- 检查 `@media (max-width:768px)` 媒体查询

---

## 六、数据文件规范速查

### 节点必需字段
```json
{
    "id": 1,                    // number, 唯一
    "label": "中文\n(English)", // string, \n 分隔
    "image": "https://...",     // string, 头像直链
    "title": "简介：...\n薪资：...\n现役：...",  // 三行
    "group": "goalkeeper|defender|midfielder|forward|coach",
    "value": 20                 // number, 10-30
}
```

### 节点可选字段
```json
{
    "isMain": true              // 核心人物，边框加粗+金色
}
```

### 连线必需字段
```json
{
    "from": 12,                 // number, 起始节点ID
    "to": 1,                    // number, 目标节点ID
    "label": "关系标签",        // string
    "color": "#ff4d4f",         // string, 十六进制颜色
    "width": 3,                 // number, 1-5
    "relationType": "red|green|gold|white",
    "summary": "一句话概述"     // string
}
```

### 连线可选字段
```json
{
    "details": "长文详情<br><br><b>📰 实锤来源：</b>..."  // 红色线必须
}
```

---

## 七、批量创建 48 支球队的规划建议

1. **自动化数据管线**：编写爬虫脚本，从 Wikipedia / Transfermarkt / 新闻媒体自动抓取球员名单和关系
2. **模板化生成**：将 `data_collection.py` 改造为通用模板，参数化球队名称和 Wikipedia 页面名
3. **图片 CDN 池**：建立 Wikipedia thumbnail URL 缓存，避免每次重新请求
4. **关系数据库**：用大模型自动从新闻文本中提取球员矛盾/密友关系，生成 JSON
5. **CDN 部署**：将 `vis-network.min.js` 上传到 CDN，减少项目体积

---

*最后更新：2026年6月*
