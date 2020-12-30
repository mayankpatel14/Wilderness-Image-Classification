"""
While uploading data, create directories like this
- train
	- forest(this directory contains all the images of forests)
	- non-forest(this directory contains images corresponding to non-forests)
"""
from PIL import Image
from shutil import copyfile
import pandas as pd
import numpy as np
import os
import cv2
from  matplotlib import pyplot as plt
import matplotlib.image as mpimg
%matplotlib inline
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
from torch.utils.data import random_split
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torchvision.datasets import ImageFolder
from torchvision.transforms import ToTensor
from torch.utils.data.dataloader import DataLoader
from torchvision.utils import make_grid

from sklearn import metrics
from sklearn import decomposition
from sklearn import manifold

import copy
import random
import time

img_folder=r'/content/drive/MyDrive/Wilderness_Classification/images/train'

dataset = ImageFolder(img_folder, transform=ToTensor())

random_seed = 42
torch.manual_seed(random_seed)
val_size = 2000
train_size = len(dataset) - val_size

train_ds, val_ds = random_split(dataset, [train_size, val_size])


batch_size=10
train_dl = DataLoader(train_ds, batch_size, shuffle=True, num_workers=4, pin_memory=True)
val_dl = DataLoader(val_ds, batch_size*2, num_workers=4, pin_memory=True)