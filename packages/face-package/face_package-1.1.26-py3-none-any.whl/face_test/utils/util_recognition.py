from numpy.linalg import norm
import numpy as np
import torch

def compute_sim(feat1, feat2):
    
    feat1 = feat1.ravel()
    feat2 = feat2.ravel()
    sim = np.dot(feat1, feat2) / (norm(feat1) * norm(feat2))
    return sim

def compute_sims(feat1, feats):
    
    feat1 = feat1.ravel()
    sims = [ np.dot(feat1,feat2.ravel())/(norm(feat1) * norm(feat2.ravel())) for feat2 in feats]
    return sims