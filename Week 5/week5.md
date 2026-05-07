Week 5 - Competency Claim(s) / 第五周能力声明

For this assignment, my biggest learning was understanding how pandas works with database-style tables, and successfully completing the analysis in Jupyter Notebook.  
这次作业我最大的收获是理解了 pandas 和数据库式表格分析的关系，并且成功用 Jupyter Notebook 完成了分析。

I used my MP1 dataset (`app_reviews_demo.csv`) to practice reading, filtering, grouping, and checking data quality in a way that feels much more practical now.  
我用 MP1 的数据集（`app_reviews_demo.csv`）练习了读取、筛选、分组和数据质量检查，这些操作现在对我来说更有“做项目”的感觉。

I demonstrated competency with:  
我展示的能力包括：

- `df.head()` and `df.info()` to quickly check what the dataset looks like, data types, and whether columns are complete.  
  用 `df.head()` 和 `df.info()` 先看清数据结构、字段类型，以及每列是否完整。

- `value_counts()` to see rating distribution and overall sentiment (more high ratings than low ratings in this dataset).  
  用 `value_counts()` 看评分分布和整体情绪（这个数据里高分明显多于低分）。

- Filtering with `df[df['rating'] < 3]` to isolate low-rated reviews and estimate how large the dissatisfied group is.  
  用筛选 `df[df['rating'] < 3]` 单独看低分评论，估计不满意用户占比。

- `groupby('app')['rating'].mean()` to compare average ratings across apps and identify which app needs more improvement.  
  用 `groupby('app')['rating'].mean()` 比较不同 app 的平均评分，判断哪些产品更需要优化。

- `isnull().sum()` to detect missing values, especially in `device_type` and `app_version`, so I know what fields may be less reliable.  
  用 `isnull().sum()` 检查缺失值，尤其是 `device_type` 和 `app_version`，帮助我判断后续分析的可靠性。

This Week 5 analysis gives me a clear starting point for my Week 6 notebook and helps me explain both findings and limitations in MP1.  
第五周的分析给我第六周 notebook 打好了基础，也让我更有信心把 pandas、数据库思维和 Jupyter Notebook 一起用在后续项目里。
