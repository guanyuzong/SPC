import cv2
import os
import os.path as osp
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import torch

datasets = ['NJUD']


def Image_variance(img, beta=0.3):
    img = np.float32(img)
    flap_img = np.transpose(img)
    flap_img = flap_img[::-1]

    df = np.array([img[151],img[152],img[153],img[154],img[155],img[156],img[157],img[158],img[159],img[160],img[161],
                                img[162],img[163],img[164],img[165],img[166],
                                img[167],img[168],img[169],img[170]])
    df2 = np.array([flap_img[119],flap_img[120],flap_img[121],flap_img[122],flap_img[123],flap_img[124],flap_img[125],
                    flap_img[126],flap_img[127],flap_img[128],flap_img[129],
                                flap_img[130],flap_img[131],flap_img[132],flap_img[133],flap_img[134],
                                flap_img[135],flap_img[136],flap_img[137],flap_img[138]])
    # df = pd.DataFrame(np.array([img[180], flap_img[180], img[181], flap_img[181], positive_vector, negtive_vector]))

    a = 0.01 * df.std(axis = None)
    b = 0.01 * df2.std(axis = None)

    f_beta = (1.+beta) * a * b / (1e-7 + a + beta * b)

    return f_beta


S = [0] * len(datasets)
for dataset in datasets:
    path = osp.join('./data/RGBD_sal/train', dataset)
    #path = osp.join('test', dataset)
    imgs = [line.rstrip() for line in open(os.path.join(path, "train.txt"))]
    # slipt = len(imgs)-int(len(imgs)*0.2)

    scores = {}
    split = {}
    sum_s = 0
    for f in tqdm(imgs):

        print(osp.join(path, "depth", f+".jpg"))

        depth = cv2.imread(osp.join(path, "depth", f+".jpg"), 0)
        depth = cv2.resize(depth,(256,320))
        if depth is None:
            print("depth is None, check:", dataset)
        assert depth is not None
        try:
            gt    = cv2.imread(osp.join(path, "gt", f+".png"), 0) # gt->mask
        except:
            gt    = cv2.imread(osp.join(path, "gt", f+".jpg"), 0)
        if gt is None:
            print("gt:{} is None!".format(os.path.join(path, "gt", f)))
        assert gt is not None
        measure = Image_variance(depth,0.3)
        split[f] = measure

    a = sorted(split.items(), key=lambda x:-x[1])
    for i in range(len(a)):
        scores[a[i][0]] = {"f_beta": a[i][1]}


    with open(osp.join("./data/RGBD_sal/train", dataset+"_score.pkl"), "wb") as fout:
        print(scores)
        pickle.dump(scores, fout)







