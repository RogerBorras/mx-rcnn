import numpy as np
from easydict import EasyDict as edict

config = edict()

# image processing config
config.EPS = 1e-14
config.PIXEL_MEANS = np.array([[[123.68, 116.779, 103.939]]])
config.SCALES = [(600, 1000)]  # first is scale (the shorter side); second is max size
config.IMAGE_STRIDE = 0

config.TRAIN = edict()

# R-CNN and RPN
config.TRAIN.BATCH_SIZE = 1  # used in grad_scale
config.TRAIN.END2END = False

# R-CNN
config.TRAIN.HAS_RPN = False
config.TRAIN.BATCH_IMAGES = 2
config.TRAIN.BATCH_ROIS = 128
config.TRAIN.FG_FRACTION = 0.25
config.TRAIN.FG_THRESH = 0.5
config.TRAIN.BG_THRESH_HI = 0.5
config.TRAIN.BG_THRESH_LO = 0.1

# R-CNN bounding box regression
config.TRAIN.BBOX_REGRESSION_THRESH = 0.5
config.TRAIN.BBOX_INSIDE_WEIGHTS = np.array([1.0, 1.0, 1.0, 1.0])

# RPN anchor loader
config.TRAIN.RPN_BATCH_SIZE = 256
config.TRAIN.RPN_FG_FRACTION = 0.5
config.TRAIN.RPN_POSITIVE_OVERLAP = 0.7
config.TRAIN.RPN_NEGATIVE_OVERLAP = 0.3
config.TRAIN.RPN_CLOBBER_POSITIVES = False
config.TRAIN.RPN_BBOX_INSIDE_WEIGHTS = (1.0, 1.0, 1.0, 1.0)
config.TRAIN.RPN_POSITIVE_WEIGHT = -1.0

# used for end2end training
# RPN proposal
config.TRAIN.RPN_NMS_THRESH = 0.7
config.TRAIN.RPN_PRE_NMS_TOP_N = 12000
config.TRAIN.RPN_POST_NMS_TOP_N = 6000
config.TRAIN.RPN_MIN_SIZE = 16
# approximate bounding box regression
config.TRAIN.BBOX_NORMALIZATION_PRECOMPUTED = False
config.TRAIN.BBOX_MEANS = (0.0, 0.0, 0.0, 0.0)
config.TRAIN.BBOX_STDS = (0.1, 0.1, 0.2, 0.2)

config.TEST = edict()

# R-CNN testing
config.TEST.HAS_RPN = False
config.TEST.BATCH_IMAGES = 1
config.TEST.NMS = 0.3

# RPN proposal
config.TEST.RPN_NMS_THRESH = 0.7
config.TEST.RPN_PRE_NMS_TOP_N = 6000
config.TEST.RPN_POST_NMS_TOP_N = 300
config.TEST.RPN_MIN_SIZE = 16
