import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def import_dummy_data():

    e = 0.1

    exact_vals = np.random.rand(8)
    mean_vals = exact_vals + e * np.random.rand(8)
    std_vals = e * np.random.rand(8)

    return exact_vals, mean_vals, std_vals


def import_data(step):
    prefixes = [
        'IdentityRightEnvironmentRatio',
        'IdentityRightEnvironmentSqrt',
        'UnitaryRightEnvironmentPostSelect',
    ]
    importPrefix = prefixes[2]
    print(f'Prefix: {importPrefix}')

    exact_smooth = pd.read_csv('data/time_evo_data/exact_smooth - data_0.csv')

    exact = pd.read_csv(f'data/time_evo_data/{importPrefix}/Exact.csv')

    exper = pd.read_csv(f'data/time_evo_data/{importPrefix}/Experiment.csv')

    stds = pd.read_csv(f'data/time_evo_data/{importPrefix}/Stds.csv')

    x_smooth = exact_smooth['step']

    return exact[step], exper[step], stds[step], x_smooth, exact_smooth[step]

def plot_data(exact, mean, stds,x_smooth, exact_smooth, ax=None, i=None):
    x = np.arange(8)
    if ax is None:
        ax = plt.subplot(111)

    ax.scatter(x, exact, c = 'b')
    ax.plot(x_smooth,exact_smooth, 'b', label = 'Exact Value')

    measured = ax.errorbar(x, mean, stds, c='g', linestyle = '--', marker = 'x', label = "Measured Value")

    if i is not None:
        t = i*0.2
        ax.set_title(f't={t:.1f}')

    # plt.legend(fontsize = 20)
    ax.set_xlabel('Parameter Step')
    ax.set_ylabel('Rescaled Measured Overlap')
    ax.set_ylim(0,1.1)


def main():
    fsize=22
    plt.rcParams.update({
        'font.size': fsize,
        'text.usetex': True,
    })
    fig, axs = plt.subplots(2, 2, figsize=(12, 12))

    for i in range(4):
        ax = axs[i//2, i%2]
        a=i
        b=i+1
        e,m,s,x_s,e_s = import_data(f'{a}->{b}')
        plot_data(e,m,s,x_s,e_s, ax=ax, i=i)
        # plt.savefig(f'/IdentityRightEnvironmentRatio/{a}_{b}_smooth.pdf')
        # plt.tight_layout()
    fig.tight_layout()
    plt.savefig('syacmoreProfiling.pdf')
    plt.show()


if __name__ == '__main__':
    main()
