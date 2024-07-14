import torch
import torch.nn as nn
import torch.optim as optim
from aurora_axiom_ml.models.transformer import TransformerModel
from aurora_axiom_ml.utils.data_loader import load_data
from aurora_axiom_ml.utils.data_augmentation import augment_data

def train(model, device, data_loader, optimizer, criterion, epochs):
    for epoch in range(epochs):
        for batch in data_loader:
            inputs, labels = batch
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(inputs, labels)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f'Epoch {epoch+1}, Loss: {loss.item()}')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = TransformerModel(10, 20, 5, 2)
data_loader = load_data('data/disaster_data.csv', batch_size=32, shuffle=True)
augmented_data = augment_data(data_loader, 2)
data_loader = load_data(augmented_data, batch_size=32, shuffle=True)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.MSELoss()
train(model, device, data_loader, optimizer, criterion, epochs=10)
