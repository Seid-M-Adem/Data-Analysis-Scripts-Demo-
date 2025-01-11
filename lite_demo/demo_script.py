import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load demo data
df = pd.read_csv("lite_demo/demo_data.csv")

# Create output directory
output_dir = "lite_demo/demo_visualizations"
os.makedirs(output_dir, exist_ok=True)

# Bar Plot: Sum of Values by Category
plt.figure(figsize=(10, 6))
bar_data = df.groupby("Category")["Value"].sum()
bar_data.plot(kind="bar", color="#1f77b4", alpha=0.9, edgecolor="black", linewidth=1.2)
plt.title("Sum of Values by Category", fontsize=18, fontweight="bold", color="#333333")
plt.xlabel("Category", fontsize=14, labelpad=10)
plt.ylabel("Sum of Values", fontsize=14, labelpad=10)
plt.xticks(fontsize=12, rotation=0, color="#555555")
plt.yticks(fontsize=12, color="#555555")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig(f"{output_dir}/bar_plot.png", dpi=300)
plt.close()

# Heatmap: Correlation Between Numeric Variables
plt.figure(figsize=(10, 6))

# Select only numeric columns for correlation
numeric_cols = df.select_dtypes(include=['number'])

sns.heatmap(
    numeric_cols.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    cbar_kws={"shrink": 0.8, "label": "Correlation Coefficient"}
)
plt.title("Correlation Heatmap", fontsize=18, fontweight="bold", color="#333333", pad=15)
plt.xticks(fontsize=12, rotation=45, ha="right", color="#555555")
plt.yticks(fontsize=12, rotation=0, color="#555555")
plt.tight_layout()
plt.savefig(f"{output_dir}/heatmap.png", dpi=300)
plt.close()

# Pie Chart: Value Distribution by Category
pie_chart = px.pie(
    df,
    names="Category",
    values="Value",
    title="Value Distribution by Category",
    color_discrete_sequence=px.colors.qualitative.Set2
)
pie_chart.update_traces(
    textinfo="percent+label",
    pull=[0.1 if v == max(df["Value"]) else 0 for v in df["Value"]],
    marker=dict(line=dict(color="#000000", width=1))
)
pie_chart.update_layout(
    title_font_size=18,
    title_font_color="#333333",
    font=dict(size=14, color="#555555"),
    legend=dict(font=dict(size=12))
)
pie_chart.write_image(f"{output_dir}/pie_chart.png", engine="kaleido")

print(f"Visualizations saved in {output_dir}/")
