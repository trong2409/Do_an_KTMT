import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import FER.FER.transforms as transforms
from FER.FER.models import *

cut_size = 44

transform_test = transforms.Compose([
    transforms.TenCrop(cut_size),
    transforms.Lambda(lambda crops: torch.stack([transforms.ToTensor()(crop) for crop in crops])),
])

class_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
checkpoint = torch.load(
    os.path.join(os.path.split(os.path.realpath(__file__))[0], 'FER2013_VGG19/PrivateTest_model.t7'))
net = VGG('VGG19')
net.load_state_dict(checkpoint['net'])
net.cuda()
net.eval()


def fer(raw_img):
    img = cv2.resize(raw_img, (48, 48))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    img = gray[:, :, np.newaxis]
    img = np.concatenate((img, img, img), axis=2)
    img = Image.fromarray(img)
    inputs = transform_test(img)

    ncrops, c, h, w = np.shape(inputs)
    inputs = inputs.view(-1, c, h, w)
    inputs = inputs.cuda()
    with torch.no_grad():
        outputs = net(inputs)
        outputs_avg = outputs.view(ncrops, -1).mean(0)  # avg over crops
        score = F.softmax(outputs_avg, dim=0)
        _, predicted = torch.max(outputs_avg.data, 0)
    return str(class_names[int(predicted.cpu().numpy())])
