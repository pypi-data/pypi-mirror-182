from .strong_sort.utils.parser import get_config
from .strong_sort.strong_sort import StrongSORT
from .ocsort.ocsort import OCSort
from .bytetrack.byte_tracker import BYTETracker
import os
import sys

def create_tracker(tracker_type, appearance_descriptor_weights, device, half):
    if tracker_type == 'strongsort':
        # initialize StrongSORT
        cfg = get_config()
        parent_dir = os.path.dirname(__file__)
        config_path = os.path.join(parent_dir, 'strong_sort/configs/strong_sort.yaml')
        cfg.merge_from_file(config_path)

        strongsort = StrongSORT(
            appearance_descriptor_weights,
            device,
            half,
            max_dist=cfg.STRONGSORT.MAX_DIST,
            max_iou_distance=cfg.STRONGSORT.MAX_IOU_DISTANCE,
            max_age=cfg.STRONGSORT.MAX_AGE,
            n_init=cfg.STRONGSORT.N_INIT,
            nn_budget=cfg.STRONGSORT.NN_BUDGET,
            mc_lambda=cfg.STRONGSORT.MC_LAMBDA,
            ema_alpha=cfg.STRONGSORT.EMA_ALPHA,

        )
        return strongsort
    elif tracker_type == 'ocsort':
        ocsort = OCSort(
            det_thresh=0.45,
            iou_threshold=0.2,
            use_byte=False 
        )
        return ocsort
    elif tracker_type == 'bytetrack':
        bytetracker = BYTETracker(
            track_thresh=0.6,
            track_buffer=30,
            match_thresh=0.8,
            frame_rate=30
        )
        return bytetracker
    else:
        print('No such tracker')
        exit()