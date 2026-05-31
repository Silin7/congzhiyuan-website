import { ref } from 'vue'
import axios from 'axios'
import { baseURL } from '@/api/baseConfig'
import { ElMessage } from 'element-plus'
import { useRoute } from 'vue-router'

// 登录注册 - 验证码
// a.phone: 手机号
// b.type:发送类型 1 注册登录二合一 2 重置密码
export function authcodeApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=SmsSend`, params, {
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
    },
  })
}

// 登录或注册二合一
// a.usercode: 登录名（手机号码或卡号）
// b.vfCode: 验证码
// c.type:验证码类型 1 短信 2 密码
export async function loginOrRegisterApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=SignIn`, params)
    if (res.data.code === 0) {
      return res.data
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 用户退出
export async function signOutApi() {
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=SignOut`, {}, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 手机用户设置密码
// a.token:用户token，必选
// a.newPass:新密码
// d.vfCode: 手机验证码(重置密码)
export async function passResetApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=PassReset`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 用户修改密码
// a.token:用户token，必选
// b.oldPass:旧密码
// c.newPass:新密码
export async function passModiApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=VfCodeModi`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 上部导航栏显示查询
export function navQueryApi() {
  return axios.post(`${baseURL}/?ctl=ajax&mod=homePage&act=NavigationQuery`, {
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
    },
  })
}

// 首页上部显示查询
// a.provice:省份
export function topInfoApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=homePage&act=TopInfo`, params, {
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
    },
  })
}

// 首页下部操作指南二维码查询
export function qrPicInfoListApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  return axios.post(`${baseURL}/?ctl=ajax&mod=homePage&act=QrPicInfoList`, params, {
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
    },
  })
}

// 志愿填报页批次查询
// a.token:用户token，必选
// b.ccdm:  1 本科 2 专科
export async function pcListApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=PcList`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 志愿填报页投档单位查询
// a.token:用户token，必选
// b.ccdm:  1 本科 2 专科
// c.pcdm: 批次代码
export async function tddwListApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=TddwList`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 通用复选框列表查询
// a.token:用户token，必选
// b.genType 查询类型字段（yxxz:院校性质prov:省份 yxts:院校特色zyts:专业特色 sfbz:收费标准）
export async function genListQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=GenListQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 名称模糊查询院校列表
// a.token: 用户token，必选
// b.yxmc：院校名称文字
export async function yxqueryBymcApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=YxqueryBymc`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 名称模糊查询专业列表
// a.token:用户token，必选
// c.zymc:专业名称
export async function zyqueryBymcApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=ZyqueryBymc`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 学科门类查询
// a.token: 用户token，必选
// c.ccdm 层次 1 本科 2 专科
export async function xkmllistApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=Xkmllist`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 一级学科查询
// a.token:用户token，必选
// b.xkml:学科门类代码
export async function yjxklistApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=Yjxklist`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 二级学科查询
// c.token:用户token，必选
// d.yjxk:一级学科代码
export async function ejxklistApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=Ejxklist`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
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
export async function lqInfoZyQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=LqInfoZyQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
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
export async function lqInfoZyGroupQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=LqInfoZyGroupQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 单个志愿填报
// a.token:用户token，必选
// d.zyId 要收藏的志愿id
// e.lqdc 录取档次
// f.lqbl 录取比例
export async function myChioesAddApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=MyChioesAdd`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 批量志愿填报
// a.token:用户token，必选
// g.jsonStr: json字符串，格式{"Rs":[{"zyid":2926,"lqbl":0.131,"lqdc":4}]}
export async function myChioesBatchAddApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=MyChioesBatchAdd`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 志愿分组查询 - 志愿填报页面
// a.token:用户token，必选
// b.ccdm  1 本科 2 专科
// c.pcdm 批次代码
export async function myChioesGroupQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=MyChoicesGroupQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 志愿分组列表查询 - 个人中心（我的志愿单）
// a.token:用户token，必选
export async function myChGroupSListApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=MyChGroupSList`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 专业模式志愿列表查询
// c.token:用户token，必选
// d.chGroupId 我的收藏组id
export async function zyChoicesQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=ZyChoicesQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 专业组模式志愿列表查询
// a.token:用户token，必选
// b.chGroupId 我的收藏组id
export async function zyGroupChoicesQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=ZyGroupChoicesQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 删除收藏专业
// a.token:用户token，必选
// b.chId 要删除的专业id
export async function delChoiceApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=DelChoice`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 删除收藏专业组
// a.token:用户token，必选
// b.chZyGroupId 要删除的分组id
export async function delChoiceGroupApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=DelChoiceGroup`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 个人信息查询
// a.token:用户token，必选
export async function myuserInfoQueryApi() {
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=user&act=MyuserInfoQuery`, {}, {
      headers: {
        'Authorization': `Bearer ${useRoute().query.sessncode || localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data || {}
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 考生可选省份查询
// a.token:用户token，必选
export async function userProvQueryApi() {
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=user&act=UserProvQuery`, {}, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      // ElMessage.error(res.data.message || '请求失败')
      console.error('res.data.code !== 0 -------->', res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 考生省份保存
// a.token:用户token，必选
export async function myUserPorvSaveApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=user&act=MyUserPorvSave`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// tips: wctype 用户信息返回int 此接口返回char
// 考生类别查询
// b.token: 用户token，必选
// c.province 省份
export async function WctypeQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=user&act=WctypeQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}


// 考试类别小类查询
// c.token:用户token，必选
// d.wctype 考试类别代码为2时才有数据
export async function yklmQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=user&act=YklmQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
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
export async function myUserInfoSaveApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=user&act=MyUserInfoSave`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 输入分数查询位次查询
// a.token:用户token，必选
// b.cj 分数
// c.wctype 考试类别
// d.yklm 用户为艺术类时的小类,可为空
export async function wcQueryBycjApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=user&act=WcQueryBycj`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 专业模式志愿专业排序
// a.token:用户token，必选
// b.jsonStr 接收排序参数，格式如{"Rs":[{"id":226,"xh":4}]}
export async function ZyChoiceSortApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=ZyChoiceSort`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 专业模式志愿专业导出Excel
// a.token:用户token，必选
// b.chGroupId 要导出的分组id
export async function ZyChoiceExportExcelApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=ZyChoiceExportExcel`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 院校列表查询
// a.ccdm：层次 1本科 2专科，单选
// b.yxmc: 院校名称
// c.genList 通用列表项查询字段拼接字符串, 格式{ "Rs": [{ "id": 1, "genType": "prov" }] } 用来传院校省份
// d.startrow: 开始页
// e.pagesize: 每页行数
export async function YxListQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=YxListQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 院校详情查询
// a.yxid: 院校id，必选
export async function YxDetailsQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=YxDetailsQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 专业库专业层次查询
export async function ZyCcQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=ZyCcQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 专业库专业层次查询
// a.ccdm：层次代码
export async function ZyListQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=ZyListQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 专业详情查询
// a.zydm:专业列表查询对应的id
export async function ZyDetailsQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=gen&act=ZyDetailsQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 测评列表查询
// a.token
export async function scalesListQueryApi() {
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=ass&act=scalesListQuery`, {}, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 测评详情查询
// a.token
export async function scaleDetailsQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=ass&act=scaleDetailsQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 开始测评
// a.token
export async function scaleStartApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=ass&act=scaleStart`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 提交测评
// a.token：
// b.asId  本次测评记录id
// c.answerJson: 本次测评情况，格式如
// [{ "questionId": 1, "answerNum": 2 }, { "questionId": 2, "answerNum": 3 }]
// answerNum是用户答题序号
export async function scaleSaveApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=ass&act=scaleSave`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 测评记录查询
// a.token
export async function assListQueryApi() {
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=ass&act=assListQuery`, {}, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 测评详情查询
// a.token
export async function assDetailQueryApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=ass&act=assDetailQuery`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}

// 志愿按录取比例自动排序
export async function choicesSortBylqblApi(data: any) {
  const params = new FormData()
  Object.keys(data).forEach(key => {
    params.append(key, data[key])
  })
  try {
    const res = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=choicesSortBylqbl`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      },
    })
    if (res.data.code === 0) {
      return res.data
    } else if (res.data.code === -998) {
      useDebounce(tokenLose)
    } else {
      ElMessage.error(res.data.message || '请求失败')
    }
  } catch (error: any) {
    console.error('error -------->', error)
    ElMessage.error('请求失败')
  }
}


// token失效处理
function tokenLose() {
  ElMessage.error('请登录后操作')
  setTimeout(() => {
    window.location.href = '/'
  }, 1000)
  window.localStorage.removeItem('token')
  window.localStorage.removeItem('userInfo')
  // window.localStorage.removeItem('selectedSchoolLevel')
  // window.localStorage.removeItem('selectedAdmissionBatch')
  // window.localStorage.removeItem('selectedAdmissionType')
  // window.localStorage.removeItem('selectedSchoolNature')
  // window.localStorage.removeItem('selectedMajorFeature')
  // window.localStorage.removeItem('selectedProvince')
  // window.localStorage.removeItem('selectedRiskLevel')
  // window.localStorage.removeItem('riskThreshold')
  // window.localStorage.removeItem('safeThreshold')
}

// 防抖函数
const timeout: any = ref(null)
function useDebounce(fn: any, wait?: number) {
  if (timeout.value !== null) {
    clearTimeout(timeout.value)
  }
  timeout.value = setTimeout(fn, wait || 200)
}