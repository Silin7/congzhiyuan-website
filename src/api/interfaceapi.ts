import api from '@/api/index'

export function testApi(data: any) {
  return api.post('/?ctl=ajax&act=SmsSend&mod=gen', data)
}

// 登录注册 - 验证码
// a.phone: 手机号
// b.type:发送类型 1 注册登录二合一 2 重置密码
export function authcodeApi(data: any) {
  return api.post('/mod/gen/SmsSend.ajax.php', data)
}

// 登录或注册二合一
// a.usercode: 登录名（手机号码或卡号）
// b.vfCode: 验证码
// c.type:验证码类型 1 短信 2 密码
export function loginOrRegisterApi(data: any) {
  return api.post('/mod/gen/SignIn.ajax.php', data)
}

// 退出登录
export function signOutApi() {
  return api.post('/mod/gen/SignOut.ajax.php')
}

// 手机用户设置密码
// a.token:用户token，必选
// a.newPass:新密码
// d.vfCode: 手机验证码(重置密码)
export function passResetApi(data: any) {
  return api.post('/mod/gen/PassReset.ajax.php', data)
}

// 用户修改密码
// a.token:用户token，必选
// b.oldPass:旧密码
// c.newPass:新密码
export function passModiApi(data: any) {
  return api.post('/mod/gen/VfCodeModi.ajax.php', data)
}

// Tip: 返回数据无路由path name
// 上部导航栏显示查询
export function navQueryApi() {
  return api.post('/mod/homePage/NavigationQuery.ajax.php')
}

// 首页上部显示查询
// a.provice:省份
export function topInfoApi(data: any) {
  return api.post('/mod/homePage/TopInfo.ajax.php', data)
}

// 志愿填报页批次查询
// a.token:用户token，必选
// b.ccdm:  1 本科 2 专科
export function pcListApi(data: any) {
  return api.post('/mod/zhiYuan/PcList.ajax.php', data)
}

// 志愿填报页投档单位查询
// a.token:用户token，必选
// b.ccdm:  1 本科 2 专科
// c.pcdm: 批次代码
export function tddwListApi(data: any) {
  return api.post('/mod/zhiYuan/TddwList.ajax.php', data)
}

// Tip： 返回空数组
// 通用复选框列表查询
// a.token:用户token，必选
// b.genType 查询类型字段（yxxz:院校性质prov:省份 yxts:院校特色zyts:专业特色）
export function genListQueryApi(data: any) {
  return api.post('/mod/zhiYuan/genListQuery.ajax.php', data)
}

// 名称模糊查询院校列表
// a.token: 用户token，必选
// b.yxmc：院校名称文字
export function yxqueryBymcApi(data: any) {
  return api.post('/mod/zhiYuan/YxqueryBymc.ajax.php', data)
}

// Tip:有的专业没有value
// 名称模糊查询专业列表
// a.token:用户token，必选
// c.zymc:专业名称
export function zyqueryBymcApi(data: any) {
  return api.post('/mod/zhiYuan/ZyqueryBymc.ajax.php', data)
}

// 学科门类查询
// a.token: 用户token，必选
// c.ccdm 层次 1 本科 2 专科
export function xkmllistApi(data: any) {
  return api.post('/mod/zhiYuan/Xkmllist.ajax.php', data)
}

// 一级学科查询
// a.token:用户token，必选
// b.xkml:学科门类代码
export function yjxklistApi(data: any) {
  return api.post('/mod/zhiYuan/Yjxklist.ajax.php', data)
}

// 二级学科查询
// c.token:用户token，必选
// d.yjxk:一级学科代码
export function ejxklistApi(data: any) {
  return api.post('/mod/zhiYuan/Ejxklist.ajax.php', data)
}

// Tip: 未开发
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
  return api.post('/mod/zhiYuan/LqInfoZyQuery.ajax.php', data)
}

// Tip: 未开发
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
  return api.post('/mod/zhiYuan/LqInfoZyGroupQuery.ajax.php', data)
}

// Tip: 未开发
// 单个志愿填报
// a.token:用户token，必选
// d.zyId 要收藏的志愿id
// e.lqdc 录取档次
// f.lqbl 录取比例
export function myChioesAddApi(data: any) {
  return api.post('/mod/zhiYuan/MyChioesAdd.ajax.php', data)
}

// Tip: 未开发
// 批量志愿填报
// a.token:用户token，必选
// g.jsonStr: json字符串，格式{"Rs":[{"zyid":2926,"lqbl":0.131,"lqdc":4}]}
export function myChioesBatchAddApi(data: any) {
  return api.post('/mod/zhiYuan/MyChioesBatchAdd.ajax.php', data)
}

// 志愿分组查询
// a.token:用户token，必选
// b.ccdm  1 本科 2 专科 99全部
export function myChioesGroupQueryApi(data: any) {
  return api.post('/mod/zhiYuan/MyChoicesGroupQuery.ajax.php', data)
}

// Tip: 未开发
// 专业模式收藏查询
// c.token:用户token，必选
// d.chGroupId 我的收藏组id
export function zyChoicesQueryApi(data: any) {
  return api.post('/mod/zhiYuan/ZyChoicesQuery.ajax.php', data)
}

// Tip: 未开发
// 专业组模式收藏查询
// a.token:用户token，必选
// b.chGroupId 我的收藏组id
export function zyGroupChoicesQueryApi(data: any) {
  return api.post('/mod/zhiYuan/ZyGroupChoicesQuery.ajax.php', data)
}

// 删除收藏专业
// a.token:用户token，必选
// b.chId 要删除的专业id
export function delChoiceApi(data: any) {
  return api.post('/mod/zhiYuan/DelChoice.ajax.php', data)
}

// Tip: 未开发
// 删除收藏专业组
// a.token:用户token，必选
// b.chZyGroupId 要删除的分组id
export function delChoiceGroupApi(data: any) {
  return api.post('/mod/zhiYuan/DelChoiceGroup.ajax.php', data)
}

// Tip: xuankeStr物理,化学，生物 逗号分割
// 个人信息查询
// a.token:用户token，必选
export function myuserInfoQueryApi(data: any) {
  return api.post('/mod/user/MyuserInfoQuery.ajax.php', data)
}

// 考试类别小类查询
// c.token:用户token，必选
// d.wctype 考试类别代码为2时才有数据
export function yklmQueryApi(data: any) {
  return api.post('/mod/user/YklmQuery.ajax.php', data)
}

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
  return api.post('/mod/user/MyUserInfoSave.ajax.php', data)
}

// 输入分数查询位次查询
// a.token:用户token，必选
// b.cj 分数
// c.wctype 考试类别
// d.yklm 用户为艺术类时的小类,可为空
export function wcQueryBycjApi(data: any) {
  return api.post('/mod/user/WcQueryBycj.ajax.php', data)
}
