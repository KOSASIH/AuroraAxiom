import torch
import torch.nn as nn
import torch.nn.functional as F

class TransformerModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_heads):
        super(TransformerModel, self).__init__()
        self.encoder = TransformerEncoderLayer(input_dim, hidden_dim, num_heads)
        self.decoder = TransformerDecoderLayer(hidden_dim, output_dim, num_heads)

    def forward(self, src, tgt):
        src = self.encoder(src)
        tgt = self.decoder(tgt, src)
        return tgt

class TransformerEncoderLayer(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_heads):
        super(TransformerEncoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention(input_dim, hidden_dim, num_heads)
        self.feed_forward = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, src):
        src = self.self_attn(src, src)
        src = F.relu(self.feed_forward(src))
        return src

class TransformerDecoderLayer(nn.Module):
    def __init__(self, hidden_dim, output_dim, num_heads):
        super(TransformerDecoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention(hidden_dim, hidden_dim, num_heads)
        self.encoder_attn = MultiHeadAttention(hidden_dim, hidden_dim, num_heads)
        self.feed_forward = nn.Linear(hidden_dim, output_dim)

    def forward(self, tgt, src):
        tgt = self.self_attn(tgt, tgt)
        tgt = self.encoder_attn(tgt, src)
        tgt = F.relu(self.feed_forward(tgt))
        return tgt

class MultiHeadAttention(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_heads):
        super(MultiHeadAttention, self).__init__()
        self.query_linear = nn.Linear(input_dim, hidden_dim)
        self.key_linear = nn.Linear(input_dim, hidden_dim)
        self.value_linear = nn.Linear(input_dim, hidden_dim)
        self.dropout = nn.Dropout(0.1)

    def forward(self, query, key, value):
        query = self.query_linear(query)
        key = self.key_linear(key)
        value = self.value_linear(value)
        attention_weights = torch.matmul(query, key.T) / math.sqrt(hidden_dim)
        attention_weights = F.softmax(attention_weights, dim=-1)
        attention_weights = self.dropout(attention_weights)
        output = attention_weights * value
        return output
