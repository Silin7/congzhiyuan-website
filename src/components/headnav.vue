<script setup lang="ts">
import { ref, reactive, computed, onMounted, onUnmounted, unref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElDialog, ElTabs, ElTabPane, ElForm, ElFormItem, ElInput, ElButton, ElCheckbox, ElMessage, ElMessageBox } from 'element-plus'
import { UserFilled } from '@element-plus/icons-vue'
import * as api from '@/api/interfaceapi'
import { agreementURL } from '@/api/baseConfig'

// Get current route
const route = useRoute()
const router = useRouter()
// Compute active menu based on current route path
const currentPath = computed(() => route.path)

const userInfo = ref<any>(null)

const syncUserInfoFromStorage = () => {
  userInfo.value = JSON.parse(localStorage.getItem('userInfo') || '{}')
}

onMounted(() => {
  syncUserInfoFromStorage()
  window.addEventListener('userInfoUpdated', syncUserInfoFromStorage)
  // if (userInfo.value?.ifProvSave == '1' && userInfo.value?.ifUserActive == '0') {
  //   ElMessage.warning('请先完善成绩信息')
  //   router.push({
  //     path: '/personalInfo',
  //   })
  // }
  // 上部导航栏显示查询
  api.navQueryApi().then(res => {
    console.log(res)
  })
})

onUnmounted(() => {
  window.removeEventListener('userInfoUpdated', syncUserInfoFromStorage)
})

// 选择的省份
const shengfen: any = ref('')

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
const sendCode = async () => {
  if (!loginForm.phone) {
    ElMessage.warning('请输入手机号码')
    return
  }
  if (!/^(?:(?:\+|00)86)?1[3-9]\d{9}$/.test(loginForm.phone)) {
    ElMessage.warning('请输入正确的手机号码')
    return
  }
  try {
    const res: any = await api.authcodeApi({
      phone: loginForm.phone,
      type: 1
    })
    ElMessage.success(`验证码已发送到 ${loginForm.phone}`)
    console.log('发送验证码 -------->', res)
    // if (res.data.code === 0) {
    //   ElMessage.success(`验证码已发送到 ${loginForm.phone}`)
    // } else {
    //   // ElMessage.error(res.data.message || '发送验证码失败')
    //   console.log('发送验证码失败 -------->', res.data.message || '发送验证码失败')
    // }
  } catch (error) {
    ElMessage.success(`验证码已发送到 ${loginForm.phone}`)
    console.log('发送验证码失败 -------->', error)
    // ElMessage.error('发送验证码失败')
  }
}

// 登录提交
const handleLogin = async () => {
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
    const res: any = await api.loginOrRegisterApi({
      usercode: loginForm.phone,
      vfCode: loginForm.code,
      type: 1
    })
    if (res) {
      userHandel(res)
    }
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
    const res: any = await api.loginOrRegisterApi({
      usercode: loginForm.account,
      vfCode: loginForm.password,
      type: 2
    })
    if (res) {
      userHandel(res)
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
    const res: any = await api.loginOrRegisterApi({
      usercode: loginForm.cardNumber,
      vfCode: loginForm.cardPassword,
      type: 2
    })
    if (res) {
      userHandel(res)
    }
  }
}

// 首次登录逻辑处理
const userHandel = (res: any) => {
  userInfo.value = res.data || {}
  localStorage.setItem('userInfo', JSON.stringify(res.data))
  localStorage.setItem('token', res.data.token)
  closeLoginModal()
  if (userInfo.value.ifProvSave == '0') {
    genListQueryList()
  } else if (userInfo.value.ifUserActive == '0') {
    ElMessage.warning('请完善成绩信息')
    router.push({
      path: '/personalInfo',
    })
  } else {
    ElMessage.success('登录成功')
  }
}

// 获取省份列表
const showProvModal = ref(false)
const provinceSelected = ref<any>('')
const provinceList = ref<any>([])
const genListQueryList = async () => {
  const res: any = await api.userProvQueryApi()
  if (res) {
    provinceList.value = res.data.Rs || []
    showProvModal.value = true
  }
}

// 保存省份
const myUserPorvSave = async () => {
  if (!provinceSelected.value) {
    ElMessage.warning('请选择省份')
    return
  }
  const res: any = await api.myUserPorvSaveApi({
    provId: provinceSelected.value
  })
  if (res) {
    showProvModal.value = false
    if (userInfo.value.ifUserActive == '0') {
      ElMessage.warning('请完善成绩信息')
      router.push({
        path: '/personalInfo',
      })
    } else {
      ElMessage.success('登录成功')
    }
  }
}

// 下拉菜单
const buttonRef = ref()
const popoverRef = ref()
function onClickOutside() {
  unref(popoverRef).popperRef?.delayHide?.()
}

// 跳转个人信息
function goUserCenter() {
  window.location.href = '/#/personalInfo'
}

// 退出登录
const logoutFunction = async () => {
  const res: any = await api.signOutApi()
  if (res) {
    ElMessage.success('退出成功')
    userInfo.value = {}
    window.location.href = '/'
    window.localStorage.removeItem('token')
    window.localStorage.removeItem('userInfo')
    window.localStorage.removeItem('selectedSchoolLevel')
    window.localStorage.removeItem('selectedAdmissionBatch')
    window.localStorage.removeItem('selectedAdmissionType')
    window.localStorage.removeItem('selectedSchoolNature')
    window.localStorage.removeItem('selectedMajorFeature')
    window.localStorage.removeItem('selectedProvince')
    window.localStorage.removeItem('selectedRiskLevel')
    window.localStorage.removeItem('riskThreshold')
    window.localStorage.removeItem('safeThreshold')
  }
}

// 处理用户协议点击事件
const handleAgreementClick = () => {
  window.open(agreementURL, '_blank')
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
        {{ shengfen }}
        <!-- <el-select v-model="shengfen" placeholder="Select" class="shengfen-select">
          <el-option v-for="(item, index) in provinceList" :key="index" :label="item.province" :value="item.id">
          </el-option>
        </el-select> -->
      </div>
      <div class="nav-menu">
        <a href="/#/" class="nav-link" :class="{ active: currentPath === '/' }">首页</a>
        <a href="/#/volunteerApply" class="nav-link" :class="{ active: currentPath === '/volunteerApply' }">志愿填报</a>
        <a href="/#/schoolSearch" class="nav-link" :class="{ active: currentPath === '/schoolSearch' }">院校查询</a>
        <a href="/#/majorAnalysis" class="nav-link" :class="{ active: currentPath === '/majorAnalysis' }">专业解析</a>
        <a href="/#/aiAssessmentList" class="nav-link" :class="{ active: currentPath === '/aiAssessmentList' }">AI测评</a>
        <a href="/#/chargingInfomating" class="nav-link" :class="{ active: currentPath === '/chargingInfomating' }">升级VIP</a>
      </div>
      <div v-if="userInfo?.userName" ref="buttonRef" v-click-outside="onClickOutside" class="username">
        <i class="fa fa-user-circle mr-2"></i>
        <span class="nameStyle">{{ userInfo.userName }}</span>
        <el-popover placement="bottom" :virtual-ref="buttonRef" virtual-triggering :width="160" trigger="click">
          <div class="userPopover">
            <div class="popoverItem" @click="goUserCenter">
              个人信息
            </div>
            <div class="popoverItem" @click="logoutFunction">
              退出登录
            </div>
          </div>
        </el-popover>
      </div>
      <button v-else
        class="bg-gradient-to-r from-blue-600 to-purple-700 text-white px-4 py-2 rounded-lg hover:from-blue-500 hover:to-purple-600 transition-all duration-300"
        @click="openLoginModal('phone')">登录</button>
    </div>
  </header>

  <!-- 登录弹窗 -->
  <el-dialog v-model="showLoginModal" width="448" center @close="closeLoginModal"
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
          <!-- <div class="form-options">
            <el-checkbox v-model="loginForm.remember">记住密码</el-checkbox>
            <a href="#" class="forgot-link">忘记密码？</a>
          </div> -->
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
        <span @click.prevent.stop="handleAgreementClick">阅读并同意 《用户协议》</span>
      </el-checkbox>
    </div>
    <div class="dialog-footer">
      <el-button type="primary" @click="handleLogin" style="width: 100%; height: 48px;">
        登录
      </el-button>
    </div>
  </el-dialog>

  <!-- 选择省份弹窗 -->
  <el-dialog v-model="showProvModal" width="600" :show-close="false" :close-on-click-modal="false"
    :close-on-press-escape="false">
    <template #header>
      <h2 class="text-2xl font-bold text-gray-800">
        请先选择省份
      </h2>
    </template>
    <div class="flex flex-wrap gap-3 province-dialog">
      <label v-for="(item, index) in provinceList" :key="index" @click="provinceSelected = item.id" :class="[
        'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
        provinceSelected === item.id
          ? 'active'
          : '',
      ]">
        <span class="text-neutral font-medium">{{ item.province }}</span>
      </label>
    </div>
    <template #footer>
      <el-button type="primary" @click="myUserPorvSave">
        保存
      </el-button>
    </template>
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

.username {
  cursor: pointer;
  display: flex;
  align-items: center;
  // font-size: 1.25rem;

  .nameStyle {
    display: inline-block;
    max-width: 210px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
}

.popoverItem {
  line-height: 30px;
  color: #262626;
  text-align: center;
  cursor: pointer;
}

.popoverItem:hover {
  color: #165dff;
  background-color: #eee;
}
</style>

<!-- <style lang="scss">
.el-collapse {
  border: 0 !important;

  .el-icon {
    display: none;
  }

  .el-collapse-item__header {
    border: 0 !important;
  }

  .el-collapse-item__header:hover {
    color: #165dff !important;
  }

  .el-collapse-item__title {
    font-size: 1.25rem !important;
  }

  .el-collapse-item__wrap {
    border: 0 !important;
  }

  .el-collapse-item__content {
    display: none;
  }

  .is-active {
    color: #165dff !important;
  }
}
</style> -->