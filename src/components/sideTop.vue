<script setup lang="ts">
import { ElBacktop } from 'element-plus'
</script>

<template>
  <el-backtop :right="32" :bottom="80" :visibility-height="300">
    <div class="gtBox">
      <img src="../assets/sys/gotop.png" alt="">
    </div>
  </el-backtop>
</template>

<style lang="scss" scoped>
.gtBox {
  width: 4rem;
  height: 4rem;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #ebf0fb;
  box-shadow:
    0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  border-radius: 4rem;

  &:hover {
    transform: scale(1.05);
    cursor: pointer;
  }

  img {
    width: 2.5rem;
    height: 2.5rem;
  }
}
</style>