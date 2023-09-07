# This file is executed to run the task (runtime = run - before_run)
import sys
import torch

tensor = torch.zeros(int(sys.argv[1]))