#!/usr/bin/env python3
"""把 design/ 下 7 张 drawio 图渲染成一个自包含 HTML 预览页。
用法：python3 render_diagrams.py  →  生成 design/_预览_全部图.html
浏览器打开即可查看每张图的布局（含连线）。
"""
import os, re, html, math

BASE = '/Users/lifanghao/Desktop/门店潜力评估产品作品集/design'
OUT = os.path.join(BASE, '_预览_全部图.html')

def parse(f):
    txt = open(f, encoding='utf-8').read()
    verts = re.findall(
        r'<mxCell id="([^"]+)" value="([^"]*)" style="([^"]*)" vertex="1" parent="1">'
        r'<mxGeometry x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', txt)
    edges = re.findall(
        r'<mxCell id="([^"]+)" style="([^"]*)" edge="1" parent="1" source="([^"]+)" target="([^"]+)"', txt)
    def pos(vid):
        for v in verts:
            if v[0] == vid:
                return float(v[3]), float(v[4]), float(v[5]), float(v[6])
        return 0, 0, 10, 10
    return verts, edges, pos

def color_of(style):
    m = re.search(r'fillColor=#([0-9a-fA-F]{6})', style)
    return '#' + m.group(1) if m else '#ffffff'

def font_color(style):
    m2 = re.search(r'fontColor=#([0-9a-fA-F]{6})', style)
    return '#' + m2.group(1) if m2 else '#14212b'

def render_fig(f, title):
    verts, edges, pos = parse(f)
    # 画布范围
    xs = [float(v[3]) for v in verts] + [float(v[3])+float(v[5]) for v in verts]
    ys = [float(v[4]) for v in verts] + [float(v[4])+float(v[6]) for v in verts]
    minx, miny = min(xs)-20, min(ys)-20
    w = max(xs)-minx+40; h = max(ys)-miny+40
    # 背景
    bg = '<rect x="0" y="0" width="%d" height="%d" fill="#f7f5f0" rx="8"/>' % (w, h)
    # 边
    edge_svg = ''
    for eid, style, src, tgt in edges:
        x1,y1,w1,h1 = pos(src); x2,y2,w2,h2 = pos(tgt)
        cx1, cy1 = x1+w1/2, y1+h1/2
        cx2, cy2 = x2+w2/2, y2+h2/2
        edge_svg += f'<line x1="{cx1-minx}" y1="{cy1-miny}" x2="{cx2-minx}" y2="{cy2-miny}" stroke="#0c7a6b" stroke-width="2"/>'
        # 箭头
        ang = math.atan2(cy2-cy1, cx2-cx1)
        ax, ay = cx2-minx-12*math.cos(ang), cy2-miny-12*math.sin(ang)
        for da in (0.4, -0.4):
            edge_svg += f'<line x1="{ax}" y1="{ay}" x2="{ax-8*math.cos(ang+da)}" y2="{ay-8*math.sin(ang+da)}" stroke="#0c7a6b" stroke-width="2"/>'
    # 节点
    node_svg = ''
    for vid, val, style, x, y, w2, h2 in verts:
        if vid in ('0', '1'): continue
        label = html.escape(val.replace('&#10;', '<br/>'))
        fill = color_of(style)
        fc = font_color(style)
        node_svg += (f'<g><rect x="{float(x)-minx}" y="{float(y)-miny}" width="{float(w2)}" height="{float(h2)}" '
                     f'fill="{fill}" stroke="#b0b0b0" rx="8"/><text x="{float(x)-minx+float(w2)/2}" '
                     f'y="{float(y)-miny+float(h2)/2}" text-anchor="middle" dominant-baseline="middle" '
                     f'font-size="12" fill="{fc}">{label}</text></g>')
    return (f'<div class="fig"><h3>{title}</h3>'
            f'<div class="wrap"><svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{bg}{edge_svg}{node_svg}</svg></div></div>')

def main():
    figs = [
        ('原型线框图/门店画像-线框图.drawio', '门店画像-线框图'),
        ('原型线框图/标签库后台-线框图.drawio', '标签库后台-线框图'),
        ('流程图/01-潜力打分流程.drawio', '潜力打分流程'),
        ('流程图/02-标签生成流程.drawio', '标签生成流程'),
        ('流程图/03-门店画像流程.drawio', '门店画像流程'),
        ('流程图/04-模拟圈选流程.drawio', '模拟圈选流程'),
        ('架构图/系统架构图.drawio', '系统架构图'),
    ]
    body = ''
    for rel, title in figs:
        body += render_fig(os.path.join(BASE, rel), title)
    page = f"""<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8"><title>作品集 · 图预览</title>
<style>
body{{font-family:'PingFang SC','Microsoft YaHei',sans-serif;background:#ece8e0;margin:0;padding:24px;color:#2f261d}}
h1{{font-size:22px}} .fig{{background:#fff;border-radius:14px;padding:16px;margin:14px 0;box-shadow:0 2px 10px rgba(0,0,0,.06)}}
.fig h3{{margin:0 0 12px;font-size:16px;color:#0a5e53}}
.wrap{{overflow:auto;max-width:100%}} svg{{display:block}}
</style></head><body><h1>门店售卖潜力评估 · 设计图预览</h1>
<p>以下为 7 张设计图的布局预览（draw.io 源文件在 design/ 下，可导入 ProcessOn）。</p>
{body}</body></html>"""
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(page)
    print('已生成:', OUT)

if __name__ == '__main__':
    main()
