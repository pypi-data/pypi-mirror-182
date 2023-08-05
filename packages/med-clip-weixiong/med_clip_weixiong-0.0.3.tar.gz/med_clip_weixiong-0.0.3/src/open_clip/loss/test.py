# %%
# torchrun --nproc_per_node=2 --rdzv_endpoint=$HOSTE_NODE_ADDR test.py
# 
import torch
import torch.distributed as dist
from torch.distributed.elastic.multiprocessing.errors import record
import os

print(torch.distributed.is_available())

# %%
def world_info_from_env():
    local_rank = 0
    for v in ('LOCAL_RANK', 'MPI_LOCALRANKID', 'SLURM_LOCALID', 'OMPI_COMM_WORLD_LOCAL_RANK'):
        if v in os.environ:
            local_rank = int(os.environ[v])
            break
    global_rank = 0
    for v in ('RANK', 'PMI_RANK', 'SLURM_PROCID', 'OMPI_COMM_WORLD_RANK'):
        if v in os.environ:
            global_rank = int(os.environ[v])
            break
    world_size = 1
    for v in ('WORLD_SIZE', 'PMI_SIZE', 'SLURM_NTASKS', 'OMPI_COMM_WORLD_SIZE'):
        if v in os.environ:
            world_size = int(os.environ[v])
            break

    return local_rank, global_rank, world_size


# %%
# Use address of one of the machines
world_size = 2
dist.init_process_group('nccl', world_size=world_size)
# dist.init_process_group('nccl', rank=0, world_size=world_size)
# dist.init_process_group('nccl', init_method='tcp://127.0.0.1:23456', rank=0, world_size=2)

rank = dist.get_rank()
print(rank)

local_rank, _, _ = world_info_from_env()
print(f'local_rank: {local_rank}')


# All tensors below are of torch.int64 dtype.
# We have 2 process groups, 2 ranks.
tensor_list = [torch.zeros(2, dtype=torch.int64).to(f'cuda:{local_rank}') for _ in range(2)]
print(tensor_list)
tensor = (torch.arange(2, dtype=torch.int64) + 1 + 2 * local_rank).to(f'cuda:{local_rank}')
print(f'tensor: {tensor.device}, tensor_list: {tensor_list[0].device}')

# dist.all_gather(tensor_list, tensor)
# print(tensor_list)

# NOTE 结果 nccl 这个 backend 不支持 gather 的操作
# https://www.pudn.com/news/6228d0a39ddf223e1ad16109.html
# res = dist.gather(tensor, tensor_list)
# print(f'res: {res}')

