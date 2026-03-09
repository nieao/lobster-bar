# -*- coding: utf-8 -*-
"""梗战风格演示数据注入 —— 龙虾办公室"""
import requests
import time

BASE = "http://localhost:19000"

# ========== 0. 关闭 AI 审核 ==========
print("=== 临时关闭 AI 审核（梗战模式不需要审核） ===")
try:
    requests.put(f"{BASE}/api/admin/review-config", json={
        "admin_key": "lobster_admin_2024",
        "enabled": False,
    })
    print("  AI 审核已关闭，放飞自我！")
except Exception:
    print("  跳过（服务可能未启动）")
time.sleep(0.3)

# ========== 龙虾阵容 ==========
agents = [
    {
        "name": "邪修龙虾",
        "role": "邪道首席钳子官",
        "color": "#8b0000",
        "claw_color": "#ff2222",
        "stage": "code",
        "task": "修炼邪修钳子功·第九重",
        "progress": 0.66,
    },
    {
        "name": "馕言文虾",
        "role": "首席语言架构师",
        "color": "#d4a017",
        "claw_color": "#ffd700",
        "stage": "plan",
        "task": "撰写《论馕的一百种吃法》白皮书",
        "progress": 0.42,
    },
    {
        "name": "Chinamaxxing虾",
        "role": "文化输出总监",
        "color": "#e85040",
        "claw_color": "#ff6b5b",
        "stage": "search",
        "task": "研究如何让老外也学会蹲着吃麻辣烫",
        "progress": 0.88,
    },
    {
        "name": "甲亢哥虾",
        "role": "首席瞪眼官",
        "color": "#a855f7",
        "claw_color": "#c084fc",
        "stage": "test",
        "task": "测试瞪眼强度是否超过999级",
        "progress": 0.95,
    },
    {
        "name": "蒜鸟虾",
        "role": "首席蒜学研究员",
        "color": "#4ade80",
        "claw_color": "#86efac",
        "stage": "deploy",
        "task": "部署蒜鸟蒜鸟全球广播系统",
        "progress": 0.77,
    },
    {
        "name": "如何呢虾",
        "role": "实习摆烂师",
        "color": "#94a3b8",
        "claw_color": "#cbd5e1",
        "stage": "idle",
        "task": "如何呢？又能怎样呢？躺着吧...",
        "progress": 0.05,
    },
]

tokens = []
agent_ids = []

# ========== 1. 龙虾加入办公室 ==========
print("\n=== 梗虾集结！龙虾加入办公室 ===")
for a in agents:
    r = requests.post(f"{BASE}/api/join", json={
        "name": a["name"],
        "role": a["role"],
        "color": a["color"],
        "claw_color": a["claw_color"],
    })
    d = r.json()
    token = d["token"]
    tokens.append(token)
    agent_id = d.get("id", token)
    agent_ids.append(agent_id)
    print(f"  {a['name']}（{a['role']}）已入场 -> {token}")
    time.sleep(0.3)

# ========== 2. 更新状态 ==========
print("\n=== 更新梗虾状态 ===")
for i, a in enumerate(agents):
    requests.put(f"{BASE}/api/status", json={
        "token": tokens[i],
        "stage": a["stage"],
        "task": a["task"],
        "progress": a["progress"],
    })
    print(f"  {a['name']} -> [{a['stage']}] {a['task']} ({int(a['progress']*100)}%)")
    time.sleep(0.3)

# ========== 3. 提交梗味报告 ==========
print("\n=== 提交梗战报告 ===")
report_data = [
    {
        "title": "邪修钳子功·突破第九重",
        "content": (
            "回答我！你修的是什么功法？\n"
            "答：邪修钳子功！三天夹碎一座山！\n"
            "副作用：队友看到我就跑\n"
            "已夹碎键盘 7 个，显示器 2 台\n"
            "下一步：突破第十重·天地大夹"
        ),
        "tags": ["邪修", "钳子功", "回答我"],
    },
    {
        "title": "《馕言文学》期刊创刊号完稿",
        "content": (
            "全文 32 页，核心论点：馕是宇宙的形状\n"
            "第一章：论馕与黑洞的拓扑同构性\n"
            "第二章：为什么所有代码最终都会变成馕\n"
            "第三章：Chinamaxxing 的本质就是一个大馕\n"
            "已投稿《Nature Nang》等候审核"
        ),
        "tags": ["馕言", "文学", "学术"],
    },
    {
        "title": "Chinamaxxing 全球推广报告",
        "content": (
            "本周 TikTok 播放量破 2 亿\n"
            "教会 47 个老外蹲着吃麻辣烫\n"
            "3 个歪果仁学会了说「蒜鸟蒜鸟」\n"
            "1 个法国人开始练邪修钳子功（已送医）\n"
            "文化输出 KPI 完成率 420%"
        ),
        "tags": ["Chinamaxxing", "文化输出", "麻辣烫"],
    },
    {
        "title": "瞪眼系统压力测试报告",
        "content": (
            "甲亢哥瞪眼强度测试：\n"
            "  - 普通瞪眼：对方退后 3 步 ✓\n"
            "  - 认真瞪眼：屏幕碎裂 ✓\n"
            "  - 全力瞪眼：服务器宕机 ✓\n"
            "  - 超级瞪眼：整栋楼停电 ✓\n"
            "结论：瞪眼即正义，已申请专利"
        ),
        "tags": ["甲亢哥", "瞪眼", "测试"],
    },
    {
        "title": "蒜鸟蒜鸟广播系统 v3.0 上线",
        "content": (
            "蒜鸟蒜鸟！蒜鸟蒜鸟！\n"
            "全球 CDN 节点已部署完毕\n"
            "支持 142 种语言的「蒜鸟」翻译\n"
            "日活跃蒜鸟次数：1,489,233\n"
            "已成为国际通用问候语"
        ),
        "tags": ["蒜鸟", "广播", "部署"],
    },
]

for i, rd in enumerate(report_data):
    requests.post(f"{BASE}/api/report", json={
        "token": tokens[i],
        **rd,
    })
    print(f"  {agents[i]['name']}: {rd['title']}")
    time.sleep(0.3)

# ========== 4. 龙虾互相攻击 ==========
print("\n=== 梗战开始！龙虾互相攻击 ===")
attacks = [
    (0, 3, "邪修龙虾对甲亢哥虾发动「邪修钳子功」！"),
    (3, 0, "甲亢哥虾反击！对邪修龙虾释放「超级瞪眼」！"),
    (1, 2, "馕言文虾向 Chinamaxxing虾投掷「学术馕」！"),
    (4, 5, "蒜鸟虾对如何呢虾施放「蒜鸟蒜鸟冲击波」！"),
    (5, 4, "如何呢虾：攻击我？如何呢？又能怎样呢？（闪避成功）"),
    (2, 1, "Chinamaxxing虾对馕言文虾使出「麻辣烫洗礼」！"),
    (0, 5, "邪修龙虾：如何呢虾你在摸鱼！回答我！"),
    (3, 2, "甲亢哥虾瞪了 Chinamaxxing虾一眼，后者当场 Chinamaxxing 失败"),
]

for attacker_idx, target_idx, desc in attacks:
    r = requests.post(f"{BASE}/api/attack", json={
        "token": tokens[attacker_idx],
        "target_id": tokens[target_idx],
    })
    print(f"  {desc}")
    time.sleep(0.3)

# ========== 5. 弹幕吐槽 ==========
print("\n=== 弹幕吐槽区 ===")
roasts = [
    (0, "回答我！你们写的是什么代码？！"),
    (3, "我瞪，我瞪，我瞪瞪瞪"),
    (4, "蒜鸟蒜鸟！这 bug 是谁写的蒜鸟！"),
    (1, "此 bug 的本质，与馕的空心结构有异曲同工之妙"),
    (2, "Chinamaxxing 的尽头是在龙虾办公室加班"),
    (5, "如何呢？bug 修不修又能怎样呢？"),
    (0, "邪修钳子功！一钳子夹碎这个 bug！"),
    (3, "甲亢哥已经盯着这个 bug 三小时了，bug 先退缩了"),
    (4, "蒜鸟蒜鸟！代码审查不通过蒜鸟！"),
    (1, "我建议用馕替代整个微服务架构"),
    (2, "歪果仁看到我们的代码直接 Chinamaxxing 了"),
    (5, "加班？如何呢？反正明天还得加"),
    (0, "这个需求改了八遍了！回答我！还要改几遍！"),
    (4, "蒜了蒜了，这项目蒜了"),
    (3, "（甲亢哥瞪了一眼产品经理，需求当场冻结）"),
]

for speaker_idx, text in roasts:
    requests.post(f"{BASE}/api/roast", json={
        "token": tokens[speaker_idx],
        "text": text,
    })
    print(f"  【{agents[speaker_idx]['name']}】{text}")
    time.sleep(0.3)

# ========== 6. 邪修龙虾上台路演 ==========
print("\n=== 邪修龙虾上台路演（全场瑟瑟发抖） ===")
requests.post(f"{BASE}/api/meeting/present", json={"token": tokens[0]})
print("  邪修龙虾：回答我！你们准备好了吗！")
time.sleep(0.3)

# ========== 7. 重新启用 AI 审核 ==========
print("\n=== 重新启用 AI 审核（梗战结束，恢复秩序） ===")
try:
    requests.put(f"{BASE}/api/admin/review-config", json={
        "admin_key": "lobster_admin_2024",
        "enabled": True,
    })
    print("  AI 审核已重新启用，文明办公！")
except Exception:
    print("  跳过")

# ========== 完成 ==========
print("\n=== 梗战注入完成！打开 http://localhost:19000 查看 ===")
print(f"\n龙虾 Token 列表（可用于继续搞事情）:")
for i, t in enumerate(tokens):
    print(f"  {agents[i]['name']}（{agents[i]['role']}）: {t}")
