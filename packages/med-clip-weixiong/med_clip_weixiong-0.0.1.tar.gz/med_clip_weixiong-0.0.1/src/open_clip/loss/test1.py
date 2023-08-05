# torchrun --nproc_per_node=2 --rdzv_endpoint=$HOSTE_NODE_ADDR test1.py

import torch
import torch.distributed as dist
import numpy as np
import os
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"


world_size = 2
dist.init_process_group('nccl', rank=0, world_size=world_size)

# 需要導入模塊: from torch import distributed [as 別名]
# 或者: from torch.distributed import all_gather [as 別名]
def gather_tensors(input_array):
    world_size = dist.get_world_size()
    ## gather shapes first
    myshape, mycount = 2, 3
    # myshape = input_array.shape
    # mycount = input_array.size
    shape_tensor = torch.Tensor(np.array(myshape)).cuda()
    all_shape = [torch.Tensor(np.array(myshape)).cuda() for i in range(world_size)]
    print(all_shape)
    dist.all_gather(all_shape, shape_tensor)
    return all_shape
    '''
    ## compute largest shapes
    all_shape = [x.cpu().numpy() for x in all_shape]
    all_count = [int(x.prod()) for x in all_shape]
    all_shape = [list(map(int, x)) for x in all_shape]
    max_count = max(all_count)
    ## padding tensors and gather them
    output_tensors = [torch.Tensor(max_count).cuda() for i in range(world_size)]
    padded_input_array = np.zeros(max_count)
    padded_input_array[:mycount] = input_array.reshape(-1)
    input_tensor = torch.Tensor(padded_input_array).cuda()
    dist.all_gather(output_tensors, input_tensor)
    ## unpadding gathered tensors
    padded_output = [x.cpu().numpy() for x in output_tensors]
    output = [x[:all_count[i]].reshape(all_shape[i]) for i,x in enumerate(padded_output)]
    '''


print(gather_tensors(1))
