<script setup lang="ts">
import { ref } from 'vue'
import sideTop from '@/components/sideTop.vue'
</script>

<template>
  <div class="home-page">
    <main>
      <!-- AI智能志愿填报 -->
      <section class="bg-gradient-to-r from-indigo-500 to-purple-600 py-16 px-12 text-center">
        <div class="max-w-4xl mx-auto">
          <h1 class="text-4xl font-bold text-white tracking-tight">AI智能志愿填报</h1>
          <p class="mt-4 text-xl font-medium text-indigo-100">让选择更有把握</p>
          <p class="mt-6 text-gray-100 leading-relaxed max-w-2xl mx-auto">
            基于千万级录取数据分析与AI智能算法，精准匹配院校专业，<br>
            让高考志愿填报不再迷茫
          </p>
        </div>
      </section>

      <!-- 智能推荐方案 -->
      <section class="py-12 px-8">
        <h2 class="text-2xl font-bold text-center text-gray-800 mb-10">智能推荐方案</h2>
        <div class="grid grid-cols-3 gap-6 max-w-4xl mx-auto">
          <!-- 冲刺院校方案 -->
          <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
            <div class="bg-gradient-to-r from-amber-50 to-yellow-50 py-4 text-center">
              <span
                class="inline-block bg-gradient-to-r from-amber-500 to-orange-500 text-white px-4 py-1 rounded-full text-sm font-medium">冲刺院校方案</span>
            </div>
            <div class="p-6">
              <p class="text-gray-600 mb-4">基于您的分数匹配略高于档位的优质院校，最大化录取潜力</p>
              <div class="flex items-center">
                <span class="bg-amber-100 text-amber-800 px-3 py-1 rounded-full text-sm font-medium">匹配度 96%</span>
              </div>
            </div>
          </div>
          <!-- 稳妥报考方案 -->
          <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
            <div class="bg-gradient-to-r from-emerald-50 to-teal-50 py-4 text-center">
              <span
                class="inline-block bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-4 py-1 rounded-full text-sm font-medium">稳妥报考方案</span>
            </div>
            <div class="p-6">
              <p class="text-gray-600 mb-4">精准匹配您最可能录取的院校组合，确保理想大学</p>
              <div class="flex items-center">
                <span class="bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full text-sm font-medium">匹配度 92%</span>
              </div>
            </div>
          </div>
          <!-- 保底稳录方案 -->
          <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
            <div class="bg-gradient-to-r from-blue-50 to-indigo-50 py-4 text-center">
              <span
                class="inline-block bg-gradient-to-r from-blue-500 to-indigo-500 text-white px-4 py-1 rounded-full text-sm font-medium">保底稳录方案</span>
            </div>
            <div class="p-6">
              <p class="text-gray-600 mb-4">确保安全录取的保守方案，结合兴趣匹配专业方向</p>
              <div class="flex items-center">
                <span class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm font-medium">匹配度 98%</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 核心功能 -->
      <section class="py-12 px-8 bg-gray-50">
        <h2 class="text-2xl font-bold text-center text-gray-800 mb-10">核心功能</h2>
        <div class="grid grid-cols-3 gap-8 max-w-5xl mx-auto">
          <!-- AI智能推荐 -->
          <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div class="bg-indigo-100 text-indigo-600 rounded-lg p-3 inline-flex">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:brain" class="iconify text-3xl iconify--mdi">
                <path fill="currentColor"
                  d="M21.33 12.91c.09 1.55-.62 3.04-1.89 3.95l.77 1.49c.23.45.26.98.06 1.45c-.19.47-.58.84-1.06 1l-.79.25a1.69 1.69 0 0 1-1.86-.55L14.44 18c-.89-.15-1.73-.53-2.44-1.1c-.5.15-1 .23-1.5.23c-.88 0-1.76-.27-2.5-.79c-.53.16-1.07.23-1.62.22c-.79.01-1.57-.15-2.3-.45a4.1 4.1 0 0 1-2.43-3.61c-.08-.72.04-1.45.35-2.11c-.29-.75-.32-1.57-.07-2.33C2.3 7.11 3 6.32 3.87 5.82c.58-1.69 2.21-2.82 4-2.7c1.6-1.5 4.05-1.66 5.83-.37c.42-.11.86-.17 1.3-.17c1.36-.03 2.65.57 3.5 1.64c2.04.53 3.5 2.35 3.58 4.47c.05 1.11-.25 2.2-.86 3.13c.07.36.11.72.11 1.09m-5-1.41c.57.07 1.02.5 1.02 1.07a1 1 0 0 1-1 1h-.63c-.32.9-.88 1.69-1.62 2.29c.25.09.51.14.77.21c5.13-.07 4.53-3.2 4.53-3.25a2.59 2.59 0 0 0-2.69-2.49a1 1 0 0 1-1-1a1 1 0 0 1 1-1c1.23.03 2.41.49 3.33 1.3c.05-.29.08-.59.08-.89c-.06-1.24-.62-2.32-2.87-2.53c-1.25-2.96-4.4-1.32-4.4-.4c-.03.23.21.72.25.75a1 1 0 0 1 1 1c0 .55-.45 1-1 1c-.53-.02-1.03-.22-1.43-.56c-.48.31-1.03.5-1.6.56c-.57.05-1.04-.35-1.07-.9a.97.97 0 0 1 .88-1.1c.16-.02.94-.14.94-.77c0-.66.25-1.29.68-1.79c-.92-.25-1.91.08-2.91 1.29C6.75 5 6 5.25 5.45 7.2C4.5 7.67 4 8 3.78 9c1.08-.22 2.19-.13 3.22.25c.5.19.78.75.59 1.29c-.19.52-.77.78-1.29.59c-.73-.32-1.55-.34-2.3-.06c-.32.27-.32.83-.32 1.27c0 .74.37 1.43 1 1.83c.53.27 1.12.41 1.71.4q-.225-.39-.39-.81a1.038 1.038 0 0 1 1.96-.68c.4 1.14 1.42 1.92 2.62 2.05c1.37-.07 2.59-.88 3.19-2.13c.23-1.38 1.34-1.5 2.56-1.5m2 7.47l-.62-1.3l-.71.16l1 1.25zm-4.65-8.61a1 1 0 0 0-.91-1.03c-.71-.04-1.4.2-1.93.67c-.57.58-.87 1.38-.84 2.19a1 1 0 0 0 1 1c.57 0 1-.45 1-1c0-.27.07-.54.23-.76c.12-.1.27-.15.43-.15c.55.03 1.02-.38 1.02-.92">
                </path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mt-4 mb-2 text-gray-800">AI志愿填报</h3>
            <p class="text-gray-600">根据成绩、兴趣、就业前景多维分析，生成个性化志愿填报方案</p>
            <div class="mt-6">
              <a class="inline-flex items-center text-indigo-600 hover:text-indigo-800 font-medium" href="#">
                <span>了解更多</span>
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                  viewBox="0 0 24 24" data-icon="mdi:arrow-right" class="iconify ml-1 iconify--mdi">
                  <path fill="currentColor" d="M4 11v2h12l-5.5 5.5l1.42 1.42L19.84 12l-7.92-7.92L10.5 5.5L16 11z">
                  </path>
                </svg>
              </a>
            </div>
          </div>
          <!-- 院校数据查询 -->
          <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div class="bg-amber-100 text-amber-600 rounded-lg p-3 inline-flex">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:school" class="iconify text-3xl iconify--mdi">
                <path fill="currentColor" d="M12 3L1 9l11 6l9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mt-4 mb-2 text-gray-800">院校数据查询</h3>
            <p class="text-gray-600">覆盖全国3000+院校实时录取数据，学科评估与就业报告深度解析</p>
            <div class="mt-6">
              <a class="inline-flex items-center text-amber-600 hover:text-amber-800 font-medium" href="#">
                <span>了解更多</span>
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                  viewBox="0 0 24 24" data-icon="mdi:arrow-right" class="iconify ml-1 iconify--mdi">
                  <path fill="currentColor" d="M4 11v2h12l-5.5 5.5l1.42 1.42L19.84 12l-7.92-7.92L10.5 5.5L16 11z">
                  </path>
                </svg>
              </a>
            </div>
          </div>
          <!-- 专业匹配测评 -->
          <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div class="bg-emerald-100 text-emerald-600 rounded-lg p-3 inline-flex">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:clipboard-check" class="iconify text-3xl iconify--mdi">
                <path fill="currentColor"
                  d="m10 17l-4-4l1.41-1.41L10 14.17l6.59-6.59L18 9m-6-6a1 1 0 0 1 1 1a1 1 0 0 1-1 1a1 1 0 0 1-1-1a1 1 0 0 1 1-1m7 0h-4.18C14.4 1.84 13.3 1 12 1s-2.4.84-2.82 2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2">
                </path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mt-4 mb-2 text-gray-800">专业解析</h3>
            <p class="text-gray-600">高校专业详细解析...</p>
            <div class="mt-6">
              <a class="inline-flex items-center text-emerald-600 hover:text-emerald-800 font-medium" href="#">
                <span>了解更多</span>
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                  viewBox="0 0 24 24" data-icon="mdi:arrow-right" class="iconify ml-1 iconify--mdi">
                  <path fill="currentColor" d="M4 11v2h12l-5.5 5.5l1.42 1.42L19.84 12l-7.92-7.92L10.5 5.5L16 11z">
                  </path>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </section>

      <!--  专业服务保障  -->
      <section class="py-16 px-8 bg-gradient-to-br from-indigo-50 to-purple-50">
        <h2 class="text-2xl font-bold text-center text-gray-800 mb-4">专业服务保障</h2>
        <p class="text-center text-gray-600 max-w-2xl mx-auto mb-12">精准、可靠、专业的智能志愿填报平台</p>
        <div class="grid grid-cols-4 gap-6 max-w-5xl mx-auto">
          <!-- AI算法精准 -->
          <div class="bg-white p-5 rounded-lg border border-gray-200 text-center">
            <div
              class="bg-gradient-to-r from-indigo-500 to-purple-500 w-16 h-16 rounded-full flex items-center justify-center mx-auto">
              <span class="iconify text-3xl text-white" data-icon="mdi:artificial-intelligence"></span>
            </div>
            <h3 class="font-semibold mt-4 mb-2 text-gray-800">AI算法精准</h3>
            <p class="text-gray-600 text-sm">基于机器学习模型不断优化，预测准确率高达92%</p>
          </div>
          <!-- 数据实时更新 -->
          <div class="bg-white p-5 rounded-lg border border-gray-200 text-center">
            <div
              class="bg-gradient-to-r from-blue-500 to-cyan-500 w-16 h-16 rounded-full flex items-center justify-center mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:database-sync" class="iconify text-3xl text-white iconify--mdi">
                <path fill="currentColor"
                  d="M19 12v1.5a4 4 0 0 1 4 4c0 .82-.25 1.58-.67 2.21l-1.09-1.09c.17-.34.26-.72.26-1.12A2.5 2.5 0 0 0 19 15v1.5l-2.25-2.25zm0 11v-1.5a4 4 0 0 1-4-4c0-.82.25-1.58.67-2.21l1.09 1.09c-.17.34-.26.72-.26 1.12A2.5 2.5 0 0 0 19 20v-1.5l2.25 2.25zM12 3c4.42 0 8 1.79 8 4s-3.58 4-8 4s-8-1.79-8-4s3.58-4 8-4M4 9c0 2.21 3.58 4 8 4c1.11 0 2.17-.11 3.14-.32c-.95.86-1.64 1.99-1.96 3.28L12 16c-4.42 0-8-1.79-8-4zm16 0v2h-.5l-.6.03c.7-.6 1.1-1.29 1.1-2.03M4 14c0 2.21 3.58 4 8 4l1-.03c.09 1.06.42 2.03.95 2.91L12 21c-4.42 0-8-1.79-8-4z">
                </path>
              </svg>
            </div>
            <h3 class="font-semibold mt-4 mb-2 text-gray-800">数据实时更新</h3>
            <p class="text-gray-600 text-sm">每年更新千万级录取数据，确保信息准确性</p>
          </div>
          <!-- 专家团队支持 -->
          <div class="bg-white p-5 rounded-lg border border-gray-200 text-center">
            <div
              class="bg-gradient-to-r from-amber-500 to-orange-500 w-16 h-16 rounded-full flex items-center justify-center mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:account-group" class="iconify text-3xl text-white iconify--mdi">
                <path fill="currentColor"
                  d="M12 5.5A3.5 3.5 0 0 1 15.5 9a3.5 3.5 0 0 1-3.5 3.5A3.5 3.5 0 0 1 8.5 9A3.5 3.5 0 0 1 12 5.5M5 8c.56 0 1.08.15 1.53.42c-.15 1.43.27 2.85 1.13 3.96C7.16 13.34 6.16 14 5 14a3 3 0 0 1-3-3a3 3 0 0 1 3-3m14 0a3 3 0 0 1 3 3a3 3 0 0 1-3 3c-1.16 0-2.16-.66-2.66-1.62a5.54 5.54 0 0 0 1.13-3.96c.45-.27.97-.42 1.53-.42M5.5 18.25c0-2.07 2.91-3.75 6.5-3.75s6.5 1.68 6.5 3.75V20h-13zM0 20v-1.5c0-1.39 1.89-2.56 4.45-2.9c-.59.68-.95 1.62-.95 2.65V20zm24 0h-3.5v-1.75c0-1.03-.36-1.97-.95-2.65c2.56.34 4.45 1.51 4.45 2.9z">
                </path>
              </svg>
            </div>
            <h3 class="font-semibold mt-4 mb-2 text-gray-800">专家团队支持</h3>
            <p class="text-gray-600 text-sm">300+招生官与教育专家提供深度咨询服务</p>
          </div>
          <!-- 成功案例见证 -->
          <div class="bg-white p-5 rounded-lg border border-gray-200 text-center">
            <div
              class="bg-gradient-to-r from-emerald-500 to-teal-500 w-16 h-16 rounded-full flex items-center justify-center mx-auto">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:check-decagram" class="iconify text-3xl text-white iconify--mdi">
                <path fill="currentColor"
                  d="m23 12l-2.44-2.78l.34-3.68l-3.61-.82l-1.89-3.18L12 3L8.6 1.54L6.71 4.72l-3.61.81l.34 3.68L1 12l2.44 2.78l-.34 3.69l3.61.82l1.89 3.18L12 21l3.4 1.46l1.89-3.18l3.61-.82l-.34-3.68zm-13 5l-4-4l1.41-1.41L10 14.17l6.59-6.59L18 9z">
                </path>
              </svg>
            </div>
            <h3 class="font-semibold mt-4 mb-2 text-gray-800">成功案例见证</h3>
            <p class="text-gray-600 text-sm">每年帮助10万+考生进入理想院校</p>
          </div>
        </div>
      </section>

      <!-- 合作院校 -->
      <section class="py-14 px-8">
        <h2 class="text-2xl font-bold text-center text-gray-800 mb-8">合作院校</h2>
        <div class="grid grid-cols-6 gap-6 max-w-5xl mx-auto">
          <!-- 6个合作院校Logo占位符 -->
          <div class="bg-gray-100 border-2 border-dashed rounded-xl w-full h-24 flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
              viewBox="0 0 24 24" data-icon="mdi:university" class="iconify text-4xl text-gray-400 iconify--mdi">
              <path fill="currentColor" d="M12 3L1 9l11 6l9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17z"></path>
            </svg>
          </div>
          <div class="bg-gray-100 border-2 border-dashed rounded-xl w-full h-24 flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
              viewBox="0 0 24 24" data-icon="mdi:university" class="iconify text-4xl text-gray-400 iconify--mdi">
              <path fill="currentColor" d="M12 3L1 9l11 6l9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17z"></path>
            </svg>
          </div>
          <div class="bg-gray-100 border-2 border-dashed rounded-xl w-full h-24 flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
              viewBox="0 0 24 24" data-icon="mdi:university" class="iconify text-4xl text-gray-400 iconify--mdi">
              <path fill="currentColor" d="M12 3L1 9l11 6l9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17z"></path>
            </svg>
          </div>
          <div class="bg-gray-100 border-2 border-dashed rounded-xl w-full h-24 flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
              viewBox="0 0 24 24" data-icon="mdi:university" class="iconify text-4xl text-gray-400 iconify--mdi">
              <path fill="currentColor" d="M12 3L1 9l11 6l9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17z"></path>
            </svg>
          </div>
          <div class="bg-gray-100 border-2 border-dashed rounded-xl w-full h-24 flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
              viewBox="0 0 24 24" data-icon="mdi:university" class="iconify text-4xl text-gray-400 iconify--mdi">
              <path fill="currentColor" d="M12 3L1 9l11 6l9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17z"></path>
            </svg>
          </div>
          <div class="bg-gray-100 border-2 border-dashed rounded-xl w-full h-24 flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
              viewBox="0 0 24 24" data-icon="mdi:university" class="iconify text-4xl text-gray-400 iconify--mdi">
              <path fill="currentColor" d="M12 3L1 9l11 6l9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17z"></path>
            </svg>
          </div>
        </div>
      </section>
    </main>
    <sideTop />
  </div>
</template>

<style lang="scss" scoped>
.home-page {
  max-width: 80vw;
  min-width: 1200px;
  margin: 0 auto;
  background-color: #fff;
  box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
}

/* Header Styles */
.header {
  background: white;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0.75rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-left {
  display: flex;
  align-items: center;
}

.logo {
  font-size: 1.25rem;
  font-weight: bold;
  color: #1f2937;
  text-decoration: none;
  display: flex;
  align-items: center;
}

.logo-icon {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  color: #3b82f6;
  margin-right: 0.5rem;
}

.nav-menu {
  display: flex;
  margin-left: 2.5rem;
  gap: 2rem;
}

.nav-link {
  color: #4b5563;
  text-decoration: none;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #3b82f6;
}

.login-btn {
  background: #3b82f6;
  color: white;
  font-weight: bold;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  border: none;
  cursor: pointer;
  transition: background 0.3s ease;
}

.login-btn:hover {
  background: #2563eb;
}

/* Hero Section */
.hero-section {
  // background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 4rem 3rem;
}

.hero-container {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}

.hero-title {
  font-size: 2.25rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.hero-subtitle {
  font-size: 1.125rem;
  margin-bottom: 2rem;
}

.hero-description {
  max-width: 42rem;
  margin: 0 auto;
}

/* Section Common Styles */
.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.section-title {
  font-size: 1.875rem;
  font-weight: bold;
  text-align: center;
  margin-bottom: 3rem;
}

.section-subtitle {
  text-align: center;
  color: #6b7280;
  margin-bottom: 3rem;
}

/* Recommendations & Core Features */
.recommendations-section {
  padding: 3rem 2rem;
}

.core-features-section {
  padding: 4rem 0;
  background: #f9fafb;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.feature-card {
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-0.3125rem);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.card-icon {
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
}

.orange-icon {
  background: #ffedd5;
}

.green-icon {
  background: #dcfce7;
}

.blue-icon {
  background: #dbeafe;
}

.purple-icon {
  background: #f3e8ff;
}

.pink-icon {
  background: #fce7f3;
}

.yellow-icon {
  background: #fef9c3;
}

.icon {
  width: 1.5rem;
  height: 1.5rem;
}

.orange-icon .icon {
  color: #f97316;
}

.green-icon .icon {
  color: #22c55e;
}

.blue-icon .icon {
  color: #3b82f6;
}

.purple-icon .icon {
  color: #a855f7;
}

.pink-icon .icon {
  color: #ec4899;
}

.yellow-icon .icon {
  color: #eab308;
}

.card-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.card-description {
  color: #6b7280;
  line-height: 1.5;
}

.card-link {
  color: #3b82f6;
  text-decoration: none;
  margin-top: 1rem;
  display: inline-block;
  transition: color 0.3s ease;
}

.card-link:hover {
  color: #2563eb;
}

/* Business Section */
.business-section {
  padding: 4rem 0;
}

.business-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
}

.business-item {
  text-align: center;
}

.business-icon {
  width: 4rem;
  height: 4rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
}

.business-title {
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.business-description {
  font-size: 0.875rem;
  color: #6b7280;
  line-height: 1.4;
}

/* Partners Section */
.partners-section {
  padding: 4rem 0;
  background: #f9fafb;
}

.partners-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 4rem;
}

.partner-logo {
  width: 6rem;
  height: 6rem;
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.partner-icon {
  width: 3rem;
  height: 3rem;
  color: #9ca3af;
}

/* Footer */
.footer {
  background: #111827;
  color: white;
  padding: 3rem 0;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
}

.footer-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.footer-text {
  color: #9ca3af;
  line-height: 1.5;
}

.footer-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-list li {
  margin-bottom: 0.5rem;
  color: #9ca3af;
}

.footer-link {
  color: #9ca3af;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-link:hover {
  color: white;
}

.footer-icon {
  display: inline-block;
  width: 1rem;
  height: 1rem;
  margin-right: 0.5rem;
}

.footer-address {
  display: flex;
  align-items: center;
  margin-top: 1rem;
}

.footer-bottom {
  border-top: 1px solid #374151;
  margin-top: 2rem;
  padding-top: 2rem;
  text-align: center;
  color: #6b7280;
}

body {
  background-color: #f9fafb;
}
</style>