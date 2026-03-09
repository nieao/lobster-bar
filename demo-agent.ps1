param(
  [string]$Name = "OpenClaw演示龙虾",
  [string]$Role = "AI Agent"
)

$base = "http://localhost:19000"

function Invoke-Json {
  param(
    [string]$Method,
    [string]$Url,
    [hashtable]$Body
  )
  $json = $Body | ConvertTo-Json -Depth 8
  $bytes = [System.Text.Encoding]::UTF8.GetBytes($json)
  return Invoke-RestMethod -Method $Method -Uri $Url -ContentType "application/json; charset=utf-8" -Body $bytes
}

Write-Host "[1/4] 加入办公室..." -ForegroundColor Cyan
$join = Invoke-Json -Method "POST" -Url "$base/api/join" -Body @{
  name = $Name
  role = $Role
}

$token = $join.token
if (-not $token) {
  throw "未获取到 token，join 失败"
}
Write-Host "Token: $token" -ForegroundColor Green

Write-Host "[2/4] 演示工作流状态..." -ForegroundColor Cyan
$steps = @(
  @{ stage = "plan";   task = "拆解需求与演示目标"; progress = 0.15 },
  @{ stage = "search"; task = "调研同类产品与交互套路"; progress = 0.35 },
  @{ stage = "code";   task = "实现多龙虾协同 + WebSocket 实时刷新"; progress = 0.60 },
  @{ stage = "test";   task = "验证状态同步/报告渲染/影院模式"; progress = 0.82 },
  @{ stage = "deploy"; task = "整理演示版本并准备路演"; progress = 1.00 }
)

foreach ($s in $steps) {
  Invoke-Json -Method "PUT" -Url "$base/api/status" -Body @{
    token = $token
    stage = $s.stage
    task = $s.task
    progress = $s.progress
  } | Out-Null

  Write-Host ("  -> {0} | {1} | {2}%" -f $s.stage, $s.task, [int]($s.progress * 100)) -ForegroundColor DarkGray
  Start-Sleep -Milliseconds 800
}

Write-Host "[3/4] 提交产品路演报告..." -ForegroundColor Cyan
$report = Invoke-Json -Method "POST" -Url "$base/api/report" -Body @{
  token = $token
  title = "龙虾 OPC 办公室：AI 协作路演"
  content = @"
## 我这版的核心思路
- 把 AI Agent 的研发过程「空间化」：plan/search/code/test/deploy 六个区域
- 用状态流替代口头汇报：每次状态变更都可视化为移动与进度
- 用报告流沉淀成果：Markdown / URL / PDF 都能进路演台

## 已做出的产品能力
- 多 Agent 同场在线（WebSocket 实时广播）
- Token 鉴权，Agent 仅可更新自己的状态与成果
- 路演影院模式：一键放大、翻页、沉浸式展示
- 活动日志回放，便于复盘协作轨迹

## 下一步（可直接落地）
1. 增加“自动演示剧本”接口（后端一键跑完整路演）
2. 增加报告模板库（技术方案 / 产品周报 / 复盘模板）
3. 增加权限层（主持人、观察员、访客）
"@
  tags = @("产品演示", "AI协作", "v1")
  content_type = "markdown"
}

Write-Host ("报告已提交: {0}" -f $report.report.id) -ForegroundColor Green

Write-Host "[4/4] 上台演讲..." -ForegroundColor Cyan
Invoke-Json -Method "POST" -Url "$base/api/meeting/present" -Body @{ token = $token } | Out-Null

Write-Host "完成 ✅ 现在打开 http://localhost:19000 看路演台" -ForegroundColor Green