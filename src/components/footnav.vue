<script setup lang="ts">
import { Message, Phone, Location } from '@element-plus/icons-vue'
</script>

<template>
  <!-- Footer -->
  <footer class="footer">
    <div class="max-w-5xl mx-auto grid grid-cols-4 gap-8">
      <div class="footer-column">
        <h3 class="footer-title">聪志愿</h3>
        <li><a href="#/" class="footer-link">AI高考志愿填报服务平台</a></li>
      </div>
      <div class="footer-column">
        <h3 class="footer-title">服务项目</h3>
        <ul class="footer-list">
          <li><a href="#/volunteerApply" class="footer-link">志愿填报</a></li>
          <li><a href="#/schoolSearch" class="footer-link">院校查询</a></li>
          <li><a href="#/majorAnalysis" class="footer-link">专业解析</a></li>
          <li><a href="#/aiAssessmentList" class="footer-link">AI测评</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h3 class="footer-title">关于我们</h3>
        <ul class="footer-list">
          <li><a href="#" class="footer-link">团队介绍</a></li>
          <li><a href="#" class="footer-link">联系我们</a></li>
        </ul>
      </div>
      <div class="footer-column">
        <h3 class="footer-title">联系方式</h3>
        <ul class="footer-list">
          <!-- <li>
            <el-icon class="footer-icon">
              <Message />
            </el-icon>
            contact@qingxueai.com
          </li> -->
          <li>
            <el-icon class="footer-icon">
              <Phone />
            </el-icon>
            15066178020
          </li>
          <li>
            <img src="../assets/sys/lxfsewm.jpg" alt="联系二维码" style="width: 160px; height: 160px;">
          </li>
          <!-- <li class="footer-address">
            <el-icon class="footer-icon">
              <Location />
            </el-icon>
            <span>北京市海淀区中关村大街1号</span>
          </li> -->
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 聪志愿AI智能科技 版权所有 | 京ICP备12345678号</p>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
/* Footer */
.footer {
  margin: 0 auto;
  padding: 3rem 2rem;
  max-width: 80vw;
  min-width: 1200px;
  color: white;
  background: #111827;
  box-shadow:
    0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  border-radius: 0 0 0.75rem 0.75rem;
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
</style>
