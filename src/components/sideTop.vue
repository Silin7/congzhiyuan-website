<script setup lang="ts">
import { ElBacktop } from 'element-plus'
</script>

<template>
  <el-backtop :right="32" :bottom="80" :visibility-height="300" style="width: 3rem; height: 3rem;">
    <div class="gtBox">
      <img src="../assets/sys/gotop.png" alt="">
    </div>
  </el-backtop>
</template>

<style lang="scss" scoped>
.gtBox {
  // position: fixed;
  // right: 32px;
  // bottom: 80px;
  width: 3rem;
  height: 3rem;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #ebf0fb;
  box-shadow:
    0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  border-radius: 3rem;

  &:hover {
    transform: scale(1.05);
    cursor: pointer;
  }

  img {
    width: 2rem;
    height: 2rem;
  }
}
</style>