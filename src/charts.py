import matplotlib.pyplot as plt
import seaborn as sns


def plot_histograms(penguins, cols, figsize=(14, 5)):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    sns.histplot(data=penguins, x='flipper_length_mm', hue='species', bins=25, alpha=0.6, ax=axes[0])
    axes[0].set_title('Длина ласт по видам')

    sns.histplot(data=penguins, x='body_mass_g', hue='species', bins=25, alpha=0.6, ax=axes[1])
    axes[1].set_title('Масса тела по видам')

    plt.tight_layout()
    plt.show()


def plot_boxplots(penguins, configs, figsize=(14, 5)):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    sns.boxplot(data=penguins, x='species', y='bill_length_mm', palette='Set2', ax=axes[0, 0])
    axes[0, 0].set_title('Длина клюва по видам')

    sns.boxplot(data=penguins, x='species', y='body_mass_g', palette='Set2', ax=axes[0, 1])
    axes[0, 1].set_title('Масса тела по видам')

    sns.violinplot(data=penguins, x='species', y='body_mass_g',
               palette='Set2', inner='quartile', ax=axes[1, 0])
    axes[1, 0].set_title('Масса тела (violin)')

    penguins['species'].value_counts().plot.bar(
        ax=axes[1, 1], color='steelblue', edgecolor='white')
    axes[1, 1].set_title('Количество по видам')
    axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=0)

    plt.tight_layout()
    plt.show()

def plot_heatmap(penguins, cols=None, figsize=(10, 8)):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(penguins.select_dtypes(include='number').corr(), annot=True, fmt='.2f',
            cmap='RdBu_r', center=0, ax=ax)
    ax.set_title('Корреляционная матрица (Penguins)')
    plt.tight_layout()
    plt.show()


def plot_scatter(penguins, x, y, hue, figsize=(10, 6), **kwargs):
    fig, axes = plt.subplots(1, 2, figsize=(16, 5))

    sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm',
                hue='species', palette='Set2', alpha=0.7, ax=axes[0])
    axes[0].set_title('Длина vs Глубина клюва (парадокс Симпсона!)')

    sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g',
                hue='species', palette='Set2', alpha=0.7, ax=axes[1])
    axes[1].set_title('Ласты vs Масса')

    plt.tight_layout()
    plt.show()
