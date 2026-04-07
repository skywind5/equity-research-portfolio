import matplotlib.pyplot as plt

def plot_series(series, title):
    plt.figure()
    series.plot(title=title)
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.show()

def plot_comparison(df, columns):
    plt.figure()
    for col in columns:
        df[col].plot(label=col)
    plt.legend()
    plt.title("Comparison Chart")
    plt.show()