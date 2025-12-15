<script setup lang="ts">
import { onMounted, nextTick } from 'vue'

onMounted(() => {
  // 确保 DOM 完全渲染后再初始化 lucide 图标
  nextTick(() => {
    if (typeof window !== 'undefined' && (window as any).lucide) {
      (window as any).lucide.createIcons()
    }
  })
})
</script>

<template>
  <!-- Header -->
  <header class="header">
    <div class="header-container">
      <div class="header-left">
        <a href="#" class="logo">
          <i data-lucide="graduation-cap" class="logo-icon"></i>
          志愿AI
        </a>
        <div class="nav-menu">
          <a href="#" class="nav-link">首页</a>
          <a href="#" class="nav-link">生涯规划</a>
          <a href="#" class="nav-link">院校专业</a>
          <a href="#" class="nav-link">AI测评</a>
          <a href="#" class="nav-link">高考资讯</a>
        </div>
      </div>
      <div>
        <button class="login-btn">登录</button>
      </div>
    </div>
  </header>
</template>

<style lang="scss" scoped>
.header {
  background: white;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0.75rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-left {
  display: flex;
  align-items: center;
}

.logo {
  font-size: 1.25rem;
  font-weight: bold;
  color: #1f2937;
  text-decoration: none;
  display: flex;
  align-items: center;
}

.logo-icon {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  color: #3b82f6;
  margin-right: 0.5rem;
}

.nav-menu {
  display: none;
  margin-left: 2.5rem;
  gap: 2rem;
}

@media (min-width: 768px) {
  .nav-menu {
    display: flex;
  }
}

.nav-link {
  color: #4b5563;
  text-decoration: none;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #3b82f6;
}

.login-btn {
  background: #3b82f6;
  color: white;
  font-weight: bold;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  border: none;
  cursor: pointer;
  transition: background 0.3s ease;
}

.login-btn:hover {
  background: #2563eb;
}
</style>