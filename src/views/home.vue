<script setup lang="ts">
import { onMounted, nextTick } from 'vue'
import Headnav from '@/components/headnav.vue'
import Footnav from '@/components/footnav.vue'

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
  <div class="home-page">
    <main>
      <!-- Hero Section -->
      <section class="hero-section">
        <div class="hero-container">
          <h1 class="hero-title">AI智能志愿填报</h1>
          <p class="hero-subtitle">让科技点亮你的未来</p>
          <p class="hero-description">基于千万级高考数据和AI智能算法，精准匹配你的分数，让你的每一分都不浪费</p>
        </div>
      </section>

      <!-- Recommendations Section -->
      <section class="recommendations-section">
        <div class="section-container">
          <h2 class="section-title">智能推荐方案</h2>
          <div class="cards-grid">

            <div class="feature-card">
              <div class="card-icon orange-icon">
                <i data-lucide="lightbulb" class="icon"></i>
              </div>
              <h3 class="card-title">基于分数的精准推荐</h3>
              <p class="card-description">根据你的高考成绩，智能筛选出最适合你的院校和专业，提供个性化的志愿填报方案。</p>
              <a href="#" class="card-link">查看更多</a>
            </div>

            <div class="feature-card">
              <div class="card-icon green-icon">
                <i data-lucide="compass" class="icon"></i>
              </div>
              <h3 class="card-title">个性化生涯规划</h3>
              <p class="card-description">通过AI测评，深入了解你的兴趣、性格与能力，为你量身定制未来的职业发展路径。</p>
              <a href="#" class="card-link">查看更多</a>
            </div>

            <div class="feature-card">
              <div class="card-icon blue-icon">
                <i data-lucide="bar-chart-3" class="icon"></i>
              </div>
              <h3 class="card-title">权威数据分析</h3>
              <p class="card-description">汇总整理最新的招生政策、院校分数线和就业前景等关键数据，助你科学决策。</p>
              <a href="#" class="card-link">查看更多</a>
            </div>
          </div>
        </div>
      </section>

      <!-- Core Features Section -->
      <section class="core-features-section">
        <div class="section-container">
          <h2 class="section-title">核心功能</h2>
          <div class="cards-grid">

            <div class="feature-card">
              <div class="card-icon purple-icon">
                <i data-lucide="bot" class="icon"></i>
              </div>
              <h3 class="card-title">AI志愿填报</h3>
              <p class="card-description">利用人工智能技术，结合你的高考成绩、兴趣特长和职业意向，生成最优的志愿填报方案。</p>
              <a href="#" class="card-link">了解更多 &rarr;</a>
            </div>

            <div class="feature-card">
              <div class="card-icon yellow-icon">
                <i data-lucide="user-check" class="icon"></i>
              </div>
              <h3 class="card-title">院校专业查询</h3>
              <p class="card-description">全面收录全国高校的详细信息，包括专业设置、录取分数线、就业情况等，供你随时查询。</p>
              <a href="#" class="card-link">了解更多 &rarr;</a>
            </div>

            <div class="feature-card">
              <div class="card-icon green-icon">
                <i data-lucide="book-open" class="icon"></i>
              </div>
              <h3 class="card-title">专业解析</h3>
              <p class="card-description">深入解析各专业的学习内容、发展前景和就业方向，帮助你更清晰地认识自己的选择。</p>
              <a href="#" class="card-link">了解更多 &rarr;</a>
            </div>
          </div>
        </div>
      </section>

      <!-- Business Support Section -->
      <section class="business-section">
        <div class="section-container">
          <h2 class="section-title">专业业务保障</h2>
          <p class="section-subtitle">权威、专业、全面的数据资源和服务</p>
          <div class="business-grid">

            <div class="business-item">
              <div class="business-icon purple-icon">
                <i data-lucide="database" class="icon"></i>
              </div>
              <h3 class="business-title">AI算法</h3>
              <p class="business-description">基于千万级数据训练的智能算法，精准匹配你的分数与院校。</p>
            </div>

            <div class="business-item">
              <div class="business-icon blue-icon">
                <i data-lucide="shield-check" class="icon"></i>
              </div>
              <h3 class="business-title">数据资源</h3>
              <p class="business-description">独家收录全国2000+高校、1200+专业的详细数据，持续更新。</p>
            </div>

            <div class="business-item">
              <div class="business-icon orange-icon">
                <i data-lucide="users" class="icon"></i>
              </div>
              <h3 class="business-title">专家团队</h3>
              <p class="business-description">汇聚高考志愿填报专家和行业资深人士，提供专业指导。</p>
            </div>

            <div class="business-item">
              <div class="business-icon green-icon">
                <i data-lucide="headphones" class="icon"></i>
              </div>
              <h3 class="business-title">贴心服务</h3>
              <p class="business-description">一对一咨询，全程陪伴，为你的升学之路保驾护航。</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Partner Schools Section -->
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
  </div>
</template>

<style lang="scss" scoped>
.home-page {
  font-family: 'Inter', sans-serif;
}

/* Header Styles */
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

/* Hero Section */
.hero-section {
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 5rem 0;
}

.hero-container {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}

.hero-title {
  font-size: 2.25rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.hero-subtitle {
  font-size: 1.125rem;
  margin-bottom: 2rem;
}

.hero-description {
  max-width: 42rem;
  margin: 0 auto;
}

/* Section Common Styles */
.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.section-title {
  font-size: 1.875rem;
  font-weight: bold;
  text-align: center;
  margin-bottom: 3rem;
}

.section-subtitle {
  text-align: center;
  color: #6b7280;
  margin-bottom: 3rem;
}

/* Recommendations & Core Features */
.recommendations-section {
  padding: 4rem 0;
}

.core-features-section {
  padding: 4rem 0;
  background: #f9fafb;
}

.cards-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

@media (min-width: 768px) {
  .cards-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.feature-card {
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-0.3125rem);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.card-icon {
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
}

.orange-icon {
  background: #ffedd5;
}

.green-icon {
  background: #dcfce7;
}

.blue-icon {
  background: #dbeafe;
}

.purple-icon {
  background: #f3e8ff;
}

.yellow-icon {
  background: #fef9c3;
}

.icon {
  width: 1.5rem;
  height: 1.5rem;
}

.orange-icon .icon {
  color: #f97316;
}

.green-icon .icon {
  color: #22c55e;
}

.blue-icon .icon {
  color: #3b82f6;
}

.purple-icon .icon {
  color: #a855f7;
}

.yellow-icon .icon {
  color: #eab308;
}

.card-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.card-description {
  color: #6b7280;
  line-height: 1.5;
}

.card-link {
  color: #3b82f6;
  text-decoration: none;
  margin-top: 1rem;
  display: inline-block;
  transition: color 0.3s ease;
}

.card-link:hover {
  color: #2563eb;
}

/* Business Section */
.business-section {
  padding: 4rem 0;
}

.business-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
}

@media (min-width: 768px) {
  .business-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

.business-item {
  text-align: center;
}

.business-icon {
  width: 4rem;
  height: 4rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
}

.business-title {
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.business-description {
  font-size: 0.875rem;
  color: #6b7280;
  line-height: 1.4;
}

/* Partners Section */
.partners-section {
  padding: 4rem 0;
  background: #f9fafb;
}

.partners-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 2rem;
}

@media (min-width: 768px) {
  .partners-grid {
    gap: 4rem;
  }
}

.partner-logo {
  width: 6rem;
  height: 6rem;
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.partner-icon {
  width: 3rem;
  height: 3rem;
  color: #9ca3af;
}

/* Footer */
.footer {
  background: #111827;
  color: white;
  padding: 3rem 0;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

@media (min-width: 768px) {
  .footer-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

.footer-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.footer-text {
  color: #9ca3af;
  line-height: 1.5;
}

.footer-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-list li {
  margin-bottom: 0.5rem;
  color: #9ca3af;
}

.footer-link {
  color: #9ca3af;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-link:hover {
  color: white;
}

.footer-icon {
  display: inline-block;
  width: 1rem;
  height: 1rem;
  margin-right: 0.5rem;
}

.footer-address {
  display: flex;
  align-items: center;
  margin-top: 1rem;
}

.footer-bottom {
  border-top: 1px solid #374151;
  margin-top: 2rem;
  padding-top: 2rem;
  text-align: center;
  color: #6b7280;
}

body {
  background-color: #f9fafb;
}
</style>