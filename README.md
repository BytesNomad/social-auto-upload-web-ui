# AI Social Auto Upload / AI 社交媒体自动上传

[English](#english) | [中文](#中文)

---

## English

### Project Introduction

This project is a **Web-UI interface** developed based on the open-source project [dreammis/social-auto-upload](https://github.com/dreammis/social-auto-upload). The underlying functionality is built upon the original project with targeted optimizations and modifications to provide a more modern and user-friendly web interface.

### Features

- **Multi-Platform Support**: Support for Xiaohongshu (小红书), Douyin (抖音), Bilibili (B站), Kuaishou (快手), WeChat Video Account (视频号)
- **Batch Publishing**: Publish content to multiple platforms simultaneously
- **Account Management**: Manage accounts across all platforms in one place
- **Material Management**: Upload and manage video materials
- **Task Management**: Track publishing status and results

### Prerequisites

- **Python 3.10+** (Backend runtime)
- **Node.js 18+** (Frontend build)
- **npm** or **yarn** (Package management)
- **Chrome/Chromium** browser (for account login automation)

### Local Development Setup

#### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (Python 3.10+)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

#### 3. Access the Application

Open your browser and navigate to: **http://localhost:5173/**

### Building for Windows

#### Using Tauri (Desktop Application)

1. **Install Rust** (required by Tauri)
   ```bash
   # Download from https://rustup.rs/
   ```

2. **Build the application**
   ```bash
   # From project root
   cd src-tauri
   cargo tauri build
   ```

3. The built executable will be in `src-tauri/target/release/`

#### Using Web Build Only

```bash
cd frontend
npm run build
```

The built files will be in `frontend/dist/`, which can be deployed to any web server.

---

## 中文

### 项目介绍

本项目是基于开源项目 [dreammis/social-auto-upload](https://github.com/dreammis/social-auto-upload) 开发的 **Web-UI 界面**。底层功能基于原项目作了针对性的优化和修改，提供更现代化、更易用的网页界面。

### 功能特性

- **多平台支持**：支持小红书、抖音、B站、快手、视频号
- **批量发布**：一次操作，同时发布内容到多个平台
- **账号管理**：统一管理所有平台的账号
- **素材管理**：上传和管理视频素材
- **任务管理**：追踪发布状态和结果

### 准备工作

- **Python 3.10+**（后端运行环境）
- **Node.js 18+**（前端构建）
- **npm** 或 **yarn**（包管理工具）
- **Chrome/Chromium** 浏览器（用于账号登录自动化）

### 本地启动

#### 1. 后端设置

```bash
# 进入后端目录
cd backend

# 创建虚拟环境 (Python 3.10+)
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

#### 2. 前端设置

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

#### 3. 访问应用

打开浏览器访问：**http://localhost:5173/**

### Windows 系统打包

#### 使用 Tauri（桌面应用）

1. **安装 Rust**（Tauri 需要）
   ```bash
   # 从 https://rustup.rs/ 下载安装
   ```

2. **构建应用**
   ```bash
   # 从项目根目录
   cd src-tauri
   cargo tauri build
   ```

3. 构建完成的可执行文件在 `src-tauri/target/release/` 目录

#### 仅构建 Web 版本

```bash
cd frontend
npm run build
```

构建产物在 `frontend/dist/`，可部署到任意 Web 服务器。

---

## 许可证 / License

本项目暂时采用 MIT License 开源许可证。

This project is currently licensed under the MIT License.

---

## Star History

如果这个项目对您有帮助，请给一个 ⭐ Star 以表示支持！

If this project is helpful to you, please give a ⭐ Star to show your support!

[![Star History Chart](https://api.star-history.com/svg?repos=DevilJie/socialUpload&type=Timeline)](https://star-history.com/#DevilJie/socialUpload&Timeline)

---

## 致谢 / Acknowledgments

### 原项目作者 / Original Project Author

[@dreammis](https://github.com/dreammis) - [dreammis/social-auto-upload](https://github.com/dreammis/social-auto-upload)

<img src="https://github.com/dreammis.png" width="150" height="150" alt="dreammis QR Code" style="border: 1px solid #ddd; border-radius: 8px;">

### 本项目维护者 / Project Maintainer

[@程序员老蔡](https://github.com/DevilJie)

<img src="qrcode.png" width="150" height="150" alt="Maintainer QR Code" style="border: 1px solid #ddd; border-radius: 8px;">