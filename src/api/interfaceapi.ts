import axios from 'axios'
import { ref } from 'vue'
import router from '@/router'
import { baseURL } from '@/api/baseConfig'
import { ElMessage } from 'element-plus'

// 登录注册 - 验证码
// a.phone: 手机号
// b.type:发送类型 1 注册登录二合一 2 重置密码
export function authcodeApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=SmsSend`, params)
}

// 登录或注册二合一
// a.usercode: 登录名（手机号码或卡号）
// b.vfCode: 验证码
// c.type:验证码类型 1 短信 2 密码
export function loginOrRegisterApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=SignIn`, params)
}

// 用户退出
export function signOutApi() {
  return axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=SignOut`)
}

// 手机用户设置密码
// a.token:用户token，必选
// a.newPass:新密码
// d.vfCode: 手机验证码(重置密码)
export function passResetApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=PassReset`, params)
}

// 用户修改密码
// a.token:用户token，必选
// b.oldPass:旧密码
// c.newPass:新密码
export function passModiApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=VfCodeModi`, params)
}

// 上部导航栏显示查询
export function navQueryApi() {
  return axios.post(`${baseURL}/?ctl=ajax&mod=homePage&act=NavigationQuery`)
}

// 首页上部显示查询
// a.provice:省份
export function topInfoApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=homePage&act=TopInfo`, params)
}

// 志愿填报页批次查询
// a.token:用户token，必选
// b.ccdm:  1 本科 2 专科
export function pcListApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=PcList`, params)
}

// 志愿填报页投档单位查询
// a.token:用户token，必选
// b.ccdm:  1 本科 2 专科
// c.pcdm: 批次代码
export function tddwListApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=TddwList`, params)
}

// 通用复选框列表查询
// a.token:用户token，必选
// b.genType 查询类型字段（yxxz:院校性质prov:省份 yxts:院校特色zyts:专业特色）
export async function genListQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  // try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=GenListQuery`, params)
    return res
  //   if (res.data.code === 0) {
  //     return res.data
  //   } else if (res.data.code === -998) {
  //     useDebounce(tokenLose)
  //   } else {
  //     ElMessage.error(res.data.Message || '请求失败')
  //   }
  // } catch (error: any) {
  //   console.error('error -------->', error)
  //   ElMessage.error('请求失败')
  // }
}

// 名称模糊查询院校列表
// a.token: 用户token，必选
// b.yxmc：院校名称文字
export function yxqueryBymcApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=YxqueryBymc`, params)
}

// 名称模糊查询专业列表
// a.token:用户token，必选
// c.zymc:专业名称
export function zyqueryBymcApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=ZyqueryBymc`, params)
}

// 学科门类查询
// a.token: 用户token，必选
// c.ccdm 层次 1 本科 2 专科
export function xkmllistApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=Xkmllist`, params)
}

// 一级学科查询
// a.token:用户token，必选
// b.xkml:学科门类代码
export function yjxklistApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=Yjxklist`, params)
}

// 二级学科查询
// c.token:用户token，必选
// d.yjxk:一级学科代码
export function ejxklistApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=Ejxklist`, params)
}

// 专业模式志愿查询
// a.token:用户token，必选
// b.ccdm：层次 1本科 2专科，单选
// c.pcdm 批次代码，多选
// d.tddw 投档单位代码,多选
// e.yxxz 院校性质,单选
// f.yxid  院校id
// g.genList通用列表项查询字段拼接字符串,格式{"Rs":[{"id":11,"genType":"yxxz"},{"id":23,"genType":"yxxz"}]}
// h.zydm 专业代码，逗号分割字符串(比如010101,010103)
// i.lqdc  录取档次 4冲 3保 2 稳 -2 新增
// j.startrow: 开始页
// k.pagesize: 每页行数
// l.progressBao 比例（0-100）
// m.progressChong 比例（0-100）
export function lqInfoZyQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=LqInfoZyQuery`, params)
}

// 专业组模式志愿查询
// a.token:用户token，必选
// b.ccdm：层次 1本科 2专科，单选
// c.pcdm 批次代码，多选
// d.tddw 投档单位代码,多选
// e.yxxz 院校性质,单选
// f.yxid  院校id
// g.genList通用列表项查询字段拼接字符串,格式{"Rs":[{"id":11,"genType":"yxxz"},{"id":23,"genType":"yxxz"}]}
// h.zydm 专业代码，逗号分割字符串
// i.lqdc  录取档次 4冲 3保 2 稳 -2 新增
// j.startrow: 开始页
// k.pagesize: 每页行数
// l.progressBao 比例（0-100）
// m.progressChong 比例（0-100）
export function lqInfoZyGroupQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=LqInfoZyGroupQuery`, params)
}

// 单个志愿填报
// a.token:用户token，必选
// d.zyId 要收藏的志愿id
// e.lqdc 录取档次
// f.lqbl 录取比例
export function myChioesAddApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=MyChioesAdd`, params)
}

// 批量志愿填报
// a.token:用户token，必选
// g.jsonStr: json字符串，格式{"Rs":[{"zyid":2926,"lqbl":0.131,"lqdc":4}]}
export function myChioesBatchAddApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=MyChioesBatchAdd`, params)
}

// 志愿分组查询
// a.token:用户token，必选
// b.ccdm  1 本科 2 专科 99全部
export function myChioesGroupQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=MyChoicesGroupQuery`, params)
}

// 专业模式收藏查询
// c.token:用户token，必选
// d.chGroupId 我的收藏组id
export function zyChoicesQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=ZyChoicesQuery`, params)
}

// 专业组模式收藏查询
// a.token:用户token，必选
// b.chGroupId 我的收藏组id
export function zyGroupChoicesQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=ZyGroupChoicesQuery`, params)
}

// 删除收藏专业
// a.token:用户token，必选
// b.chId 要删除的专业id
export function delChoiceApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=DelChoice`, params)
}

// 删除收藏专业组
// a.token:用户token，必选
// b.chZyGroupId 要删除的分组id
export function delChoiceGroupApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=DelChoiceGroup`, params)
}

// 个人信息查询
// a.token:用户token，必选
export function myuserInfoQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=user&act=MyuserInfoQuery`, params)
}

// 考生可选省份查询
// a.token:用户token，必选
export function userProvQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=user&act=UserProvQuery`, params)
}


// tips: wctype 用户信息返回int 此接口返回char
// 考生类别查询
// b.token: 用户token，必选
// c.province 省份
export function WctypeQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=user&act=WctypeQuery`, params)
}


// 考试类别小类查询
// c.token:用户token，必选
// d.wctype 考试类别代码为2时才有数据
export function yklmQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=user&act=YklmQuery`, params)
}

// tips: xuankeStr 保存用字母，查询返回文字
// 个人信息保存
// 1.传入参数：
// a.token:用户token，必选
// a.userName : 昵称
// e.province : 省份
// f.phone：手机号
// g.sex 1男 2 女
// h.wctype 用户考试类别
// i.yklm 用户为艺术类时的小类
// j.cj  分数
// k.wc  位次
// l.xkkm  逗号分割选科字符传,物理A化学B生物C历史D地理E政治F
export function myUserInfoSaveApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=user&act=MyUserInfoSave`, params)
}

// 输入分数查询位次查询
// a.token:用户token，必选
// b.cj 分数
// c.wctype 考试类别
// d.yklm 用户为艺术类时的小类,可为空
export function wcQueryBycjApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=user&act=WcQueryBycj`, params)
}

// token失效处理
function tokenLose() {
  router.push({ path: '/' })
  ElMessage.error('用户信息失效,请重新登录')
  window.localStorage.removeItem('token')
  window.localStorage.removeItem('userInfo')
}

const timeout: any = ref(null)

function useDebounce(fn: any, wait?: number) {
  if (timeout.value !== null) {
    clearTimeout(timeout.value)
  }
  timeout.value = setTimeout(fn, wait || 1000)
}