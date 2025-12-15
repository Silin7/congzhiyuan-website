<script setup lang="ts">
import { ref } from 'vue'

// 学业能力测评维度
const academicDimensions = ref([
  {
    id: 1,
    name: '逻辑思维',
    description: '问题分析与推理能力',
    status: '未开始'
  },
  {
    id: 2,
    name: '语言能力',
    description: '理解表达与写作水平',
    status: '未开始'
  },
  {
    id: 3,
    name: '数理能力',
    description: '抽象思维与计算能力',
    status: '未开始'
  },
  {
    id: 4,
    name: '创新思维',
    description: '原创想法与实践能力',
    status: '未开始'
  }
])

// 职业类型
const careerTypes = ref([
  { id: 1, name: '研究型', icon: '🧪' },
  { id: 2, name: '艺术型', icon: '🎨' },
  { id: 3, name: '社会型', icon: '👥' },
  { id: 4, name: '企业型', icon: '💼' },
  { id: 5, name: '现实型', icon: '🔧' },
  { id: 6, name: '传统型', icon: '📋' }
])
</script>

<template>
  <div class="ai-assessment-page">
    <main class="ai-assessment-main">
      <!-- 页面标题 -->
      <div class="page-header">
        <h1 class="page-title">AI智能测评</h1>
        <p class="page-subtitle">科学评估你的能力与兴趣，为专业选择提供数据支撑</p>
      </div>

      <!-- 学业能力测评 -->
      <section class="assessment-section">
        <h2 class="section-title">学业能力测评</h2>
        <p class="section-description">通过科学的评估模型，精准分析您的学科优势与学习潜力，为专业选择提供数据支撑。测评涵盖逻辑思维、语言能力等核心维度。</p>

        <div class="dimensions-grid">
          <div v-for="dimension in academicDimensions" :key="dimension.id" class="dimension-card">
            <h3 class="dimension-name">{{ dimension.name }}</h3>
            <p class="dimension-description">{{ dimension.description }}</p>
            <div class="dimension-status">
              <span class="status-label">测评状态：</span>
              <span class="status-value">{{ dimension.status }}</span>
            </div>
            <button class="start-btn">开始测评</button>
          </div>
        </div>
      </section>

      <!-- 职业测评 -->
      <section class="assessment-section">
        <h2 class="section-title">职业测评</h2>
        <p class="section-description">基于霍兰德职业理论模型，深入分析您的职业兴趣倾向，匹配适合的专业发展方向。识别潜在职业优势，提供发展建议。</p>

        <div class="career-types">
          <h3 class="career-types-title">测评涵盖职业类型</h3>
          <div class="career-types-grid">
            <div v-for="type in careerTypes" :key="type.id" class="career-type-card">
              <span class="career-type-icon">{{ type.icon }}</span>
              <span class="career-type-name">{{ type.name }}</span>
            </div>
          </div>
        </div>

        <div class="assessment-status">
          <div class="status-info">
            <h3 class="status-title">测评状态</h3>
            <span class="status-value">未开始</span>
          </div>
          <button class="start-btn large-btn">开始职业测评</button>
        </div>
      </section>

      <!-- 测评报告示例 -->
      <section class="report-section">
        <h2 class="section-title">测评报告示例</h2>

        <div class="report-card">
          <div class="report-header">
            <h3 class="report-title">职业兴趣测评报告</h3>
            <p class="report-description">包含详细职业倾向分析和专业匹配建议</p>
          </div>
          <div class="report-content">
            <div class="report-preview">
              <div class="preview-header">
                <div class="preview-title">职业兴趣测评结果</div>
                <div class="preview-date">2024年6月15日</div>
              </div>
              <div class="preview-body">
                <div class="preview-section">
                  <h4 class="preview-section-title">核心职业倾向</h4>
                  <div class="preview-chart">
                    <div class="chart-placeholder">
                      <div class="chart-title">职业兴趣分布</div>
                      <div class="chart-bars">
                        <div class="chart-bar">
                          <div class="bar-label">研究型</div>
                          <div class="bar-container">
                            <div class="bar-fill" style="width: 85%"></div>
                          </div>
                        </div>
                        <div class="chart-bar">
                          <div class="bar-label">艺术型</div>
                          <div class="bar-container">
                            <div class="bar-fill" style="width: 72%"></div>
                          </div>
                        </div>
                        <div class="chart-bar">
                          <div class="bar-label">社会型</div>
                          <div class="bar-container">
                            <div class="bar-fill" style="width: 68%"></div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="preview-section">
                  <h4 class="preview-section-title">专业匹配建议</h4>
                  <div class="preview-suggestions">
                    <div class="suggestion-item">计算机科学与技术</div>
                    <div class="suggestion-item">软件工程</div>
                    <div class="suggestion-item">数据科学与大数据技术</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<style lang="scss" scoped>
.ai-assessment-page {
  min-height: 100vh;
  background: #f8fafc;
}

.ai-assessment-main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

/* 页面标题 */
.page-header {
  text-align: center;
  margin-bottom: 3rem;
}

.page-title {
  font-size: 2rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.page-subtitle {
  font-size: 1rem;
  color: #6b7280;
}

/* 通用section样式 */
.assessment-section,
.report-section {
  background: white;
  border-radius: 0.75rem;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.75rem;
}

.section-description {
  color: #6b7280;
  margin-bottom: 2rem;
  line-height: 1.6;
}

/* 学业能力测评维度 */
.dimensions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.dimension-card {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  padding: 1.5rem;
  transition: all 0.2s;
}

.dimension-card:hover {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transform: translateY(-1px);
}

.dimension-name {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.dimension-description {
  color: #6b7280;
  margin-bottom: 1rem;
  font-size: 0.875rem;
}

.dimension-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
}

.status-label {
  color: #6b7280;
}

.status-value {
  color: #dc2626;
  font-weight: 500;
}

.start-btn {
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 0.375rem;
  padding: 0.625rem 1.25rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  width: 100%;
}

.start-btn:hover {
  background: #2563eb;
  box-shadow: 0 2px 4px rgba(59, 130, 246, 0.2);
}

.start-btn.large-btn {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
}

/* 职业测评 */
.career-types {
  margin-bottom: 2rem;
}

.career-types-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 1.5rem;
}

.career-types-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 1rem;
}

.career-type-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  padding: 1.5rem 1rem;
  transition: all 0.2s;
}

.career-type-card:hover {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transform: translateY(-1px);
}

.career-type-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.career-type-name {
  font-size: 0.875rem;
  font-weight: 500;
  color: #1f2937;
}

/* 测评状态 */
.assessment-status {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fef3c7;
  border: 1px solid #fde68a;
  border-radius: 0.5rem;
  padding: 1.5rem;
}

.status-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.status-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #92400e;
}

/* 测评报告示例 */
.report-card {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  overflow: hidden;
}

.report-header {
  background: #3b82f6;
  color: white;
  padding: 1.5rem 2rem;
}

.report-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.report-description {
  font-size: 0.875rem;
  opacity: 0.9;
}

.report-content {
  padding: 2rem;
}

.report-preview {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  overflow: hidden;
}

.preview-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f3f4f6;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.preview-title {
  font-weight: 600;
  color: #1f2937;
}

.preview-date {
  font-size: 0.875rem;
  color: #6b7280;
}

.preview-body {
  padding: 1.5rem;
}

.preview-section {
  margin-bottom: 1.5rem;
}

.preview-section:last-child {
  margin-bottom: 0;
}

.preview-section-title {
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 1rem;
}

.preview-chart {
  background: #f9fafb;
  border-radius: 0.375rem;
  padding: 1rem;
}

.chart-placeholder {
  text-align: center;
}

.chart-title {
  font-size: 0.875rem;
  font-weight: 500;
  color: #6b7280;
  margin-bottom: 1rem;
}

.chart-bars {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  max-width: 300px;
  margin: 0 auto;
}

.chart-bar {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.bar-label {
  width: 60px;
  font-size: 0.75rem;
  color: #6b7280;
  text-align: right;
}

.bar-container {
  flex: 1;
  height: 12px;
  background: #e5e7eb;
  border-radius: 6px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #3b82f6 0%, #60a5fa 100%);
  border-radius: 6px;
  transition: width 0.3s ease;
}

.preview-suggestions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.suggestion-item {
  background: #dbeafe;
  color: #1d4ed8;
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .ai-assessment-main {
    padding: 1rem;
  }

  .assessment-section,
  .report-section {
    padding: 1.5rem;
  }

  .page-title {
    font-size: 1.5rem;
  }

  .dimensions-grid {
    grid-template-columns: 1fr;
  }

  .career-types-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .assessment-status {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .status-info {
    justify-content: center;
  }

  .preview-header {
    flex-direction: column;
    gap: 0.5rem;
    text-align: center;
  }
}
</style>