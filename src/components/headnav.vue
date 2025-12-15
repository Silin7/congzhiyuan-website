<script setup lang="ts">
import { ref, reactive } from 'vue'
import { ElDialog, ElTabs, ElTabPane, ElForm, ElFormItem, ElInput, ElButton, ElCheckbox, ElMessage } from 'element-plus'

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
    ElMessage.warning('请输入手机号码')
    return
  }
  ElMessage.success(`验证码已发送到 ${loginForm.phone}`)
}

// 登录提交
const handleLogin = () => {
  if (!loginForm.agree) {
    ElMessage.warning('请阅读并同意用户协议')
    return
  }

  // 模拟登录成功
  ElMessage.success('登录成功')
  closeLoginModal()
}
</script>

<template>
  <!-- Header -->
  <header class="header">
    <div class="header-container">
      <div class="header-left">
        <a href="/" class="logo">
          <i class="fa fa-graduation-cap logo-icon"></i>
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
        <el-button type="primary" @click="openLoginModal('phone')">登录</el-button>
      </div>
    </div>
  </header>

  <!-- 登录弹窗 -->
  <el-dialog v-model="showLoginModal" title="登录聪志愿AI" width="400px" center @close="closeLoginModal">
    <el-tabs v-model="loginType" class="login-tabs">
      <el-tab-pane label="手机登录" name="phone">
        <el-form label-position="top">
          <el-form-item label="手机号码">
            <el-input v-model="loginForm.phone" type="tel" placeholder="请输入手机号码"></el-input>
          </el-form-item>
          <el-form-item label="验证码">
            <el-input v-model="loginForm.code" placeholder="请输入验证码" clearable>
              <template #append>
                <el-button @click="sendCode">获取验证码</el-button>
              </template>
            </el-input>
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="账号登录" name="account">
        <el-form label-position="top">
          <el-form-item label="账号/手机号">
            <el-input v-model="loginForm.account" placeholder="请输入账号或手机号"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="loginForm.password" type="password" placeholder="请输入密码" show-password></el-input>
          </el-form-item>
          <div class="form-options">
            <el-checkbox v-model="loginForm.remember">记住密码</el-checkbox>
            <a href="#" class="forgot-link">忘记密码？</a>
          </div>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="志愿卡登录" name="card">
        <el-form label-position="top">
          <el-form-item label="志愿卡号">
            <el-input v-model="loginForm.cardNumber" placeholder="请输入志愿卡号"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="loginForm.cardPassword" type="password" placeholder="请输入密码" show-password></el-input>
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>

    <div class="form-agreement">
      <el-checkbox v-model="loginForm.agree">
        阅读并同意 《用户协议》
      </el-checkbox>
    </div>

    <div class="dialog-footer">
      <el-button type="primary" @click="handleLogin" style="width: 100%">
        登录
      </el-button>
    </div>
  </el-dialog>
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

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 1rem 0;
  font-size: 0.875rem;
}

.forgot-link {
  color: #6b7280;
  text-decoration: none;
}

.forgot-link:hover {
  color: #374151;
}

.form-agreement {
  margin: 1.5rem 0;
}

.dialog-footer {
  margin-top: 1rem;
}
</style>