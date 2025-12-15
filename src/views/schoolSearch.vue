<script setup lang="ts">
import { ref } from 'vue'
import sideTop from '@/components/sideTop.vue'
</script>

<template>
  <div class="school-search-page">
    <main>
      <!-- Hero Section -->
      <section class="hero-section">
        <div class="hero-container">
          <h1 class="hero-title">院校查询</h1>
          <p class="hero-subtitle">智能匹配你的分数，精准找到适合你的院校</p>
        </div>
      </section>

      <!-- Search Section -->
      <section class="search-section">
        <div class="section-container">
          <div class="search-form">
            <div class="search-input-group">
              <label for="score" class="form-label">高考分数</label>
              <input type="number" id="score" class="form-input" placeholder="请输入你的高考分数">
            </div>
            <div class="search-input-group">
              <label for="province" class="form-label">所在省份</label>
              <select id="province" class="form-select">
                <option value="">请选择省份</option>
                <option value="北京">北京</option>
                <option value="上海">上海</option>
                <option value="广东">广东</option>
                <option value="江苏">江苏</option>
                <option value="浙江">浙江</option>
              </select>
            </div>
            <div class="search-input-group">
              <label for="subject" class="form-label">选科组合</label>
              <select id="subject" class="form-select">
                <option value="">请选择选科组合</option>
                <option value="物理+化学+生物">物理+化学+生物</option>
                <option value="物理+化学+地理">物理+化学+地理</option>
                <option value="物理+生物+地理">物理+生物+地理</option>
                <option value="历史+政治+地理">历史+政治+地理</option>
                <option value="历史+政治+化学">历史+政治+化学</option>
              </select>
            </div>
            <div class="search-button-group">
              <button class="search-btn primary-btn">立即查询</button>
              <button class="search-btn secondary-btn">重置</button>
            </div>
          </div>
        </div>
      </section>

      <!-- Filters Section -->
      <section class="filters-section">
        <div class="section-container">
          <div class="filters-container">
            <div class="filter-group">
              <h3 class="filter-title">院校类型</h3>
              <div class="filter-options">
                <label class="filter-option">
                  <input type="checkbox" name="school-type">
                  <span>综合类</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-type">
                  <span>理工类</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-type">
                  <span>师范类</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-type">
                  <span>农林类</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-type">
                  <span>医药类</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-type">
                  <span>财经类</span>
                </label>
              </div>
            </div>
            <div class="filter-group">
              <h3 class="filter-title">院校层次</h3>
              <div class="filter-options">
                <label class="filter-option">
                  <input type="checkbox" name="school-level">
                  <span>本科一批</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-level">
                  <span>本科二批</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-level">
                  <span>本科三批</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-level">
                  <span>专科</span>
                </label>
              </div>
            </div>
            <div class="filter-group">
              <h3 class="filter-title">院校地区</h3>
              <div class="filter-options">
                <label class="filter-option">
                  <input type="checkbox" name="school-area">
                  <span>华北地区</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-area">
                  <span>华东地区</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-area">
                  <span>华南地区</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-area">
                  <span>华中地区</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-area">
                  <span>西南地区</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" name="school-area">
                  <span>西北地区</span>
                </label>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Results Section -->
      <section class="results-section">
        <div class="section-container">
          <div class="results-header">
            <div class="results-info">
              <span class="results-count">共找到 <strong>1234</strong> 所院校</span>
            </div>
            <div class="results-sort">
              <label class="sort-label">排序方式：</label>
              <select class="sort-select">
                <option value="relevance">相关性</option>
                <option value="score-desc">分数从高到低</option>
                <option value="score-asc">分数从低到高</option>
                <option value="rank">院校排名</option>
              </select>
            </div>
          </div>

          <!-- Results List -->
          <div class="results-list">
            <div class="result-item">
              <div class="result-header">
                <h3 class="school-name">清华大学</h3>
                <span class="school-level">本科一批</span>
              </div>
              <div class="result-content">
                <div class="school-info">
                  <div class="info-item">
                    <i class="fa fa-map-marker info-icon"></i>
                    <span>北京</span>
                  </div>
                  <div class="info-item">
                    <i class="fa fa-building info-icon"></i>
                    <span>综合类</span>
                  </div>
                  <div class="info-item">
                    <i class="fa fa-trophy info-icon"></i>
                    <span>双一流</span>
                  </div>
                  <div class="info-item">
                    <i class="fa fa-users info-icon"></i>
                    <span>10000+在校生</span>
                  </div>
                </div>
                <div class="school-score">
                  <div class="score-item">
                    <span class="score-label">最低录取分数：</span>
                    <span class="score-value">680</span>
                  </div>
                  <div class="score-item">
                    <span class="score-label">最低录取位次：</span>
                    <span class="score-value">120</span>
                  </div>
                </div>
              </div>
              <div class="result-footer">
                <button class="action-btn">查看详情</button>
                <button class="action-btn secondary">加入志愿表</button>
              </div>
            </div>

            <div class="result-item">
              <div class="result-header">
                <h3 class="school-name">北京大学</h3>
                <span class="school-level">本科一批</span>
              </div>
              <div class="result-content">
                <div class="school-info">
                  <div class="info-item">
                    <i class="fa fa-map-marker info-icon"></i>
                    <span>北京</span>
                  </div>
                  <div class="info-item">
                    <i class="fa fa-building info-icon"></i>
                    <span>综合类</span>
                  </div>
                  <div class="info-item">
                    <i class="fa fa-trophy info-icon"></i>
                    <span>双一流</span>
                  </div>
                  <div class="info-item">
                    <i class="fa fa-users info-icon"></i>
                    <span>10000+在校生</span>
                  </div>
                </div>
                <div class="school-score">
                  <div class="score-item">
                    <span class="score-label">最低录取分数：</span>
                    <span class="score-value">678</span>
                  </div>
                  <div class="score-item">
                    <span class="score-label">最低录取位次：</span>
                    <span class="score-value">150</span>
                  </div>
                </div>
              </div>
              <div class="result-footer">
                <button class="action-btn">查看详情</button>
                <button class="action-btn secondary">加入志愿表</button>
              </div>
            </div>

            <div class="result-item">
              <div class="result-header">
                <h3 class="school-name">复旦大学</h3>
                <span class="school-level">本科一批</span>
              </div>
              <div class="result-content">
                <div class="school-info">
                  <div class="info-item">
                    <i class="fa fa-map-marker info-icon"></i>
                    <span>上海</span>
                  </div>
                  <div class="info-item">
                    <i class="fa fa-building info-icon"></i>
                    <span>综合类</span>
                  </div>
                  <div class="info-item">
                    <i class="fa fa-trophy info-icon"></i>
                    <span>双一流</span>
                  </div>
                  <div class="info-item">
                    <i class="fa fa-users info-icon"></i>
                    <span>10000+在校生</span>
                  </div>
                </div>
                <div class="school-score">
                  <div class="score-item">
                    <span class="score-label">最低录取分数：</span>
                    <span class="score-value">675</span>
                  </div>
                  <div class="score-item">
                    <span class="score-label">最低录取位次：</span>
                    <span class="score-value">200</span>
                  </div>
                </div>
              </div>
              <div class="result-footer">
                <button class="action-btn">查看详情</button>
                <button class="action-btn secondary">加入志愿表</button>
              </div>
            </div>
          </div>

          <!-- Pagination -->
          <div class="pagination">
            <button class="page-btn disabled">
              <i class="fa fa-chevron-left page-icon"></i>
              上一页
            </button>
            <button class="page-btn active">1</button>
            <button class="page-btn">2</button>
            <button class="page-btn">3</button>
            <button class="page-btn">4</button>
            <button class="page-btn">5</button>
            <button class="page-btn">...</button>
            <button class="page-btn">124</button>
            <button class="page-btn">
              下一页
              <i class="fa fa-chevron-right page-icon"></i>
            </button>
          </div>
        </div>
      </section>
    </main>
    <sideTop />
  </div>
</template>

<style lang="scss" scoped>
.school-search-page {
  font-family: 'Inter', sans-serif;
}

/* Hero Section */
.hero-section {
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 3rem 0;
}

.hero-container {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}

.hero-title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.hero-subtitle {
  font-size: 1rem;
}

/* Section Common Styles */
.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

/* Search Section */
.search-section {
  background: white;
  padding: 2rem 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.search-form {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  align-items: end;
}

@media (min-width: 768px) {
  .search-form {
    grid-template-columns: repeat(3, 1fr) auto;
  }
}

.search-input-group {
  display: flex;
  flex-direction: column;
}

.form-label {
  font-size: 0.875rem;
  font-weight: 500;
  margin-bottom: 0.5rem;
  color: #374151;
}

.form-input,
.form-select {
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.form-input:focus,
.form-select:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.search-button-group {
  display: flex;
  gap: 0.75rem;
}

.search-btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.375rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.search-btn.primary-btn {
  background: #3b82f6;
  color: white;
}

.search-btn.primary-btn:hover {
  background: #2563eb;
}

.search-btn.secondary-btn {
  background: #f3f4f6;
  color: #374151;
  border: 1px solid #d1d5db;
}

.search-btn.secondary-btn:hover {
  background: #e5e7eb;
}

/* Filters Section */
.filters-section {
  background: #f9fafb;
  padding: 2rem 0;
}

.filters-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

@media (min-width: 768px) {
  .filters-container {
    grid-template-columns: repeat(3, 1fr);
  }
}

.filter-group {
  background: white;
  padding: 1.5rem;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.filter-title {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #111827;
}

.filter-options {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.filter-option {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #4b5563;
  cursor: pointer;
  user-select: none;
}

.filter-option input[type="checkbox"] {
  width: 1rem;
  height: 1rem;
  cursor: pointer;
}

/* Results Section */
.results-section {
  padding: 2rem 0;
  background: white;
}

.results-header {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
  gap: 1rem;
}

@media (min-width: 768px) {
  .results-header {
    flex-direction: row;
    align-items: center;
  }
}

.results-info {
  font-size: 0.875rem;
  color: #6b7280;
}

.results-info strong {
  color: #111827;
}

.results-sort {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.sort-label {
  font-size: 0.875rem;
  color: #4b5563;
}

.sort-select {
  padding: 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 0.875rem;
}

/* Results List */
.results-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2rem;
}

.result-item {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.result-item:hover {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border-color: #d1d5db;
}

.result-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.school-name {
  font-size: 1.125rem;
  font-weight: 600;
  color: #111827;
  margin: 0;
}

.school-level {
  background: #3b82f6;
  color: white;
  font-size: 0.75rem;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-weight: 500;
}

.result-content {
  margin-bottom: 1.5rem;
}

.school-info {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-bottom: 1rem;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #6b7280;
}

.info-icon {
  width: 1rem;
  height: 1rem;
  color: #9ca3af;
}

.school-score {
  background: white;
  padding: 1rem;
  border-radius: 0.375rem;
  border: 1px solid #e5e7eb;
}

.score-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.5rem;
  font-size: 0.875rem;
}

.score-item:last-child {
  margin-bottom: 0;
}

.score-label {
  color: #6b7280;
}

.score-value {
  font-weight: 600;
  color: #3b82f6;
}

.result-footer {
  display: flex;
  gap: 0.75rem;
  justify-content: flex-end;
}

.action-btn {
  padding: 0.5rem 1.25rem;
  border: none;
  border-radius: 0.375rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.875rem;
}

.action-btn:not(.secondary) {
  background: #3b82f6;
  color: white;
}

.action-btn:not(.secondary):hover {
  background: #2563eb;
}

.action-btn.secondary {
  background: white;
  color: #3b82f6;
  border: 1px solid #3b82f6;
}

.action-btn.secondary:hover {
  background: #eff6ff;
}

/* Pagination */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
}

.page-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #d1d5db;
  background: white;
  color: #374151;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.page-btn:hover:not(.disabled) {
  background: #f3f4f6;
  border-color: #9ca3af;
}

.page-btn.active {
  background: #3b82f6;
  color: white;
  border-color: #3b82f6;
}

.page-btn.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-icon {
  width: 0.875rem;
  height: 0.875rem;
}
</style>