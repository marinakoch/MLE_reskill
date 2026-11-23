from src.data_loader import load_data
from src.analysis import analyze_missing, handle_missing, compute_correlations, groupby_stats
from src.charts import plot_histograms, plot_boxplots, plot_heatmap, plot_scatter

def run_eda(name, sample_n=None,
            hist_cols=None, box_configs=None, bar_configs=None,
            corr_pairs=None, heatmap_cols=None,
            scatter_configs=None, groupby_configs=None,
            missing_kw=None):

    # Блок 1: Чтение
    penguins = load_data(name, sample_n=sample_n)
    print(penguins.head())

    # Блок 2: Пропуски
    analyze_missing(penguins)
    if missing_kw:
        penguins = handle_missing(penguins, **missing_kw)

    # Блок 3: Графики
    if hist_cols:
        plot_histograms(penguins, hist_cols)
    if box_configs:
        plot_boxplots(penguins, box_configs)

    # Блок 4: Корреляции и статистики
    if corr_pairs:
        compute_correlations(penguins, corr_pairs)
    if heatmap_cols:
        plot_heatmap(penguins, cols=heatmap_cols)
    if scatter_configs:
        for x, y, hue, s_title in scatter_configs:
            plot_scatter(penguins, x, y, hue, s_title)
    if groupby_configs:
        print(groupby_stats(penguins, cols=groupby_configs))

    return penguins

#Запуск
penguin = run_eda(
    'penguins',
    hist_cols=['flipper_length_mm', 'body_mass_g'],
    box_configs=[('species','bill_length_mm'), ('species','body_mass_g')],    
    corr_pairs=[('bill_length_mm','flipper_length_mm'), ('flipper_length_mm','body_mass_g'), ('bill_length_mm','bill_depth_mm')],
    heatmap_cols=['species','bill_length_mm'],
    scatter_configs=[('bill_length_mm', 'bill_depth_mm', 'species', 'Длина vs Глубина клюва (парадокс Симпсона!)'), ('flipper_length_mm', 'body_mass_g', 'species', 'Ласты vs Масса')],
    groupby_configs=['bill_length_mm','body_mass_g'],
    missing_kw=dict(fill_median=['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'], fill_mode=['sex']),
)