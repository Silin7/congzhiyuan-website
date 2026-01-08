<script setup lang="ts">
import { ref } from 'vue'
import sideTop from '@/components/sideTop.vue'
import { ElTable, ElTableColumn, ElPagination } from 'element-plus'

// 声明响应式变量
// 院校省份 - 可选值：'all' 或省份代码
const selectedProvince = ref('all')
// 办学层次 - 可选值：'all', 'bachelor', 'college'
const selectedLevel = ref('all')
// 院校名称
const schoolName = ref('')

// 声明表格数据响应式变量
const tableData = ref([
  {
    id: 1,
    schoolName: '北京大学',
    province: '北京',
    city: '北京市',
    level: '本科',
    nature: '公办',
    features: ['双一流', '国家级优势'],
    insuranceRate: '56%',
    hasLink: true
  },
  {
    id: 2,
    schoolName: '清华大学',
    province: '北京',
    city: '北京市',
    level: '本科',
    nature: '公办',
    features: ['双一流', '重点学科'],
    insuranceRate: '58%',
    hasLink: false
  },
  {
    id: 3,
    schoolName: '复旦大学',
    province: '上海',
    city: '上海市',
    level: '本科',
    nature: '公办',
    features: ['双一流', '特色专业'],
    insuranceRate: '54%',
    hasLink: false
  }
])

// 声明分页相关变量
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(tableData.value.length)

// 省份按钮点击事件处理函数
const handleProvinceClick = (province: string) => {
  selectedProvince.value = province
  console.log(`选择了省份: ${province}`)
}

// 办学层次点击事件处理函数
const handleLevelClick = (level: string) => {
  selectedLevel.value = level
  console.log(`选择了办学层次: ${level}`)
}

// 查询按钮点击事件处理函数
const handleSearch = () => {
  // 收集查询条件
  const searchParams = {
    province: selectedProvince.value,
    level: selectedLevel.value,
    schoolName: schoolName.value,
  }
  console.log('查询条件:', searchParams)
  // 这里可以添加实际的查询逻辑，比如调用API
}

// 处理分页变化
const handlePageChange = (page: number) => {
  currentPage.value = page
  console.log(`当前页码: ${page}`)
}

// 处理每页条数变化
const handleSizeChange = (size: number) => {
  pageSize.value = size
  currentPage.value = 1
  console.log(`每页条数: ${size}`)
}
</script>

<template>
  <div class="school-search-page">
    <main class="flex-grow container mx-auto px-6 py-8">
      <div class="bg-white rounded-lg shadow-sm p-8 mb-8">
        <h2 class="text-2xl font-bold text-gray-800 mb-6">院校查询</h2>
        <!-- 查询表单 -->
        <div class="bg-gray-50 rounded-lg p-6 mb-8">
          <div class="grid grid-cols-1 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">院校省份</label>
              <div class="grid grid-cols-4 md:grid-cols-8 gap-2">
                <button @click="handleProvinceClick('all')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'all'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="all" type="button">
                  全部
                </button>
                <button @click="handleProvinceClick('beijing')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'beijing'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="beijing" type="button">
                  北京
                </button>
                <button @click="handleProvinceClick('tianjin')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'tianjin'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="tianjin" type="button">
                  天津
                </button>
                <button @click="handleProvinceClick('hebei')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'hebei'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="hebei" type="button">
                  河北
                </button>
                <button @click="handleProvinceClick('shanxi')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'shanxi'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="shanxi" type="button">
                  山西
                </button>
                <button @click="handleProvinceClick('neimenggu')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'neimenggu'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="neimenggu" type="button">
                  内蒙古
                </button>
                <button @click="handleProvinceClick('liaoning')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'liaoning'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="liaoning" type="button">
                  辽宁
                </button>
                <button @click="handleProvinceClick('jilin')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'jilin'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="jilin" type="button">
                  吉林
                </button>
                <button @click="handleProvinceClick('heilongjiang')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'heilongjiang'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="heilongjiang" type="button">
                  黑龙江
                </button>
                <button @click="handleProvinceClick('shanghai')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'shanghai'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="shanghai" type="button">
                  上海
                </button>
                <button @click="handleProvinceClick('jiangsu')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'jiangsu'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="jiangsu" type="button">
                  江苏
                </button>
                <button @click="handleProvinceClick('zhejiang')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'zhejiang'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="zhejiang" type="button">
                  浙江
                </button>
                <button @click="handleProvinceClick('anhui')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'anhui'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="anhui" type="button">
                  安徽
                </button>
                <button @click="handleProvinceClick('fujian')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'fujian'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="fujian" type="button">
                  福建
                </button>
                <button @click="handleProvinceClick('jiangxi')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'jiangxi'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="jiangxi" type="button">
                  江西
                </button>
                <button @click="handleProvinceClick('shandong')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'shandong'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="shandong" type="button">
                  山东
                </button>
                <button @click="handleProvinceClick('henan')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'henan'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="henan" type="button">
                  河南
                </button>
                <button @click="handleProvinceClick('hubei')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'hubei'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="hubei" type="button">
                  湖北
                </button>
                <button @click="handleProvinceClick('hunan')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'hunan'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="hunan" type="button">
                  湖南
                </button>
                <button @click="handleProvinceClick('guangdong')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'guangdong'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="guangdong" type="button">
                  广东
                </button>
                <button @click="handleProvinceClick('guangxi')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'guangxi'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="guangxi" type="button">
                  广西
                </button>
                <button @click="handleProvinceClick('hainan')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'hainan'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="hainan" type="button">
                  海南
                </button>
                <button @click="handleProvinceClick('chongqing')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'chongqing'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="chongqing" type="button">
                  重庆
                </button>
                <button @click="handleProvinceClick('sichuan')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'sichuan'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="sichuan" type="button">
                  四川
                </button>
                <button @click="handleProvinceClick('guizhou')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'guizhou'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="guizhou" type="button">
                  贵州
                </button>
                <button @click="handleProvinceClick('yunnan')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'yunnan'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="yunnan" type="button">
                  云南
                </button>
                <button @click="handleProvinceClick('xizang')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'xizang'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="xizang" type="button">
                  西藏
                </button>
                <button @click="handleProvinceClick('shaanxi')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'shaanxi'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="shaanxi" type="button">
                  陕西
                </button>
                <button @click="handleProvinceClick('gansu')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'gansu'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="gansu" type="button">
                  甘肃
                </button>
                <button @click="handleProvinceClick('qinghai')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'qinghai'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="qinghai" type="button">
                  青海
                </button>
                <button @click="handleProvinceClick('ningxia')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'ningxia'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="ningxia" type="button">
                  宁夏
                </button>
                <button @click="handleProvinceClick('xinjiang')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'xinjiang'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="xinjiang" type="button">
                  新疆
                </button>
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">办学层次</label>
              <div class="flex gap-4">
                <button @click="handleLevelClick('all')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedLevel === 'all'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-level="all">不限</button>
                <button @click="handleLevelClick('bachelor')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedLevel === 'bachelor'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-level="bachelor">本科</button>
                <button @click="handleLevelClick('college')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedLevel === 'college'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-level="college">专科</button>
              </div>
            </div>
            <div class="flex items-end gap-4">
              <div class="w-1/2">
                <label class="block text-sm font-medium text-gray-700 mb-2">院校名称</label>
                <input v-model="schoolName"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                  placeholder="请输入院校名称" type="text" />
              </div>
            </div>
            <div>
              <button @click="handleSearch"
                class="w-full bg-blue-700 hover:bg-blue-800 text-white py-2 px-4 rounded-md font-medium">
                查询
              </button>
            </div>
          </div>
        </div>
        <!-- 查询结果表格 -->
        <div class="overflow-x-auto">
          <el-table v-loading="false" :data="tableData" style="width: 100%" stripe border size="small"
            class="custom-table">
            <!-- 院校名称列 -->
            <el-table-column prop="schoolName" label="院校名称" min-width="180" align="left">
              <template #default="scope">
                <div class="text-sm font-medium text-gray-900">
                  <a v-if="scope.row.hasLink" href="院校简介.html" class="text-blue-600 hover:underline">
                    {{ scope.row.schoolName }}
                  </a>
                  <span v-else>{{ scope.row.schoolName }}</span>
                </div>
              </template>
            </el-table-column>

            <!-- 所在省份列 -->
            <el-table-column prop="province" label="所在省份" min-width="120" align="left"></el-table-column>

            <!-- 城市列 -->
            <el-table-column prop="city" label="城市" min-width="120" align="left"></el-table-column>

            <!-- 办学层次列 -->
            <el-table-column prop="level" label="办学层次" min-width="100" align="center">
              <template #default="scope">
                <span
                  class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">{{
                    scope.row.level }}</span>
              </template>
            </el-table-column>

            <!-- 院校性质列 -->
            <el-table-column prop="nature" label="院校性质" min-width="100" align="center"></el-table-column>

            <!-- 特色专业列 -->
            <el-table-column prop="features" label="特色专业" min-width="200" align="left">
              <template #default="scope">
                <span v-for="(feature, index) in scope.row.features" :key="index"
                  class="mr-2 px-2 py-1 text-xs rounded-full" :class="{
                    'bg-blue-100 text-blue-800': feature === '双一流',
                    'bg-purple-100 text-purple-800': feature === '国家级优势',
                    'bg-yellow-100 text-yellow-800': feature === '重点学科',
                    'bg-red-100 text-red-800': feature === '特色专业'
                  }">
                  {{ feature }}
                </span>
              </template>
            </el-table-column>

            <!-- 保研率列 -->
            <el-table-column prop="insuranceRate" label="保研率" min-width="80" sortable align="center"></el-table-column>
          </el-table>
        </div>
        <!-- 分页控件 -->
        <div class="flex items-center justify-between border-t border-gray-200 pt-6">
          <div class="text-sm text-gray-700">
            共 <span class="font-medium">{{ total }}</span> 条结果 | 第
            <span class="font-medium">{{ currentPage }}</span> 页，共 <span class="font-medium">{{ Math.ceil(total /
              pageSize)
              }}</span> 页
          </div>
          <el-pagination v-model:current-page="currentPage" v-model:page-size="pageSize" :page-sizes="[10, 20, 50, 100]"
            :total="total" layout="sizes, prev, pager, next, jumper" :prev-text="'上一页'" :next-text="'下一页'"
            @size-change="handleSizeChange" @current-change="handlePageChange"></el-pagination>
        </div>
      </div>
    </main>
    <sideTop />
  </div>
</template>

<style lang="scss" scoped>
.school-search-page {
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
