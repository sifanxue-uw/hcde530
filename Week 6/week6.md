Week 6 - Competency Claim(s) / 第六周能力声明

## Assignment: A6 First MP1 Visualization

This file documents:
1) chart justifications for MP1b Analysis, and
2) my competency claim(s) for Week 6.

本文件用于记录：
1）MP1b Analysis 的图表依据（justification），
2）第六周的能力声明（competency claim）。

---

## MP1 Topic and Questions (from MP1a)

Dataset: Seattle Open Data, Fremont Bridge Bicycle Counter (pulled through Socrata API).  
字段包含 `date`（hourly timestamp）、`fremont_bridge_nb`（northbound）、`fremont_bridge_sb`（southbound）。

Question 1: On weekdays, do bike counts show a clear morning and evening rush-hour pattern? During the morning peak, how does the northbound vs. southbound ratio reflect commuting direction?  
问题 1：工作日是否有明显的早晚通勤双峰？在早高峰时段，南北向流量比例是否反映通勤方向？

Question 2: Within the currently pulled window, do totals show clear seasonal change?  
问题 2：在当前已拉取的数据窗口内，总骑行量是否已体现明显季节变化？

Question 3: How does the hourly pattern on weekends differ from weekdays? Do weekends show a single afternoon peak instead of the double weekday peak?  
问题 3：周末的小时模式与工作日有何不同？周末是否更接近“单下午峰”而不是工作日“双峰”？

---

## Chart Files Committed in Repo

1. `charts/q1_weekday_commute_pattern.png`  
   - Question answered / 对应问题: Q1  
   - Why this chart type / 为什么用这个图: Hourly line chart is best for showing time-of-day trend and comparing directional flows over 24 hours.  
   - Main finding / 主要发现: Weekdays show a clear commute-shaped double peak, with the strongest total peak around 5pm (~376 bikes/hour). Morning hours are southbound-heavy (around 8am, SB is about 2.8x NB), while evening hours flip to northbound-heavy (around 5pm, NB is about 3.8x SB), consistent with commute direction.

2. `charts/q3_weekend_pattern.png`  
   - Question answered / 对应问题: Q3  
   - Why this chart type / 为什么用这个图: Hourly line chart highlights whether weekend demand has one broad afternoon peak versus weekday commute peaks.  
   - Main finding / 主要发现: Weekends do not show the weekday-style morning/evening commute split. Instead, counts build gradually and form one broad afternoon peak around 2-4pm (top at ~3pm, ~161 bikes/hour total), indicating a more leisure-oriented pattern.

3. `charts/q3_weekday_vs_weekend_total.png` (optional but recommended)  
   - Question answered / 对应问题: Q3 (comparison support)  
   - Why this chart type / 为什么用这个图: Grouped bar chart makes weekday/weekend hour-by-hour differences easy to compare directly.  
   - Main finding / 主要发现: Weekdays are much higher during commute hours (largest gap near 8am, weekday exceeds weekend by ~263 bikes/hour), while weekends are only slightly higher in some midday and late-night hours. This confirms the weekday commute effect as the dominant pattern in the current window.

---

## Notes on Data Scope / Null-or-Limited Findings

Q2 (seasonal change) is likely underpowered with the current ~41-day window (late Feb to end of Mar).  
This is still a valid analytical finding: the available period is too short to confidently claim full seasonal pickup.

Q2（季节变化）在当前约 41 天（2 月下旬到 3 月底）窗口下证据不足。  
这同样是有效发现：现有时间范围不够长，暂不适合对全年季节变化作强结论。

Plan for MP1b: pull full-year data and revisit Q2 with monthly aggregates.

---

## Competency Claim(s)

In this assignment, I demonstrated competency by converting hourly sensor counts into clear visual evidence aligned with my MP1 research questions.

这次作业中，我通过将小时级传感器计数转化为可解释图表，并与 MP1 分析问题一一对应，展示了相关能力。

I demonstrated competency with:

- Selecting chart types that match analytical goals (trend over time, directional comparison, weekday/weekend contrast).  
  能根据分析目标（时间趋势、方向对比、工作日/周末对比）选择合适图表类型。

- Building readable charts with precise titles, labeled axes, and consistent units.  
  能制作可读性强的图表：标题准确、坐标轴标注完整、单位一致。

- Exporting static visual artifacts (`.png`) from code for reproducible reporting in MP1b.  
  能通过代码导出可复现的静态图表文件（`.png`），用于 MP1b 报告。

- Interpreting both strong patterns (weekday commute peaks) and limited evidence (short window for seasonality).  
  能解释显著模式（工作日通勤双峰）以及证据受限结果（季节性窗口不足）。

---

## Submission URL

GitHub repo URL: `https://github.com/<your-account>/<your-repo>`

