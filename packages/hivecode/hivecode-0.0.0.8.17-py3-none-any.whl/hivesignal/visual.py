from matplotlib.pyplot import figure, plot, legend, show

def plot_fourier(dfs, figsize_x: int = 50, figsize_y: int = 5):
    if not isinstance(dfs, list):
        dfs = [dfs]
        
    for df in dfs:
        figure(figsize = (figsize_x, figsize_y))
        plot(df.frequency, df.amplitude, label = "Waves")
        legend()

    show()