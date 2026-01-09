<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { ElDialog, ElTabs, ElTabPane, ElForm, ElFormItem, ElInput, ElButton, ElCheckbox, ElMessage } from 'element-plus'
import { UserFilled } from '@element-plus/icons-vue'
import * as api from '@/api/interfaceapi'

// onMounted(() => {
//   api.testListApi({}).then(res => {
//     console.log(res)
//   })
// })

// Get current route
const route = useRoute()

// Compute active menu based on current route path
const currentPath = computed(() => route.path)

// 选择的省份
const shengfen: any = ref('beijing')
const options = [
  {
    value: 'shandong',
    label: '山东',
  },
  {
    value: 'henan',
    label: '河南',
  },
  {
    value: 'sichuan',
    label: '四川',
  },
  {
    value: 'guangdong',
    label: '广东',
  },
  {
    value: 'beijing',
    label: '北京',
  },
]
// 处理省份选择变化
const handleShengfenChange = (value: string) => {
  shengfen.value = value
}

// 登录弹窗状态
const showLoginModal = ref(false)
const loginType = ref('phone') // phone, account, card

// 登录表单数据
const loginForm = reactive({
  phone: '13256605200',
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
  if (!/^(?:(?:\+|00)86)?1[3-9]\d{9}$/.test(loginForm.phone)) {
    ElMessage.warning('请输入正确的手机号码')
    return
  }
  api.authcodeApi({
    phone: loginForm.phone,
    type: 1
  }).then(res => {
    console.log(res)
  })
  ElMessage.success(`验证码已发送到 ${loginForm.phone}`)
}

// 登录提交
const handleLogin = () => {
  // api.signOutApi().then(res => {
  //   console.log(res)
  // })
  if (!loginForm.agree) {
    ElMessage.warning('请阅读并同意用户协议')
    return
  }
  if (loginType.value === 'phone') {
    if (!loginForm.phone) {
      ElMessage.warning('请输入手机号码')
      return
    }
    if (!/^(?:(?:\+|00)86)?1[3-9]\d{9}$/.test(loginForm.phone)) {
      ElMessage.warning('请输入正确的手机号码')
      return
    }
    if (!loginForm.code) {
      ElMessage.warning('请输入验证码')
      return
    }
    api.loginOrRegisterApi({
      usercode: loginForm.phone,
      vfCode: loginForm.code,
      type: 1
    }).then(res => {
      console.log(res)
    })
  }
  else if (loginType.value === 'account') {
    if (!loginForm.account) {
      ElMessage.warning('请输入账号')
      return
    }
    if (!loginForm.password) {
      ElMessage.warning('请输入密码')
      return
    }
  }
  else if (loginType.value === 'card') {
    if (!loginForm.cardNumber) {
      ElMessage.warning('请输入卡号')
      return
    }
    if (!loginForm.cardPassword) {
      ElMessage.warning('请输入密码')
      return
    }
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
      <div class="frcc">
        <a href="/" class="logo">
          <i class="fa fa-graduation-cap logo-icon"></i>
          <span
            class="text-xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">聪志愿AI</span>
        </a>
        <el-select v-model="shengfen" placeholder="Select" class="shengfen-select" @change="handleShengfenChange">
          <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
        </el-select>
      </div>
      <div class="nav-menu">
        <a href="/" class="nav-link" :class="{ active: currentPath === '/' }">首页</a>
        <a href="/volunteerApply" class="nav-link" :class="{ active: currentPath === '/volunteerApply' }">志愿填报</a>
        <a href="/schoolSearch" class="nav-link" :class="{ active: currentPath === '/schoolSearch' }">院校查询</a>
        <a href="/majorAnalysis" class="nav-link" :class="{ active: currentPath === '/majorAnalysis' }">专业解析</a>
        <a href="/aiAssessment" class="nav-link" :class="{ active: currentPath === '/aiAssessment' }">AI测评</a>
      </div>
      <button
        class="bg-gradient-to-r from-blue-600 to-purple-700 text-white px-4 py-2 rounded-lg hover:from-blue-500 hover:to-purple-600 transition-all duration-300"
        @click="openLoginModal('phone')">登录</button>
    </div>
  </header>

  <!-- 登录弹窗 -->
  <el-dialog v-model="showLoginModal" width="448px" center @close="closeLoginModal"
    style="padding: 1.5rem; border-radius: 0.75rem">
    <template #header>
      <h2 class="text-2xl font-bold text-gray-800">
        登录聪志愿AI
      </h2>
    </template>
    <el-tabs v-model="loginType" class="login-tabs">
      <el-tab-pane label="手机登录" name="phone">
        <el-form label-position="top">
          <el-form-item label="手机号码">
            <el-input v-model="loginForm.phone" type="tel" placeholder="请输入手机号码"
              style="height: 48px; line-height: 48px;">
              <template #prefix>
                <el-icon class="el-input__icon">
                  <PhoneFilled />
                </el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item label="验证码">
            <el-input v-model="loginForm.code" placeholder="请输入验证码" clearable style="height: 48px; line-height: 48px;">
              <template #prefix>
                <el-icon class="el-input__icon">
                  <GoodsFilled />
                </el-icon>
              </template>
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
            <el-input v-model="loginForm.account" placeholder="请输入账号或手机号码" style="height: 48px; line-height: 48px;">
              <template #prefix>
                <el-icon class="el-input__icon">
                  <user-filled />
                </el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="loginForm.password" type="password" placeholder="请输入密码" show-password
              style="height: 48px; line-height: 48px;">
              <template #prefix>
                <el-icon class="el-input__icon">
                  <GoodsFilled />
                </el-icon>
              </template>
            </el-input>
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
            <el-input v-model="loginForm.cardNumber" placeholder="请输入志愿卡号" style="height: 48px; line-height: 48px;">
              <template #prefix>
                <el-icon class="el-input__icon">
                  <Platform />
                </el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="loginForm.cardPassword" type="password" placeholder="请输入密码" show-password
              style="height: 48px; line-height: 48px;">
              <template #prefix>
                <el-icon class="el-input__icon">
                  <GoodsFilled />
                </el-icon>
              </template>
            </el-input>
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
      <el-button type="primary" @click="handleLogin" style="width: 100%; height: 48px;">
        登录
      </el-button>
    </div>
  </el-dialog>
</template>

<style lang="scss" scoped>
.header {
  max-width: 80vw;
  min-width: 1200px;
  margin: 0 auto;
  padding: 1rem 1.5rem;
  background: #fff;
  box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  border-radius: 0.75rem 0.75rem 0 0;
}

.header-container {
  height: 40px;
  display: flex;
  justify-content: space-between;
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
  // width: 2rem;
  // height: 2rem;
  color: #3b82f6;
  margin-right: 0.5rem;
}

.shengfen-select {
  margin-left: 0.75rem;
  width: 86px;
}

.nav-menu {
  display: flex;
  gap: 2rem;
}

.nav-link {
  color: #4b5563;
  text-decoration: none;
  transition: all 0.3s ease;
  font-weight: 500;
  position: relative;
  padding: 0.25rem 0;
}

.nav-link:hover {
  color: #3b82f6;
}

.nav-link.active {
  color: #3b82f6;
  font-weight: 600;
}

// .nav-link.active::after {
//   content: '';
//   position: absolute;
//   bottom: -0.5rem;
//   left: 0;
//   width: 100%;
//   height: 2px;
//   background: #3b82f6;
//   border-radius: 2px;
// }

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