<script setup lang="ts">
import { ref, onMounted } from 'vue'
import * as api from '@/api/interfaceapi'
import sideTop from '@/components/sideTop.vue'

import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(async () => {
  getScalesListQueryApi()
})

const scalesList: any = ref([])
const getScalesListQueryApi = async () => {
  const res = await api.scalesListQueryApi()
  console.log('res -------->', res)
  if (res) {
    scalesList.value = res.data.Rs || []
  }
}

const goAiAssessmentDetail = (scaleId: string) => {
  router.push({ name: 'aiAssessmentDetail', query: { scaleId } })
}
</script>

<template>
  <div class="ai-assessment-page">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section class="mb-6">
        <h2 class="text-2xl font-bold text-center mb-2">AI智能测评</h2>
        <h4 class="text-1xl text-center mb-6" style="color: #646566">科学测评，精准规划未来</h4>
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <!-- <div class="tagBox">
            <div class="tagContent">
            </div>
          </div> -->
          <div class="zygh-zycp-list">
            <div v-for="(item,index) in scalesList" :key="index" class="list-item">
              <div class="img-box">
                <img :src="item.picUrl" alt="" />
              </div>
              <div class="list-right">
                <div class="right-title">{{ item.name }}</div>
                <div class="right-desc">
                  {{item.title}}
                </div>
                <!-- <div class="right-btn" @click="goAiAssessmentDetail(item.scaleId)">开始测评</div> -->
                 <el-button plain type="primary" class="right-btn" @click="goAiAssessmentDetail(item.scaleId)">查看详情
                  <el-icon class="el-icon--right">
                    <Right />
                  </el-icon>
                </el-button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
    <sideTop />
  </div>
</template>

<style lang="scss" scoped>
.ai-assessment-page {
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
    background-color: #2563eb;
    border: 1px solid #2563eb;
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

<style>
.zygh-zycp-list {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  padding-bottom: 38px;
}

.zygh-zycp-list .list-item {
  width: 100%;
  padding: 20px;
  display: flex;
  background-color: #fff;
  margin-bottom: 20px;
  border-radius: 10px;
}

.zygh-zycp-list .img-box {
  overflow: hidden;
  border-radius: 4px;
  margin-right: 16px;
}

.zygh-zycp-list .list-item img {
  display: block;
  width: 244px;
  height: 156px;
  -o-object-fit: cover;
  object-fit: cover;
  transition: transform 0.5s;
  border-radius: 10px;
}

.zygh-zycp-list .list-item .list-right {
  flex: 1;
  position: relative;
}

.zygh-zycp-list .list-item .right-title {
  font-size: 18px;
  line-height: 26px;
  color: #2b3330;
  font-weight: 700;
}

.zygh-zycp-list .list-item .right-desc {
  font-size: 14px;
  line-height: 24px;
  color: #67716c;
  margin: 8px 0 18px;
  display: -webkit-box;
  overflow: hidden;
  text-overflow: ellipsis;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
}

.zygh-zycp-list .list-item .right-btn {
  position: absolute;
  right: 0;
  bottom: 0;
}
</style>
