# -*- coding: utf-8 -*-
"""
Generate a professional, beginner-friendly Word manual for CongZhiYuan AI Website.
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

def set_callout_border(cell, border_color="1E40AF"):
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

def set_table_borders(table, border_color="D1D5DB"):
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

def add_styled_paragraph(doc, text, style='Normal', space_before=0, space_after=6, line_spacing=1.2, font_name="微软雅黑", font_size=10.5, font_color=RGBColor(31, 41, 55), bold=False):
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

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "微软雅黑"
    run._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    run.font.size = Pt(16)
    run.font.color.rgb = RGBColor(30, 64, 175) # Navy Blue
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
    run.font.size = Pt(13)
    run.font.color.rgb = RGBColor(67, 56, 202) # Indigo
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
    run.font.color.rgb = RGBColor(55, 65, 81)
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
        r_pre.font.size = Pt(10)
        r_pre.font.color.rgb = RGBColor(31, 41, 55)
        r_pre.bold = True
    run = p.add_run(text)
    run.font.name = "微软雅黑"
    run._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(55, 65, 81)
    return p

def add_callout(doc, text, title="操作小贴士", callout_type="note"):
    """Add a professional styled callout box."""
    colors = {
        "note": {"bg": "EFF6FF", "border": "2563EB", "title_color": RGBColor(30, 64, 175)},
        "tip": {"bg": "ECFDF5", "border": "059669", "title_color": RGBColor(4, 120, 87)},
        "warning": {"bg": "FEF2F2", "border": "DC2626", "title_color": RGBColor(185, 28, 28)},
    }
    cfg = colors.get(callout_type, colors["note"])
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.0)
    set_cell_background(cell, cfg["bg"])
    set_callout_border(cell, cfg["border"])
    set_cell_margins(cell, top=140, bottom=140, left=200, right=180)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    run_t = p.add_run(f"【{title}】")
    run_t.font.name = "微软雅黑"
    run_t._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    run_t.font.size = Pt(10.5)
    run_t.font.color.rgb = cfg["title_color"]
    run_t.bold = True
    
    p_body = cell.add_paragraph()
    p_body.paragraph_format.space_before = Pt(0)
    p_body.paragraph_format.space_after = Pt(2)
    p_body.paragraph_format.line_spacing = 1.2
    run_b = p_body.add_run(text)
    run_b.font.name = "微软雅黑"
    run_b._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    run_b.font.size = Pt(9.5)
    run_b.font.color.rgb = RGBColor(55, 65, 81)
    
    # Empty paragraph after table for spacing
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(4)

def add_figure(doc, img_path, caption):
    """Add a screenshot with proper styling and caption."""
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run = p_img.add_run()
        run.add_picture(img_path, width=Inches(5.8))
        
        # Caption
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(10)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = "微软雅黑"
        run_cap._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
        run_cap.font.size = Pt(9)
        run_cap.font.color.rgb = RGBColor(107, 114, 128)
        run_cap.italic = True
    else:
        print(f"Warning: image {img_path} not found!")

def create_styled_table(doc, headers, rows_data, col_widths=None):
    """Create a beautiful formatted table."""
    table = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    
    # Header Row
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
        set_cell_background(hdr_cells[i], "1E40AF")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=120, right=120)
        if col_widths and i < len(col_widths):
            hdr_cells[i].width = col_widths[i]
            
    # Data Rows
    for r_idx, r_data in enumerate(rows_data):
        row_cells = table.rows[r_idx + 1].cells
        bg_color = "F9FAFB" if r_idx % 2 == 1 else "FFFFFF"
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
            run.font.color.rgb = RGBColor(55, 65, 81)
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=120, right=120)
            if col_widths and c_idx < len(col_widths):
                row_cells[c_idx].width = col_widths[c_idx]

    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(2)
    p_space.paragraph_format.space_after = Pt(6)

def generate_manual():
    doc = docx.Document()
    
    # Set page margins
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
        r_head = p_head.add_run("聪志愿AI · 新手保姆级操作手册")
        r_head.font.name = "微软雅黑"
        r_head._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
        r_head.font.size = Pt(8.5)
        r_head.font.color.rgb = RGBColor(156, 163, 175)
        
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
            r.font.color.rgb = RGBColor(156, 163, 175)

    # -------------------------------------------------------------
    # COVER PAGE
    # -------------------------------------------------------------
    p_cov_space = doc.add_paragraph()
    p_cov_space.paragraph_format.space_before = Pt(40)
    
    # Title Tag
    p_tag = doc.add_paragraph()
    p_tag.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_tag = p_tag.add_run("【新高考新方案 · 官方正版操作指引】")
    r_tag.font.name = "微软雅黑"
    r_tag._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    r_tag.font.size = Pt(12)
    r_tag.font.color.rgb = RGBColor(37, 99, 235)
    r_tag.bold = True
    
    # Main Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(12)
    r_title = p_title.add_run("聪志愿 AI 智能志愿填报系统\n零基础新手保姆级操作手册")
    r_title.font.name = "微软雅黑"
    r_title._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    r_title.font.size = Pt(26)
    r_title.font.color.rgb = RGBColor(30, 64, 175)
    r_title.bold = True
    
    # Subtitle
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(30)
    r_sub = p_sub.add_run("从账号登录、成绩选科核对，到“冲稳保”智能方案生成与志愿表导出全流程图解")
    r_sub.font.name = "微软雅黑"
    r_sub._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(75, 85, 99)
    
    # Meta Box Table
    meta_table = doc.add_table(rows=5, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("适用平台", "聪志愿AI高考志愿智能辅助系统（Web端）"),
        ("适用对象", "新高考生、考生家长、高中毕业班班主任、志愿规划顾问"),
        ("支持考选模式", "全国传统文理科模式、新高考“3+1+2”与“3+3”专业组模式"),
        ("测试体验账号", "13256605200（VIP旗舰体验权限已激活）"),
        ("编制日期 / 版本", "2026年9月 · 正式发布版 V1.0"),
    ]
    for idx, (k, v) in enumerate(meta_data):
        row = meta_table.rows[idx]
        cell_k, cell_v = row.cells[0], row.cells[1]
        cell_k.width = Inches(1.8)
        cell_v.width = Inches(4.2)
        set_cell_background(cell_k, "EFF6FF")
        set_cell_background(cell_v, "FFFFFF")
        set_cell_margins(cell_k, top=70, bottom=70, left=100, right=100)
        set_cell_margins(cell_v, top=70, bottom=70, left=100, right=100)
        
        p_k = cell_k.paragraphs[0]
        r_k = p_k.add_run(k)
        r_k.font.name = "微软雅黑"
        r_k._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
        r_k.font.size = Pt(9.5)
        r_k.bold = True
        r_k.font.color.rgb = RGBColor(30, 64, 175)
        
        p_v = cell_v.paragraphs[0]
        r_v = p_v.add_run(v)
        r_v.font.name = "微软雅黑"
        r_v._element.rPr.rFonts.set(qn('w:eastAsia'), "微软雅黑")
        r_v.font.size = Pt(9.5)
        r_v.font.color.rgb = RGBColor(55, 65, 81)
    
    set_table_borders(meta_table, "93C5FD")
    doc.add_page_break()

    # -------------------------------------------------------------
    # PREFACE & QUICK GUIDE
    # -------------------------------------------------------------
    add_heading_1(doc, "前言：写给完全新手的话")
    add_styled_paragraph(doc, "高考志愿填报常被称为“第二次高考”，往往“考得好还要报得好”。传统志愿填报面临海量数据检索难、高校往年录取分数线换算繁琐、各批次志愿梯度把握不准等痛点，极易造成“高分低就”甚至“滑档退档”的巨大风险。")
    add_styled_paragraph(doc, "“聪志愿AI”是基于千万级权威高校历年录取数据、专业学科评估体系及新高考录取规则研发的智能化志愿辅助平台。平台为考生提供从【职业性格测评】到【院校与专业匹配】、再到【“冲稳保”智能梯度推荐】及【一键导出志愿表】的全流程一站式服务。")
    
    add_heading_2(doc, "★ 新手5步极速通关总览图")
    steps = [
        ("第1步：账号登录与平台接入", "使用分配的账号密码登录系统，阅读并确认用户协议，激活VIP权限。"),
        ("第2步：核对个人成绩与选科信息", "进入【个人中心】，核实省份（如甘肃省）、选科组合（物理/化学/生物）、高考分数及全省位次。"),
        ("第3步：智能志愿检索与梯度分档", "进入【志愿填报】，设置批次与投档单位，通过“冲（50%）”、“稳”、“保（80%）”阈值生成科学的志愿推荐列表。"),
        ("第4步：辅助查询与专业深度探索", "借助【院校查询】与【专业解析】了解高校办学特色、历年录取趋势与专业未来就业前景。"),
        ("第5步：管理志愿单与一键导出Excel", "在【我的志愿单】中调整专业组志愿顺序（支持拖拽），核验无误后一键导出标准Excel志愿表用于最终填报。")
    ]
    for s_title, s_desc in steps:
        add_bullet(doc, s_desc, bold_prefix=s_title + "：")

    add_callout(doc, "请各位考生和家长在正式开始前准备好：① 考生的准确高考投档总分；② 官方公布的全省一分一段位次表对应名次；③ 考生的首选及再选选考科目。系统将基于位次换算模型为您做出最精准的录取概率推算。", title="填报前准备", callout_type="tip")
    
    add_figure(doc, "screenshots/01_home_page.png", "图 0-1：聪志愿AI系统首页全景图（功能导航、推荐方案与核心服务入口）")

    # -------------------------------------------------------------
    # CHAPTER 1: LOGIN & ACCESS
    # -------------------------------------------------------------
    add_heading_1(doc, "第一章：平台访问与账号登录")
    add_styled_paragraph(doc, "聪志愿AI平台采用纯B/S架构，无需安装任何客户端软件，考生及家长可在台式机、笔记本电脑或平板电脑的现代浏览器上流畅使用。推荐使用 Google Chrome、Microsoft Edge 或 360安全浏览器（极速模式）访问。")
    
    add_heading_2(doc, "1.1 平台访问地址")
    add_bullet(doc, "https://congzhiyuan.cn", bold_prefix="线上生产环境地址：")
    add_bullet(doc, "http://localhost:3010（本地服务启动后）", bold_prefix="局域网/内网测试地址：")
    
    add_heading_2(doc, "1.2 账号登录步骤详解（保姆级操作）")
    login_steps = [
        ("点击右上角【登录】按钮", "打开网站首页，在顶部右上方可以看到蓝色的【登录】按钮，鼠标单击打开弹窗。"),
        ("切换至【账号登录】标签页", "系统登录弹窗默认提供三种登录方式：【手机登录】、【账号登录】和【志愿卡登录】。请点击切换到【账号登录】。"),
        ("输入登录凭证", "在“账号/手机号”输入框中输入您的账号（如本手册示例体验账号：13256605200），在“密码”输入框中输入对应密码（如：123456）。"),
        ("勾选用户协议", "务必勾选左下方的【已阅读并同意《用户协议》】复选框，否则系统会提示“请阅读并同意用户协议”。"),
        ("点击【登录】完成认证", "点击蓝色【登录】按钮，系统完成后台鉴权。登录成功后，弹窗自动关闭，首页右上角将显示您的账号名，表示已成功进入系统。")
    ]
    for l_title, l_desc in login_steps:
        add_bullet(doc, l_desc, bold_prefix=l_title + "：")
        
    add_figure(doc, "screenshots/02_login_dialog.png", "图 1-1：系统登录弹窗界面（切换至“账号登录”并输入凭证）")
    add_figure(doc, "screenshots/03_home_loggedin.png", "图 1-2：登录成功后的首页状态（右上角已显示用户身份）")

    add_callout(doc, "如果您使用的是学校或机构统一发放的志愿报考卡，可在弹窗中切换至【志愿卡登录】页签，输入志愿卡卡号与卡密同样可以一键激活VIP服务。", title="志愿卡用户注意", callout_type="note")

    # -------------------------------------------------------------
    # CHAPTER 2: PERSONAL INFO & SCORE VERIFICATION
    # -------------------------------------------------------------
    add_heading_1(doc, "第二章：个人信息与高考成绩选科核对")
    add_styled_paragraph(doc, "个人信息是整个系统运行AI匹配算法的基石！智能推荐系统正是依据您填写的【高考分数】、【位次】、【选科组合】以及【所在省份录取政策】来为您量身匹配高校的，因此在正式填报前必须进入个人中心进行仔细核对。")
    
    add_heading_2(doc, "2.1 进入个人中心")
    add_styled_paragraph(doc, "登录后，点击网页右上角的账号名称（如“13256605200”）或点击头像图标，即可直接进入【个人信息】管理中心。页面左侧为功能导航，右侧为主信息面板。")
    
    add_heading_2(doc, "2.2 核心信息字段解读（对应示例考生档案）")
    info_headers = ["信息字段", "示例考生取值", "业务含义与影响", "新手操作建议"]
    info_data = [
        ["考生省份", "甘肃省", "决定了调用的招生计划、院校专业组及批次划线规则", "如省份有误，请在首次登录时准确选择"],
        ["选科模式", "新高考 3+1+2", "甘肃自2024年起实行新高考，统考语数外+物理/历史首选+两门再选", "按高中选考实际科目匹配"],
        ["选考科目", "物理, 化学, 生物", "首选物理(A)，再选化学(B)与生物(C)，属于传统理科典型选科组合", "高校招生简章中对专业有严格选科限制"],
        ["考试类别", "普通类", "区分普通类、艺术类、体育类等", "普通高考生请保持选择“普通类”"],
        ["高考分数", "466 分", "高考成绩原始投档分", "须为含政策性加分后的最终投档成绩"],
        ["全省位次", "44,088 位", "【最关键指标】系统根据位次换算往年同位分，比分数更精准", "对照本省一分一段表精准录入"],
        ["修改机会", "剩余 31 次", "为防止误操作和恶意修改，系统限制信息修改次数", "每次修改请再三核对后再点击保存"]
    ]
    create_styled_table(doc, info_headers, info_data, [Inches(1.1), Inches(1.2), Inches(2.2), Inches(1.5)])
    
    add_figure(doc, "screenshots/04_personal_info.png", "图 2-1：个人中心 - 成绩与选科信息设置界面")

    add_callout(doc, "在志愿填报中，“位次”的参考价值远高于“绝对分数”！因为每年高考试卷难度不同、批次线有升有降，但某所高校在全省录取的位次区间相对稳定。录入正确的位次是使用AI智能推荐的前提。", title="关键避坑指南：认准位次", callout_type="warning")

    # -------------------------------------------------------------
    # CHAPTER 3: VOLUNTEER APPLY (CORE FEATURE)
    # -------------------------------------------------------------
    add_heading_1(doc, "第三章：核心功能——智能志愿填报实战指南")
    add_styled_paragraph(doc, "【志愿填报】是本系统的核心功能模块。系统基于考生 466 分（44,088 位次）及物理+化学+生物选考组合，运用AI大数据算法在海量院校专业组中智能筛选出契合度最高的志愿方案。")
    
    add_heading_2(doc, "3.1 界面布局与参数面板")
    add_styled_paragraph(doc, "点击顶部导航栏中的【志愿填报】，进入志愿检索主面板。界面由筛选条件区、高级展开区和智能检索触发按钮构成。")
    
    add_heading_2(doc, "3.2 筛选条件手把手设置步骤")
    apply_steps = [
        ("步骤 1：选择院校层次", "提供【本科】与【专科】两个选项。本科线上考生请选择【本科】，系统会自动载入本科各招生批次。"),
        ("步骤 2：选择录取批次", "以甘肃省新高考为例，本科阶段设有【本科提前批A】（1A）与【本科批】（2C）。主力普通类志愿选择【本科批】。"),
        ("步骤 3：选择投档单位类型", "系统支持多达13种投档分类。普通类考生请保持选择【普通类】（2_pt）；农村专项考生可选择【国家专项计划】或【地方专项计划】。"),
        ("步骤 4：点击【展开】查看高级选项", "点击中间的“展开 ↓”按钮，可以进一步展开更多精细化筛选维度：院校性质（公办/民办）、院校特色（985/211/双一流）、意向省市区域及学费范围。"),
        ("步骤 5：调节“冲、稳、保”梯度阈值滑块", "展开后可看到两个核心概率调节滑块：【冲刺阈值】（默认50%）与【保底阈值】（默认80%）。"),
        ("步骤 6：点击【立即开始智能检索】", "设置好心仪的筛选条件后，点击醒目的蓝色按钮【立即开始智能检索】，系统将秒级生成符合条件的院校专业组列表。")
    ]
    for a_title, a_desc in apply_steps:
        add_bullet(doc, a_desc, bold_prefix=a_title + "：")

    add_figure(doc, "screenshots/05_volunteer_apply.png", "图 3-1：志愿填报基础检索面板（院校层次、批次与性质选择）")
    add_figure(doc, "screenshots/05_volunteer_apply_expanded.png", "图 3-2：展开后的高级筛选面板（包含冲/保阈值滑块及多维指标）")

    add_heading_2(doc, "3.3 深入理解“冲、稳、保”志愿梯度黄金法则")
    add_styled_paragraph(doc, "平行志愿填报切忌全部填报同层次学校，必须遵循“冲一冲、稳一稳、保一保”的科学阶梯布局原则：")
    
    strat_headers = ["梯度档次", "录取概率区间", "策略定位与报考意义", "填报建议比例（以60个志愿组为例）"]
    strat_data = [
        ["冲 (冲刺院校)", "30% - 50%", "位次略高于考生成绩的优质院校，博取录取上限，哪怕去冷门专业也愿意接受", "建议填报 10 - 15 个专业组（约 20%）"],
        ["稳 (稳妥院校)", "50% - 80%", "考生成绩与高校往年位次高度吻合的主力院校，学校和专业均较为满意", "建议填报 30 - 35 个专业组（约 55%）"],
        ["保 (保底院校)", "80% - 98%", "往年录取位次远低于考生成绩的安全兜底院校，确保绝不滑档、有学可上", "建议填报 10 - 15 个专业组（约 25%）"]
    ]
    create_styled_table(doc, strat_headers, strat_data, [Inches(1.1), Inches(1.3), Inches(2.2), Inches(1.4)])

    add_callout(doc, "新高考专业组模式下，一个志愿单位是【某高校 + 某专业组】。在专业组内填报具体专业时，务必勾选【服从专业调剂】！平行志愿一旦投档进校后被退档，将无法再投向后续其他志愿，只能参加征集志愿或跌入下一批次！", title="高危红线警示：必须服从专业调剂", callout_type="warning")

    # -------------------------------------------------------------
    # CHAPTER 4: SCHOOL SEARCH & MAJOR ANALYSIS
    # -------------------------------------------------------------
    add_heading_1(doc, "第四章：海量信息库——院校查询与专业深度解析")
    add_styled_paragraph(doc, "俗话说“知己知彼，百战不殆”。在填报志愿前，考生需要全面了解大学的综合实力、地理区位，以及各个专业的学科特色与就业前景。系统内置了权威的高校与专业信息库。")
    
    add_heading_2(doc, "4.1 院校查询模块使用指南")
    add_styled_paragraph(doc, "点击顶部导航【院校查询】，可进入全国高校数据库。平台收录了全国共 **1,417 所** 普通本科高校的完整档案。")
    add_bullet(doc, "支持按全国31个省市自治区快速过滤（如点击“北京市”、“甘肃省”、“江苏省”等）。", bold_prefix="省份多维筛选：")
    add_bullet(doc, "支持快速切换“不限”、“本科”、“专科”。", bold_prefix="层次精准定位：")
    add_bullet(doc, "在输入框中输入高校全称或关键字（如“清华”、“交大”、“师范”），点击【查询】即可一键直达。", bold_prefix="院校名称模糊搜索：")
    
    add_figure(doc, "screenshots/06_school_search.png", "图 4-1：院校查询初始检索面板（省份选择与办学层次）")
    add_figure(doc, "screenshots/06_school_search_results.png", "图 4-2：院校检索结果列表（展示高校名称、属地、公办/民办性质与查看详情入口）")

    add_heading_2(doc, "4.2 大学专业信息库与解析")
    add_styled_paragraph(doc, "选大学决定了未来四年在哪度过，而选专业则很大程度上决定了未来的职业方向。点击顶部导航【专业解析】，进入教育部标准学科专业目录库。")
    add_styled_paragraph(doc, "系统完整收录了普通本科全部 **13 个学科门类**。点击任一门类标签（如工学、理学、经济学等），下方将自动展开对应门类下的一级学科专业类及下属具体二级专业数量：")
    
    major_headers = ["门类代码", "门类名称", "包含专业类数", "下属具体专业数", "典型代表专业举例"]
    major_data = [
        ["01", "哲学", "1 个专业类", "4 个专业", "哲学、逻辑学、宗教学、伦理学"],
        ["02", "经济学", "4 个专业类", "30 个专业", "经济学、金融学、国际经济与贸易、财政学"],
        ["03", "法学", "6 个专业类", "55 个专业", "法学、政治学与行政学、社会学、马克思主义理论"],
        ["04", "教育学", "2 个专业类", "36 个专业", "教育学、学前教育、小学教育、体育教育"],
        ["05", "文学", "3 个专业类", "132 个专业", "汉语言文学、英语、新闻学、网络与新媒体"],
        ["06", "历史学", "1 个专业类", "9 个专业", "历史学、世界史、考古学、文物与博物馆学"],
        ["07", "理学", "12 个专业类", "53 个专业", "数学与应用数学、物理学、化学、地理科学"],
        ["08", "工学", "32 个专业类", "293 个专业", "计算机科学与技术、软件工程、电气工程、机械工程"],
        ["09", "农学", "7 个专业类", "51 个专业", "农学、园艺、动物医学、林学"],
        ["10", "医学", "11 个专业类", "62 个专业", "临床医学、口腔医学、中医学、药学"],
        ["12", "管理学", "9 个专业类", "65 个专业", "工商管理、会计学、财务管理、电子商务"],
        ["13", "艺术学", "5 个专业类", "50 个专业", "音乐表演、视觉传达设计、环境设计、广播电视编导"],
        ["14", "交叉学科", "1 个专业类", "若干专业", "集成电路设计、人工智能等新兴交叉方向"]
    ]
    create_styled_table(doc, major_headers, major_data, [Inches(0.9), Inches(1.0), Inches(1.2), Inches(1.3), Inches(1.6)])
    
    add_figure(doc, "screenshots/07_major_analysis.png", "图 4-3：大学专业信息库全景（13大学科门类分布总览）")

    add_callout(doc, "点击具体专业名称后，可弹出专业详情浮层，详细查阅该专业的核心课程体系、培养目标、考研升学方向以及毕业生薪酬水平与行业分布统计数据。", title="专业探索小技巧", callout_type="tip")

    # -------------------------------------------------------------
    # CHAPTER 5: AI ASSESSMENT
    # -------------------------------------------------------------
    add_heading_1(doc, "第五章：科学规划——AI 智能测评应用")
    add_styled_paragraph(doc, "很多考生填报志愿时感到迷茫，根本原因是“不知道自己喜欢什么、擅长什么”。盲目跟风所谓的热门专业，往往导致入学后缺乏兴趣甚至产生厌学情绪。聪志愿AI提供科学的测评工具，帮助考生进行自我认知与职业探索。")
    
    add_heading_2(doc, "5.1 三大科学测评量表深度介绍")
    scale_headers = ["量表名称", "理论渊源与模型", "评估核心维度", "对填报志愿的指导意义"]
    scale_data = [
        ["心理健康测评", "国际通用身心健康筛查模型", "情绪管理、抗压能力、适应力、自我调节", "评估考生应对高强度学业与环境变化的承受力"],
        ["职业兴趣能力测评", "霍兰德职业兴趣六边形理论(RIASEC)", "实际型、研究型、艺术型、社会型、企业型、常规型", "精准定位考生的天赋专长与未来匹配的行业岗位群"],
        ["MBTI 性格特征测评", "迈尔斯-布里格斯性格分类指标", "四个维度：E/I(外倾/内倾)、S/N(感觉/直觉)、T/F(思维/情感)、J/P(判断/感知)", "生成专属16型人格报告，推荐高度契合的大学专业方向"]
    ]
    create_styled_table(doc, scale_headers, scale_data, [Inches(1.3), Inches(1.5), Inches(1.8), Inches(1.4)])
    
    add_figure(doc, "screenshots/08_ai_assessment.png", "图 5-1：AI智能测评模块主页（三大测评量表列表）")

    add_heading_2(doc, "5.2 参与测评与答题流程")
    test_steps = [
        ("选择感兴趣的量表", "在【AI测评】页面，点击目标量表卡片右侧的【查看详情】按钮（如：MBTI性格测评）。"),
        ("阅读测评指引与注意事项", "进入测评介绍页，仔细阅读测评说明。测评没有对错之分，凭第一直觉作答即可。"),
        ("点击【开始测评】进行在线作答", "点击【开始测评】进入问卷答题流，系统逐道展示情景选择题，点击选择对应选项。"),
        ("查看与生成测评综合报告", "全部题目作答完毕后，系统将自动计算维度得分，并在【个人中心】->【我的测评】中生成图文并茂的分析报告，为后续专业挑选提供客观参考。")
    ]
    for t_title, t_desc in test_steps:
        add_bullet(doc, t_desc, bold_prefix=t_title + "：")

    add_figure(doc, "screenshots/10_mbti_detail.png", "图 5-2：MBTI性格测评详情与开始测评界面")

    # -------------------------------------------------------------
    # CHAPTER 6: MANAGE VOLUNTEER LIST & EXCEL EXPORT
    # -------------------------------------------------------------
    add_heading_1(doc, "第六章：志愿单精修——管理、拖拽排序与 Excel 导出")
    add_styled_paragraph(doc, "当我们在【志愿填报】界面将心仪的高校专业组逐一添加至志愿单后，必须进入【我的志愿单】进行最终的微调、排序和导出，确保完全符合本省高考志愿表的格式要求。")
    
    add_heading_2(doc, "6.1 进入我的志愿单")
    add_styled_paragraph(doc, "进入【个人中心】，在左侧菜单栏点击【我的志愿单】，右侧将展示您当前批次已添加的所有院校专业组列表。")
    
    add_figure(doc, "screenshots/09_my_volunteer_list.png", "图 6-1：个人中心 - 我的志愿单管理与操作面板")

    add_heading_2(doc, "6.2 核心操作功能全解")
    op_items = [
        ("拖拽自由调序", "鼠标长按表格行左侧或拖拽手柄，即可上下拖动调整该专业组在平行志愿中的先后顺序。松开鼠标后，系统会自动保存最新的排序序号。"),
        ("按录取比例一键自动排序", "点击表格上方的【按录取比例自动排序】按钮，AI系统将按照各院校专业组的预测录取概率由低到高（冲 -> 稳 -> 保）进行智能梯度排列，防止出现“高分志愿垫底”的倒挂现象。"),
        ("单项删除与清空重选", "对不再考虑的专业组，可点击右侧的【删除】按钮将其移出志愿单。"),
        ("一键导出标准 Excel 志愿表", "点击顶部的【导出Excel】按钮，系统将自动生成标准格式的 `.xlsx` 电子表格并下载至本地电脑。表格中包含志愿序号、院校代码、院校名称、专业组代码、专业组名称、拟填专业列表及服从调剂标记。")
    ]
    for o_title, o_desc in op_items:
        add_bullet(doc, o_desc, bold_prefix=o_title + "：")

    add_callout(doc, "导出后的Excel表格可直接打印出来，供全家人围坐在一起逐项复核讨论；在各省教育考试院正式填报系统开放时，亦可对照该Excel表格中的院校代码与专业代码逐一录入，确保万无一失！", title="填报终极步骤：打印复核", callout_type="tip")

    # -------------------------------------------------------------
    # CHAPTER 7: FAQS & COMMON PITFALLS
    # -------------------------------------------------------------
    add_heading_1(doc, "第七章：新手必读常见问题与排坑答疑（FAQ）")
    
    faqs = [
        ("Q1：为什么在【志愿填报】点击智能检索后，查询结果显示为空？",
         "答：产生该情况通常有以下三种原因：\n"
         "① 批次未选择：请检查是否已在【录取批次】中点击了具体批次（如“本科批”）；\n"
         "② 筛选条件过于严苛：例如同时勾选了“985院校”且将省份限定在偏远省份，导致该交集下无招生计划。建议点击各筛选标签的“不限”先放开限制；\n"
         "③ 选科冲突：部分高校专业组对选科有严格限定（如只招首选历史），考生首选物理则不会被检索出来，此属于系统选科规则保护。"),
        
        ("Q2：提示“请完善成绩信息”或无法跳转填报页面怎么办？",
         "答：首次登录的新账号，系统会自动检测是否已在【个人中心】录入考生的省份、选科与位次。请直接点击右上角进入【个人信息】，将分数、位次补充完整后点击保存即可解除限制。"),
        
        ("Q3：个人信息中的“剩余修改机会”用完了怎么办？",
         "答：系统默认提供充足的修改次数（如初始31次以上），足以应对平时模拟考试与高考放榜后的成绩调整。高考放榜后系统还会赠送新的修改机会。如确实误操作耗尽，请联系系统管理员或客服专线进行后台重置。"),
        
        ("Q4：新高考专业组模式下，多个专业组可以报同一个大学吗？",
         "答：完全可以！在院校专业组志愿填报中，同一所大学的不同专业组被视为互相独立的“志愿项”。例如考生可以在第1个志愿报“北京大学（专业组01）”，在第2个志愿报“北京大学（专业组02）”，相互之间互不影响。"),
        
        ("Q5：平行志愿被退档后，后面的志愿还能继续投档吗？",
         "答：绝对不能！这是平行志愿最容易让新手踩坑的规则！一个录取批次内，考生的电子档案一旦被投档进入某所高校，无论何种原因被该高校退档（如不服从专业调剂、身体条件不符等），该批次的所有后续志愿立即全部作废失效，考生只能等待该批次的“征集志愿”或者跌入下一批次。因此务必确保所填专业体检合格且务必勾选服从调剂！"),
        
        ("Q6：如何修改已绑定的登录密码？",
         "答：进入【个人中心】，在左侧菜单栏点击【修改密码】，输入当前旧密码以及两次输入一致的新密码，点击提交即可完成修改。请妥善保管新密码，切勿泄露给第三方机构。")
    ]
    
    for q, a in faqs:
        add_heading_2(doc, q)
        for line in a.split('\n'):
            add_styled_paragraph(doc, line, space_after=3)

    # -------------------------------------------------------------
    # EPILOGUE
    # -------------------------------------------------------------
    add_heading_1(doc, "结语：预祝金榜题名 · 步入理想学府")
    add_styled_paragraph(doc, "高考是人生旅途中的重要驿站，而科学、严谨、深思熟虑的志愿填报将为您的理想大学生活铺平道路。聪志愿AI平台全体团队预祝每一位莘莘学子都能精准定位优势，在心仪的高校与热爱的专业中扬帆起航、成就非凡未来！")
    add_styled_paragraph(doc, "如在使用系统过程中有任何疑问或改进建议，欢迎随时联系平台专属顾问或技术支持团队。")
    
    # Save document
    output_path = r"E:\Silin7 Git\CONGZHIYUAN\congzhiyuan-website\聪志愿AI智能志愿填报系统-新手保姆级操作手册.docx"
    doc.save(output_path)
    print(f"Manual saved successfully to: {output_path}")

if __name__ == "__main__":
    generate_manual()
