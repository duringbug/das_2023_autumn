import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns


def get_bar(prices):
    # 创建图表
    plt.figure(figsize=(8, 6))

    # 绘制价格数据
    plt.plot(prices, marker='o', linestyle='-')

    # 添加标签
    plt.xlabel('Item Index')
    plt.ylabel('Price (¥)')
    plt.title('Price Distribution')

    # 显示图表
    plt.grid()
    plt.savefig('lecture06/resources/price_bar.png')


def get_scatter(prices):
    plt.figure(figsize=(8, 6))
    plt.scatter(range(len(prices)), prices, marker='o')

    # Add labels and title
    plt.xlabel('Item Index')
    plt.ylabel('Price (¥)')
    plt.title('Price Distribution (Scatter Plot)')

    # Save the scatter plot as an image
    plt.grid()
    plt.savefig('lecture06/resources/price_scatter.png')


def get_histogram(prices):
    plt.figure(figsize=(8, 6))
    plt.hist(prices, bins=50, edgecolor='black')

    # Add labels and title
    plt.xlabel('Price (¥)')
    plt.ylabel('Frequency')
    plt.title('Price Distribution (Histogram)')

    # Save the histogram as an image
    plt.grid()
    plt.savefig('lecture06/resources/price_histogram.png')


def get_seaborn_line(prices):
    # 创建图表
    plt.figure(figsize=(10, 6))

    # 使用Seaborn绘制价格数据的折线图
    sns.lineplot(x=range(len(prices)), y=prices)

    # 添加标签和标题
    plt.xlabel('Item Index')
    plt.ylabel('Price (¥)')
    plt.title('Price Distribution (Line Plot)')

    # 显示图表
    plt.grid()
    plt.savefig('lecture06/resources/price_seaborn_line.png')


def get_seaborn_scatter(prices):
    plt.figure(figsize=(8, 6))

    # 使用Seaborn绘制散点图
    sns.scatterplot(x=range(len(prices)), y=prices, marker='o')

    # 添加标签和标题
    plt.xlabel('Item Index')
    plt.ylabel('Price (¥)')
    plt.title('Price Distribution (Seaborn Scatter Plot)')

    # 保存散点图为图像
    plt.grid()
    plt.savefig('lecture06/resources/price_seaborn_scatter.png')


def get_seaborn_histogram(prices):
    plt.figure(figsize=(8, 6))

    # 使用Seaborn绘制直方图
    sns.histplot(prices, bins=50, kde=True, color='blue')

    # 添加标签和标题
    plt.xlabel('Price (¥)')
    plt.ylabel('Frequency')
    plt.title('Price Distribution (Seaborn Histogram)')

    # 保存直方图为图像
    plt.grid()
    plt.savefig('lecture06/resources/price_seaborn_histogram.png')


def get_price():
    # 连接到数据库
    conn = sqlite3.connect(
        'lecture06/dangdang/mydata.db')
    cursor = conn.cursor()

    # 执行SQL查询
    cursor.execute("SELECT price FROM books")

    # 获取所有价格数据
    prices = cursor.fetchall()

    # 关闭数据库连接
    conn.close()

    return [float(price[0].replace('¥', '')) for price in prices]


prices = get_price()
get_bar(prices)
get_scatter(prices)
get_histogram(prices)
get_seaborn_line(prices)
get_seaborn_scatter(prices)
get_seaborn_histogram(prices)
