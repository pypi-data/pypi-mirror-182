import torch
import torch_directml
import numpy as np
device = torch_directml.device(torch_directml.default_device())
# device = "cpu"

# grad_weight = torch.zeros(10, 3).to(device)

# index = torch.tensor([1,2,2,2,3,3,4, 9]).to(device)

# src = torch.ones(8, 3).to(device)

# r = grad_weight.index_put([index], src, accumulate=True)

# print (r.to("cpu"))


# grad_weight = torch.zeros(512, 768)
# index = torch.randint(0, 512, (75,)) # {75}

# src = torch.randn(75, 768)
grad_weight = torch.zeros(2, 3)
index = torch.tensor([0, 1, 0, 0])
src = torch.ones(4, 3)

r_cpu = grad_weight.index_put([index], src, accumulate=True)
#with torch.profiler.profile(activities=[torch.profiler.ProfilerActivity.CPU], record_shapes=True) as prof:
  #r = grad_weight.index_put([index], src, accumulate=True)
r = grad_weight.to(device).index_put([index.to(device)], src.to(device), accumulate=True)
#print(prof.key_averages().table(sort_by="cpu_time_total", row_limit=1000))

print (r_cpu)
print (r.to("cpu"))
print (torch.all(torch.eq(r_cpu, r.to("cpu"))))