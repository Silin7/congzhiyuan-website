<script setup lang="ts">
import { ref, reactive } from 'vue'
import sideTop from '@/components/sideTop.vue'

// 筛选条件
const filters = reactive({
  schoolLevel: '',
  batch: '',
  admissionType: '',
  schoolName: '',
  schoolType: '',
  province: '',
  majorName: '',
  majorFeature: '',
  admissionRange: '全部'
})

// 院校专业数据
const universities = ref([
  {
    id: 1,
    name: '山东大学',
    province: '山东省 济南市',
    type: '公办',
    code: 'A422',
    tags: ['一流大学', '一流学科建设高校', '211', '985'],
    major: '人工智能',
    requirements: '物理和化学',
    majorCode: '34',
    tuition: '6600',
    majorRating: 'B',
    majorFeatures: ['国家级特色专业'],
    batch: '常规批',
    admissionType: '普通类',
    planCount: '120人',
    analysis: {
      year25: { minRank: '62', minScore: '620', count: '120' },
      year24: { minRank: '71', minScore: '625', count: '115' },
      year23: { minRank: '59', minScore: '624', count: '110' }
    },
    probability: '75%',
    level: '可冲击',
    selected: false
  },
  {
    id: 2,
    name: '中国海洋大学',
    province: '山东省 青岛市',
    type: '公办',
    code: 'A423',
    tags: ['一流大学', '211', '985'],
    major: '法学',
    requirements: '不限',
    majorCode: '49',
    tuition: '5280',
    majorRating: 'B',
    majorFeatures: ['教育部涉外法治人才协同培养创新基地'],
    batch: '常规批',
    admissionType: '普通类',
    planCount: '80人',
    analysis: {
      year25: { minRank: '621', minScore: '610', count: '80' },
      year24: { minRank: '711', minScore: '611', count: '90' },
      year23: { minRank: '519', minScore: '615', count: '90' }
    },
    probability: '82%',
    level: '较稳妥',
    selected: false
  }
])

// 分页
const pagination = reactive({
  currentPage: 1,
  pageSize: 10,
  total: 3
})

// 选择院校
const toggleSelection = (index: number) => {
  universities.value[index].selected = !universities.value[index].selected
}

// 重置筛选条件
const resetFilters = () => {
  Object.keys(filters).forEach(key => {
    (filters as any)[key] = ''
  })
  filters.admissionRange = '全部'
}
</script>

<template>
  <div class="volunteer-apply-page">

    <main class="volunteer-apply-main">
      <!-- 页面标题 -->
      <div class="page-header">
        <h1 class="page-title">志愿填报查询</h1>
      </div>

      <!-- 筛选条件区域 -->
      <div class="filter-section">
        <div class="filter-grid">
          <div class="filter-group">
            <label class="filter-label">院校层次</label>
            <select v-model="filters.schoolLevel" class="filter-select">
              <option value="">全部</option>
              <option value="985">985</option>
              <option value="211">211</option>
              <option value="一流大学">一流大学</option>
              <option value="一流学科">一流学科</option>
            </select>
          </div>

          <div class="filter-group">
            <label class="filter-label">录取批次</label>
            <select v-model="filters.batch" class="filter-select">
              <option value="">全部</option>
              <option value="提前批">提前批</option>
              <option value="常规批">常规批</option>
              <option value="专项批">专项批</option>
            </select>
          </div>

          <div class="filter-group">
            <label class="filter-label">录取类型</label>
            <select v-model="filters.admissionType" class="filter-select">
              <option value="">全部</option>
              <option value="普通类">普通类</option>
              <option value="艺术类">艺术类</option>
              <option value="体育类">体育类</option>
            </select>
          </div>

          <div class="filter-group">
            <label class="filter-label">院校名称</label>
            <input v-model="filters.schoolName" type="text" class="filter-input" placeholder="输入院校名称">
          </div>

          <div class="filter-group">
            <label class="filter-label">院校性质</label>
            <select v-model="filters.schoolType" class="filter-select">
              <option value="">全部</option>
              <option value="公办">公办</option>
              <option value="民办">民办</option>
              <option value="中外合作">中外合作</option>
            </select>
          </div>

          <div class="filter-group">
            <label class="filter-label">院校省份</label>
            <select v-model="filters.province" class="filter-select">
              <option value="">全部</option>
              <option value="北京">北京</option>
              <option value="上海">上海</option>
              <option value="山东">山东</option>
              <option value="江苏">江苏</option>
              <option value="浙江">浙江</option>
            </select>
          </div>

          <div class="filter-group">
            <label class="filter-label">专业名称</label>
            <input v-model="filters.majorName" type="text" class="filter-input" placeholder="输入专业名称">
          </div>

          <div class="filter-group">
            <label class="filter-label">专业特色</label>
            <select v-model="filters.majorFeature" class="filter-select">
              <option value="">全部</option>
              <option value="国家级特色专业">国家级特色专业</option>
              <option value="省级特色专业">省级特色专业</option>
              <option value="重点学科">重点学科</option>
            </select>
          </div>

          <div class="filter-group">
            <label class="filter-label">录取范围</label>
            <select v-model="filters.admissionRange" class="filter-select">
              <option value="全部">全部</option>
              <option value="可冲击">可冲击</option>
              <option value="较稳妥">较稳妥</option>
              <option value="可保底">可保底</option>
            </select>
          </div>
        </div>

        <div class="filter-actions">
          <button class="reset-btn" @click="resetFilters">重置</button>
          <button class="search-btn">查询</button>
        </div>
      </div>

      <!-- 结果统计 -->
      <div class="result-info">
        <span class="result-count">共 {{ pagination.total }} 条结果</span>
        <span class="result-page">第 {{ pagination.currentPage }} 页，共 {{ Math.ceil(pagination.total /
          pagination.pageSize) }} 页</span>
      </div>

      <!-- 院校专业列表 -->
      <div class="university-list">
        <div class="list-header">
          <div class="header-checkbox">选择</div>
          <div class="header-school">招生院校</div>
          <div class="header-major">招生专业</div>
          <div class="header-batch">批次类型</div>
          <div class="header-plan">本年计划</div>
          <div class="header-analysis">成绩分析</div>
          <div class="header-probability">录取概率</div>
          <div class="header-actions">填报操作</div>
        </div>

        <div v-for="(uni, index) in universities" :key="uni.id" class="university-item">
          <div class="item-checkbox">
            <input type="checkbox" :checked="uni.selected" @change="toggleSelection(index)">
          </div>

          <div class="item-school">
            <div class="school-name">{{ uni.name }}</div>
            <div class="school-info">
              <span class="school-province">{{ uni.province }}</span>
              <span class="school-type">{{ uni.type }}</span>
            </div>
            <div class="school-code">院校代码：{{ uni.code }}</div>
            <div class="school-tags">
              <span v-for="tag in uni.tags" :key="tag" class="tag">{{ tag }}</span>
            </div>
          </div>

          <div class="item-major">
            <div class="major-name">{{ uni.major }}</div>
            <div class="major-requirements">{{ uni.requirements }}</div>
            <div class="major-code">代号:{{ uni.majorCode }} 学费:{{ uni.tuition }}</div>
            <div class="major-rating">学科评估:{{ uni.majorRating }}</div>
            <div class="major-features">
              <span v-for="feature in uni.majorFeatures" :key="feature" class="feature">{{ feature }}</span>
            </div>
          </div>

          <div class="item-batch">
            <div>批次：{{ uni.batch }}</div>
            <div>类型：{{ uni.admissionType }}</div>
          </div>

          <div class="item-plan">{{ uni.planCount }}</div>

          <div class="item-analysis">
            <div>精确:25年最低位:{{ uni.analysis.year25.minRank }}，最低分:{{ uni.analysis.year25.minScore }}，录取数:{{
              uni.analysis.year25.count }}</div>
            <div>精确:24年最低位:{{ uni.analysis.year24.minRank }}，最低分:{{ uni.analysis.year24.minScore }}，录取数:{{
              uni.analysis.year24.count }}</div>
            <div>精确:23年最低位:{{ uni.analysis.year23.minRank }}，最低分:{{ uni.analysis.year23.minScore }}，录取数:{{
              uni.analysis.year23.count }}</div>
          </div>

          <div class="item-probability">
            <div class="probability-value">{{ uni.probability }}</div>
            <div class="probability-level">{{ uni.level }}</div>
          </div>

          <div class="item-actions">
            <button class="add-btn">加入志愿表</button>
            <button class="detail-btn">查看详情</button>
          </div>
        </div>
      </div>

      <!-- 分页 -->
      <div class="pagination">
        <button class="page-btn" :disabled="pagination.currentPage === 1">上一页</button>
        <span class="page-info">跳转到第</span>
        <input type="number" class="page-input" v-model="pagination.currentPage" min="1"
          :max="Math.ceil(pagination.total / pagination.pageSize)">
        <span class="page-info">页</span>
        <button class="page-btn"
          :disabled="pagination.currentPage === Math.ceil(pagination.total / pagination.pageSize)">下一页</button>
      </div>
    </main>
    <sideTop />

  </div>
</template>

<style lang="scss" scoped>
.volunteer-apply-page {
  min-height: 100vh;
  background: #f8fafc;
}

.volunteer-apply-main {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

/* 页面标题 */
.page-header {
  margin-bottom: 2rem;
}

.page-title {
  font-size: 2rem;
  font-weight: 600;
  color: #1f2937;
  text-align: center;
}

/* 筛选条件区域 */
.filter-section {
  background: white;
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.filter-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 1rem;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #374151;
}

.filter-select,
.filter-input {
  padding: 0.5rem 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  background: white;
}

.filter-select:focus,
.filter-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.filter-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}

.reset-btn,
.search-btn {
  padding: 0.5rem 1.5rem;
  border: none;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.reset-btn {
  background: #f3f4f6;
  color: #374151;
}

.reset-btn:hover {
  background: #e5e7eb;
}

.search-btn {
  background: #3b82f6;
  color: white;
}

.search-btn:hover {
  background: #2563eb;
}

/* 结果统计 */
.result-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  color: #6b7280;
  font-size: 0.875rem;
}

/* 院校专业列表 */
.university-list {
  background: white;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.list-header {
  display: grid;
  grid-template-columns: 60px 2fr 1.5fr 1fr 1fr 1.5fr 1fr 1fr;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: #f9fafb;
  border-bottom: 1px solid #e5e7eb;
  font-weight: 600;
  color: #374151;
  font-size: 0.875rem;
}

.university-item {
  display: grid;
  grid-template-columns: 60px 2fr 1.5fr 1fr 1fr 1.5fr 1fr 1fr;
  gap: 1rem;
  padding: 1.5rem;
  border-bottom: 1px solid #f3f4f6;
  transition: background-color 0.2s;
}

.university-item:hover {
  background: #f9fafb;
}

.university-item:last-child {
  border-bottom: none;
}

/* 复选框 */
.item-checkbox {
  display: flex;
  align-items: flex-start;
}

.item-checkbox input {
  width: 1rem;
  height: 1rem;
}

/* 院校信息 */
.school-name {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.school-info {
  display: flex;
  gap: 1rem;
  margin-bottom: 0.5rem;
  font-size: 0.875rem;
  color: #6b7280;
}

.school-code {
  font-size: 0.875rem;
  color: #6b7280;
  margin-bottom: 0.5rem;
}

.school-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  padding: 0.25rem 0.5rem;
  background: #eff6ff;
  color: #1d4ed8;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 500;
}

/* 专业信息 */
.major-name {
  font-size: 1rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.major-requirements {
  font-size: 0.875rem;
  color: #6b7280;
  margin-bottom: 0.5rem;
}

.major-code {
  font-size: 0.875rem;
  color: #6b7280;
  margin-bottom: 0.5rem;
}

.major-rating {
  font-size: 0.875rem;
  color: #6b7280;
  margin-bottom: 0.5rem;
}

.major-features {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.feature {
  padding: 0.25rem 0.5rem;
  background: #f0fdf4;
  color: #166534;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 500;
}

/* 批次类型 */
.item-batch {
  font-size: 0.875rem;
  color: #374151;
}

/* 计划人数 */
.item-plan {
  font-size: 0.875rem;
  color: #374151;
  font-weight: 500;
}

/* 成绩分析 */
.item-analysis {
  font-size: 0.75rem;
  color: #6b7280;
  line-height: 1.4;
}

/* 录取概率 */
.probability-value {
  font-size: 1rem;
  font-weight: 600;
  color: #059669;
  margin-bottom: 0.25rem;
}

.probability-level {
  font-size: 0.75rem;
  color: #6b7280;
  padding: 0.25rem 0.5rem;
  background: #f0fdf4;
  border-radius: 0.25rem;
  display: inline-block;
}

/* 操作按钮 */
.item-actions {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.add-btn,
.detail-btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.add-btn {
  background: #3b82f6;
  color: white;
}

.add-btn:hover {
  background: #2563eb;
}

.detail-btn {
  background: #f3f4f6;
  color: #374151;
}

.detail-btn:hover {
  background: #e5e7eb;
}

/* 分页 */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin-top: 2rem;
  padding: 1rem;
  background: white;
  border-radius: 0.75rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.page-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #d1d5db;
  background: white;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s;
}

.page-btn:hover:not(:disabled) {
  background: #f3f4f6;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-input {
  width: 4rem;
  padding: 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  text-align: center;
}

.page-info {
  font-size: 0.875rem;
  color: #6b7280;
}

/* 响应式设计 */
@media (max-width: 1200px) {

  .list-header,
  .university-item {
    grid-template-columns: 60px 1fr;
    gap: 0.5rem;
  }

  .list-header>div:not(.header-checkbox):not(.header-school),
  .university-item>div:not(.item-checkbox):not(.item-school) {
    display: none;
  }

  .item-school,
  .item-major,
  .item-batch,
  .item-plan,
  .item-analysis,
  .item-probability,
  .item-actions {
    grid-column: 2;
  }

  .item-school {
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 1rem;
    margin-bottom: 1rem;
  }
}

@media (max-width: 768px) {
  .volunteer-apply-main {
    padding: 1rem;
  }

  .filter-grid {
    grid-template-columns: 1fr;
  }

  .filter-actions {
    justify-content: center;
  }

  .pagination {
    flex-direction: column;
    gap: 0.5rem;
  }
}
</style>