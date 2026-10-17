import os
import matplotlib.pyplot as plt


# =========================
# 保存路径
# =========================

os.makedirs("figures", exist_ok=True)


# =========================
# 横坐标
# =========================

x_labels = [
    "MuSiQue Ans\nEM",
    "MuSiQue Ans\nF1",
    "MuSiQue Full\nEM",
    "MuSiQue Full\nF1",
    "Wiki\nEM",
    "Wiki\nF1",
    "HotpotQA\nEM",
    "HotpotQA\nF1"
]


x = range(len(x_labels))


# =========================
# 数据
# =========================

data = {

    "NaiveRAG":
    [63.2,77.97,25.4,36.42,24.3,46.98,43.2,65.23],

    "GraphRAG":
    [66.4,78.67,30.6,40.33,36.2,39.84,36.8,59.36],

    "LightRAG":
    [65.8,78.65,30.4,40.09,35.3,50.77,39.5,60.57],

    "FaithfulRAG":
    [55.6,74.30,28.6,40.18,34.2,51.30,49.3,69.58],

    "TH-RAG":
    [63.8,77.82,28.4,38.69,40.3,24.34,58.3,73.00],

    "S2G-RAG":
    [63.4,76.01,30.4,40.91,36.5,22.13,43.2,78.60],

    "Q-RAG":
    [50.7,79.50,30.6,41.36,41.5,58.32,39.5,60.31],

    "HippoRAG 2":
    [56.8,68.30,28.8,39.46,42.3,55.86,50.2,69.80],

    "UGRAG":
    [67.3,79.35,30.8,45.80,46.2,60.37,59.4,79.80]

}



# =========================
# marker
# =========================

markers = [
    "o",
    "s",
    "^",
    "D",
    "v",
    "P",
    "X",
    "*",
    "h"
]


# =========================
# 绘图
# =========================

plt.figure(
    figsize=(9,6),
    dpi=300
)



for i,(method,values) in enumerate(data.items()):

    if method=="UGRAG":

        plt.plot(
            x,
            values,
            marker=markers[i],
            linewidth=2.8,
            markersize=7,
            label=method
        )

    else:

        plt.plot(
            x,
            values,
            marker=markers[i],
            linewidth=1.8,
            markersize=5,
            label=method
        )



# =========================
# 坐标轴
# =========================


plt.xticks(
    x,
    x_labels,
    fontsize=9
)


plt.yticks(
    fontsize=10
)


plt.ylabel(
    "Score (%)",
    fontsize=12
)



plt.ylim(
    0,
    100
)



plt.grid(
    linestyle="--",
    linewidth=0.6,
    alpha=0.5
)



# =========================
# 图例放内部
# =========================


leg = plt.legend(
    loc="lower center",
    bbox_to_anchor=(0.5,0.05),
    ncol=3,
    fontsize=9,
    frameon=True,
    fancybox=True,
    framealpha=0.9
)


leg.set_zorder(10)



# =========================
# 调整布局
# 不使用 tight_layout
# =========================


plt.subplots_adjust(
    left=0.08,
    right=0.98,
    top=0.95,
    bottom=0.12
)



# =========================
# 保存
# =========================


plt.savefig(
    "figures/em_f1_line_chart.pdf",
    bbox_inches="tight"
)


plt.savefig(
    "figures/em_f1_line_chart.png",
    dpi=600,
    bbox_inches="tight"
)


plt.show()