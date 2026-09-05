# 聪志愿 AI 智能志愿填报系统 (CONGZHIYUAN-WEBSITE)

基于 Vue 3.5 + TypeScript 5.8 + Vite 6.x 构建的新高考 AI 智能志愿填报 Web 端服务平台。

---

## 🛠️ 技术栈与环境依赖

- **前端框架**：Vue 3.5 (`<script setup>` Composition API)
- **开发构建**：Vite 6.x
- **编程语言**：TypeScript 5.8
- **状态管理**：Pinia 3.x
- **路由管理**：Vue Router 4.x (Hash 模式)
- **UI 组件库**：Element Plus 2.10
- **环境基线**：
  - **Node.js**：`>= 18.18.0`（推荐 Node 20.x / 22.x LTS，实测兼容 Node 25.x）
  - **包管理器**：`pnpm >= 8.x / 10.x`（强制使用 pnpm，严禁使用 npm/yarn）

---

## 🚀 快速开始

### 1. 安装依赖
```bash
# 推荐配置国内镜像源
pnpm config set registry https://registry.npmmirror.com

# 安装全部依赖
pnpm install
```

### 2. 启动本地开发服务
```bash
pnpm dev
```
- 本地访问地址：`http://localhost:3010/#/`
- 监听网络：`0.0.0.0:3010`，自动拉起默认浏览器。

### 3. 项目构建打包
```bash
# 生产标准全量打包（类型检查 + Vite 打包）
pnpm build

# 仅打包（跳过 vue-tsc 检查）
pnpm build-only

# 本地预览构建产物
pnpm preview

# 代码统一格式化
pnpm format
```

---

## 🌐 多环境接口配置（正式 / 测试切换）

配置文件路径：`src/api/baseConfig.ts`

```typescript
// 1. 正式生产环境 (上线时启用)
const baseURL = 'https://api.congzhiYuan.cn/index.php'

// 2. 测试/联调环境 (内部联调测试时启用)
// const baseURL = 'http://testapi.congzhiyuan.cn/index.php'

// 3. 静态资源根路径
const fileURL = 'http://congzhiyuan.cn'

// 4. 用户协议与支付链接
const agreementURL = 'https://api.congzhiyuan.cn/xieyi.html'
const chargePayURL = 'https://api.congzhiYuan.cn/pay/chargePayDeal.php'

export { baseURL, fileURL, agreementURL, chargePayURL }
```

---

## ⚠️ 生产部署注意事项（必读）

1. **静态资源路径**：
   - 打包后生成 `dist/` 文件夹。
   - 因 `index.html` 引用了 `/public/js/lucide.js` 与 `/public/js/tailwindcss.js`，打包完成后**建议将根目录下的 `public` 文件夹完整拷贝至 `dist/` 目录下**（即形成 `dist/public/`），确保外部字体与图标脚本无缝加载。
2. **Web 服务器托管**：
   - 采用 **Hash 路由**，直接将 `dist/` 部署至 Nginx 或 Windows IIS 网站根目录下即可，无需繁琐的 `try_files` 路由重写。

---

## 📚 详细文档指引

- 📄 **新手使用手册**：[聪志愿AI智能志愿填报系统-新手保姆级操作手册.docx](./聪志愿AI智能志愿填报系统-新手保姆级操作手册.docx) *(含 11 张高清全流程操作截图)*
- 🛠️ **技术维护手册**：[聪志愿AI智能志愿填报系统-项目技术维护手册.docx](./聪志愿AI智能志愿填报系统-项目技术维护手册.docx) *(含技术选型、插件清单、多环境配置、打包与 IIS/Nginx 部署规范)*
