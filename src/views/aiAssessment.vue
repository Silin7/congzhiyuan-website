<script setup lang="ts">
import { ref } from 'vue'
import sideTop from '@/components/sideTop.vue'

</script>

<template>
  <div class="ai-assessment-page">
    <main class="container mx-auto px-6 py-10 max-w-7xl">
      <!-- 页面标题 -->
      <div class="text-center mb-12 animate-fadeIn">
        <h1 class="text-3xl md:text-4xl font-bold text-[#333] mb-4">AI智能测评</h1>
        <p class="text-lg text-[#666] max-w-2xl mx-auto">科学测评，精准规划未来</p>
      </div>
      <!-- 双模块布局 -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <!-- 学业能力测评模块 -->
        <div class="bg-white rounded-lg shadow-sm p-6 border border-[#E8E8E8] transition-all hover:shadow-md">
          <div class="flex items-center mb-6">
            <div class="bg-primary-blue bg-opacity-10 p-3 rounded-full mr-4">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:book-education"
                class="iconify text-primary-blue text-2xl iconify--mdi">
                <path fill="currentColor"
                  d="M8.82 17L13 19.28V22H6c-1.11 0-2-.89-2-2V4a2 2 0 0 1 2-2h1v7l2.5-1.5L12 9V2h6a2 2 0 0 1 2 2v8.54l-1.5-.82zM24 17l-5.5-3l-5.5 3l5.5 3zm-9 2.09v2L18.5 23l3.5-1.91v-2L18.5 21z">
                </path>
              </svg>
            </div>
            <h2 class="text-xl font-semibold text-[#333]">学业能力测评</h2>
          </div>
          <p class="text-[#666] mb-6 leading-relaxed">
            通过科学的评估模型，精准分析您的学科优势与学习潜力，为专业选择提供数据支撑。测评涵盖逻辑思维、语言能力等核心维度。
          </p>
          <!-- 测评维度 -->
          <div class="grid grid-cols-2 gap-4 mb-8">
            <div class="flex items-start">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:brain" class="iconify text-primary-blue text-2xl mr-2 iconify--mdi">
                <path fill="currentColor"
                  d="M21.33 12.91c.09 1.55-.62 3.04-1.89 3.95l.77 1.49c.23.45.26.98.06 1.45c-.19.47-.58.84-1.06 1l-.79.25a1.69 1.69 0 0 1-1.86-.55L14.44 18c-.89-.15-1.73-.53-2.44-1.1c-.5.15-1 .23-1.5.23c-.88 0-1.76-.27-2.5-.79c-.53.16-1.07.23-1.62.22c-.79.01-1.57-.15-2.3-.45a4.1 4.1 0 0 1-2.43-3.61c-.08-.72.04-1.45.35-2.11c-.29-.75-.32-1.57-.07-2.33C2.3 7.11 3 6.32 3.87 5.82c.58-1.69 2.21-2.82 4-2.7c1.6-1.5 4.05-1.66 5.83-.37c.42-.11.86-.17 1.3-.17c1.36-.03 2.65.57 3.5 1.64c2.04.53 3.5 2.35 3.58 4.47c.05 1.11-.25 2.2-.86 3.13c.07.36.11.72.11 1.09m-5-1.41c.57.07 1.02.5 1.02 1.07a1 1 0 0 1-1 1h-.63c-.32.9-.88 1.69-1.62 2.29c.25.09.51.14.77.21c5.13-.07 4.53-3.2 4.53-3.25a2.59 2.59 0 0 0-2.69-2.49a1 1 0 0 1-1-1a1 1 0 0 1 1-1c1.23.03 2.41.49 3.33 1.3c.05-.29.08-.59.08-.89c-.06-1.24-.62-2.32-2.87-2.53c-1.25-2.96-4.4-1.32-4.4-.4c-.03.23.21.72.25.75a1 1 0 0 1 1 1c0 .55-.45 1-1 1c-.53-.02-1.03-.22-1.43-.56c-.48.31-1.03.5-1.6.56c-.57.05-1.04-.35-1.07-.9a.97.97 0 0 1 .88-1.1c.16-.02.94-.14.94-.77c0-.66.25-1.29.68-1.79c-.92-.25-1.91.08-2.91 1.29C6.75 5 6 5.25 5.45 7.2C4.5 7.67 4 8 3.78 9c1.08-.22 2.19-.13 3.22.25c.5.19.78.75.59 1.29c-.19.52-.77.78-1.29.59c-.73-.32-1.55-.34-2.3-.06c-.32.27-.32.83-.32 1.27c0 .74.37 1.43 1 1.83c.53.27 1.12.41 1.71.4q-.225-.39-.39-.81a1.038 1.038 0 0 1 1.96-.68c.4 1.14 1.42 1.92 2.62 2.05c1.37-.07 2.59-.88 3.19-2.13c.23-1.38 1.34-1.5 2.56-1.5m2 7.47l-.62-1.3l-.71.16l1 1.25zm-4.65-8.61a1 1 0 0 0-.91-1.03c-.71-.04-1.4.2-1.93.67c-.57.58-.87 1.38-.84 2.19a1 1 0 0 0 1 1c.57 0 1-.45 1-1c0-.27.07-.54.23-.76c.12-.1.27-.15.43-.15c.55.03 1.02-.38 1.02-.92">
                </path>
              </svg>
              <div>
                <h3 class="font-medium text-[#333]">逻辑思维</h3>
                <p class="text-sm text-[#999]">问题分析与推理能力</p>
              </div>
            </div>
            <div class="flex items-start">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:alphabetical"
                class="iconify text-primary-blue text-2xl mr-2 iconify--mdi">
                <path fill="currentColor"
                  d="M6 11a2 2 0 0 1 2 2v4H4a2 2 0 0 1-2-2v-2a2 2 0 0 1 2-2zm-2 2v2h2v-2zm16 0v2h2v2h-2a2 2 0 0 1-2-2v-2a2 2 0 0 1 2-2h2v2zm-8-6v4h2a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2h-2a2 2 0 0 1-2-2V7zm0 8h2v-2h-2z">
                </path>
              </svg>
              <div>
                <h3 class="font-medium text-[#333]">语言能力</h3>
                <p class="text-sm text-[#999]">理解表达与写作水平</p>
              </div>
            </div>
            <div class="flex items-start">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:calculator"
                class="iconify text-primary-blue text-2xl mr-2 iconify--mdi">
                <path fill="currentColor"
                  d="M7 2h10a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2m0 2v4h10V4zm0 6v2h2v-2zm4 0v2h2v-2zm4 0v2h2v-2zm-8 4v2h2v-2zm4 0v2h2v-2zm4 0v2h2v-2zm-8 4v2h2v-2zm4 0v2h2v-2zm4 0v2h2v-2z">
                </path>
              </svg>
              <div>
                <h3 class="font-medium text-[#333]">数理能力</h3>
                <p class="text-sm text-[#999]">抽象思维与计算能力</p>
              </div>
            </div>
            <div class="flex items-start">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:lightbulb"
                class="iconify text-primary-blue text-2xl mr-2 iconify--mdi">
                <path fill="currentColor"
                  d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7M9 21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z">
                </path>
              </svg>
              <div>
                <h3 class="font-medium text-[#333]">创新思维</h3>
                <p class="text-sm text-[#999]">原创想法与实践能力</p>
              </div>
            </div>
          </div>
          <!-- 测评状态 -->
          <div class="mb-6">
            <div class="flex justify-between text-sm mb-1">
              <span class="text-[#666]">测评状态</span>
              <span class="font-medium">未开始</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-1.5">
              <div class="bg-accent-green h-1.5 rounded-full w-0"></div>
            </div>
          </div>
          <button
            class="w-full bg-primary-blue text-white py-3 rounded font-semibold hover:bg-opacity-90 transition-colors">
            开始测评
          </button>
        </div>
        <!-- 职业测评模块 -->
        <div class="bg-white rounded-lg shadow-sm p-6 border border-[#E8E8E8] transition-all hover:shadow-md">
          <div class="flex items-center mb-6">
            <div class="bg-primary-blue bg-opacity-10 p-3 rounded-full mr-4">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:briefcase" class="iconify text-primary-blue text-2xl iconify--mdi">
                <path fill="currentColor"
                  d="M10 2h4a2 2 0 0 1 2 2v2h4a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8c0-1.11.89-2 2-2h4V4c0-1.11.89-2 2-2m4 4V4h-4v2z">
                </path>
              </svg>
            </div>
            <h2 class="text-xl font-semibold text-[#333]">职业测评</h2>
          </div>
          <p class="text-[#666] mb-6 leading-relaxed">
            基于霍兰德职业理论模型，深入分析您的职业兴趣倾向，匹配适合的专业发展方向。识别潜在职业优势，提供发展建议。
          </p>
          <!-- 职业类型 -->
          <div class="mb-6 bg-[#FAFAFA] rounded-lg p-4">
            <h3 class="font-medium text-[#333] mb-3">测评涵盖职业类型</h3>
            <div class="flex flex-wrap gap-2">
              <span class="bg-primary-blue bg-opacity-10 text-primary-blue text-xs px-3 py-1 rounded-full">研究型</span>
              <span class="bg-primary-blue bg-opacity-10 text-primary-blue text-xs px-3 py-1 rounded-full">艺术型</span>
              <span class="bg-primary-blue bg-opacity-10 text-primary-blue text-xs px-3 py-1 rounded-full">社会型</span>
              <span class="bg-primary-blue bg-opacity-10 text-primary-blue text-xs px-3 py-1 rounded-full">企业型</span>
              <span class="bg-primary-blue bg-opacity-10 text-primary-blue text-xs px-3 py-1 rounded-full">现实型</span>
              <span class="bg-primary-blue bg-opacity-10 text-primary-blue text-xs px-3 py-1 rounded-full">传统型</span>
            </div>
          </div>
          <!-- 测评报告示例 -->
          <div class="mb-6">
            <h3 class="font-medium text-[#333] mb-3">测评报告示例</h3>
            <div class="border border-dashed border-gray-300 rounded-lg p-4 flex items-center bg-[#FAFAFA]">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:file-document"
                class="iconify text-gray-400 text-3xl mr-3 iconify--mdi">
                <path fill="currentColor"
                  d="M13 9h5.5L13 3.5zM6 2h8l6 6v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4c0-1.11.89-2 2-2m9 16v-2H6v2zm3-4v-2H6v2z">
                </path>
              </svg>
              <div>
                <p class="text-sm font-medium text-[#333]">职业兴趣测评报告</p>
                <p class="text-xs text-[#999]">包含详细职业倾向分析和专业匹配建议</p>
              </div>
            </div>
          </div>
          <button
            class="w-full bg-primary-blue text-white py-3 rounded font-semibold hover:bg-opacity-90 transition-colors">
            开始测评
          </button>
        </div>
      </div>
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
  box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  border-top: 1px solid #e5e7eb;
}
</style>