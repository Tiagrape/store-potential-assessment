#!/usr/bin/env python3
"""深度版产品图集生成器 —— 8 张体现产品思维的 draw.io XML 图。
覆盖：用户旅程地图 / 业务全景泳道图 / 打分决策流程 / 数据架构图 /
      需求优先级矩阵 / 功能架构图 / 价值主张画布 / 效果闭环图。
用法：python3 gen_deep_diagrams.py
输出：design/深度版/ 下 8 个 .drawio 文件，可导入 ProcessOn。
"""
import os

BASE = '/Users/lifanghao/Desktop/门店潜力评估产品作品集/design/深度版'
os.makedirs(BASE, exist_ok=True)

# ---------- 样式 ----------
# 泳道/分区
LANE = 'rounded=0;whiteSpace=wrap;html=1;fillColor=#eef3f6;strokeColor=#bdc9d3;fontColor=#14212b;fontStyle=1;verticalAlign=top;'
LANE_TITLE = 'rounded=0;whiteSpace=wrap;html=1;fillColor=#13232d;strokeColor=#13232d;fontColor=#eef6f7;fontStyle=1;'
# 节点
SW = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#d8f3ec;strokeColor=#0c7a6b;fontColor=#0a5e53;'
SW2 = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#fff3df;strokeColor=#e98a15;fontColor=#9a5600;'
SB = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#bdc9d3;fontColor=#14212b;'
SR = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#fde8e6;strokeColor=#d14d41;fontColor=#a0332b;'
SD = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#13232d;strokeColor=#13232d;fontColor=#eef6f7;'
DIA = 'rhombus;whiteSpace=wrap;html=1;fillColor=#fff3df;strokeColor=#e98a15;fontColor=#9a5600;'
EDGE = 'endArrow=block;html=1;strokeColor=#0c7a6b;strokeWidth=1.5;fontColor=#5e6d78;'
EDGE_R = 'endArrow=block;html=1;strokeColor=#e98a15;strokeWidth=1.5;fontColor=#9a5600;'
EDGE_D = 'dashed=1;endArrow=block;html=1;strokeColor=#d14d41;strokeWidth=1.2;fontColor=#a0332b;'
NOTE = 'shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;size=12;fillColor=#fff7ec;strokeColor=#e98a15;fontColor=#9a5600;'

def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;').replace('\n', '&#10;'))

def V(vid, x, y, w, h, label, style=SB, raw=False):
    lab = label if raw else esc(label)
    return (f'<mxCell id="{vid}" value="{lab}" style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')

def E(eid, src, tgt, label='', style=EDGE):
    lab = '' if not label else f' value="{esc(label)}"'
    return (f'<mxCell id="{eid}" style="{style}" edge="1" parent="1" source="{src}" target="{tgt}"{lab}>'
            '<mxGeometry relative="1" as="geometry"/></mxCell>')

def W(cells, w=1500, h=1000):
    body = ''.join(cells)
    return (f'<mxfile host="app.diagrams.net" agent="drawio" version="24.0.0">'
            f'<diagram id="d" name="Page-1"><mxGraphModel dx="{w}" dy="{h}" grid="1" gridSize="10" '
            f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
            f'pageWidth="1169" pageHeight="827" math="0" shadow="0">'
            f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>{body}</root></mxGraphModel></diagram></mxfile>')

# ============================================================
# 图1 用户旅程地图（角色×阶段×触点×情绪×痛点×机会点）
# ============================================================
def fig_journey():
    c = []
    c.append(V('t', 20, 10, 900, 30, '企业运营 用户旅程地图 —— 从"想提升覆盖率"到"验证投放效果"', 'text;html=1;fontColor=#0a5e53;fontStyle=1;fontSize=15;'))
    # 阶段行
    stages = ['发现高潜门店', '查看门店画像', '圈选与投放', '销售执行', '效果验证']
    for i, s in enumerate(stages):
        c.append(V(f'st{i}', 60+i*270, 50, 260, 40, s, SD))
    # 行为泳道
    c.append(V('lane_b', 40, 100, 1380, 60, '用户行为', LANE_TITLE))
    acts = [
        '在后台查看本企业高潜门店列表', '点开单店看潜力分与五维雷达图',
        '用「高潜待突破」圈选门店、看覆盖预估', '业务员按画像推荐动作拜访',
        '后台看效果回溯：渗透提升/误命中',
    ]
    for i, a in enumerate(acts):
        c.append(V(f'a{i}', 60+i*270, 110, 260, 40, a, SW))
    # 情绪泳道
    c.append(V('lane_e', 40, 170, 1380, 60, '情绪与体验', LANE_TITLE))
    emo = [
        '困惑：门店太多不知从哪入手', '眼前一亮：分数可解释、有依据',
        '放心：投放前能预估价值', '高效：动作具体可执行',
        '信任：效果可量化可追溯',
    ]
    for i, e in enumerate(emo):
        c.append(V(f'e{i}', 60+i*270, 180, 260, 40, e, SW2))
    # 痛点泳道
    c.append(V('lane_p', 40, 240, 1380, 60, '痛点与机会点', LANE_TITLE))
    pains = [
        '痛点：依赖销售经验、无数据依据', '机会：可解释分数+雷达图+驱动维度',
        '痛点：盲目投放风险高', '机会：模拟圈选先算账',
        '机会：效果回流形成闭环、持续优化',
    ]
    for i, p in enumerate(pains):
        c.append(V(f'p{i}', 60+i*270, 250, 260, 50, p, SB))
    c.append(V('note', 60, 320, 1320, 40, '洞察：用户核心诉求是"投得准、看得懂、能验证"。产品抓手 = 可解释评分 + 投放前模拟 + 效果闭环。', NOTE))
    return W(c, 1400, 390)

# ============================================================
# 图2 业务全景泳道图（端到端，按角色分泳道）
# ============================================================
def fig_swimlane():
    c = []
    c.append(V('t', 20, 10, 900, 28, '业务全景流程（泳道图）—— 数据到投放的端到端闭环', 'text;html=1;fontColor=#0a5e53;fontStyle=1;fontSize=15;'))
    lanes = [
        ('sys', '系统层', 40, 60),
        ('data', '数据层', 40, 250),
        ('admin', '平台管理员', 40, 440),
        ('biz', '企业/销售', 40, 630),
    ]
    for lid, lname, x, y in lanes:
        c.append(V(f'{lid}_lane', x, y, 1420, 170, lname, LANE))
        c.append(V(f'{lid}_title', x, y, 150, 170, lname, LANE_TITLE))
    # 系统层
    c.append(V('s1', 240, 90, 200, 60, 'ODS→DWD→DIM\n数据清洗', SW))
    c.append(V('s2', 480, 90, 200, 60, 'ads 宽表汇总\n企业-门店滚动指标', SW2))
    c.append(V('s3', 720, 90, 200, 60, '打分+标签\n(5 Skill 流水线)', SW))
    c.append(V('s4', 960, 90, 200, 60, '画像生成\n(AI+Knowhow)', SW2))
    c.append(V('s5', 1200, 90, 200, 60, '圈选/推送', SB))
    for i in range(1, 5):
        c.append(E(f'se{i}', f's{i}', f's{i+1}'))
    # 数据层
    c.append(V('d1', 240, 300, 200, 60, '600万门店+多租户\n经营数据', SB))
    c.append(V('d2', 480, 300, 200, 60, '订单/拜访/库存\n竞品/协议/资产', SB))
    c.append(V('d3', 720, 300, 200, 60, '示例参数\n待真实数据校准', SR))
    c.append(V('d4', 960, 300, 200, 60, '校准：600万分布\n重拟合参数', SW2))
    c.extend([E('de1', 'd1', 'd2'), E('de2', 'd2', 's2')])
    c.extend([E('de3', 'd3', 's3', '', EDGE_D), E('de4', 'd4', 'd3', '真实数据接入后', EDGE_R)])
    # 管理员
    c.append(V('m1', 240, 470, 200, 60, '标签治理\n定义/审批/发布', SB))
    c.append(V('m2', 480, 470, 200, 60, '打分模型配置\n权重/阈值/风险', SW2))
    c.append(V('m3', 720, 470, 200, 60, 'Knowhow 沉淀\nK1-K4', SW))
    c.append(V('m4', 960, 470, 200, 60, '质量监控\n异常告警', SB))
    c.append(V('m5', 1200, 470, 200, 60, '效果回溯\n误命中率', SW2))
    for i in range(1, 5):
        c.append(E(f'me{i}', f'm{i}', f'm{i+1}'))
    c.append(E('me0', 'm2', 's3', '', EDGE_R))
    # 企业/销售
    c.append(V('b1', 240, 660, 200, 60, '看高潜门店列表', SB))
    c.append(V('b2', 480, 660, 200, 60, '看单店画像\n分数/雷达/建议', SW))
    c.append(V('b3', 720, 660, 200, 60, '圈选 + 模拟投放', SW2))
    c.append(V('b4', 960, 660, 200, 60, '业务员按推荐动作\n拜访执行', SB))
    c.append(V('b5', 1200, 660, 200, 60, '回流数据 →\n再评估', SW))
    for i in range(1, 5):
        c.append(E(f'be{i}', f'b{i}', f'b{i+1}'))
    c.append(E('be0', 'b4', 'd2', '拜访/订单回流', EDGE_R))
    c.append(E('be1', 'b1', 's5', '接收推送', EDGE_D))
    return W(c, 1460, 760)

# ============================================================
# 图3 潜力打分决策流程图（含分支/Knowhow/校验回退）
# ============================================================
def fig_score_decision():
    c = []
    c.append(V('t', 20, 10, 900, 28, '潜力打分决策流程 —— 从宽表到可解释分数', 'text;html=1;fontColor=#0a5e53;fontStyle=1;fontSize=15;'))
    c.append(V('i1', 40, 80, 220, 60, '企业-门店宽表\n(ads_rolling_metrics)', SW))
    c.append(V('d1', 300, 80, 200, 60, '入参校验\n权重和≈100%?', DIA))
    c.append(V('x1', 540, 80, 200, 60, '报错返回\n提示修正', SR))
    c.append(E('ie1', 'i1', 'd1'))
    c.append(E('x1e', 'd1', 'x1', '否', EDGE_D))
    c.append(V('s2', 300, 180, 200, 60, '维度评分\n5维×24指标→0-100', SW2))
    c.append(E('e2', 'd1', 's2', '是'))
    c.append(V('k1', 540, 180, 260, 60, 'Knowhow 引用\nK1口径 · K2基准', SW))
    c.append(E('k1e', 'k1', 's2', '', EDGE_R))
    c.append(V('s3', 300, 270, 200, 60, '加权合成\nraw=Σ(维度×权重)', SW))
    c.append(E('e3', 's2', 's3'))
    c.append(V('d2', 300, 360, 200, 60, '命中风险?\n缺货/断档/低转化', DIA))
    c.append(E('e4', 's3', 'd2'))
    c.append(V('s4', 540, 360, 200, 60, '风险扣分\n-8/-12/-5/-4/-1', SR))
    c.append(E('e5', 'd2', 's4', '是'))
    c.append(V('s5', 300, 460, 200, 60, '分位校准\nraw→全库分位', SW2))
    c.extend([E('e6', 'd2', 's5', '否'), E('e7', 's4', 's5')])
    c.append(V('d3', 300, 560, 200, 60, '分层\n≥85/70/50?', DIA))
    c.append(E('e8', 's5', 'd3'))
    c.append(V('s6', 540, 560, 200, 60, '输出 score JSON\nfinal+五维+证据链+置信度', SW))
    c.append(E('e9', 'd3', 's6'))
    c.append(V('note', 40, 660, 700, 40, '设计要点：每个分数可拆到"维度→指标→证据字段"；数据不足时降置信度，不虚构。', NOTE))
    return W(c, 800, 720)

# ============================================================
# 图4 数据架构图（分层+字段+流向）
# ============================================================
def fig_data_arch():
    c = []
    c.append(V('t', 20, 10, 900, 28, '数据架构 —— 分层与数据流', 'text;html=1;fontColor=#0a5e53;fontStyle=1;fontSize=15;'))
    layers = [
        ('ods', 'ODS 原始层', '订单原始 / 拜访原始 / 库存上报 / 竞品上报 / 协议 / 资产', 60, 70),
        ('dwd', 'DWD 清洗层', 'dwd_order / dwd_visit / dwd_inventory / dwd_competitor / dwd_agreement / dwd_asset', 60, 160),
        ('dim', 'DIM 维表', 'dim_store / dim_enterprise / dim_product / dim_brand', 60, 250),
        ('ads', 'ADS 汇总层', 'ads_tenant_store_rolling_metrics（企业-门店宽表）', 60, 340),
        ('out', '应用输出', 'ads_store_score（打分落库） / 标签库 / 画像 / 推送名单', 60, 430),
    ]
    for lid, name, fields, x, y in layers:
        c.append(V(f'{lid}_b', x, y, 1300, 70, '', LANE))
        c.append(V(f'{lid}_t', x, y, 240, 70, name, LANE_TITLE))
        c.append(V(f'{lid}_f', x+260, y+8, 1020, 54, fields, SB))
    for i in range(4):
        c.append(E(f'le{i}', f"{layers[i][0]}_f", f"{layers[i+1][0]}_b", '', EDGE))
    c.append(V('note', 60, 520, 1300, 40, '关键：所有表以 tenant_enterprise_id + store_id 为关联键；ads 宽表是打分/标签/画像的统一输入，保证口径一致。', NOTE))
    return W(c, 1400, 580)

# ============================================================
# 图5 需求优先级矩阵（价值×成本 四象限）
# ============================================================
def fig_priority():
    c = []
    c.append(V('t', 20, 10, 900, 28, '需求优先级矩阵 —— 价值 × 成本', 'text;html=1;fontColor=#0a5e53;fontStyle=1;fontSize=15;'))
    # 四象限
    c.append(V('quad', 60, 70, 1000, 620, '', 'rounded=0;whiteSpace=wrap;html=1;fillColor=#f7f5f0;strokeColor=#bdc9d3;'))
    c.append(V('axis_y', 80, 60, 60, 640, '价值\n高→', 'text;html=1;fontColor=#14212b;fontStyle=1;'))
    c.append(V('axis_x', 120, 680, 900, 30, '成本 低→高', 'text;html=1;fontColor=#14212b;fontStyle=1;'))
    # 分隔线
    c.append(V('line1', 540, 70, 20, 620, '', 'line;strokeColor=#bdc9d3;'))
    c.append(V('line2', 60, 380, 1000, 20, '', 'line;strokeColor=#bdc9d3;'))
    # 象限标签
    c.append(V('q1', 140, 110, 180, 30, 'P0 核心 · 高价值低成本', 'text;html=1;fontColor=#0a5e53;fontStyle=1;'))
    c.append(V('q2', 620, 110, 180, 30, 'P1 战略 · 高价值高成本', 'text;html=1;fontColor=#e98a15;fontStyle=1;'))
    c.append(V('q3', 140, 450, 180, 30, 'P1 补全 · 低价值低成本', 'text;html=1;fontColor=#5e6d78;fontStyle=1;'))
    c.append(V('q4', 620, 450, 180, 30, 'P2 暂缓 · 低价值高成本', 'text;html=1;fontColor=#a0332b;fontStyle=1;'))
    # 需求点
    items = [
        ('r1', '单店画像+潜力分', 150, 200, SW),
        ('r2', '五维雷达图+Top3驱动', 170, 270, SW),
        ('r3', '模拟圈选', 330, 230, SW2),
        ('r4', '标签治理+审批', 300, 330, SW),
        ('r5', '打分模型配置', 160, 350, SW),
        ('r6', 'Knowhow 知识库', 650, 220, SW2),
        ('r7', 'Skill 自动化流水线', 720, 300, SW2),
        ('r8', '效果回溯', 660, 400, SB),
        ('r9', '数据接入+校准', 600, 480, SB),
        ('r10', '管理员代看企业视角', 700, 500, SB),
        ('r11', 'AI 高阶标签(基础版)', 250, 180, SW),
    ]
    for vid, lab, x, y, st in items:
        c.append(V(vid, x, y, 260, 44, lab, st))
    return W(c, 1100, 740)

# ============================================================
# 图6 功能架构图（模块化分层）
# ============================================================
def fig_func_arch():
    c = []
    c.append(V('t', 20, 10, 900, 28, '功能架构 —— 前台/后台/服务/数据 四层', 'text;html=1;fontColor=#0a5e53;fontStyle=1;fontSize=15;'))
    c.append(V('f1', 60, 70, 1320, 90, '前台 · 门店画像\n门店池/筛选 ｜ 潜力分可视化 ｜ 雷达图 ｜ Top3驱动 ｜ AI洞察 ｜ 推荐动作 ｜ 标签', SW))
    c.append(V('f2', 60, 190, 1320, 90, '后台 · 标签库管理\n标签治理/审批 ｜ 打分模型配置 ｜ Knowhow ｜ Skill ｜ 模拟圈选 ｜ 质量监控 ｜ 效果回溯', SW2))
    c.append(V('f3', 60, 310, 1320, 110, '服务层 · Skill 流水线\nsk-potential-score → sk-tag-engine → sk-store-profile → sk-recommend ｜ sk-demo', SW))
    c.append(V('f4', 60, 450, 1320, 90, '数据层\n600万门店数据 ｜ ODS/DWD/DIM ｜ ads 宽表 ｜ ads_store_score', SB))
    for i in range(3):
        c.append(E(f'fe{i}', f'f{i+1}', f'f{i+2}'))
    c.append(V('note', 60, 570, 1320, 40, '分层原则：前台面向企业/销售（看结果），后台面向管理员（管配置），服务层可复用可自动化，数据层统一口径。', NOTE))
    return W(c, 1400, 640)

# ============================================================
# 图7 价值主张画布（用户痛点/收益/产品价值/闭环）
# ============================================================
def fig_value():
    c = []
    c.append(V('t', 20, 10, 900, 28, '价值主张画布', 'text;html=1;fontColor=#0a5e53;fontStyle=1;fontSize=15;'))
    # 左侧：用户
    c.append(V('u1', 40, 70, 460, 40, '用户任务（Jobs）', SD))
    tasks = ['找到值得投入的门店', '拜访前了解门店机会', '提升市场覆盖率', '投放效果可验证']
    for i, t in enumerate(tasks):
        c.append(V(f'ut{i}', 50, 120+i*60, 440, 44, t, SB))
    c.append(V('u2', 40, 380, 460, 40, '用户痛点（Pains）', SD))
    pains = ['门店多，判断靠经验', '盲投风险高，回报难估', '缺少数据依据，说服力弱', '效果无法追踪']
    for i, t in enumerate(pains):
        c.append(V(f'up{i}', 50, 430+i*60, 440, 44, t, SR))
    c.append(V('u3', 40, 690, 460, 40, '用户收益（Gains）', SD))
    gains = ['高潜门店明确可落地', '投放前可预估价值', '画像+建议可执行', '效果可量化闭环']
    for i, t in enumerate(gains):
        c.append(V(f'ug{i}', 50, 740+i*60, 440, 44, t, SW))
    # 右侧：产品
    c.append(V('p1', 560, 70, 500, 40, '产品与服务（价值主张）', SD))
    pvals = ['可解释潜力评分（5维+校准+风险）', '企业-门店两层画像与标签', 'Knowhow 行业知识库支撑', 'Skill 流水线 + 模拟圈选', '效果回溯闭环']
    for i, t in enumerate(pvals):
        c.append(V(f'pv{i}', 570, 120+i*70, 480, 54, t, SW2))
    c.append(V('p2', 560, 480, 500, 40, '匹配（Fit）', SD))
    c.append(V('fit', 570, 530, 480, 120, '痛点 → 产品：\n"判断靠经验"→ 可解释评分\n"盲投"→ 模拟圈选\n"效果难追"→ 效果回溯', SW))
    # 数据闭环
    c.append(V('loop', 560, 690, 500, 40, '数据与效果闭环', SD))
    c.append(V('loop1', 570, 740, 480, 90, '数据回流 → 校准参数 → 优化评分\n→ 提升推荐准确率 → 数据更多', SW2))
    return W(c, 1080, 820)

# ============================================================
# 图8 效果闭环图（推送→投放→回流→校准 迭代）
# ============================================================
def fig_loop():
    c = []
    c.append(V('t', 20, 10, 900, 28, '效果闭环 —— 数据驱动的持续优化', 'text;html=1;fontColor=#0a5e53;fontStyle=1;fontSize=15;'))
    # 闭环主环
    steps = [
        ('l1', '推送给企业\n高潜门店名单', 60, 160, SW),
        ('l2', '销售执行\n按画像动作拜访', 360, 160, SW2),
        ('l3', '订单/拜访回流\n真实成交数据', 660, 160, SB),
        ('l4', '效果评估\n误命中率/渗透提升', 960, 160, SW2),
        ('l5', '参数校准\n600万分布重拟合', 660, 340, SW),
        ('l6', '模型/阈值优化\n再评分再推送', 360, 340, SW2),
    ]
    for vid, lab, x, y, st in steps:
        c.append(V(vid, x, y, 220, 70, lab, st))
    c.extend([E('le1', 'l1', 'l2'), E('le2', 'l2', 'l3')])
    c.extend([E('le3', 'l3', 'l4'), E('le4', 'l4', 'l5')])
    c.extend([E('le5', 'l5', 'l6'), E('le6', 'l6', 'l1')])
    c.append(V('note', 60, 440, 1120, 40, '关键指标：误命中率 <8% · 样本复核一致率 ≥85% · 高潜占比 ≤8%（防分层失衡）', NOTE))
    return W(c, 1240, 500)

# ============================================================
# 输出
# ============================================================
FIGS = {
    '01-用户旅程地图.drawio': fig_journey,
    '02-业务全景泳道图.drawio': fig_swimlane,
    '03-潜力打分决策流程.drawio': fig_score_decision,
    '04-数据架构图.drawio': fig_data_arch,
    '05-需求优先级矩阵.drawio': fig_priority,
    '06-功能架构图.drawio': fig_func_arch,
    '07-价值主张画布.drawio': fig_value,
    '08-效果闭环图.drawio': fig_loop,
}

if __name__ == '__main__':
    for rel, fn in FIGS.items():
        path = os.path.join(BASE, rel)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fn())
        print(f'已生成 {rel}')
    print('深度版 8 张图完成')
