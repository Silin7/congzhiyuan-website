<script setup lang="ts">
import { ref, reactive } from 'vue'

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
const openLoginModal = (type: string) => {
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
  <div class="home-page">

    <main class="home-main">
      <!-- Hero Section -->
      <section class="hero-section">
        <div class="hero-container">
          <h1 class="hero-title">AI智能志愿填报</h1>
          <p class="hero-subtitle">让选择更有把握</p>
          <p class="hero-description">
            基于千万级录取数据分析与AI智能算法，精准匹配院校专业，<br>
            让高考志愿填报不再迷茫
          </p>
        </div>
      </section>

      <!-- 智能推荐方案 -->
      <section class="recommendations-section">
        <div class="section-container">
          <h2 class="section-title">智能推荐方案</h2>
          <div class="recommendations-grid">
            <div class="recommendation-card">
              <div class="card-header">
                <h3 class="card-title">冲刺院校方案</h3>
                <div class="match-rate">匹配度 96%</div>
              </div>
              <p class="card-description">基于您的分数匹配略高于档位的优质院校，最大化录取潜力</p>
            </div>

            <div class="recommendation-card">
              <div class="card-header">
                <h3 class="card-title">稳妥报考方案</h3>
                <div class="match-rate">匹配度 92%</div>
              </div>
              <p class="card-description">精准匹配您最可能录取的院校组合，确保理想大学</p>
            </div>

            <div class="recommendation-card">
              <div class="card-header">
                <h3 class="card-title">保底稳录方案</h3>
                <div class="match-rate">匹配度 98%</div>
              </div>
              <p class="card-description">确保安全录取的保守方案，结合兴趣匹配专业方向</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 核心功能 -->
      <section class="features-section">
        <div class="section-container">
          <h2 class="section-title">核心功能</h2>
          <div class="features-grid">
            <div class="feature-item">
              <div class="feature-icon">
                <i data-lucide="bot" class="icon"></i>
              </div>
              <h3 class="feature-title">AI志愿填报</h3>
              <p class="feature-description">根据成绩、兴趣、就业前景多维分析，生成个性化志愿填报方案</p>
              <a href="/zytb" class="feature-link">了解更多</a>
            </div>

            <div class="feature-item">
              <div class="feature-icon">
                <i data-lucide="database" class="icon"></i>
              </div>
              <h3 class="feature-title">院校数据查询</h3>
              <p class="feature-description">覆盖全国3000+院校实时录取数据，学科评估与就业报告深度解析</p>
              <a href="#" class="feature-link">了解更多</a>
            </div>

            <div class="feature-item">
              <div class="feature-icon">
                <i data-lucide="book-open" class="icon"></i>
              </div>
              <h3 class="feature-title">专业解析</h3>
              <p class="feature-description">高校专业详细解析...</p>
              <a href="#" class="feature-link">了解更多</a>
            </div>
          </div>
        </div>
      </section>

      <!-- 专业服务保障 -->
      <section class="service-section">
        <div class="section-container">
          <h2 class="section-title">专业服务保障</h2>
          <p class="section-subtitle">精准、可靠、专业的智能志愿填报平台</p>

          <div class="service-grid">
            <div class="service-item">
              <div class="service-icon">
                <i data-lucide="brain" class="icon"></i>
              </div>
              <h3 class="service-title">AI算法精准</h3>
              <p class="service-description">基于机器学习模型不断优化，预测准确率高达92%</p>
            </div>

            <div class="service-item">
              <div class="service-icon">
                <i data-lucide="refresh-cw" class="icon"></i>
              </div>
              <h3 class="service-title">数据实时更新</h3>
              <p class="service-description">每年更新千万级录取数据，确保信息准确性</p>
            </div>

            <div class="service-item">
              <div class="service-icon">
                <i data-lucide="users" class="icon"></i>
              </div>
              <h3 class="service-title">专家团队支持</h3>
              <p class="service-description">300+招生官与教育专家提供深度咨询服务</p>
            </div>

            <div class="service-item">
              <div class="service-icon">
                <i data-lucide="award" class="icon"></i>
              </div>
              <h3 class="service-title">成功案例见证</h3>
              <p class="service-description">每年帮助10万+考生进入理想院校</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 合作院校 -->
      <section class="partners-section">
        <div class="section-container">
          <h2 class="section-title">合作院校</h2>
          <div class="partners-grid">
            <div class="partner-logo">
              <i data-lucide="school" class="partner-icon"></i>
            </div>
            <div class="partner-logo">
              <i data-lucide="school" class="partner-icon"></i>
            </div>
            <div class="partner-logo">
              <i data-lucide="school" class="partner-icon"></i>
            </div>
            <div class="partner-logo">
              <i data-lucide="school" class="partner-icon"></i>
            </div>
            <div class="partner-logo">
              <i data-lucide="school" class="partner-icon"></i>
            </div>
          </div>
        </div>
      </section>
    </main>

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
  </div>
</template>

<style lang="scss" scoped>
.home-page {
  min-height: 100vh;
  background: #f8fafc;
}

.home-main {
  max-width: 1400px;
  margin: 0 auto;
}

/* Hero Section */
.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 6rem 0;
  text-align: center;
}

.hero-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.hero-description {
  font-size: 1.125rem;
  line-height: 1.6;
  opacity: 0.8;
}

/* Section Common Styles */
.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.section-title {
  font-size: 2.25rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 3rem;
  color: #1f2937;
}

.section-subtitle {
  text-align: center;
  color: #6b7280;
  font-size: 1.125rem;
  margin-bottom: 4rem;
}

/* Recommendations Section */
.recommendations-section {
  padding: 5rem 0;
  background: white;
}

.recommendations-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

@media (min-width: 768px) {
  .recommendations-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.recommendation-card {
  background: #f8fafc;
  border-radius: 1rem;
  padding: 2rem;
  border: 1px solid #e5e7eb;
  transition: all 0.3s ease;
}

.recommendation-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.card-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
}

.match-rate {
  background: #10b981;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  font-weight: 500;
}

.card-description {
  color: #6b7280;
  line-height: 1.6;
}

/* Features Section */
.features-section {
  padding: 5rem 0;
  background: #f8fafc;
}

.features-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

@media (min-width: 768px) {
  .features-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.feature-item {
  background: white;
  border-radius: 1rem;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.feature-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  width: 4rem;
  height: 4rem;
  background: #3b82f6;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
}

.feature-icon .icon {
  width: 2rem;
  height: 2rem;
  color: white;
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #1f2937;
}

.feature-description {
  color: #6b7280;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.feature-link {
  color: #3b82f6;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

.feature-link:hover {
  color: #2563eb;
}

/* Service Section */
.service-section {
  padding: 5rem 0;
  background: white;
}

.service-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

@media (min-width: 768px) {
  .service-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .service-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

.service-item {
  text-align: center;
  padding: 1.5rem;
}

.service-icon {
  width: 4rem;
  height: 4rem;
  background: #eff6ff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
}

.service-icon .icon {
  width: 2rem;
  height: 2rem;
  color: #3b82f6;
}

.service-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #1f2937;
}

.service-description {
  color: #6b7280;
  line-height: 1.5;
  font-size: 0.875rem;
}

/* Partners Section */
.partners-section {
  padding: 5rem 0;
  background: #f8fafc;
}

.partners-grid {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 2rem;
}

.partner-logo {
  width: 6rem;
  height: 6rem;
  background: white;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.partner-icon {
  width: 3rem;
  height: 3rem;
  color: #9ca3af;
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

/* Responsive Design */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1.25rem;
  }

  .section-title {
    font-size: 1.75rem;
  }

  .recommendations-grid,
  .features-grid {
    grid-template-columns: 1fr;
  }

  .service-grid {
    grid-template-columns: 1fr;
  }
}
</style>