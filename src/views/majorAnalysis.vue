<script setup lang="ts">
import { ref, reactive } from 'vue'
import sideTop from '@/components/sideTop.vue'

// 声明响应式变量
// 教育类型 - 可选值：'undergraduate', 'vocational-undergrad', 'vocational-college'
const selectedEducationType = ref('undergraduate')
// 筛选条件
const selectedCategory = ref('') // 门类
const selectedMajorType = ref('') // 专业类
const selectedMajor = ref('') // 专业
// 表格展开状态 - 存储展开的行ID
const expandedRows = ref<string[]>([])

// 教育类型点击事件处理函数
const handleEducationTypeClick = (type: string) => {
  selectedEducationType.value = type
  console.log(`选择了教育类型: ${type}`)
}

// 重置筛选事件处理函数
const handleResetFilter = () => {
  selectedCategory.value = ''
  selectedMajorType.value = ''
  selectedMajor.value = ''
  console.log('重置了筛选条件')
}

// 表格行展开/折叠事件处理函数
const handleRowClick = (rowId: string) => {
  const index = expandedRows.value.indexOf(rowId)
  if (index > -1) {
    expandedRows.value.splice(index, 1)
  } else {
    expandedRows.value.push(rowId)
  }
  console.log(`切换行展开状态: ${rowId}, 当前展开行: ${expandedRows.value}`)
}

// 查看开设院校事件处理函数
const handleViewSchools = (majorCode: string, majorName: string) => {
  console.log(`查看专业开设院校: ${majorName} (${majorCode})`)
  // 这里可以添加跳转到开设院校页面的逻辑
}
</script>

<template>
  <div class="major-analysis-page">
    <main class="container mx-auto px-6 py-8">
      <div class="bg-white rounded-lg shadow-sm">
        <!-- 内容标题 -->
        <div class="px-6 py-4 border-b">
          <h1 class="text-2xl font-bold text-secondary">大学专业信息库</h1>
          <p class="text-info mt-2">全面解析专业门类、培养方向与就业前景</p>
        </div>
        <!-- 分类按钮区域 -->
        <div class="px-6 py-4 flex items-center justify-between border-b">
          <div class="flex space-x-3">
            <button @click="handleEducationTypeClick('undergraduate')" :class="[
              'px-4 py-2 rounded-full education-type-btn',
              selectedEducationType === 'undergraduate' ? 'bg-blue-600 text-white border-blue-600' : 'border',
            ]" data-type="undergraduate">
              本科（普通教育）
            </button>
            <button @click="handleEducationTypeClick('vocational-undergrad')" :class="[
              'px-4 py-2 rounded-full education-type-btn',
              selectedEducationType === 'vocational-undergrad'
                ? 'bg-blue-600 text-white border-blue-600'
                : 'border',
            ]" data-type="vocational-undergrad">
              本科（职业教育）
            </button>
            <button @click="handleEducationTypeClick('vocational-college')" :class="[
              'px-4 py-2 rounded-full education-type-btn',
              selectedEducationType === 'vocational-college' ? 'bg-blue-600 text-white border-blue-600' : 'border',
            ]" data-type="vocational-college">
              高职（专科）
            </button>
          </div>
        </div>
        <!-- 联动筛选区域 -->
        <div class="px-6 py-4 flex flex-wrap gap-4 border-b bg-gray-50">
          <div class="flex flex-col">
            <label class="text-sm font-medium text-secondary mb-2">选择门类</label>
            <select v-model="selectedCategory"
              class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
              id="majorCategorySelect">
              <option value="">全部门类</option>
              <option value="哲学">哲学</option>
              <option value="经济学">经济学</option>
              <option value="法学">法学</option>
              <option value="教育学">教育学</option>
              <option value="文学">文学</option>
            </select>
          </div>
          <div class="flex flex-col">
            <label class="text-sm font-medium text-secondary mb-2">选择专业类</label>
            <select v-model="selectedMajorType"
              class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
              id="majorTypeSelect">
              <option value="">全部专业类</option>
            </select>
          </div>
          <div class="flex flex-col">
            <label class="text-sm font-medium text-secondary mb-2">选择专业</label>
            <select v-model="selectedMajor"
              class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
              id="majorNameSelect">
              <option value="">全部专业</option>
            </select>
          </div>
          <div class="flex items-end">
            <button @click="handleResetFilter"
              class="px-4 py-2 border border-gray-300 rounded-md hover:bg-gray-100 transition" id="resetFilterBtn">
              重置筛选
            </button>
          </div>
        </div>
        <!-- 专业目录表格 -->
        <div class="overflow-x-auto hide-scrollbar">
          <table class="min-w-full divide-y divide-gray-200">
            <thead>
              <tr class="bg-gray-50">
                <th class="px-6 py-3 text-left text-xs font-medium text-secondary uppercase tracking-wider" scope="col">
                  门类
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-secondary uppercase tracking-wider" scope="col">
                  专业类
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-secondary uppercase tracking-wider" scope="col">
                  专业名称
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-secondary uppercase tracking-wider" scope="col">
                  专业代码
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-secondary uppercase tracking-wider" scope="col">
                  开设院校
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-secondary uppercase tracking-wider" scope="col">
                  专业满意度
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200" id="professionTableBody">
              <tr @click="handleRowClick('-1')" class="cursor-pointer hover:bg-blue-50" data-row-id="-1">
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                      viewBox="0 0 24 24" data-icon="mdi:chevron-right" class="iconify iconify--mdi"
                      :class="expandedRows.includes('-1') ? 'rotate-90 transition-transform' : ''">
                      <path fill="currentColor" d="M8.59 16.58L13.17 12L8.59 7.41L10 6l6 6l-6 6z"></path>
                    </svg>
                    <span class="ml-2 text-primary">哲学</span>
                  </div>
                </td>
                <td class="px-6 py-4"><span class="text-primary">哲学类</span></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
              </tr>
              <tr :class="[expandedRows.includes('-1') ? '' : 'hidden', 'data-child']" data-parent="-1">
                <td class="px-6 py-4 pl-16 text-info">哲学</td>
                <td class="px-6 py-4 text-info">哲学类</td>
                <td class="px-6 py-4 font-medium">哲学</td>
                <td class="px-6 py-4 text-info">010101</td>
                <td class="px-6 py-4 text-primary cursor-pointer" @click="handleViewSchools('010101', '哲学')">
                  查看
                </td>
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <div class="w-32 h-2 bg-gray-200 rounded-full mr-2">
                      <div class="h-full bg-success rounded-full" style="width: 78%"></div>
                    </div>
                    <span class="text-success font-medium">3.9</span>
                  </div>
                </td>
              </tr>
              <tr :class="[expandedRows.includes('-1') ? '' : 'hidden', 'data-child']" data-parent="-1">
                <td class="px-6 py-4 pl-16 text-info">哲学</td>
                <td class="px-6 py-4 text-info">哲学类</td>
                <td class="px-6 py-4 font-medium">逻辑学</td>
                <td class="px-6 py-4 text-info">010102</td>
                <td class="px-6 py-4 text-primary cursor-pointer" @click="handleViewSchools('010102', '逻辑学')">
                  查看
                </td>
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <div class="w-32 h-2 bg-gray-200 rounded-full mr-2">
                      <div class="h-full bg-success rounded-full" style="width: 82%"></div>
                    </div>
                    <span class="text-success font-medium">4.1</span>
                  </div>
                </td>
              </tr>
              <tr @click="handleRowClick('-2')" class="cursor-pointer hover:bg-blue-50" data-row-id="-2">
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                      viewBox="0 0 24 24" data-icon="mdi:chevron-right" class="iconify iconify--mdi"
                      :class="expandedRows.includes('-2') ? 'rotate-90 transition-transform' : ''">
                      <path fill="currentColor" d="M8.59 16.58L13.17 12L8.59 7.41L10 6l6 6l-6 6z"></path>
                    </svg>
                    <span class="ml-2 text-primary">经济学</span>
                  </div>
                </td>
                <td class="px-6 py-4"><span class="text-primary">经济学类</span></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
              </tr>
              <tr :class="[expandedRows.includes('-2') ? '' : 'hidden', 'data-child']" data-parent="-2">
                <td class="px-6 py-4 pl-16 text-info">经济学</td>
                <td class="px-6 py-4 text-info">经济学类</td>
                <td class="px-6 py-4 font-medium">经济学</td>
                <td class="px-6 py-4 text-info">020101</td>
                <td class="px-6 py-4 text-primary cursor-pointer" @click="handleViewSchools('020101', '经济学')">
                  查看
                </td>
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <div class="w-32 h-2 bg-gray-200 rounded-full mr-2">
                      <div class="h-full bg-success rounded-full" style="width: 78%"></div>
                    </div>
                    <span class="text-success font-medium">3.9</span>
                  </div>
                </td>
              </tr>
              <tr :class="[expandedRows.includes('-2') ? '' : 'hidden', 'data-child']" data-parent="-2">
                <td class="px-6 py-4 pl-16 text-info">经济学</td>
                <td class="px-6 py-4 text-info">经济学类</td>
                <td class="px-6 py-4 font-medium">经济统计学</td>
                <td class="px-6 py-4 text-info">020102</td>
                <td class="px-6 py-4 text-primary cursor-pointer" @click="handleViewSchools('020102', '经济统计学')">
                  查看
                </td>
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <div class="w-32 h-2 bg-gray-200 rounded-full mr-2">
                      <div class="h-full bg-success rounded-full" style="width: 82%"></div>
                    </div>
                    <span class="text-success font-medium">4.1</span>
                  </div>
                </td>
              </tr>
              <tr @click="handleRowClick('-3')" class="cursor-pointer hover:bg-blue-50" data-row-id="-3">
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                      viewBox="0 0 24 24" data-icon="mdi:chevron-right" class="iconify iconify--mdi"
                      :class="expandedRows.includes('-3') ? 'rotate-90 transition-transform' : ''">
                      <path fill="currentColor" d="M8.59 16.58L13.17 12L8.59 7.41L10 6l6 6l-6 6z"></path>
                    </svg>
                    <span class="ml-2 text-primary">法学</span>
                  </div>
                </td>
                <td class="px-6 py-4"><span class="text-primary">法学类</span></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
              </tr>
              <tr :class="[expandedRows.includes('-3') ? '' : 'hidden', 'data-child']" data-parent="-3">
                <td class="px-6 py-4 pl-16 text-info">法学</td>
                <td class="px-6 py-4 text-info">法学类</td>
                <td class="px-6 py-4 font-medium">知识产权</td>
                <td class="px-6 py-4 text-info">030102</td>
                <td class="px-6 py-4 text-primary cursor-pointer" @click="handleViewSchools('030102', '知识产权')">
                  查看
                </td>
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <div class="w-32 h-2 bg-gray-200 rounded-full mr-2">
                      <div class="h-full bg-success rounded-full" style="width: 74%"></div>
                    </div>
                    <span class="text-success font-medium">3.7</span>
                  </div>
                </td>
              </tr>
              <tr @click="handleRowClick('-4')" class="cursor-pointer hover:bg-blue-50" data-row-id="-4">
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                      viewBox="0 0 24 24" data-icon="mdi:chevron-right" class="iconify iconify--mdi"
                      :class="expandedRows.includes('-4') ? 'rotate-90 transition-transform' : ''">
                      <path fill="currentColor" d="M8.59 16.58L13.17 12L8.59 7.41L10 6l6 6l-6 6z"></path>
                    </svg>
                    <span class="ml-2 text-primary">教育学</span>
                  </div>
                </td>
                <td class="px-6 py-4"><span class="text-primary">教育学类</span></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
              </tr>
              <tr :class="[expandedRows.includes('-4') ? '' : 'hidden', 'data-child']" data-parent="-4">
                <td class="px-6 py-4 pl-16 text-info">教育学</td>
                <td class="px-6 py-4 text-info">教育学类</td>
                <td class="px-6 py-4 font-medium">教育学</td>
                <td class="px-6 py-4 text-info">040101</td>
                <td class="px-6 py-4 text-primary cursor-pointer" @click="handleViewSchools('040101', '教育学')">
                  查看
                </td>
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <div class="w-32 h-2 bg-gray-200 rounded-full mr-2">
                      <div class="h-full bg-success rounded-full" style="width: 80%"></div>
                    </div>
                    <span class="text-success font-medium">4</span>
                  </div>
                </td>
              </tr>
              <tr @click="handleRowClick('-5')" class="cursor-pointer hover:bg-blue-50" data-row-id="-5">
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                      viewBox="0 0 24 24" data-icon="mdi:chevron-right" class="iconify iconify--mdi"
                      :class="expandedRows.includes('-5') ? 'rotate-90 transition-transform' : ''">
                      <path fill="currentColor" d="M8.59 16.58L13.17 12L8.59 7.41L10 6l6 6l-6 6z"></path>
                    </svg>
                    <span class="ml-2 text-primary">文学</span>
                  </div>
                </td>
                <td class="px-6 py-4"><span class="text-primary">中国语言文学类</span></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
                <td class="px-6 py-4"></td>
              </tr>
              <tr :class="[expandedRows.includes('-5') ? '' : 'hidden', 'data-child']" data-parent="-5">
                <td class="px-6 py-4 pl-16 text-info">文学</td>
                <td class="px-6 py-4 text-info">中国语言文学类</td>
                <td class="px-6 py-4 font-medium">汉语言文学</td>
                <td class="px-6 py-4 text-info">050101</td>
                <td class="px-6 py-4 text-primary cursor-pointer" @click="handleViewSchools('050101', '汉语言文学')">
                  查看
                </td>
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <div class="w-32 h-2 bg-gray-200 rounded-full mr-2">
                      <div class="h-full bg-success rounded-full" style="width: 72%"></div>
                    </div>
                    <span class="text-success font-medium">3.6</span>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </main>
    <sideTop />
  </div>
</template>

<style lang="scss" scoped>
.major-analysis-page {
  max-width: 80vw;
  min-width: 1200px;
  min-height: calc(100vh - 428px);
  margin: 0 auto;
  background-color: #fff;
  box-shadow:
    0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  border-top: 1px solid #e5e7eb;
}
</style>
