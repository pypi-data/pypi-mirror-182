from abc import ABC, abstractmethod
import gymnasium
from gymnasium import spaces
from torch import nn, distributions
import torch


class Distribution:
    pass


class Decoder(ABC, nn.Module):
    def __init__(self, space: gymnasium.Space):
        super().__init__()
        self.space = space

    @abstractmethod
    def forward(self, x: torch.Tensor) -> Distribution:
        """Decode the input into a distribution of self.space."""


class DiscreteDecoder(Decoder):
    def __init__(self, space: spaces.Discrete, embed_dim: int):
        super().__init__(space)
        self.decoder = nn.Linear(embed_dim, space.n)

    def forward(self, x: torch.Tensor) -> distributions.Categorical:
        return distributions.Categorical(logits=self.decoder(x))
