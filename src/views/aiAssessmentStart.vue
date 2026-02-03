<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import * as api from '@/api/interfaceapi'
import { ElMessage, ElMessageBox } from 'element-plus'

onMounted(() => {
  getScaleStartApi()
})
const route = useRoute()

const scaleId = ref(route.query.scaleId)
const name = ref(route.query.name)
const activeIndex = ref(0)
const scaleDetailsQuery: any = ref({})
const getScaleStartApi = async () => {
  const res = await api.scaleStartApi({ scaleId: scaleId.value })
  if (res) {
    scaleDetailsQuery.value = res.data || {}
    if (scaleDetailsQuery.value.questionsJson.length > 0) {
      scaleDetailsQuery.value.questionsJson.forEach((item: any) => {
        item.answerNum = null
      })
    }
  }
}

// 选中题目，自动下一题
const handleChange = () => {
  if (activeIndex.value === scaleDetailsQuery.value.questionsJson.length - 1) {
    return
  }
  setTimeout(() => {
    activeIndex.value++
  }, 500)
}

// 提交评估-校验
const submitCheck = () => {
  const index = scaleDetailsQuery.value.questionsJson.findIndex((item: any) => item.answerNum === null)
  if (index !== -1) {
    ElMessage.error(`请回答第 ${index + 1} 题`)
    return
  }
  const answerJson = scaleDetailsQuery.value.questionsJson.map((item: any) => ({
    questionId: item.questionId,
    answerNum: item.answerNum
  }))
  const params = {
    asId: scaleDetailsQuery.value.asId,
    answerJson: JSON.stringify(answerJson)
  }
  ElMessageBox.confirm(
    '是否确认提交？',
    '温馨提示',
    {
      confirmButtonText: '提交',
      cancelButtonText: '取消',
      type: 'warning',
    }
  )
    .then(() => {
      getscaleSaveApi(params)
    })
    .catch(() => {
    })
}

// 提交评估
const router = useRouter()
const getscaleSaveApi = async (params: any) => {
  const res = await api.scaleSaveApi(params)
  if (res) {
    ElMessage({
      type: 'success',
      message: '提交成功',
    })
    setTimeout(() => {
      router.push({
        path: '/aiAssessmentView',
        query: {
          asId: scaleDetailsQuery.value.asId
        }
      })
    }, 1000)
  }
}
</script>

<template>
  <div class="ai-assessment-start">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section>
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <div class="card-title">
            {{ name }}
            <span v-if="scaleDetailsQuery?.questionsJson?.length > 0" class="card-num">
              ( {{ activeIndex + 1 }} / {{ scaleDetailsQuery.questionsJson.length }}题)
            </span>
          </div>
          <div class="mb-6">
            <div v-for="(item, index) in scaleDetailsQuery.questionsJson" :key="item.questionId">
              <div v-if="index === activeIndex" class="question-item">
                <div class="question-title">
                  {{ item.questionNum }}. {{ item.question }}
                </div>
                <div class="question-answers">
                  <div v-for="(answer, answerIndex) in item.answers" :key="answerIndex" class="answer-item">
                    <el-radio-group v-model="item.answerNum" @change="handleChange">
                      <el-radio :value="answer.answerNum" size="large">{{ answer.answer }}</el-radio>
                    </el-radio-group>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-if="scaleDetailsQuery?.questionsJson?.length > 0" class="flex justify-center">
            <el-button type="primary" :disabled="activeIndex === 0" @click="activeIndex--">上一题</el-button>
            <el-button type="success" v-if="activeIndex === scaleDetailsQuery.questionsJson.length - 1"
              @click="submitCheck">提交答案</el-button>
            <el-button v-else type="primary" @click="activeIndex++">下一题</el-button>
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

.card-title {
  margin-bottom: 20px;
  font-size: 30px;
  line-height: 42px;
  font-weight: 400;
  // color: #2563EB;
}

.card-num {
  margin-left: 10px;
  font-size: 24px;
  line-height: 36px;
  font-weight: 400;
  // color: #2563EB;
}

.question-title {
  margin-bottom: 20px;
  font-size: 24px;
  line-height: 36px;
  font-weight: 400;
}

.question-answers {
  margin-bottom: 20px;
}

.answer-item {
  margin-bottom: 10px;
}
</style>