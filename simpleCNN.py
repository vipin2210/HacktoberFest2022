import torch
import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary

class OneShotDetection(nn.Module):
    def __init__(self):
        super(OneShotDetection, self).__init__()
        self.filter = 16
        self.flat = 6400
        self.ndim = 64

        self.conv1 = nn.Conv2d(3, self.filter, 3) 
        self.conv2 = nn.Conv2d(self.filter, self.filter*2 , 3) 
        self.conv3 = nn.Conv2d(self.filter*2, self.filter*4, 3)
        self.conv4 = nn.Conv2d(self.filter*4, self.filter*8, 3)
        self.conv5 = nn.Conv2d(self.filter*8, self.filter*16, 3)

        self.mxpol = nn.MaxPool2d(2, 2)
        self.pad   = nn.ZeroPad2d(1)
        self.batchnorm1 = nn.BatchNorm2d(self.filter*1)
        self.batchnorm2 = nn.BatchNorm2d(self.filter*2)
        self.batchnorm3 = nn.BatchNorm2d(self.filter*4)
        self.batchnorm4 = nn.BatchNorm2d(self.filter*8)
        self.batchnorm5 = nn.BatchNorm2d(self.filter*16)

        self.dense = nn.Linear(self.flat, self.ndim)
        self.final = nn.Linear(self.ndim, 1)

    def forward(self, xi, xj):
        xi = self.mxpol(F.relu(self.batchnorm1(self.pad(self.conv1(xi)))))
        xi = self.mxpol(F.relu(self.batchnorm2(self.pad(self.conv2(xi)))))
        xi = self.mxpol(F.relu(self.batchnorm3(self.pad(self.conv3(xi)))))
        xi = self.mxpol(F.relu(self.batchnorm4(self.pad(self.conv4(xi)))))
        xi = self.mxpol(F.relu(self.batchnorm5(self.pad(self.conv5(xi)))))
        xi = xi.view(-1, self.flat)
        xi = self.dense(xi) 

        xj = self.mxpol(F.relu(self.batchnorm1(self.pad(self.conv1(xj)))))
        xj = self.mxpol(F.relu(self.batchnorm2(self.pad(self.conv2(xj)))))
        xj = self.mxpol(F.relu(self.batchnorm3(self.pad(self.conv3(xj)))))
        xj = self.mxpol(F.relu(self.batchnorm4(self.pad(self.conv4(xj)))))
        xj = self.mxpol(F.relu(self.batchnorm5(self.pad(self.conv5(xj)))))
        xj = xj.view(-1, self.flat)
        xj = self.dense(xj)

        x = xi-xj
        x = torch.sigmoid(self.final(F.relu(x)))

        return x
img_shape = 160
model = OneShotDetection()
summary(model, [(3, img_shape, img_shape), (3, img_shape, img_shape)])




# class OneShotDetection(nn.Module):
#     def __init__(self):
#         super(OneShotDetection, self).__init__()
#         self.filter = 16
#         self.flat = 6400
#         self.ndim = 64

#         self.conv0 = nn.Conv2d(3, self.filter, 3) 
#         self.conv1 = nn.Conv2d(self.filter, self.filter*2 , 3) 
#         self.conv2 = nn.Conv2d(self.filter*2, self.filter*4, 3)
#         self.conv3 = nn.Conv2d(self.filter*4, self.filter*8, 3)
#         self.conv4 = nn.Conv2d(self.filter*8, self.filter*16, 3)

#         self.mxpol = nn.MaxPool2d(2, 2)
#         self.pad   = nn.ZeroPad2d(1)
#         self.batchnorm1 = nn.BatchNorm2d(self.filter*1)
#         self.batchnorm2 = nn.BatchNorm2d(self.filter*2)
#         self.batchnorm3 = nn.BatchNorm2d(self.filter*4)
#         self.batchnorm4 = nn.BatchNorm2d(self.filter*8)
#         self.batchnorm5 = nn.BatchNorm2d(self.filter*16)

#         self.dense = nn.Linear(self.flat, self.ndim)
#         self.final = nn.Linear(self.ndim, 1)

#     def forward(self, xi, xj):
#         xi = self.mxpol(F.relu(self.conv1(xi)))
#         xi = self.mxpol(F.relu(self.conv2(xi)))
#         xi = self.mxpol(F.relu(self.conv3(xi)))
#         xi = self.mxpol(F.relu(self.conv4(xi)))
#         xi = self.mxpol(F.relu(self.conv5(xi)))
#         xi = xi.view(-1, self.flat)
#         xi = self.dense(xi) 

#         xj = self.mxpol(F.relu(self.conv1(xj)))
#         xj = self.mxpol(F.relu(self.conv2(xj)))
#         xj = self.mxpol(F.relu(self.conv3(xj)))
#         xj = self.mxpol(F.relu(self.conv4(xj)))
#         xj = self.mxpol(F.relu(self.conv5(xj)))
#         xj = xj.view(-1, self.flat)
#         xj = self.dense(xj)

#         x = xi-xj
#         x = torch.sigmoid(self.final(F.relu(x)))

#         return x