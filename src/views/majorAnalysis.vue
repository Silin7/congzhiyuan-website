<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import sideTop from '@/components/sideTop.vue'
import * as api from '@/api/interfaceapi'

onMounted(() => {
  getZyCcQueryApi()
})

// 获取专业分类数据
const selectedEducationType: any = ref('')
const educationTypeList: any = ref([])
const getZyCcQueryApi = async () => {
  const res: any = await api.ZyCcQueryApi({})
  if (res) {
    educationTypeList.value = res.data || []
    selectedEducationType.value = educationTypeList.value[0]?.ccdm || ''
    getZyListQueryApi()
  }
}

const handleEducationTypeClick = (type: string) => {
  selectedEducationType.value = type
  getZyListQueryApi()
}

// 获取专业列表数据
const majorTypeList: any = ref([])
const getZyListQueryApi = async () => {
  const res: any = await api.ZyListQueryApi({
    ccdm: selectedEducationType.value,
  })
  if (res) {
    majorTypeList.value = res.data.Rs || []
  }
}

const defaultProps = {
  children: 'children',
  label: 'label',
}


const handleNodeClick = (data: any) => {
  if (!data.children) {
    console.log('-------->', '最后一层', data.id)
    window.open(`/#/majorDetail?zydm=${data.id}`)
  }
}

</script>

<template>
  <div class="major-analysis-page">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section class="mb-6">
        <h2 class="text-2xl font-bold text-center mb-2">大学专业信息库</h2>
        <h4 class="text-1xl text-center mb-6" style="color: #646566;">全面解析专业门类、培养方向与就业前景</h4>
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <div class="tagBox">
            <!-- <div class="tagTitle">院校层次：</div> -->
            <div class="tagContent">
              <div v-for="(item, index) in educationTypeList" :key="index">
                <div :class="selectedEducationType === item.ccdm ? 'primaryTag' : 'infoTag'"
                  @click="handleEducationTypeClick(item.ccdm)">
                  {{ item.ccmc }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section>
        <div class="rounded-2xl shadow-lg p-6 border border-gray-200">
          <el-tree indent="100" :data="majorTypeList" :props="defaultProps" @node-click="handleNodeClick" />
        </div>
      </section>
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

.tagBox {
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
    margin-right: 8px;
    font-size: 14px;
    line-height: 30px;
    padding: 0 20px;
    color: #fff;
    background-color: #2563EB;
    border: 1px solid #2563EB;
    border-radius: 4px;
  }

  .infoTag {
    cursor: pointer;
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
</style>