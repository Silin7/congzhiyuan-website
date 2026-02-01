<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import * as api from '@/api/interfaceapi'
import dayjs from 'dayjs'

onMounted(() => {
  getScaleStartApi()
})
const route = useRoute()

const asId = ref(route.query.asId)
const scaleDetailsQuery: any = ref({})
const getScaleStartApi = async () => {
  const res = await api.assDetailQueryApi({ asId: asId.value })
  if (res) {
    scaleDetailsQuery.value = res.data.Rs || {}
  }
}
</script>

<template>
  <div class="ai-assessment-start">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section>
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <h2 class="cp-result-title">{{ scaleDetailsQuery.scaleName || '' }}</h2>
          <div class="cp-result-time">
            报告时间：{{ scaleDetailsQuery.completeTime ? dayjs(scaleDetailsQuery.completeTime).format('YYYY-MM-DD HH:mm:ss') : '暂无时间' }}
          </div>
          <h3 class="result-part-title">测评结果</h3>
          <div class="result-top-des">
            <p>
              {{ scaleDetailsQuery.report || '暂无测评结果' }}
            </p>
          </div>
          <h3 class="result-part-title">综合建议</h3>
          <div class="result-top-des">
            <p>
              {{ scaleDetailsQuery.recommendations || '暂无建议' }}
            </p>
          </div>
          <h3 class="result-part-title">重要提示</h3>
          <div class="result-top-des">
            <p>
              测评结果及解读内容仅供参考。
            </p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<style lang="scss" scoped>
.ai-assessment-start {
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

.cp-result-title {
  margin-bottom: 8px;
  text-align: center;
  font-size: 30px;
  font-weight: 400;
  color: #13161b;
  line-height: 42px;
}

.cp-result-time {
  line-height: 20px;
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  color: #8d949f;
  margin-bottom: 48px;
}

.result-part-title::before {
  content: "";
  display: inline-block;
  width: 5px;
  height: 16px;
  background: #294ed6;
  vertical-align: middle;
  margin-right: 6px;
  transform: rotate(4deg);
  margin-bottom: 2px;
}

.result-part-title {
  font-size: 22px;
  font-weight: 700;
  color: #13161b;
  line-height: 30px;
  margin-bottom: 24px;
}

.result-top-des {
  margin-bottom: 64px;
  font-size: 16px;
  font-weight: 400;
  color: #525252;
  line-height: 30px;
}
</style>