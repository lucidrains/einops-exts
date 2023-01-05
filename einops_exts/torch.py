from torch import nn
from einops import rearrange

# for rearranging to and from a pattern

class EinopsToAndFrom(nn.Module):
    def __init__(self, from_einops, to_einops, fn):
        super().__init__()
        self.from_einops = from_einops
        self.to_einops = to_einops
        self.fn = fn

        if '...' in from_einops:
            before, after = [part.strip().split() for part in from_einops.split('...')]
            self.reconstitute_keys = tuple(zip(before, range(len(before)))) + tuple(zip(after, range(-len(after), 0)))
        else:
            split = from_einops.strip().split()
            self.reconstitute_keys = tuple(zip(split, range(len(split))))


    def forward(self, x, **kwargs):
        shape = x.shape
        reconstitute_kwargs = {key: shape[position] for key, position in self.reconstitute_keys}
        x = rearrange(x, f'{self.from_einops} -> {self.to_einops}')
        x = self.fn(x, **kwargs)
        x = rearrange(x, f'{self.to_einops} -> {self.from_einops}', **reconstitute_kwargs)
        return x
