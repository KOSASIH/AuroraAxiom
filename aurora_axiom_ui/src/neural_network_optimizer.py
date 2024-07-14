import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

class NeuralNetworkOptimizer(nn.Module):
    def __init__(self):
        super(NeuralNetworkOptimizer, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = nn.CrossEntropyLoss()(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print(f'Epoch {epoch}, Batch {batch_idx}, Loss: {loss.item()}')

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = NeuralNetworkOptimizer()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    dataset = CustomDataset(data, labels)
    train_loader = DataLoader(dataset, batch_size=32, shuffle=True)
    for epoch in range(10):
        train(model, device, train_loader, optimizer, epoch)

if __name__ == '__main__':
    main()
