<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import * as api from '@/api/interfaceapi'

onMounted(async () => {
  getScalesDetailQueryApi()
})

const route = useRoute()
const router = useRouter()
const scaleId = ref(route.query.scaleId)
const scaleDetailsQuery: any = ref({})
const getScalesDetailQueryApi = async () => {
  const res = await api.scaleDetailsQueryApi({ scaleId: scaleId.value })
  if (res) {
    scaleDetailsQuery.value = res.data.Rs || {}
  }
}

const goAiAssessmentStart = () => {
  router.push({ name: 'aiAssessmentStart', query: { scaleId: scaleDetailsQuery.value.scaleId, name: scaleDetailsQuery.value.name } })
}
</script>

<template>
  <div class="ai-assessment-detail">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section>
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <div class="xz-cp-card">
            <div class="card-title">
              <h2>{{ scaleDetailsQuery.name }}</h2>
            </div>
            <div class="card-content clearfix">
              <div class="card-content-left">
                <img :src="scaleDetailsQuery.picUrl" />
              </div>
              <div class="card-content-right">
                <div class="des">
                  {{ scaleDetailsQuery.title }}
                </div>
                <div class="tip">{{ scaleDetailsQuery.description }}</div>
                <div class="other">
                  <el-tag type="success">
                    {{ scaleDetailsQuery.completeCount == 0 ? '未测试' : '已测试' + scaleDetailsQuery.completeCount + '次' }}
                  </el-tag>
                  <el-button plain type="primary" @click="goAiAssessmentStart">开始测评
                    <el-icon class="el-icon--right">
                      <Right />
                    </el-icon>
                  </el-button>
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
.ai-assessment-detail {
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

.xz-cp-card {
  padding: 20px;
  background: #fff;
  border-radius: 10px;
}

.xz-cp-card .card-title {
  margin-bottom: 20px;
}

.xz-cp-card .card-title h2 {
  font-size: 30px;
  line-height: 42px;
  font-weight: 400;
  // color: #2563EB;
}

.xz-cp-card .card-sub {
  display: -ms-flexbox;
  display: flex;
  align-items: center;
  margin-bottom: 8px;
}

.xz-cp-card .card-sub .ycrs {
  font-size: 14px;
  font-weight: 400;
  color: #8d949f;
  line-height: 22px;
  margin-left: 16px;
}

.xz-cp-card .card-sub .other-des {
  -ms-flex: 1;
  flex: 1;
  font-size: 14px;
  line-height: 42px;
  font-weight: 400;
  text-align: right;
}

.clearfix {
  display: flex;
}

.xz-cp-card .card-content .card-content-left {
  width: 488px;
  height: 312px;
  float: left;
  margin-right: 20px;
}

.xz-cp-card .card-content .card-content-left img {
  height: 100%;
  width: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.xz-cp-card .card-content .card-content-right {
  width: 572px;
  min-height: 312px;
  padding-bottom: 60px;
  float: right;
  position: relative;
}

.xz-cp-card .card-content .card-content-right .des {
  line-height: 26px;
  margin-bottom: 24px;
  font-size: 24px;
}

.xz-cp-card .card-content .card-content-right .tip {
  color: #909399;
  line-height: 22px;
}

.xz-cp-card .card-content .card-content-right .other {
  position: absolute;
  width: 100%;
  bottom: 0;
  display: -ms-flexbox;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>
