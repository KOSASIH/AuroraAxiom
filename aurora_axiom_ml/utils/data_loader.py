import pandas as pd
from torch.utils.data import Dataset, DataLoader

class DisasterDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        self.data = pd.read_csv(csv_file)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
sample = self.data.iloc[idx]
        if self.transform:
            sample = self.transform(sample)
        return sample

def load_data(csv_file, batch_size=32, shuffle=True):
    dataset = DisasterDataset(csv_file)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    return data_loader
