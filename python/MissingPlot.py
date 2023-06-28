def MissingPlot(DataFrame):
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter
    plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
    plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
    # No. of missing values by features
    DataFrame_missing = DataFrame.isna().sum()
    DataFrame_missing=DataFrame_missing.sort_values(ascending=False).reset_index()
    # Renaming the columns
    DataFrame_missing.columns = ['feature', 'missing_count']
    # Filtering features with missing values
    DataFrame_missing = DataFrame_missing.loc[DataFrame_missing['missing_count'] > 0].reset_index(drop=True)
    # Create a bar chart
    DataFrame_missing.plot.bar(x='feature', y='missing_count')
    # Set the chart title and axis labels
    plt.title('Missing Values Count', fontsize=16)
    plt.xlabel('Columns', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.tick_params(axis='x', which='major', labelsize=14)
    plt.tick_params(axis='y', which='major', labelsize=14)

    # Display the chart
    plt.show()