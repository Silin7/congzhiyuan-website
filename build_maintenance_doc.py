# -*- coding: utf-8 -*-
"""
Generate a comprehensive, professional Project Maintenance Manual (.docx) for CongZhiYuan AI Website.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    """Set background color of a table cell."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner padding of a cell in dxa (1 pt = 20 dxa)."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_callout_border(cell, border_color="0284C7"):
    """Set a thick left border and clear other borders for callout."""
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="36" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)

def set_table_borders(table, border_color="CBD5E1"):
    """Set subtle gray borders for data table."""
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(f'''
            <w:tblBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="6" w:space="0" w:color="{border_color}"/>
                <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{border_color}"/>
                <w:left w:val="none"/>
                <w:right w:val="none"/>
                <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>
                <w:insideV w:val="none"/>
            </w:tblBorders>
        ''')
        tblPr[0].append(borders)

def add_styled_paragraph(doc, text, style='Normal', space_before=0, space_after=6, line_spacing=1.2, font_name="微软雅黑", font_size=10, font_color=RGBColor(51, 65, 85), bold=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    run = p.add_run(text)
    run.font.name = font_name
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)
    run.font.size = Pt(font_size)
    run.font.color.rgb = font_color
    run.bold = bold
    return p

def add_code_block(doc, code_text):
    """Add a monospace styled code box."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.0)
    set_cell_background(cell, "0F172A") # Deep dark background
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    
    # Border
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="334155"/>
            <w:left w:val="single" w:sz="4" w:space="0" w:color="334155"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="334155"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="334155"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(code_text)
    run.font.name = "Consolas"
    run._element.rPr.rFonts.set(qn('w:eastAsia'), "Consolas")
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(226, 232, 240)
    
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(4)

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "微软雅黑"
    run._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    run.font.size = Pt(15)
    run.font.color.rgb = RGBColor(15, 23, 42) # Slate 900
    run.bold = True
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "微软雅黑"
    run._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    run.font.size = Pt(12.5)
    run.font.color.rgb = RGBColor(30, 64, 175) # Blue 800
    run.bold = True
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "微软雅黑"
    run._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(71, 85, 105) # Slate 600
    run.bold = True
    return p

def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.2
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "微软雅黑"
        r_pre._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
        r_pre.font.size = Pt(9.5)
        r_pre.font.color.rgb = RGBColor(15, 23, 42)
        r_pre.bold = True
    run = p.add_run(text)
    run.font.name = "微软雅黑"
    run._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(51, 65, 85)
    return p

def add_callout(doc, text, title="运维提示", callout_type="note"):
    """Add a professional styled callout box."""
    colors = {
        "note": {"bg": "F0F9FF", "border": "0284C7", "title_color": RGBColor(2, 132, 199)},
        "tip": {"bg": "F0FDF4", "border": "16A34A", "title_color": RGBColor(22, 163, 74)},
        "warning": {"bg": "FEF2F2", "border": "E11D48", "title_color": RGBColor(225, 29, 72)},
    }
    cfg = colors.get(callout_type, colors["note"])
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.0)
    set_cell_background(cell, cfg["bg"])
    set_callout_border(cell, cfg["border"])
    set_cell_margins(cell, top=120, bottom=120, left=180, right=160)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    run_t = p.add_run(f"【{title}】")
    run_t.font.name = "微软雅黑"
    run_t._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    run_t.font.size = Pt(10)
    run_t.font.color.rgb = cfg["title_color"]
    run_t.bold = True
    
    p_body = cell.add_paragraph()
    p_body.paragraph_format.space_before = Pt(0)
    p_body.paragraph_format.space_after = Pt(2)
    p_body.paragraph_format.line_spacing = 1.2
    run_b = p_body.add_run(text)
    run_b.font.name = "微软雅黑"
    run_b._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    run_b.font.size = Pt(9)
    run_b.font.color.rgb = RGBColor(51, 65, 85)
    
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(4)

def create_styled_table(doc, headers, rows_data, col_widths=None):
    """Create a beautiful formatted table."""
    table = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = ""
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(h)
        run.font.name = "微软雅黑"
        run._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.bold = True
        set_cell_background(hdr_cells[i], "1E3A8A")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=120, right=120)
        if col_widths and i < len(col_widths):
            hdr_cells[i].width = col_widths[i]
            
    for r_idx, r_data in enumerate(rows_data):
        row_cells = table.rows[r_idx + 1].cells
        bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            row_cells[c_idx].text = ""
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            run = p.add_run(str(val))
            run.font.name = "微软雅黑"
            run._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(51, 65, 85)
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=120, right=120)
            if col_widths and c_idx < len(col_widths):
                row_cells[c_idx].width = col_widths[c_idx]

    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(2)
    p_space.paragraph_format.space_after = Pt(6)

def generate_maintenance_manual():
    doc = docx.Document()
    
    # Page Margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2.2)
        section.bottom_margin = Cm(2.2)
        section.left_margin = Cm(2.2)
        section.right_margin = Cm(2.2)
        
        # Header & Footer
        header = section.header
        p_head = header.paragraphs[0]
        p_head.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_head = p_head.add_run("聪志愿AI · 项目技术维护与部署手册")
        r_head.font.name = "微软雅黑"
        r_head._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
        r_head.font.size = Pt(8.5)
        r_head.font.color.rgb = RGBColor(148, 163, 184)
        
        footer = section.footer
        p_foot = footer.paragraphs[0]
        p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_foot = p_foot.add_run("第 - ")
        fldSimple = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
        p_foot._element.append(fldSimple)
        r_foot2 = p_foot.add_run(" - 页")
        for r in [r_foot, r_foot2]:
            r.font.name = "微软雅黑"
            r._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
            r.font.size = Pt(8.5)
            r.font.color.rgb = RGBColor(148, 163, 184)

    # -------------------------------------------------------------
    # COVER PAGE
    # -------------------------------------------------------------
    p_cov_space = doc.add_paragraph()
    p_cov_space.paragraph_format.space_before = Pt(40)
    
    p_tag = doc.add_paragraph()
    p_tag.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_tag = p_tag.add_run("【前端工程化 · 架构与运维技术规范】")
    r_tag.font.name = "微软雅黑"
    r_tag._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    r_tag.font.size = Pt(12)
    r_tag.font.color.rgb = RGBColor(14, 116, 144)
    r_tag.bold = True
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(12)
    r_title = p_title.add_run("聪志愿 AI 智能志愿填报系统\n项目技术维护与部署手册")
    r_title.font.name = "微软雅黑"
    r_title._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    r_title.font.size = Pt(26)
    r_title.font.color.rgb = RGBColor(15, 23, 42)
    r_title.bold = True
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(30)
    r_sub = p_sub.add_run("技术栈全解、Node/pnpm版本基线、多环境配置切换、打包编译与服务器部署完整指南")
    r_sub.font.name = "微软雅黑"
    r_sub._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    r_sub.font.size = Pt(11.5)
    r_sub.font.color.rgb = RGBColor(71, 85, 105)
    
    meta_table = doc.add_table(rows=6, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("项目工程名称", "congzhiyuan-website"),
        ("核心技术体系", "Vue 3.5 + TypeScript 5.8 + Vite 6.x + Pinia 3.x"),
        ("运行基线规范", "Node.js >= 18.x (推荐 20.x/22.x LTS, 实测 25.x) | pnpm >= 8.x/10.x"),
        ("开发服务端口", "http://localhost:3010 (host: 0.0.0.0, open: true)"),
        ("生产部署环境", "Microsoft-IIS 8.5 / Nginx 静态托管 | Hash 路由驱动"),
        ("编制日期 / 版本", "2026年9月 · 研发运维正式版 V1.0")
    ]
    for idx, (k, v) in enumerate(meta_data):
        row = meta_table.rows[idx]
        cell_k, cell_v = row.cells[0], row.cells[1]
        cell_k.width = Inches(1.8)
        cell_v.width = Inches(4.2)
        set_cell_background(cell_k, "F1F5F9")
        set_cell_background(cell_v, "FFFFFF")
        set_cell_margins(cell_k, top=70, bottom=70, left=100, right=100)
        set_cell_margins(cell_v, top=70, bottom=70, left=100, right=100)
        
        p_k = cell_k.paragraphs[0]
        r_k = p_k.add_run(k)
        r_k.font.name = "微软雅黑"
        r_k._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
        r_k.font.size = Pt(9.5)
        r_k.bold = True
        r_k.font.color.rgb = RGBColor(15, 23, 42)
        
        p_v = cell_v.paragraphs[0]
        r_v = p_v.add_run(v)
        r_v.font.name = "微软雅黑"
        r_v._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
        r_v.font.size = Pt(9.5)
        r_v.font.color.rgb = RGBColor(51, 65, 85)
    
    set_table_borders(meta_table, "CBD5E1")
    doc.add_page_break()

    # -------------------------------------------------------------
    # SECTION 1: PROJECT ARCHITECTURE & TECH STACK
    # -------------------------------------------------------------
    add_heading_1(doc, "第一章：项目架构与技术栈全景")
    add_styled_paragraph(doc, "“聪志愿AI”前端工程（`congzhiyuan-website`）基于现代前端工程化标准构建，采用组件化、响应式与强类型设计。系统具备毫秒级冷启动、极速热模块更新（HMR）、轻量级状态管理以及完善的 TypeScript 类型推导支持。")
    
    add_heading_2(doc, "1.1 核心驱动技术栈")
    tech_headers = ["技术维度", "采用框架 / 库", "当前版本", "核心作用与选型理由"]
    tech_data = [
        ["前端框架", "Vue 3", "^3.5.13", "基于 Composition API（`<script setup>`），性能卓越，内存占用极低"],
        ["开发与构建工具", "Vite", "^6.2.4 / 6.3.5", "基于原生 ESM，冷启动极速，基于 Rollup 进行高效生产打包"],
        ["编程语言", "TypeScript", "~5.8.0", "强类型保障，与 Vue 3 深度集成，提供严谨的编译期接口契约"],
        ["状态管理", "Pinia", "^3.0.1", "Vue 3 官方推荐状态库，轻量直观，天然支持完整 TypeScript 自动补全"],
        ["路由管理", "Vue Router", "^4.5.0", "采用 Hash 模式（`createWebHashHistory`），具备极高的静态托管兼容性"],
        ["UI 组件库", "Element Plus", "^2.10.1", "成熟的企业级组件生态，表格、弹窗、表单、分页一站式开箱即用"],
        ["CSS 预编译", "Sass / SCSS", "^1.89.2", "样式变量化与模块化，支持嵌套语法与组件内独立样式隔离"]
    ]
    create_styled_table(doc, tech_headers, tech_data, [Inches(1.1), Inches(1.3), Inches(1.1), Inches(2.5)])

    add_heading_2(doc, "1.2 生产依赖插件清单全解析（Dependencies）")
    plugin_headers = ["依赖包名", "版本", "功能说明与主要应用场景"]
    plugin_data = [
        ["axios", "^1.9.0", "基于 Promise 的网络请求库，统一封装拦截器、Bearer Token 鉴权与表单提交"],
        ["dayjs", "^1.11.13", "轻量级日期时间处理库，用于测评时间、高考倒计时及信息修改时间戳格式化"],
        ["echarts", "^5.6.0", "百度开源可视化图表库，用于院校历年录取位次走势图、分数线分布图与雷达图展示"],
        ["sortablejs", "^1.15.6", "现代拖拽排序原生核心库，用于个人中心【我的志愿单】表格行自由拖动调序"],
        ["vuedraggable", "^2.24.3", "基于 Sortable.js 的 Vue 封装指令，实现志愿列表双向绑定拖拽排序"],
        ["@iconify/vue", "^5.0.0", "海量图标组件集合，用于志愿填报页面各类状态图标渲染"],
        ["@element-plus/icons-vue", "^2.3.1", "Element Plus 官方配套图标集（UserFilled、Right 等通用操作图标）"],
        ["font-awesome", "^4.7.0", "传统经典矢量图标字体库，提供通用界面微修饰图标"],
        ["@wangeditor/editor", "^5.1.23", "开箱即用的国内开源富文本编辑器，用于资讯公告、志愿填报说明编辑与渲染"],
        ["@wangeditor/editor-for-vue", "^5.1.12", "WangEditor 的 Vue 3 官方组件适配层"],
        ["qrcode", "^1.5.4", "二维码生成库，用于首页客服微信、志愿咨询群及扫码支付二维码动态绘制"],
        ["vue3-seamless-scroll", "^3.0.2", "平滑无缝滚动跑马灯组件，用于首页高校录取喜报、系统动态滚动播报"],
        ["mitt", "^3.0.1", "极其微小的事件总线（Event Bus），用于跨组件非父子级事件派发（如用户信息全局更新）"],
        ["@vueuse/head", "^2.0.0", "Vue 3 页面 Head 管理库，用于动态调整各路由页面的 Title 与 Meta 标签优化 SEO"]
    ]
    create_styled_table(doc, plugin_headers, plugin_data, [Inches(1.8), Inches(0.9), Inches(3.3)])

    add_heading_2(doc, "1.3 开发依赖工具（DevDependencies）")
    dev_headers = ["工具名称", "版本", "职责说明"]
    dev_data = [
        ["vue-tsc", "^2.2.8", "针对 Vue SFC 单文件组件的命令行 TypeScript 类型检查器，构建前校验类型安全"],
        ["prettier", "3.5.3", "代码风格自动化格式化程序，保障团队协同编码规范统一"],
        ["npm-run-all2", "^7.0.2", "跨平台 CLI 任务编排工具，实现 `type-check` 与 `build-only` 并行高效构建"],
        ["@tsconfig/node22", "^22.0.1", "Node.js 22 LTS 推荐编译选项基线规范"],
        ["@types/node", "^22.14.0", "Node.js 运行时环境 TypeScript 类型定义文件"]
    ]
    create_styled_table(doc, dev_headers, dev_data, [Inches(1.6), Inches(0.9), Inches(3.5)])

    # -------------------------------------------------------------
    # SECTION 2: ENVIRONMENT BASELINE
    # -------------------------------------------------------------
    add_heading_1(doc, "第二章：运行环境与版本基线要求")
    add_styled_paragraph(doc, "为确保团队成员本地开发、自动化构建服务器（CI/CD）以及生产环境的一致性，请严格遵守以下环境基线标准：")
    
    env_headers = ["环境要素", "官方推荐规范", "最低兼容下限", "当前实机验证版本", "验证命令"]
    env_data = [
        ["操作系统", "Windows 10/11 64位 / macOS / Linux", "Windows 10 64位", "Windows 10 Pro 64-bit", "systeminfo"],
        ["Node.js", "v20.x / v22.x (LTS 稳定版)", "Node.js >= 18.18.0", "v25.1.0", "node -v"],
        ["包管理器", "pnpm >= 9.x / 10.x", "pnpm >= 8.0.0", "pnpm 10.32.1", "pnpm -v"],
        ["依赖锁文件", "严格使用 pnpm-lock.yaml", "——", "pnpm-lock.yaml", "git status"]
    ]
    create_styled_table(doc, env_headers, env_data, [Inches(1.1), Inches(1.5), Inches(1.3), Inches(1.1), Inches(1.0)])

    add_callout(doc, "本工程强制要求使用 pnpm 作为唯一包管理器，严禁混合使用 npm 或 yarn 执行安装！混合使用会导致 node_modules 目录结构混乱，破坏 pnpm 的硬链接与符号链接机制，引发“幽灵依赖”甚至构建打包崩溃。", title="高危禁令：严禁使用 npm / yarn", callout_type="warning")

    # -------------------------------------------------------------
    # SECTION 3: INSTALL & RUN LOCAL DEV
    # -------------------------------------------------------------
    add_heading_1(doc, "第三章：依赖安装与本地项目启动")
    
    add_heading_2(doc, "3.1 首次安装项目依赖")
    add_styled_paragraph(doc, "从 Git 仓库拉取源码后，打开终端进入工程根目录：")
    add_code_block(doc, 
"""# 1. 验证 pnpm 与 node 版本
node -v
pnpm -v

# 2. 安装项目依赖（国内推荐配置淘宝镜像源加速）
pnpm config set registry https://registry.npmmirror.com

# 3. 执行安装命令
pnpm install
# 或者缩写为:
pnpm i""")

    add_heading_2(doc, "3.2 启动本地开发服务器")
    add_styled_paragraph(doc, "在工程根目录下执行开发启动命令：")
    add_code_block(doc, "pnpm dev")
    add_styled_paragraph(doc, "Vite 启动配置详情（位于 `vite.config.ts`）：")
    add_bullet(doc, "3010", bold_prefix="监听端口（port）：")
    add_bullet(doc, "0.0.0.0（支持局域网内其他设备如手机端同屏测试访问）", bold_prefix="网络监听（host）：")
    add_bullet(doc, "true（启动后自动拉起系统默认浏览器访问）", bold_prefix="自动打开浏览器（open）：")
    add_bullet(doc, "http://localhost:3010/#/", bold_prefix="本地访问地址：")

    add_heading_2(doc, "3.3 路径别名（Alias）机制")
    add_styled_paragraph(doc, "工程配置了 `@` 别名映射到 `./src` 目录：")
    add_code_block(doc, 
"""// 引入组件或接口时，统一使用 @/ 绝对映射，避免出现 ../../../ 多层相对路径
import * as api from '@/api/interfaceapi'
import useHeaderStore from '@/store/modules/header'""")

    # -------------------------------------------------------------
    # SECTION 4: MULTI-ENV API CONFIGURATION
    # -------------------------------------------------------------
    add_heading_1(doc, "第四章：多环境接口配置与切换策略")
    add_styled_paragraph(doc, "项目的后端通信配置统一维护在：[src/api/baseConfig.ts](file:///e:/Silin7%20Git/CONGZHIYUAN/congzhiyuan-website/src/api/baseConfig.ts)。在打包测试系统或正式上线时，必须在此处检查 API 地址配置。")
    
    add_heading_2(doc, "4.1 核心环境配置文件源码结构")
    add_code_block(doc, 
"""// 文件路径: src/api/baseConfig.ts

// 1. 正式生产系统接口地址 (发布正式外网时使用)
const baseURL = 'https://api.congzhiYuan.cn/index.php'

// 2. 测试环境接口地址 (内部联调、功能回归时解除注释使用)
// const baseURL = 'http://testapi.congzhiyuan.cn/index.php'

// 3. 静态资源与文件服务器地址
const fileURL = 'http://congzhiyuan.cn'

// 4. 用户协议页面链接
const agreementURL = 'https://api.congzhiyuan.cn/xieyi.html'

// 5. 充值收银台网关支付处理页面
const chargePayURL = 'https://api.congzhiYuan.cn/pay/chargePayDeal.php'

export { baseURL, fileURL, agreementURL, chargePayURL }""")

    add_heading_2(doc, "4.2 正式系统 VS 测试系统 切换对照表")
    switch_headers = ["部署环境目标", "baseURL 当前取值", "注意事项"]
    switch_data = [
        ["正式生产系统 (Production)", "'https://api.congzhiYuan.cn/index.php'", "必须开启 HTTPS 保证网络传输安全，对应正式高考招考数据库"],
        ["测试演练系统 (Staging/Test)", "'http://testapi.congzhiyuan.cn/index.php'", "用于内部功能演练、假数据注入、新省份规则测试，切勿外发给真实考生"]
    ]
    create_styled_table(doc, switch_headers, switch_data, [Inches(1.8), Inches(2.3), Inches(1.9)])

    add_callout(doc, "每次执行 `pnpm build` 打包发布前，必须第一步核对 `src/api/baseConfig.ts` 中的 `baseURL` 是否指向目标环境！如需切换至测试环境，注释掉第一行，解除第二行的注释即可。", title="发布前必备核查步骤", callout_type="warning")

    # -------------------------------------------------------------
    # SECTION 5: BUILD & PACKAGING
    # -------------------------------------------------------------
    add_heading_1(doc, "第五章：项目构建打包与发布全流程")
    
    add_heading_2(doc, "5.1 常用构建打包脚本说明")
    add_styled_paragraph(doc, "在 `package.json` 中预置了以下标准构建脚本：")
    
    build_headers = ["脚本名称", "执行命令", "执行动作与适用场景"]
    build_data = [
        ["标准全量构建", "pnpm build", "【正式发布必用】并行执行 `vue-tsc` 类型安全检查与 `vite build` 生产打包，有任何 TS 报错会立即熔断中断打包"],
        ["仅打包构建", "pnpm build-only", "跳过 `vue-tsc` 类型检查直接使用 Vite 编译生成生产包，适合紧急修复发布或已知轻微类型警告时使用"],
        ["独立类型检查", "pnpm type-check", "仅执行 `vue-tsc --build`，不输出文件，用于在提交代码前检查 TypeScript 语法与类型规范"],
        ["本地产物预览", "pnpm preview", "启动 Vite 本地静态服务（默认端口 4173）预览 `dist` 目录产物，用于验证打包后的资源加载与路由跳转是否正常"],
        ["代码格式化", "pnpm format", "调用 Prettier 递归格式化 `src/` 下所有的 `.vue`、`.ts`、`.scss` 代码文件"]
    ]
    create_styled_table(doc, build_headers, build_data, [Inches(1.2), Inches(1.3), Inches(3.5)])

    add_heading_2(doc, "5.2 标准打包执行实操")
    add_code_block(doc, 
"""# 执行全量打包命令
pnpm build

# 终端成功输出示例:
# vite v6.3.5 building for production...
# ✓ 1568 modules transformed.
# dist/index.html                                     0.68 kB │ gzip: 0.44 kB
# dist/assets/index-cd3unFYV.css                      444.38 kB
# dist/assets/index-x_B_RbLI.js                       1.28 MB
# ✓ built in 5.44s""")

    add_heading_2(doc, "5.3 【极度重要】静态资源与 public 目录部署注意事项")
    add_styled_paragraph(doc, "在项目的 `index.html` 头部，直接通过静态绝对路径引入了部分基础全局脚本与字体：")
    add_code_block(doc, 
"""<!-- index.html 中的引用 -->
<script src="/public/js/lucide.js"></script>
<link rel="stylesheet" href="/public/fonts/inter-font.css">
<script src="/public/js/tailwindcss.js"></script>""")

    add_callout(doc, 
"由于 Vite 打包机制默认会将根目录 `public/` 下的子文件平铺复制到 `dist/` 根路径下（例如 `public/js/lucide.js` 会被复制为 `dist/js/lucide.js`）。\n"
"但由于 `index.html` 中硬编码了 `/public/...` 路径，因此在执行 `pnpm build` 打包完成后，部署前务必执行以下两项之一：\n"
"【推荐运维规范操作】：将项目根目录下的 `public` 文件夹直接完整复制一份粘贴放入 `dist/` 文件夹中（即形成 `dist/public/js/lucide.js`），确保生产环境页面中引用的 Lucide 图标与 TailwindCSS 脚本能够 100% 正常命中加载！", 
title="打包发布关键踩坑点", callout_type="warning")

    # -------------------------------------------------------------
    # SECTION 6: PRODUCTION DEPLOYMENT (NGINX / IIS)
    # -------------------------------------------------------------
    add_heading_1(doc, "第六章：生产 Web 服务器部署配置")
    add_styled_paragraph(doc, "本项目路由模式为 **Hash 模式**（`createWebHashHistory`，URL 形如 `https://congzhiyuan.cn/#/volunteerApply`）。相比于 HTML5 History 模式，Hash 路由的所有路由跳转均发生在 `#` 之后，由前端浏览器捕获，**不会向服务器发起后端请求**，因此天然免去了 Nginx/IIS 的 `try_files` 404 重写繁琐配置。")
    
    add_heading_2(doc, "6.1 Microsoft-IIS 服务器部署配置（线上实机）")
    add_styled_paragraph(doc, "目前线上生产服务器采用 Windows Server + IIS 8.5/10 运行：")
    add_bullet(doc, "将打包完成并包含 public 目录的 `dist/` 文件夹内全部内容上传到 IIS 站点的物理根目录（例如 `D:\\wwwroot\\congzhiyuan-website\\`）。", bold_prefix="1. 部署路径：")
    add_bullet(doc, "确保 IIS 应用程序池使用的是【无托管代码】模式（No Managed Code），管道模式为【集成】。", bold_prefix="2. 应用程序池配置：")
    add_bullet(doc, "在 IIS 管理器的【MIME 类型】中，确保已添加 `.woff` (font/x-woff)、`.woff2` (font/woff2)、`.json` (application/json) 映射，避免字体加载报 404。", bold_prefix="3. MIME 类型映射：")

    add_heading_2(doc, "6.2 Nginx 服务器标准部署配置模板（Linux 备选）")
    add_code_block(doc, 
"""server {
    listen 80;
    server_name congzhiyuan.cn www.congzhiyuan.cn;
    # 强制重定向至 HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name congzhiyuan.cn;

    ssl_certificate     /etc/nginx/ssl/congzhiyuan.cn.crt;
    ssl_certificate_key /etc/nginx/ssl/congzhiyuan.cn.key;
    ssl_protocols       TLSv1.2 TLSv1.3;

    root /var/www/congzhiyuan-website/dist;
    index index.html;

    # 开启 Gzip 压缩，大幅提升首屏秒开速度
    gzip on;
    gzip_min_length 1k;
    gzip_types text/plain text/css application/javascript application/json image/svg+xml;

    # 静态资源强缓存配置
    location /assets/ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # SPA 默认路由托管
    location / {
        try_files $uri $uri/ /index.html;
    }
}""")

    # -------------------------------------------------------------
    # SECTION 7: PROJECT STRUCTURE TOPOLOGY
    # -------------------------------------------------------------
    add_heading_1(doc, "第七章：工程目录拓扑结构与核心文件职责")
    add_styled_paragraph(doc, "项目核心代码严格遵循模块化、高内聚低耦合的工程架构规范：")
    
    dir_headers = ["目录 / 文件路径", "所属层级", "主要职责说明"]
    dir_data = [
        ["src/main.ts", "入口模块", "系统启动入口，挂载 Vue 实例、Pinia 状态、路由及 Element-Plus 全局插件"],
        ["src/App.vue", "根组件", "包含全局 `<router-view>` 与全局消息、弹窗容器"],
        ["src/api/baseConfig.ts", "接口配置", "管理生产与测试后端 BaseURL、静态文件域名、支付与用户协议链接"],
        ["src/api/interfaceapi.ts", "API接口层", "统一封装全系统 POST/GET 接口（包含登录、查分、选科、批次、智能推荐、高校与专业查询）"],
        ["src/router/index.ts", "路由层", "注册系统全部路由映射，配置网页标题及全局前置守卫（`beforeEach`）"],
        ["src/store/modules/user.ts", "状态层", "Pinia 用户全局状态管理（Token、VIP 等级、用户信息存储与派发）"],
        ["src/components/headnav.vue", "公共组件", "顶部全局导航栏，集成登录/注册弹窗、省份切换、VIP 指引与退出登录"],
        ["src/views/home.vue", "页面层", "系统首页（轮播横幅、冲稳保方案卡片、核心服务与操作指南）"],
        ["src/views/volunteerApply.vue", "页面层", "【核心业务】志愿填报大厅（批次、投档分类、冲稳保阈值滑块、专业组检索与收藏）"],
        ["src/views/personalInfo.vue", "页面层", "个人中心（466分成绩核对、物化生选科、我的志愿单拖拽排序与 Excel 导出）"],
        ["src/views/schoolSearch.vue", "页面层", "全国 1,417 所高校检索库、按省份多选过滤与院校详情入口"],
        ["src/views/schoolDetail.vue", "页面层", "院校详情页，展示办学特色、重点学科与历年在甘肃录取历年分"],
        ["src/views/majorAnalysis.vue", "页面层", "普通本科 13 大学科门类专业信息库与一级/二级学科专业目录树"],
        ["src/views/aiAssessmentList.vue", "页面层", "AI 智能测评主页（心理健康测评、职业兴趣测评、MBTI性格测评）"],
        ["src/views/chargingInfomating.vue", "页面层", "VIP 会员权益说明与套餐升级支付页面"],
        ["public/", "静态资源", "存放独立于构建打包的脚本（lucide.js、tailwindcss.js）与字体文件"]
    ]
    create_styled_table(doc, dir_headers, dir_data, [Inches(1.8), Inches(0.9), Inches(3.3)])

    # -------------------------------------------------------------
    # SECTION 8: TROUBLESHOOTING
    # -------------------------------------------------------------
    add_heading_1(doc, "第八章：运维与维护常见故障排查（Troubleshooting）")
    
    troubles = [
        ("故障 1：执行 pnpm install 报网络超时或挂起",
         "原因与解法：\n"
         "1. 主要是由于默认官方 npm 源（registry.npmjs.org）在国内访问缓慢所致；\n"
         "2. 执行命令切换为淘宝镜像：`pnpm config set registry https://registry.npmmirror.com`；\n"
         "3. 重新执行 `pnpm install` 即可迅速恢复下载。"),
        
        ("故障 2：执行 pnpm build 提示 vue-tsc 类型检查报错中断",
         "原因与解法：\n"
         "1. `pnpm build` 命令被配置为 `run-p type-check \"build-only {@}\"`，如果业务代码中存在类型不匹配，`vue-tsc` 会返回非0退出码中断构建；\n"
         "2. 修复对应的 TypeScript 类型错误（或通过 TS 接口补充 `any` 宽松类型）；\n"
         "3. 若线上需紧急临时发布打包，可执行：`pnpm build-only`，绕过类型校验直接输出 `dist` 产物。"),
        
        ("故障 3：打包发布后页面图标不显示或 TailwindCSS 样式不生效",
         "原因与解法：\n"
         "1. 检查线上部署的站点根目录是否缺少 `public` 文件夹；\n"
         "2. 确认 `dist/public/js/tailwindcss.js` 与 `dist/public/js/lucide.js` 是否存在并可通过浏览器直接 URL 访问返回 200；\n"
         "3. 若报 404，将工程根目录下的 `public` 文件夹拷贝到 `dist/` 即可立即解决。"),
        
        ("故障 4：调用后端 API 报 HTTP 411 Length Required",
         "原因与解法：\n"
         "1. 现象：部分 POST 请求直接被 IIS 服务器前置拦截并返回 411；\n"
         "2. 原因：微软 IIS 服务器严格要求 POST 请求必须携带 `Content-Length` 请求头，或传递空请求体 `params`；\n"
         "3. 规范解法：在 `axios.post(url, data)` 中，即使无入参也必须传递空对象 `{}` 或空的 FormData，不可传递 `undefined`。"),
        
        ("故障 5：用户登录后刷新页面丢失登录状态",
         "原因与解法：\n"
         "1. 系统将登录 Token 与 UserInfo 持久化保存在浏览器的 `localStorage` 中；\n"
         "2. 在组件挂载时通过 `localStorage.getItem('token')` 进行回填；\n"
         "3. 若出现刷新丢失，请检查浏览器是否处于“隐身/无痕模式”或浏览器隐私设置禁用了本地 Storage 存储功能。")
    ]
    
    for t_title, t_desc in troubles:
        add_heading_2(doc, t_title)
        for line in t_desc.split('\n'):
            add_styled_paragraph(doc, line, space_after=3)

    # Save Document
    output_path = r"E:\Silin7 Git\CONGZHIYUAN\congzhiyuan-website\聪志愿AI智能志愿填报系统-项目技术维护手册.docx"
    doc.save(output_path)
    print(f"Maintenance manual saved successfully to: {output_path}")

if __name__ == "__main__":
    generate_maintenance_manual()
