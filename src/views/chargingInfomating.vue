<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import * as api from '@/api/interfaceapi'
import { chargePayURL } from '@/api/baseConfig'
import sideTop from '@/components/sideTop.vue'

const route = useRoute()

const chargeItem = ref('Vip会员充值')
const totalFee = ref('')
const chargeMemo = ref('')
const paytype = ref('1')
const paying = ref(false)
const loading = ref(false)

const defaultNotes = [
  'Vip会员特权：升级后您可以不受条数限制进行精准填报和一键填报，并查看完整的分析结果，并可下载我的志愿填报表；并获得2次修改成绩类型机会和5次修改选科和成绩机会',
  '使用日期：有效期至当年年底',
  '适用范围：仅限山东省考生',
  '充值仅限于微信支付',
]

const CHARGE_PAY_ACTION = chargePayURL

const submitTotalFee = computed(() => {
  if (totalFee.value) return totalFee.value
  const queryPrice = route.query.price || route.query.amount
  return queryPrice ? String(queryPrice) : ''
})

const displayPrice = computed(() => submitTotalFee.value || '--')

const payToken = computed(() => {
  const token = localStorage.getItem('token') || ''
  return token ? `Bearer ${token}` : ''
})

const paymentMethodName = computed(() => {
  if (paytype.value === '2') return '支付宝'
  return '微信支付'
})

const rechargeNotes = computed(() => {
  if (!chargeMemo.value) return defaultNotes
  const lines = chargeMemo.value.split(/\r?\n/).map((line) => line.trim()).filter(Boolean)
  return lines.length > 0 ? lines : defaultNotes
})

onMounted(() => {
  fetchChargingInfo()
})

const fetchChargingInfo = async () => {
  loading.value = true
  try {
    const res: any = await api.chargingInfoQueryApi()
    if (res?.data) {
      chargeItem.value = res.data.chargeItem || chargeItem.value
      totalFee.value = res.data.totalFee != null ? String(res.data.totalFee) : ''
      chargeMemo.value = res.data.chargeMemo || ''
      paytype.value = String(res.data.paytype || '1')
    }
  } finally {
    loading.value = false
  }
}

const handlePay = (e: Event) => {
  if (paying.value) {
    e.preventDefault()
    return
  }
  if (!localStorage.getItem('token')) {
    e.preventDefault()
    ElMessage.warning('请先登录后再充值')
    return
  }
  if (!submitTotalFee.value) {
    e.preventDefault()
    ElMessage.warning('充值金额无效，请稍后再试')
    return
  }
  paying.value = true
}
</script>

<template>
  <div class="charging-page">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section class="mb-6">
        <h2 class="text-2xl font-bold text-center mb-2">欢迎充值成为Vip会员</h2>
        <h4 class="text-1xl text-center mb-6" style="color: #646566">
          仅需支付金额
          <span class="price-amount">¥{{ displayPrice }}</span>
          元 即可成为Vip会员
        </h4>

        <div v-loading="loading" class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <div class="vip-charge-list">
            <div class="list-item">
              <div class="vip-icon-box">
                <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <rect width="48" height="48" rx="10" fill="#76a33c" />
                  <path
                    d="M24 12l3.5 7.1 7.8 1.1-5.6 5.5 1.3 7.7L24 29.4l-7 3.9 1.3-7.7-5.6-5.5 7.8-1.1L24 12z"
                    fill="#fff"
                  />
                </svg>
              </div>
              <div class="list-right">
                <div class="right-title">{{ chargeItem }}</div>
                <div class="right-desc">
                  升级后可不受条数限制进行精准填报和一键填报，查看完整分析结果并下载志愿填报表
                </div>
                <div class="payment-row">
                  <span class="payment-label">支付方式：</span>
                  <div class="payment-option active">
                    <span class="wechat-icon" aria-hidden="true">
                      <svg v-if="paytype !== '2'" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="12" cy="12" r="12" fill="#07C160" />
                        <path
                          d="M8.5 7.5c-2.5 0-4.5 1.6-4.5 3.6 0 1.2.7 2.3 1.8 3.1l-.4 1.4 1.5-.8c.5.1 1 .2 1.6.2 2.5 0 4.5-1.6 4.5-3.6S11 7.5 8.5 7.5zm-1.3 2.8c-.3 0-.6-.2-.6-.5s.3-.5.6-.5.6.2.6.5-.3.5-.6.5zm2.6 0c-.3 0-.6-.2-.6-.5s.3-.5.6-.5.6.2.6.5-.3.5-.6.5z"
                          fill="#fff"
                        />
                        <path
                          d="M15.5 10.5c-2.2 0-4 1.4-4 3.1 0 .9.5 1.7 1.3 2.3l-.3 1.1 1.2-.6c.4.1.9.2 1.4.2 2.2 0 4-1.4 4-3.1s-1.8-3.1-4-3.1zm-1 2.4c-.2 0-.4-.2-.4-.4s.2-.4.4-.4.4.2.4.4-.2.4-.4.4zm2 0c-.2 0-.4-.2-.4-.4s.2-.4.4-.4.4.2.4.4-.2.4-.4.4z"
                          fill="#fff"
                        />
                      </svg>
                      <svg v-else viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="12" cy="12" r="12" fill="#1677FF" />
                        <path
                          d="M7 8h10v1.5H7V8zm0 3.2h6.5v1.5H7v-1.5zm0 3.2h8.5v1.5H7v-1.5z"
                          fill="#fff"
                        />
                      </svg>
                    </span>
                    <span class="payment-name">{{ paymentMethodName }}</span>
                  </div>
                </div>
                <form
                  method="post"
                  :action="CHARGE_PAY_ACTION"
                  class="pay-form"
                  @submit="handlePay"
                >
                  <input type="hidden" name="paytype" :value="paytype" />
                  <input type="hidden" name="chargeItem" :value="chargeItem" />
                  <input type="hidden" name="totalFee" :value="submitTotalFee" />
                  <input type="hidden" name="token" :value="payToken" />
                  <el-button
                    type="success"
                    class="pay-btn"
                    native-type="submit"
                    :loading="paying"
                  >
                    {{ paying ? '支付中...' : '立即支付' }}
                  </el-button>
                </form>
              </div>
            </div>

            <div class="list-item notes-item">
              <div class="list-right notes-right">
                <div class="right-title">充值说明</div>
                <div v-html="chargeMemo"></div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
    <sideTop />
  </div>
</template>

<style lang="scss" scoped>
.charging-page {
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

.price-amount {
  margin: 0 4px;
  font-weight: 600;
  color: #76a33c;
}
</style>

<style>
.vip-charge-list {
  padding-bottom: 8px;
}

.vip-charge-list .list-item {
  width: 100%;
  padding: 20px;
  display: flex;
  background-color: #fff;
  margin-bottom: 20px;
  border-radius: 10px;
}

.vip-charge-list .list-item:last-child {
  margin-bottom: 0;
}

.vip-charge-list .vip-icon-box {
  overflow: hidden;
  border-radius: 10px;
  margin-right: 16px;
  flex-shrink: 0;
}

.vip-charge-list .vip-icon-box svg {
  display: block;
  width: 80px;
  height: 80px;
}

.vip-charge-list .list-right {
  flex: 1;
  position: relative;
}

.vip-charge-list .right-title {
  font-size: 18px;
  line-height: 26px;
  color: #2b3330;
  font-weight: 700;
}

.vip-charge-list .right-desc {
  font-size: 14px;
  line-height: 24px;
  color: #67716c;
  margin: 8px 0 18px;
}

.vip-charge-list .payment-row {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.vip-charge-list .payment-label {
  font-size: 14px;
  line-height: 24px;
  color: #67716c;
  margin-right: 8px;
}

.vip-charge-list .payment-option {
  display: inline-flex;
  align-items: center;
  cursor: default;
  user-select: none;
}

.vip-charge-list .wechat-icon {
  display: inline-flex;
  width: 24px;
  height: 24px;
  margin-right: 8px;
}

.vip-charge-list .wechat-icon svg {
  width: 100%;
  height: 100%;
}

.vip-charge-list .payment-name {
  font-size: 14px;
  line-height: 24px;
  color: #2b3330;
}

.vip-charge-list .pay-form {
  position: absolute;
  right: 0;
  bottom: 0;
}

.vip-charge-list .pay-btn {
  position: static;
  min-width: 120px;
  height: 40px;
  background-color: #76a33c !important;
  border-color: #76a33c !important;
}

.vip-charge-list .pay-btn:hover {
  background-color: #689435 !important;
  border-color: #689435 !important;
}

.vip-charge-list .notes-item {
  display: block;
}

.vip-charge-list .notes-right {
  position: static;
}

.vip-charge-list .notes-list {
  margin: 8px 0 0;
  padding-left: 1.5em;
  font-size: 14px;
  line-height: 24px;
  color: #67716c;
}

.vip-charge-list .notes-list li + li {
  margin-top: 8px;
}
</style>
