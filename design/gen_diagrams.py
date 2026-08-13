#!/usr/bin/env python3
"""生成门店潜力评估作品集的 draw.io XML 图（可导入 ProcessOn）。
用法：python3 gen_diagrams.py
输出：design/ 下 7 个 .drawio 文件，均为规范 mxGraphModel 格式。
"""
import os

BASE = '/Users/lifanghao/Desktop/门店潜力评估产品作品集/design'

# ---------- 样式常量 ----------
SW = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#d8f3ec;strokeColor=#0c7a6b;fontColor=#0a5e53;fontStyle=1;'
SW2 = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#fff3df;strokeColor=#e98a15;fontColor=#9a5600;fontStyle=1;'
SB = 'rounded=0;whiteSpace=wrap;html=1;fillColor=#eef3f6;strokeColor=#5e6d78;fontColor=#14212b;'
SD = 'rounded=0;whiteSpace=wrap;html=1;fillColor=#13232d;strokeColor=#13232d;fontColor=#eef6f7;fontStyle=1;'
ST = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#bdc9d3;fontColor=#14212b;'
EDGE = 'endArrow=block;html=1;strokeColor=#0c7a7b;strokeWidth=1.5;fontColor=#5e6d78;'
EDGE_R = 'endArrow=block;html=1;strokeColor=#e98a15;strokeWidth=1.5;fontColor=#9a5600;'

def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;').replace('\n', '&#10;'))

def mx_vertex(vid, x, y, w, h, label, style, raw_label=False):
    """raw_label=True 时 label 已转义/含HTML."""
    lab = label if raw_label else esc(label)
    return (f'<mxCell id="{vid}" value="{lab}" style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')

def mx_edge(eid, src, tgt, label='', style=EDGE):
    lab = '' if not label else f' value="{esc(label)}"'
    return (f'<mxCell id="{eid}" style="{style}" edge="1" parent="1" source="{src}" target="{tgt}"{lab}>'
            '<mxGeometry relative="1" as="geometry"/></mxCell>')

def xml_wrap(cells, w=1400, h=900, gx=10, gy=10, bg='#ffffff'):
    body = ''.join(cells)
    return (f'<mxfile host="app.diagrams.net" modified="" agent="drawio" version="24.0.0">'
            f'<diagram id="d1" name="Page-1">'
            f'<mxGraphModel dx="{w}" dy="{h}" grid="1" gridSize="10" guides="1" '
            f'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
            f'pageWidth="1169" pageHeight="827" math="0" shadow="0">'
            f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>'
            f'{body}</root></mxGraphModel></diagram></mxfile>')

# ============================================================
# 图1：门店画像-线框图
# ============================================================
def fig_store_profile():
    c = []
    # 画布底色 + 说明
    c.append(mx_vertex('bg', -60, -60, 1300, 900, '', 'rounded=0;whiteSpace=wrap;html=1;fillColor=#f7f4ee;strokeColor=none;', raw_label=True))
    c.append(mx_vertex('t1', 0, 0, 300, 30, '门店画像页 · 线框图 (v2)', 'text;html=1;fontColor=#0a5e53;fontStyle=1;fontSize=16;'))
    # 顶部统计 hero
    c.append(mx_vertex('hero', 20, 40, 860, 90, '顶部统计区\n门店数10 · 高潜2 · 平均潜力分62 · 均单店GMV · 缺货3 · 业态6', SD))
    # 左侧：门店池列表
    c.append(mx_vertex('ls', 20, 150, 300, 500, '门店池列表（左侧）', SB))
    c.append(mx_vertex('ls1', 30, 200, 280, 50, '搜索框 ｜ 城市层级 ｜ 业态 ｜ 潜力分层', ST))
    c.append(mx_vertex('ls2', 30, 260, 280, 40, 'S001 上海万航便利店  潜力86.6 高潜', ST))
    c.append(mx_vertex('ls3', 30, 305, 280, 40, 'S002 杭州江南小馆  潜力70.6 成长', ST))
    c.append(mx_vertex('ls4', 30, 350, 280, 40, 'S003 成都玉林烟酒  潜力66.7 基础', ST))
    c.append(mx_vertex('ls5', 30, 395, 280, 40, 'S008 昆明云岭便利店  潜力87.5 高潜', ST))
    c.append(mx_vertex('ls6', 30, 440, 280, 40, 'S010 县城家家福  潜力21.5 低效', ST))
    c.append(mx_vertex('ls7', 30, 490, 280, 30, '… 共 10 家 · 可搜索筛选', 'text;html=1;fontColor=#5e6d78;'))
    # 右侧：详情区
    c.append(mx_vertex('rs', 340, 150, 540, 520, '画像详情区（右侧）', SB))
    c.append(mx_vertex('r1', 350, 200, 240, 80, '潜力分区块\nfinal 86.6 · 高潜 · 分位0.866\nraw 83.8 → 校准 86.6 · 风险0', SW))
    c.append(mx_vertex('r2', 600, 200, 270, 80, '五维雷达图（SVG）\nbase/asset/perf/opp/reach\n+ Top3 驱动', SW2))
    c.append(mx_vertex('r3', 350, 290, 240, 60, '企业视角概览\n企业订单¥96,800 · 渗透中高', ST))
    c.append(mx_vertex('r4', 600, 290, 270, 60, '核心经营指标\nGMV/订单/客单/活跃/SKU/排面', ST))
    c.append(mx_vertex('r5', 350, 360, 240, 80, 'AI 洞察\n事实依据 / 经营判断', SW))
    c.append(mx_vertex('r6', 600, 360, 270, 80, '推荐动作 + 近90天信号', SW2))
    c.append(mx_vertex('r7', 350, 450, 240, 60, '企业机会标签 · 机会品类', ST))
    c.append(mx_vertex('r8', 600, 450, 270, 60, '竞品 · 库存资产 · 拜访协议', ST))
    c.append(mx_vertex('r9', 350, 520, 520, 60, '门店全局标签 · 企业视角标签 · AI提示词面板', ST))
    c.append(mx_vertex('note', 20, 670, 860, 40, '说明：可交互高保真原型见 prototype/门店画像_v2.html；本图用于展示信息架构与页面布局。', 'text;html=1;fontColor=#9a5600;fontSize=12;'))
    return xml_wrap(c, 1300, 760)

# ============================================================
# 图2：标签库后台-线框图
# ============================================================
def fig_admin():
    c = []
    c.append(mx_vertex('bg', -60, -60, 1300, 940, '', 'rounded=0;whiteSpace=wrap;html=1;fillColor=#f3f6f8;strokeColor=none;', raw_label=True))
    c.append(mx_vertex('t1', 0, 0, 300, 30, '标签库管理后台 · 线框图 (v2)', 'text;html=1;fontColor=#0a5e53;fontStyle=1;fontSize=16;'))
    # 左侧导航
    c.append(mx_vertex('nav', 20, 40, 200, 520, '左侧导航', SD))
    c.append(mx_vertex('nav1', 30, 85, 180, 35, '① 标签总览与分析', SW))
    c.append(mx_vertex('nav2', 30, 128, 180, 35, '② 打分模型配置', SW))
    c.append(mx_vertex('nav3', 30, 171, 180, 35, '③ Knowhow 知识库', SW))
    c.append(mx_vertex('nav4', 30, 214, 180, 35, '④ Skill 注册与调用', SW))
    c.append(mx_vertex('nav5', 30, 257, 180, 35, '⑤ 数据接入(规划)', SW2))
    c.append(mx_vertex('nav6', 30, 310, 180, 80, '标签来源映射\n门店/订单/拜访/库存\n竞品/协议/AI推断', SB))
    # 主区
    c.append(mx_vertex('hero', 240, 40, 640, 110, 'Hero · 门店标签从定义到发布全流程\nKPI: 标签总数128 · 覆盖门店483万 · 异常告警11 · 发布批次9', SD))
    c.append(mx_vertex('tb', 240, 170, 640, 150, '标签列表与分组管理\n搜索/筛选(对象/分组/状态/来源) · 标签表(编码/优先级/覆盖/发布)', SB))
    c.append(mx_vertex('det', 240, 340, 640, 120, '标签详情\n口径 · 数据血缘 · 规则配置 · AI提示词 · 版本 · 权限 · 审批流 · 效果回溯', SW))
    c.append(mx_vertex('cov', 240, 480, 640, 90, '覆盖预估与模拟圈选\n命中门店82,460 · 可转化GMV¥1.28亿 · 规则可信度89% · 样本预览', SW2))
    c.append(mx_vertex('note', 20, 580, 860, 40, '说明：可交互高保真原型见 prototype/标签库管理后台_v2.html；本图展示后台信息架构。', 'text;html=1;fontColor=#9a5600;fontSize=12;'))
    return xml_wrap(c, 1300, 680)

# ============================================================
# 图3：潜力打分流程
# ============================================================
def fig_score_flow():
    c = []
    steps = [
        ('p1', 20, 80, '企业-门店宽表\ntenant_store 指标集', SW),
        ('p2', 210, 80, '入参校验\n权重和≈100% · 日期/窗口合法', SB),
        ('p3', 400, 80, '维度评分\n5维 × 24指标 → 0-100\n引用 K1/K2 Knowhow', SW2),
        ('p4', 590, 80, '加权合成\nraw = Σ(维度×权重)', SW),
        ('p5', 780, 80, '风险扣分\n缺货/占压/断档/低转化', SB),
        ('p6', 970, 80, '分位校准\nraw→全库分位\n+ 分层(85/70/50)', SW2),
        ('p7', 1160, 80, '输出 score JSON\nfinal + 五维 + 证据链', SW),
    ]
    for i, (vid, x, y, lab, st) in enumerate(steps):
        c.append(mx_vertex(vid, x, y, 170, 90, lab, st))
        if i:
            c.append(mx_edge(f'e{i}', steps[i-1][0], vid, '', EDGE))
    c.append(mx_vertex('note', 20, 220, 1320, 40, '最终分 final = clamp(加权合成 − 风险扣分) 再分位校准 → 高潜/成长/基础/低效；所有参数为示例值，待真实数据校准。', 'text;html=1;fontColor=#9a5600;fontSize=12;'))
    return xml_wrap(c, 1380, 320)

# ============================================================
# 图4：标签生成流程
# ============================================================
def fig_tag_flow():
    c = []
    c.append(mx_vertex('t1', 20, 40, 170, 80, '企业-门店宽表', SW))
    c.append(mx_vertex('t2', 240, 40, 190, 80, '普通标签 L1-L3\n规则引擎直接计算', SW2))
    c.append(mx_vertex('t3', 480, 40, 210, 80, 'AI 高阶标签 L4\n提示词 + 推理', SW))
    c.append(mx_vertex('t4', 740, 40, 190, 80, '标签 JSON\n值 + 置信度 + 证据', SW2))
    c.append(mx_vertex('t5', 980, 40, 180, 80, '标签库管理后台\n治理 · 审批 · 发布', SB))
    c.extend([
        mx_edge('e1', 't1', 't2'), mx_edge('e2', 't1', 't3'),
        mx_edge('e3', 't2', 't4'), mx_edge('e4', 't3', 't4'),
        mx_edge('e5', 't4', 't5'),
    ])
    c.append(mx_vertex('kb', 240, 160, 450, 60, 'Knowhow 支撑：K1指标口径 · K2基准阈值 · K3场景知识 · K4动作库', SD))
    c.append(mx_edge('e6', 'kb', 't2', '', EDGE_R))
    c.append(mx_edge('e7', 'kb', 't3', '', EDGE_R))
    return xml_wrap(c, 1200, 280)

# ============================================================
# 图5：门店画像流程
# ============================================================
def fig_profile_flow():
    c = []
    c.append(mx_vertex('a1', 20, 60, 170, 80, 'score JSON\n(打分结果)', SW))
    c.append(mx_vertex('a2', 250, 60, 170, 80, 'tags JSON\n(标签结果)', SW2))
    c.append(mx_vertex('a3', 480, 60, 190, 80, '明细摘要\n订单/库存/竞品/协议', SB))
    c.append(mx_vertex('a4', 720, 60, 180, 80, 'AI 画像生成\n提示词 + 约束', SW))
    c.append(mx_vertex('a5', 950, 60, 200, 80, '画像 JSON\n一句话/事实/判断/动作/风险', SW2))
    c.extend([
        mx_edge('e1', 'a1', 'a4'), mx_edge('e2', 'a2', 'a4'), mx_edge('e3', 'a3', 'a4'),
        mx_edge('e4', 'a4', 'a5'),
    ])
    c.append(mx_vertex('kb', 480, 180, 450, 50, 'Knowhow K3 场景模板 · K4 动作库（支撑画像判断与推荐）', SD))
    c.append(mx_edge('e5', 'kb', 'a4', '', EDGE_R))
    return xml_wrap(c, 1200, 280)

# ============================================================
# 图6：模拟圈选流程
# ============================================================
def fig_seg_flow():
    c = []
    c.append(mx_vertex('s1', 20, 60, 180, 80, '选择圈选标签\n如：高潜力待突破门店', SW))
    c.append(mx_vertex('s2', 250, 60, 190, 80, '运行圈选规则\n跑 600 万门店', SW2))
    c.append(mx_vertex('s3', 490, 60, 180, 80, '预估命中规模\n门店数 · 城市分布', SB))
    c.append(mx_vertex('s4', 720, 60, 180, 80, '预估可转化 GMV\n价值估算', SW))
    c.append(mx_vertex('s5', 950, 60, 200, 80, '规则可信度 + 样本预览\n确认是否投放', SW2))
    c.append(mx_vertex('s6', 950, 160, 200, 60, '确认 → 正式圈选\n推送给企业', SW))
    c.extend([
        mx_edge('e1', 's1', 's2'), mx_edge('e2', 's2', 's3'),
        mx_edge('e3', 's3', 's4'), mx_edge('e4', 's4', 's5'),
        mx_edge('e5', 's5', 's6'),
    ])
    c.append(mx_vertex('note', 20, 240, 900, 40, '说明：当前为演示原型(内置示例值)；真实圈选需等 600 万真实数据接入后运行。', 'text;html=1;fontColor=#9a5600;fontSize=12;'))
    return xml_wrap(c, 1180, 320)

# ============================================================
# 图7：系统架构图
# ============================================================
def fig_arch():
    c = []
    c.append(mx_vertex('l1', 40, 40, 1120, 70, '应用层：门店画像 v2 · 标签库管理后台 v2', SD))
    c.append(mx_vertex('l2', 40, 150, 1120, 90, '服务层（5 个 Skill · 标准输入输出 JSON Schema）\nsk-potential-score → sk-tag-engine → sk-store-profile → sk-recommend ｜ sk-demo(造数/校验)', SW))
    c.append(mx_vertex('l3', 40, 280, 1120, 80, '汇总层：ads 宽表（企业-门店滚动指标）\n规模/活跃/渗透/库存/竞争/资源', SW2))
    c.append(mx_vertex('l4', 40, 400, 1120, 90, '明细层：ODS 原始 → DWD 清洗 → DIM 维表\n订单 / 拜访 / 库存上报 / 竞品上报 / 活动协议 / 资产盘点', SB))
    c.extend([
        mx_edge('e1', 'l4', 'l3'), mx_edge('e2', 'l3', 'l2'), mx_edge('e3', 'l2', 'l1'),
    ])
    c.append(mx_vertex('kh', 40, 530, 520, 60, 'Knowhow：K1指标口径 · K2基准阈值 · K3场景 · K4动作', SW))
    c.append(mx_vertex('cal', 590, 530, 570, 60, '参数校准：示例值 → 600 万分布重拟合 → 版本化发布', SW2))
    c.extend([
        mx_edge('e4', 'kh', 'l2', '', EDGE_R), mx_edge('e5', 'cal', 'l2', '', EDGE_R),
    ])
    return xml_wrap(c, 1200, 620)

# ============================================================
# 写文件
# ============================================================
FIGS = {
    '原型线框图/门店画像-线框图.drawio': fig_store_profile,
    '原型线框图/标签库后台-线框图.drawio': fig_admin,
    '流程图/01-潜力打分流程.drawio': fig_score_flow,
    '流程图/02-标签生成流程.drawio': fig_tag_flow,
    '流程图/03-门店画像流程.drawio': fig_profile_flow,
    '流程图/04-模拟圈选流程.drawio': fig_seg_flow,
    '架构图/系统架构图.drawio': fig_arch,
}

if __name__ == '__main__':
    for rel, fn in FIGS.items():
        path = os.path.join(BASE, rel)
        xml = fn()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(xml)
        print(f'已生成 {rel} ({os.path.getsize(path)} bytes)')
    print('全部完成')
PY