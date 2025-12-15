<script setup lang="ts">
import { ref, reactive } from 'vue'
import sideTop from '@/components/sideTop.vue'

// 筛选条件
const filters = reactive({
  category: '',
  majorType: '',
  major: ''
})

// 模拟数据
const categories = ref([
  { value: '', label: '请选择门类' },
  { value: '哲学', label: '哲学' },
  { value: '经济学', label: '经济学' },
  { value: '法学', label: '法学' },
  { value: '教育学', label: '教育学' },
  { value: '文学', label: '文学' }
])

const majorTypes = ref([
  { value: '', label: '请选择专业类' }
])

const majors = ref([
  { value: '', label: '请选择专业' }
])

// 专业列表数据
const majorList = ref([
  {
    id: 1,
    category: '哲学',
    majorType: '哲学类',
    name: '哲学',
    code: '010101',
    schools: '查看',
    satisfaction: '3.9'
  },
  {
    id: 2,
    category: '哲学',
    majorType: '哲学类',
    name: '逻辑学',
    code: '010102',
    schools: '查看',
    satisfaction: '4.1'
  },
  {
    id: 3,
    category: '经济学',
    majorType: '经济学类',
    name: '经济学',
    code: '020101',
    schools: '查看',
    satisfaction: '3.9'
  },
  {
    id: 4,
    category: '经济学',
    majorType: '经济学类',
    name: '经济统计学',
    code: '020102',
    schools: '查看',
    satisfaction: '4.1'
  },
  {
    id: 5,
    category: '法学',
    majorType: '法学类',
    name: '知识产权',
    code: '030102',
    schools: '查看',
    satisfaction: '3.7'
  },
  {
    id: 6,
    category: '教育学',
    majorType: '教育学类',
    name: '教育学',
    code: '040101',
    schools: '查看',
    satisfaction: '4.0'
  },
  {
    id: 7,
    category: '文学',
    majorType: '中国语言文学类',
    name: '汉语言文学',
    code: '050101',
    schools: '查看',
    satisfaction: '3.6'
  }
])

// 筛选后的专业列表
const filteredMajors = ref([...majorList.value])

// 模拟专业类数据
const mockMajorTypes = {
  '哲学': [{ value: '哲学类', label: '哲学类' }],
  '经济学': [{ value: '经济学类', label: '经济学类' }],
  '法学': [{ value: '法学类', label: '法学类' }],
  '教育学': [{ value: '教育学类', label: '教育学类' }],
  '文学': [{ value: '中国语言文学类', label: '中国语言文学类' }]
}

// 模拟专业数据
const mockMajors = {
  '哲学类': [
    { value: '', label: '请选择专业' },
    { value: '哲学', label: '哲学' },
    { value: '逻辑学', label: '逻辑学' }
  ],
  '经济学类': [
    { value: '', label: '请选择专业' },
    { value: '经济学', label: '经济学' },
    { value: '经济统计学', label: '经济统计学' }
  ],
  '法学类': [
    { value: '', label: '请选择专业' },
    { value: '知识产权', label: '知识产权' }
  ],
  '教育学类': [
    { value: '', label: '请选择专业' },
    { value: '教育学', label: '教育学' }
  ],
  '中国语言文学类': [
    { value: '', label: '请选择专业' },
    { value: '汉语言文学', label: '汉语言文学' }
  ]
}

// 门类选择变化
const handleCategoryChange = () => {
  // 重置专业类和专业
  filters.majorType = ''
  filters.major = ''

  // 更新专业类选项
  majorTypes.value = mockMajorTypes[filters.category as keyof typeof mockMajorTypes] || [{ value: '', label: '请选择专业类' }]

  // 重置专业选项
  majors.value = [{ value: '', label: '请选择专业' }]

  // 筛选专业列表
  filterMajors()
}

// 专业类选择变化
const handleMajorTypeChange = () => {
  // 重置专业
  filters.major = ''

  // 更新专业选项
  majors.value = mockMajors[filters.majorType as keyof typeof mockMajors] || [{ value: '', label: '请选择专业' }]

  // 筛选专业列表
  filterMajors()
}

// 专业选择变化
const handleMajorChange = () => {
  // 筛选专业列表
  filterMajors()
}

// 筛选专业列表
const filterMajors = () => {
  filteredMajors.value = majorList.value.filter(major => {
    let match = true

    if (filters.category && major.category !== filters.category) {
      match = false
    }

    if (filters.majorType && major.majorType !== filters.majorType) {
      match = false
    }

    if (filters.major && major.name !== filters.major) {
      match = false
    }

    return match
  })
}
</script>

<template>
  <div class="major-analysis-page">

    <main class="major-analysis-main">
      <!-- 页面标题 -->
      <div class="page-header">
        <h1 class="page-title">大学专业信息库</h1>
        <p class="page-subtitle">全面解析专业门类、培养方向与就业前景</p>
      </div>

      <!-- 筛选区域 -->
      <div class="filter-section">
        <div class="filter-title">选择专业</div>
        <div class="filter-grid">
          <div class="filter-group">
            <label class="filter-label">门类</label>
            <select v-model="filters.category" class="filter-select" @change="handleCategoryChange">
              <option v-for="category in categories" :key="category.value" :value="category.value">
                {{ category.label }}
              </option>
            </select>
          </div>

          <div class="filter-group">
            <label class="filter-label">专业类</label>
            <select v-model="filters.majorType" class="filter-select" @change="handleMajorTypeChange">
              <option v-for="type in majorTypes" :key="type.value" :value="type.value">
                {{ type.label }}
              </option>
            </select>
          </div>

          <div class="filter-group">
            <label class="filter-label">专业</label>
            <select v-model="filters.major" class="filter-select" @change="handleMajorChange">
              <option v-for="major in majors" :key="major.value" :value="major.value">
                {{ major.label }}
              </option>
            </select>
          </div>
        </div>
      </div>

      <!-- 专业列表表格 -->
      <div class="major-table-container">
        <table class="major-table">
          <thead>
            <tr>
              <th>门类</th>
              <th>专业类</th>
              <th>专业名称</th>
              <th>专业代码</th>
              <th>开设院校</th>
              <th>专业满意度</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="major in filteredMajors" :key="major.id">
              <td>{{ major.category }}</td>
              <td>{{ major.majorType }}</td>
              <td>{{ major.name }}</td>
              <td>{{ major.code }}</td>
              <td>{{ major.schools }}</td>
              <td>{{ major.satisfaction }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
    <sideTop />

  </div>
</template>

<style lang="scss" scoped>
.major-analysis-page {
  min-height: 100vh;
  background: #f8fafc;
}

.major-analysis-main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

/* 页面标题 */
.page-header {
  text-align: center;
  margin-bottom: 2.5rem;
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

/* 筛选区域 */
.filter-section {
  background: white;
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.filter-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 1rem;
}

.filter-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
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

.filter-select {
  padding: 0.5rem 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  background: white;
  transition: all 0.2s;
}

.filter-select:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* 专业表格 */
.major-table-container {
  background: white;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.major-table {
  width: 100%;
  border-collapse: collapse;
}

.major-table th,
.major-table td {
  padding: 1rem 1.5rem;
  text-align: left;
  border-bottom: 1px solid #f3f4f6;
}

.major-table th {
  background: #f9fafb;
  font-weight: 600;
  color: #374151;
  font-size: 0.875rem;
}

.major-table td {
  color: #6b7280;
  font-size: 0.875rem;
}

.major-table tbody tr:hover {
  background: #f9fafb;
}

.major-table tbody tr:last-child td {
  border-bottom: none;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .major-analysis-main {
    padding: 1rem;
  }

  .page-title {
    font-size: 1.5rem;
  }

  .filter-grid {
    grid-template-columns: 1fr;
  }

  .major-table-container {
    overflow-x: auto;
  }

  .major-table {
    min-width: 600px;
  }
}
</style>