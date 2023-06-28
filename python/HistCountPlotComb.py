def HistCountPlotComb(DataFrame, NoneNumericalFeatures=[]):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from matplotlib.ticker import FuncFormatter
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
    plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
    row = 0
    col = 10
    for col in range(10, 4, -1):
        if DataFrame.shape[1] % col == 0:
            row = int(DataFrame.shape[1] / col)
            col = col
            break
    if row == 0:
        row = int(DataFrame.shape[1] // col) + 1

    fig, ax = plt.subplots(row, col, figsize=(col * 5, row * 5))

    for i in range(0, DataFrame.shape[1]):
        if row != 1:
            if DataFrame.columns[i] not in NoneNumericalFeatures:
                sns.histplot(data=DataFrame, x=DataFrame.iloc[:, i], bins=int(DataFrame.shape[0] / 30),
                             ax=ax[int(i / col), i % col])
            else:
                sns.histplot(data=DataFrame[DataFrame.columns[i]],
                             x=DataFrame[DataFrame.columns[i]].value_counts(dropna=False).sort_values(
                                 ascending=False).index.tolist(),
                             ax=ax[int(i / col), i % col])
                ax[int(i / col), i % col].set_title(DataFrame.columns[i], y=-0.2)
        else:
            if DataFrame.columns[i] not in NoneNumericalFeatures:
                sns.histplot(data=DataFrame, x=DataFrame.iloc[:, i], bins=int(DataFrame.shape[0] / 30), ax=ax[i])
            else:
                sns.histplot(data=DataFrame[DataFrame.columns[i]],
                             x=DataFrame[DataFrame.columns[i]].value_counts(dropna=False).sort_values(
                                 ascending=False).index.tolist(),
                             ax=ax[i])
                ax[i].set_title(DataFrame.columns[i], y=-0.2)

    plt.subplots_adjust(hspace=0.5)

    plt.show()