import seaborn as sns

def load_data(name, sample_n=None, random_state=42):
    penguins = sns.load_dataset(name)
    if sample_n:
        penguins = penguins.sample(sample_n, random_state=random_state)
    print(f'Размер: {penguins.shape}')
    print(f'Столбцы: {list(penguins.columns)}')
    penguins.info()
    return penguins