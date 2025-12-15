<script setup lang="ts">
import { Message, Phone, Location } from '@element-plus/icons-vue'
</script>

<template>
  <!-- Footer -->
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-column">
          <h3 class="footer-title">志愿AI</h3>
          <p class="footer-text">AI智能高考志愿填报平台，让科技助力梦想，让每一分都有价值。</p>
        </div>
        <div class="footer-column">
          <h3 class="footer-title">服务项目</h3>
          <ul class="footer-list">
            <li><a href="#" class="footer-link">AI志愿填报</a></li>
            <li><a href="#" class="footer-link">生涯规划</a></li>
            <li><a href="#" class="footer-link">院校库</a></li>
            <li><a href="#" class="footer-link">专业库</a></li>
            <li><a href="#" class="footer-link">高考工具箱</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3 class="footer-title">关于我们</h3>
          <ul class="footer-list">
            <li><a href="#" class="footer-link">公司简介</a></li>
            <li><a href="#" class="footer-link">团队介绍</a></li>
            <li><a href="#" class="footer-link">联系我们</a></li>
            <li><a href="#" class="footer-link">加入我们</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3 class="footer-title">联系方式</h3>
          <ul class="footer-list">
            <li><el-icon class="footer-icon"><Message /></el-icon> contact@zhiyuanai.com</li>
            <li><el-icon class="footer-icon"><Phone /></el-icon> 400-123-4567</li>
            <li class="footer-address">
              <el-icon class="footer-icon"><Location /></el-icon>
              <span>北京市海淀区中关村大街1号</span>
            </li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2025 志愿AI 版权所有 | 京ICP备12345678号-1</p>
      </div>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
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
  grid-template-columns: 1fr;
  gap: 2rem;
}

@media (min-width: 768px) {
  .footer-grid {
    grid-template-columns: repeat(4, 1fr);
  }
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