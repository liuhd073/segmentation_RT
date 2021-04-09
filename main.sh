#!/bin/bash
#SBATCH --job-name=seg_DIBH     # job name
#SBATCH --ntasks=1                   # number of MP tasks
#SBATCH --ntasks-per-node=1          # number of MPI tasks per node
#SBATCH --gres=gpu:1                 # number of GPUs per node
#SBATCH --cpus-per-task=10           # number of cores per tasks
#SBATCH --hint=nomultithread         # we get physical cores not logical
#SBATCH --distribution=block:block   # we pin the tasks on contiguous cores
#SBATCH --time=99:59:59              # maximum execution time (HH:MM:SS)
#SBATCH --output=log/segmentation_RT_DIBH%j.out # output file name
#SBATCH --error=log/segmentation_RT_DIBH%j.err  # error file name
#SBATCH --partition=gpu_p2
# SBATCH --qos=qos_gpu-t4
set -x
# shellcheck disable=SC2164
cd "$WORK/segmentation_RT"

module purge
module load pytorch-gpu/py3/1.7.1
python main.py
