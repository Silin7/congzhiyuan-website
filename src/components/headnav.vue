<script setup lang="ts">
import { onMounted, nextTick, ref, reactive } from 'vue'

onMounted(() => {
  // 确保 DOM 完全渲染后再初始化 lucide 图标
  nextTick(() => {
    if (typeof window !== 'undefined' && (window as any).lucide) {
      (window as any).lucide.createIcons()
    }
  })
})

// 登录弹窗状态
const showLoginModal = ref(false)
const loginType = ref('phone') // phone, account, card

// 登录表单数据
const loginForm = reactive({
  phone: '',
  code: '',
  account: '',
  password: '',
  cardNumber: '',
  cardPassword: '',
  remember: false,
  agree: false
})

// 打开登录弹窗
const openLoginModal = (type: string = 'phone') => {
  loginType.value = type
  showLoginModal.value = true
}

// 关闭登录弹窗
const closeLoginModal = () => {
  showLoginModal.value = false
  // 重置表单
  Object.keys(loginForm).forEach(key => {
    (loginForm as any)[key] = ''
  })
  loginForm.remember = false
  loginForm.agree = false
}

// 发送验证码
const sendCode = () => {
  if (!loginForm.phone) {
    alert('请输入手机号码')
    return
  }
  alert(`验证码已发送到 ${loginForm.phone}`)
}

// 登录提交
const handleLogin = () => {
  if (!loginForm.agree) {
    alert('请阅读并同意用户协议')
    return
  }

  // 模拟登录成功
  alert('登录成功')
  closeLoginModal()
}
</script>

<template>
  <!-- Header -->
  <header class="header">
    <div class="header-container">
      <div class="header-left">
        <a href="/" class="logo">
          <i data-lucide="graduation-cap" class="logo-icon"></i>
          志愿AI
        </a>
        <div class="nav-menu">
          <a href="/" class="nav-link">首页</a>
          <a href="/volunteerApply" class="nav-link">志愿填报</a>
          <a href="/schoolSearch" class="nav-link">院校查询</a>
          <a href="/majorAnalysis" class="nav-link">专业解析</a>
          <a href="/aiAssessment" class="nav-link">AI测评</a>
        </div>
      </div>
      <div>
        <button class="login-btn" @click="openLoginModal('phone')">登录</button>
      </div>
    </div>
  </header>

  <!-- 登录弹窗 -->
  <div v-if="showLoginModal" class="login-modal-overlay" @click="closeLoginModal">
    <div class="login-modal" @click.stop>
      <div class="modal-header">
        <h3 class="modal-title">登录聪志愿AI</h3>
        <button class="close-btn" @click="closeLoginModal">
          <i data-lucide="x" class="icon"></i>
        </button>
      </div>

      <div class="login-tabs">
        <button :class="['tab-btn', { active: loginType === 'phone' }]" @click="loginType = 'phone'">
          手机登录
        </button>
        <button :class="['tab-btn', { active: loginType === 'account' }]" @click="loginType = 'account'">
          账号登录
        </button>
        <button :class="['tab-btn', { active: loginType === 'card' }]" @click="loginType = 'card'">
          志愿卡登录
        </button>
      </div>

      <div class="login-form">
        <!-- 手机登录 -->
        <div v-if="loginType === 'phone'" class="form-content">
          <div class="form-group">
            <label class="form-label">手机号码</label>
            <input v-model="loginForm.phone" type="tel" class="form-input" placeholder="请输入手机号码">
          </div>
          <div class="form-group">
            <label class="form-label">验证码</label>
            <div class="code-input-group">
              <input v-model="loginForm.code" type="text" class="form-input" placeholder="请输入验证码">
              <button class="code-btn" @click="sendCode">获取验证码</button>
            </div>
          </div>
        </div>

        <!-- 账号登录 -->
        <div v-if="loginType === 'account'" class="form-content">
          <div class="form-group">
            <label class="form-label">账号/手机号</label>
            <input v-model="loginForm.account" type="text" class="form-input" placeholder="请输入账号或手机号">
          </div>
          <div class="form-group">
            <label class="form-label">密码</label>
            <input v-model="loginForm.password" type="password" class="form-input" placeholder="请输入密码">
          </div>
          <div class="form-options">
            <label class="checkbox-label">
              <input v-model="loginForm.remember" type="checkbox" class="checkbox">
              记住密码
            </label>
            <a href="#" class="forgot-link">忘记密码？</a>
          </div>
        </div>

        <!-- 志愿卡登录 -->
        <div v-if="loginType === 'card'" class="form-content">
          <div class="form-group">
            <label class="form-label">志愿卡号</label>
            <input v-model="loginForm.cardNumber" type="text" class="form-input" placeholder="请输入志愿卡号">
          </div>
          <div class="form-group">
            <label class="form-label">密码</label>
            <input v-model="loginForm.cardPassword" type="password" class="form-input" placeholder="请输入密码">
          </div>
        </div>

        <div class="form-agreement">
          <label class="checkbox-label">
            <input v-model="loginForm.agree" type="checkbox" class="checkbox">
            阅读并同意 《用户协议》
          </label>
        </div>

        <button class="login-submit-btn" @click="handleLogin">登录</button>
      </div>
    </div>
  </div>
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

/* Login Modal */
.login-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.login-modal {
  background: white;
  border-radius: 1rem;
  width: 90%;
  max-width: 400px;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.modal-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
}

.close-btn {
  background: none;
  border: none;
  padding: 0.5rem;
  cursor: pointer;
  border-radius: 0.375rem;
  transition: background 0.2s;
}

.close-btn:hover {
  background: #f3f4f6;
}

.close-btn .icon {
  width: 1.25rem;
  height: 1.25rem;
  color: #6b7280;
}

.login-tabs {
  display: flex;
  border-bottom: 1px solid #e5e7eb;
}

.tab-btn {
  flex: 1;
  padding: 1rem;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 0.875rem;
  color: #6b7280;
  transition: all 0.2s;
}

.tab-btn.active {
  color: #3b82f6;
  border-bottom: 2px solid #3b82f6;
}

.tab-btn:hover:not(.active) {
  background: #f9fafb;
}

.login-form {
  padding: 1.5rem;
}

.form-content {
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-label {
  display: block;
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.5rem;
}

.form-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  transition: border-color 0.2s;
}

.form-input:focus {
  outline: none;
  border-color: #3b82f6;
}

.code-input-group {
  display: flex;
  gap: 0.5rem;
}

.code-btn {
  padding: 0.75rem 1rem;
  background: #f3f4f6;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.2s;
}

.code-btn:hover {
  background: #e5e7eb;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.75rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.checkbox {
  width: 1rem;
  height: 1rem;
}

.forgot-link {
  color: #6b7280;
  text-decoration: none;
}

.forgot-link:hover {
  color: #374151;
}

.form-agreement {
  margin-bottom: 1.5rem;
}

.login-submit-btn {
  width: 100%;
  padding: 0.75rem;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s;
}

.login-submit-btn:hover {
  background: #2563eb;
}
</style>