from scipy.stats import pearsonr, spearmanr
import pandas as pd


def analyze_missing(penguins):
    missing = penguins.isnull().sum()
    missing_pct = (penguins.isnull().mean() * 100).round(1)
    missing_penguins = pd.DataFrame({'Пропуски': missing, '%': missing_pct})
    missing_with = missing_penguins[missing_penguins['Пропуски'] > 0]
    if len(missing_with) > 0:
        print('Пропуски:')
        print(missing_with.sort_values('%', ascending=False))
    else:
        print('Пропусков нет')

    print(f'\nВсего строк с пропусками: {penguins.isnull().any(axis=1).sum()} из {len(penguins)}')

    print('\n=== Числовые столбцы ===')
    print(penguins.describe().round(2))
    print('\n=== Категориальные столбцы ===')
    print(penguins.describe(include=['object', 'category']))
    return missing_penguins


def handle_missing(penguins, fill_median=None, fill_mode=None, drop_cols=None):
    print('До:', penguins.shape, f'пропусков: {penguins.isnull().sum().sum()}')

    for col in penguins.select_dtypes(include='number').columns:
        if penguins[col].isnull().any():
            med = penguins[col].median()
            penguins[col] = penguins[col].fillna(med)
            print(f'  {col}: заполнено медианой ({med:.1f})')

    for col in penguins.select_dtypes(include=['object', 'category']).columns:
        if penguins[col].isnull().any():
            mode_val = penguins[col].mode()[0]
            penguins[col] = penguins[col].fillna(mode_val)
            print(f'  {col}: заполнено модой ({mode_val})')

    print('После:', penguins.shape, f'пропусков: {penguins.isnull().sum().sum()}')
    return penguins


def compute_correlations(penguins, pairs):    
    for c1, c2 in pairs:
        clean = penguins[[c1, c2]].dropna()
        p_corr, _ = pearsonr(clean[c1], clean[c2])
        s_corr, _ = spearmanr(clean[c1], clean[c2])
        print(f'{c1} vs {c2}:  Пирсон r={p_corr:.3f}  Спирмен p={s_corr:.3f}')

def groupby_stats(penguins, cols):
    print('Средние по видам:')
    print(penguins.groupby('species')[cols].mean().round(1))
    print('\nМасса по виду и острову:')
    print(penguins.groupby(['species', 'island'])['body_mass_g'].agg(['mean', 'count']).round(0))