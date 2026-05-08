# Social Auto Upload 项目进度

> 最后更新: 2026-05-08

---

## 总体架构

基于 `dreammis/social-auto-upload` 开源仓库，构建类似"蚁小二"的内容分发桌面应用。核心策略：复用上游 Flask + Vue 3 架构，通过 Git Submodule 引入上游代码，在包装层上扩展功能。

```
social-auto-upload/
├── vendor/upstream/     # 上游仓库 (git submodule)
├── backend/             # Flask 后端封装层
├── frontend/            # Vue 3 前端 (暗色主题)
├── data/                # 运行时数据 (SQLite, 视频, Cookie)
├── docs/                # 文档
└── design-system/       # 设计系统
```

---

## 阶段一：环境搭建与上游验证 (当前阶段)

### 已完成

| 项目 | 状态 | 说明 |
|------|------|------|
| Git 仓库初始化 | ✅ | 7 次提交 |
| 上游 Submodule 引入 | ✅ | `vendor/upstream/` 指向 dreammis/social-auto-upload |
| 后端骨架 (conf.py, app.py) | ✅ | sys.path.insert(1,...) 确保 conf.py 优先 |
| 数据库初始化 (init_db.py) | ✅ | data/db/database.db, 两张表 (user_info, file_records) |
| Python 虚拟环境 + 依赖 | ✅ | 包含 patchright, flask, playwright, xhs 等 |
| Patchright Chromium 安装 | ✅ | ~280MB 浏览器二进制 |
| 前端复制 | ✅ | 从上游 sau_frontend/ 复制 |
| Vite 代理配置 | ✅ | 14 个 API 端点代理到 localhost:5409 |
| 暗色主题设计系统 | ✅ | variables.scss + design-system.scss + Element Plus 覆盖 |
| App Shell (侧边栏+顶栏) | ✅ | 7 个导航项，暗色主题 |
| 占位页面 (Tasks, History, Settings) | ✅ | "Coming Soon" 占位组件 |
| 路由扩展 | ✅ | 7 个路由，Hash 模式 |
| 后端 API 冒烟测试 | ✅ | /getFiles, /getAccounts 正常返回 |
| 前端构建验证 | ✅ | npm run build 8s 完成，无报错 |

### 端到端验证结果

| 验证项 | 状态 | 说明 |
|--------|------|------|
| 抖音扫码登录 | ✅ 通过 | 需要有头模式（抖音二次校验） |
| 抖音视频发布 | ✅ 通过 | 完整链路正常 |
| 多平台验证 | 待做 | 小红书等平台待验证 |

### 已知问题

| 问题 | 严重度 | 状态 | 说明 |
|------|--------|------|------|
| playwright→patchright 兼容 | 高 | 已修复 | 上游 import playwright，创建了兼容层重定向到 patchright |
| stealth.min.js 路径 | 高 | 已修复 | BASE_DIR 变更后路径不对，已复制到 data/utils/ |
| 缺失依赖 playwright+xhs | 中 | 已修复 | 上游未声明，已补充到 requirements.txt |
| 登录必须有头模式 | 中 | 待优化 | 抖音二次校验需要弹窗，发布可用无头模式 |
| 登录/发布浏览器模式应分离 | 中 | 阶段二 | 当前共用 LOCAL_CHROME_HEADLESS，需拆分为独立配置 |

### 启动方式

```bash
# 后端 (终端 1)
cd backend && source venv/bin/activate
PLAYWRIGHT_HOST_PLATFORM_OVERRIDE=ubuntu24.04-x64 python app.py
# → http://localhost:5409

# 前端 (终端 2)
cd frontend && npm run dev
# → http://localhost:5173
```

### 已知环境问题

1. **Python 版本**: 系统为 Python 3.14.4，上游约束 `>=3.10,<3.13`，已放宽为 `>=3.10`
2. **Patchright 平台**: Ubuntu 26.04 需设置 `PLAYWRIGHT_HOST_PLATFORM_OVERRIDE=ubuntu24.04-x64`
3. **缺失依赖**: 上游代码引用 `playwright` 和 `xhs` 但未声明在依赖中，已补充

---

## 阶段二：任务队列与后端扩展 (未开始)

### 计划内容

| 项目 | 说明 |
|------|------|
| 任务队列系统 | asyncio Queue + Worker 模式，并发控制，失败重试（指数退避） |
| 数据库扩展 | 新增 publish_tasks 表、publish_logs 表 |
| 扩展 API | `/api/v2/tasks`, `/api/v2/history`, `/api/v2/stats` 等 |
| SSE 任务推送 | 实时通知前端任务状态变更 |
| Cookie 心跳检测 | 定期验证所有账号 Cookie 有效性，失效通知 |
| ext_api/ Blueprint | 填充 backend/ext_api/ 模块 |

### 关键文件 (待创建/修改)

```
backend/ext_api/
├── __init__.py          # Blueprint 注册
├── task_queue.py        # 任务队列
├── publish_scheduler.py # 定时调度
├── heartbeat.py         # Cookie 心跳
└── log_manager.py       # 发布日志
```

---

## 阶段三：前端新页面开发 (未开始)

### 计划内容

| 页面 | 路由 | 说明 |
|------|------|------|
| TaskCenter.vue | /task-center | 实时任务队列，SSE 进度，取消/重试 |
| PublishHistory.vue | /publish-history | 发布历史，筛选，导出 CSV |
| Settings.vue | /settings | 发布间隔、并发数、浏览器模式、代理 |
| Dashboard 增强 | / | 任务统计图表，发布趋势 |

### 设计参考

- `design-system/social-auto-upload/pages/task-center.md`
- `design-system/social-auto-upload/pages/publish-history.md`
- `design-system/social-auto-upload/pages/settings.md`

---

## 阶段四：桌面壳与打包 (未开始)

| 项目 | 说明 |
|------|------|
| Tauri 壳 | 窗口管理、系统托盘 |
| Python 打包 | 内嵌 Python 环境 |
| Patchright 内嵌 | Chromium 二进制 (~200MB) |
| 自动更新 | Tauri updater |
| 安装包 | Windows/macOS 安装测试 |

---

## 阶段五：测试与优化 (未开始)

| 项目 | 说明 |
|------|------|
| 全平台发布测试 | 抖音、快手、小红书、视频号、B站 |
| 错误恢复测试 | 浏览器崩溃、网络断开、Cookie 过期 |
| 性能优化 | 大量任务下的队列表现 |
| UI 润色 | 交互细节、动画、空状态 |
| 文档编写 | 用户使用手册 |
