# 01_load_data.py - 最终提交版
import pandas as pd
import os

# 读取桌面文件
desktop = "/Users/lrf15336328932/Desktop"
effect = pd.read_csv(os.path.join(desktop, "CRISPRGeneEffect.csv"))
meta = pd.read_csv(os.path.join(desktop, "Model.csv"))

# 合并数据（适配你的真实列名）
merged_df = pd.merge(
    effect, 
    meta, 
    left_on=effect.columns[0],
    right_on="ModelID",
    how="inner"
)

# 输出结果
print("✅ 01数据预处理完成")
print(f"合并后数据维度：{merged_df.shape}")
print(f"有效细胞系数量：{merged_df.shape[0]}")
print(f"基因+元数据总列数：{merged_df.shape[1]}")

# 保存合并后的数据，给后续脚本使用
merged_df.to_csv(os.path.join(desktop, "depmap_merged_data.csv"), index=False)
print("✅ 已保存合并后数据到桌面：depmap_merged_data.csv")
