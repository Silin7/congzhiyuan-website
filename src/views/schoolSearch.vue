<script setup lang="ts">
import { onMounted, ref } from 'vue'
// import { useRouter } from 'vue-router'
import { ElTable, ElTableColumn, ElPagination } from 'element-plus'
import * as api from '@/api/interfaceapi'
import sideTop from '@/components/sideTop.vue'

onMounted(() => {
  getProvinceList()
})

// 院校省份
const provinceList = ref<any>([])
const getProvinceList = async () => {
  const res: any = await api.genListQueryApi({
    genType: 'prov',
  })
  if (res) {
    provinceList.value = res.data.Rs || []
  }
}
const selectedProvince: any = ref([])
const handleProvinceClick = (province: string) => {
  if (province === '') {
    selectedProvince.value = ['']
    return
  } else {
    const index = selectedProvince.value.indexOf('')
    if (index > -1) {
      selectedProvince.value.splice(index, 1)
    }
  }
  // 切换省份选中状态
  const index = selectedProvince.value.indexOf(province)
  if (index > -1) {
    selectedProvince.value.splice(index, 1)
  } else {
    selectedProvince.value.push(province)
  }
}

// 院校层次
const selectedSchoolLevel = ref('')
const handleSchoolLevelClick = (level: string) => {
  selectedSchoolLevel.value = level
}

// 院校名称
const schoolName = ref('')

// 声明 表格数据 分页 相关变量
const tableData = ref([])
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(tableData.value.length)


// 查询按钮点击事件处理函数
const handleSearch = async () => {
  const Rs: any = ref([])
  await selectedProvince.value.forEach((item: any) => {
    Rs.value.push({ "id": item, "genType": "prov" })
  })
  // 这里可以添加实际的查询逻辑，比如调用API
  const res: any = await api.YxListQueryApi({
    genList: JSON.stringify({
      Rs: Rs.value
    }),
    ccdm: selectedSchoolLevel.value,
    yxmc: schoolName.value,
    startrow: currentPage.value,
    pagesize: pageSize.value,
  })
  if (res) {
    tableData.value = res.data.Rs || []
    total.value = res.recordsTotal || 0
  }
}

// 处理分页变化
const handlePageChange = (page: number) => {
  currentPage.value = page
  handleSearch()
}

// 处理每页条数变化
const handleSizeChange = (size: number) => {
  pageSize.value = size
  currentPage.value = 1
  handleSearch()
}

// 处理院校详情点击事件
// const router = useRouter()

const handleSchoolDetailClick = (school: any) => {
  // // 跳转到院校详情页面
  // router.push({
  //   path: '/schoolDetail',
  //   query: {
  //     yxid: school.yxid,
  //   }
  // })
  window.open(`/#/schoolDetail?yxid=${school.yxid}`)
}
</script>

<template>
  <div class="school-search-page">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section class="mb-10">
        <h2 class="text-2xl font-bold text-center mb-6">院校查询</h2>
        <!-- 查询表单 -->
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <div class="tagBox">
            <div class="tagTitle">院校省份：</div>
            <div class="tagContent">
              <div :class="selectedProvince.includes('') ? 'primaryTag' : 'infoTag'" @click="handleProvinceClick('')">
                全选
              </div>
              <div v-for="(item, index) in provinceList" :key="index"
                :class="selectedProvince.includes(item.id) ? 'primaryTag' : 'infoTag'"
                @click="handleProvinceClick(item.id)">
                {{ item.province }}
              </div>
            </div>
          </div>
          <!-- <el-row :gutter="20">
            <el-col :span="6"></el-col>
            <el-col :span="6"></el-col>
          </el-row> -->
          <div class="tagBox">
            <div class="tagTitle">院校层次：</div>
            <div class="tagContent">
              <div :class="selectedSchoolLevel === '' ? 'primaryTag' : 'infoTag'" @click="handleSchoolLevelClick('')">
                不限
              </div>
              <div :class="selectedSchoolLevel === '1' ? 'primaryTag' : 'infoTag'" @click="handleSchoolLevelClick('1')">
                本科
              </div>
              <div :class="selectedSchoolLevel === '2' ? 'primaryTag' : 'infoTag'" @click="handleSchoolLevelClick('2')">
                专科
              </div>
            </div>
          </div>
          <div class="tagBox">
            <div class="tagTitle">院校名称：</div>
            <el-input v-model="schoolName" placeholder="输入院校名称" class="input-tall38px"
              style="margin-bottom: 10px; width: calc(50% - 90px)"></el-input>
          </div>
          <!-- 立即开始智能检索 -->
          <div class="mt-8 flex justify-center">
            <button
              class="w-full md:w-64 py-4 px-8 bg-blue-600 text-white rounded-2xl font-bold text-lg shadow-lg shadow-blue-200 hover:bg-blue-700 active:scale-95 transition-all flex items-center justify-center space-x-3"
              @click="handleSearch">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="solar:minimalistic-magnifer-zoom-in-bold"
                class="iconify text-2xl iconify--solar">
                <defs>
                  <mask id="IconifyId19b962244b31ed2cc0">
                    <g fill="none">
                      <path fill="#fff" d="M20.313 11.157a9.157 9.157 0 1 1-18.313 0a9.157 9.157 0 0 1 18.313 0"></path>
                      <path fill="#000" fill-rule="evenodd"
                        d="M11.157 8.024c.399 0 .723.324.723.723v1.687h1.686a.723.723 0 0 1 0 1.446H11.88v1.686a.723.723 0 1 1-1.445 0V11.88H8.747a.723.723 0 1 1 0-1.445h1.687V8.747c0-.4.323-.723.723-.723"
                        clip-rule="evenodd"></path>
                      <path fill="#fff" fill-rule="evenodd"
                        d="M18.838 18.838a.723.723 0 0 1 1.023 0l1.927 1.928a.723.723 0 0 1-1.022 1.022l-1.928-1.927a.723.723 0 0 1 0-1.023"
                        clip-rule="evenodd"></path>
                    </g>
                  </mask>
                </defs>
                <path fill="currentColor" d="M0 0h24v24H0z" mask="url(#IconifyId19b962244b31ed2cc0)"></path>
              </svg>
              <span>查询</span>
            </button>
          </div>
        </div>
      </section>
      <section>
        <!-- 查询结果表格 -->
        <div class="overflow-x-auto">
          <el-table v-loading="false" :data="tableData" stripe border size="small" class="custom-table"
            style="width: 100%" @row-click="handleSchoolDetailClick">
            <!-- <el-table-column label="院校名称" min-width="180" align="left">
              <template #default="scope">
                <div class="tableyxmc" @click="handleSchoolDetailClick(scope.row)">{{ scope.row.yxmc }}</div>
              </template>
            </el-table-column> -->
            <el-table-column prop="yxmc" label="院校名称" min-width="180" align="left"></el-table-column>
            <el-table-column prop="provcity" label="所在省份" min-width="120" align="left"></el-table-column>
            <el-table-column prop="ccmc" label="办学层次" min-width="100" align="left"></el-table-column>
            <el-table-column prop="yxxz" label="院校性质" min-width="100" align="left"></el-table-column>
          </el-table>
        </div>
        <!-- 分页控件 -->
        <div class="flex items-center justify-between border-t border-gray-200 pt-6">
          <div class="text-sm text-gray-700">
            共 <span class="font-medium">{{ total }}</span> 条结果 | 第
            <span class="font-medium">{{ currentPage }}</span> 页，共
            <span class="font-medium">{{ Math.ceil(total / pageSize) }}</span> 页
          </div>
          <el-pagination v-model:current-page="currentPage" v-model:page-size="pageSize" :page-sizes="[10, 20, 50, 100]"
            :total="total" layout="sizes, prev, pager, next, jumper" :prev-text="'上一页'" :next-text="'下一页'"
            @size-change="handleSizeChange" @current-change="handlePageChange"></el-pagination>
        </div>
      </section>
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


  .tagBox {
    margin-bottom: 10px;
    display: flex;
    align-items: center;
  }

  .tagTitle {
    margin-bottom: 10px;
    margin-right: 20px;
    font-size: 14px;
    color: #646566;
  }

  .tagContent {
    width: calc(100% - 100px);
    display: flex;
    align-items: center;
    flex-wrap: wrap;

    .primaryTag {
      cursor: pointer;
      margin-bottom: 10px;
      margin-right: 8px;
      font-size: 14px;
      line-height: 30px;
      padding: 0 20px;
      color: #fff;
      background-color: #2563eb;
      border: 1px solid #2563eb;
      border-radius: 4px;
    }

    .infoTag {
      cursor: pointer;
      margin-bottom: 10px;
      margin-right: 8px;
      font-size: 14px;
      line-height: 30px;
      color: rgb(55 65 81);
      padding: 0 20px;
      background-color: #fff;
      border: 1px solid rgb(209 213 219 / var(--tw-border-opacity));
      border-radius: 4px;
    }
  }

  .zksqBox {
    cursor: pointer;
    margin: 20px auto;
    width: 100px;
    display: flex;
    align-items: center;
    justify-content: center;

    span {
      margin-right: 6px;
      color: #2563eb;
    }
  }

  .chGroupBox {
    cursor: pointer;
    position: relative;
    margin-bottom: 20px;
    background-color: #2563eb10;
    padding: 10px;
    border-radius: 10px;

    .chGroupName {
      display: flex;
      flex-wrap: wrap;
      font-size: 16px;
      line-height: 20px;
      font-weight: 600;
      color: #333;
      margin-bottom: 6px;

      span {
        display: inline-block;
        margin-right: 10px;
        margin-bottom: 10px;
      }
    }

    .chGroupSub {
      display: flex;
      flex-wrap: wrap;
      font-size: 12px;
      line-height: 20px;
      color: #646566;

      p {
        margin-right: 10px;
        margin-bottom: 6px;
        line-height: 20px;
      }

      span {
        font-size: 14px;
        line-height: 20px;
        color: #2563eb;
      }
    }

    .chGroupIcon {
      position: absolute;
      top: 50%;
      right: 10px;
      transform: translateY(-50%);
    }

    .deleteIcon {
      cursor: pointer;
      position: absolute;
      top: 10px;
      right: 10px;
    }

    .deleteIcon2 {
      cursor: pointer;
      position: absolute;
      top: 0;
      right: 0;
    }
  }
}

.tableyxmc:hover {
  cursor: pointer;
  color: #2563eb;
}
</style>
