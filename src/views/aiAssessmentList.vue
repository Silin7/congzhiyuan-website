<script setup lang="ts">
import { ref, onMounted } from 'vue'
import * as api from '@/api/interfaceapi'
import sideTop from '@/components/sideTop.vue'

onMounted(async () => {
  getScalesListQueryApi()
})

const getScalesListQueryApi = async () => {
  const res = await api.scalesListQueryApi()
  console.log('res -------->', res)
}
</script>

<template>
  <div class="ai-assessment-page">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section class="mb-6">
        <h2 class="text-2xl font-bold text-center mb-2">AI智能测评</h2>
        <h4 class="text-1xl text-center mb-6" style="color: #646566;">科学测评，精准规划未来</h4>
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <!-- <div class="tagBox">
            <div class="tagContent">
            </div>
          </div> -->
          <div class="zygh-zycp-list"><a
              href="https://xz.chsi.com.cn/cp/sph/fmxx.do?surveyId=6qs55vir9c2kq1p3&amp;from=zyck" target="_blank"
              class="list-item">
              <div class="img-box"><img src="https://t1.chei.com.cn/cp/cdn/showimg/3kke4flv9lkjnbkz.jpeg" alt=""></div>
              <div class="list-right">
                <div class="right-title">最优化倾向测试</div>
                <div class="right-desc">
                  当你做小的决定时，应当依靠你的大脑，把利弊罗列出来，分析并作出正确的决定；当你做大的决定，如寻找终身伴侣或寻找理想时，你就应该依靠你的潜意识，因为这么重要的决定必须在你的心灵深处找到依据。-弗洛伊德（精神分析学派，著有《梦的解析》）
                  那么你是如何使用大脑和潜意识做出决策的呢？自测一下你是“完美主义者”还是“选择困难症患者”吧！</div>
                <div class="right-btn">开始测评</div>
              </div>
            </a><a href="https://xz.chsi.com.cn/cp/sph/fmxx.do?surveyId=5jw56vdhzaswvue1&amp;from=zyck" target="_blank"
              class="list-item">
              <div class="img-box"><img src="https://t1.chei.com.cn/cp/cdn/showimg/n8i4vrua0bg6nxee.jpeg" alt=""></div>
              <div class="list-right">
                <div class="right-title">测你的生涯控制点</div>
                <div class="right-desc">
                  归因指个体根据信息和线索对行为原因进行推测与判断。不同的归因方式决定了你对自我生涯的看法和行动，显然积极的归因方式更有利于个体或关系的发展。想知道你在生涯发展中是怎样的归因者吗，来测测看吧。</div>
                <div class="right-btn">开始测评</div>
              </div>
            </a><a href="https://xz.chsi.com.cn/cp/sph/fmxx.do?surveyId=e1feihqgt8vbey6f&amp;from=zyck" target="_blank"
              class="list-item">
              <div class="img-box"><img src="https://t1.chei.com.cn/cp/cdn/showimg/8zyigtp969ubbmeu.jpeg" alt=""></div>
              <div class="list-right">
                <div class="right-title">测你的生涯适应力</div>
                <div class="right-desc">职业生涯是一个漫长的过程，也是一个动态的不断调整的过程，面对未来未知的职业长路，不妨从现在开始，认清自己，不断探索，为未来的职业之旅绘一份行路指南。</div>
                <div class="right-btn">开始测评</div>
              </div>
            </a></div>
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

<style>
.zygh-zycp-list {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  padding-bottom: 38px;
}

.zygh-zycp-list .list-item {
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
  transition: transform .5s;
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
  width: 88px;
  height: 32px;
  line-height: 32px;
  background: #1cb278;
  border-radius: 2px;
  font-size: 14px;
  color: #fff;
  text-align: center;
  position: absolute;
  right: 0;
  bottom: 0;
}
</style>