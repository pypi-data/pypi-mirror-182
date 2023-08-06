
# _____________________________________Metrics ________________________________________________
import numpy as np
import tensorflow as tf


from skimage.metrics import hausdorff_distance
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
from scipy.spatial.distance import directed_hausdorff

from skimage.morphology import remove_small_objects
from skimage.morphology import remove_small_holes

def hausdorff(_vol_t, _vol_s, threshold=0.02, threshold_2=0.001):
    
    if _vol_t.shape != _vol_t.shape:
        raise ValueError ("Shape mismatch")
        
    vol_t = binary_threshold(_vol_t, threshold=threshold)
    vol_s = binary_threshold(_vol_s, threshold=threshold)
    binary_volume

    h_distance = hausdorff_distance(_vol_t, _vol_s)
    return h_distance

def binary_metrics(_vol_t, _vol_s, threshold_1=0.04, dec_points = 5):
    
    if _vol_t.shape != _vol_t.shape:
        raise ValueError ("Shape mismatch")
        
    vol_t = binary_threshold(_vol_t, threshold=threshold_1)
    vol_s = binary_threshold(_vol_s, threshold=threshold_1)
    
#     vol_t = _vol_t
#     vol_s = _vol_s
    
    intersection= (np.logical_and(vol_s,vol_t)).sum()
    union = (vol_s.sum() + vol_t.sum())

    if intersection ==0 and union == 0:
        return 1., 1., 1., 1.
    
    if union == 0:
        union = 1e-7
    
    dice_value = np.round(2. * intersection / union, dec_points)
    ppv = np.round(intersection / vol_t.sum(), dec_points)
    sensitivity = np.round(intersection / vol_s.sum(), dec_points)
    volume_ratio = np.round(vol_t.sum() / vol_s.sum(), dec_points)
    
    return dice_value, ppv, sensitivity, volume_ratio
#     return dice_value

def binary_threshold(volume, threshold=0.04, dtype=np.float32):
    volume_cp = np.copy(volume)
    volume_cp [volume_cp<threshold] = 0
    volume_cp [volume_cp>=threshold] = 1
    return np.array(volume_cp).astype(dtype)

def dsc_metric(_vol_t, _vol_s, threshold_1=0.04, dec_points = 5):
    return binary_metrics(_vol_t, _vol_s, threshold_1=0.04, dec_points = 5)[0]

def similarity_metric(y_true, y_pred, masked = False, threshold = 0.05):
    if masked:
        y_pred = y_pred * tf.where(y_pred > threshold, 1., 0.)
    return tf.keras.losses.mse(y_pred, y_true)

def ssim_metric(y_true, y_pred, masked = False, threshold = 0.05):
    if masked:
        y_pred = y_pred * tf.where(y_pred > threshold, 1., 0.)
    return tf.image.ssim(tf.expand_dims(y_true, axis = -1),
                         tf.expand_dims(y_pred, axis = -1),
                         max_val = 1)

def psnr_metric(y_true, y_pred, masked = False, threshold = 0.05):
    if masked:
        y_pred = y_pred * tf.where(y_pred > threshold, 1., 0.)
    return tf.image.psnr(tf.expand_dims(y_true, axis = -1),
                         tf.expand_dims(y_pred, axis = -1),
                         max_val = 1)

def histogram_difference_metric(y_true, y_pred, method = 'chi_square', masked = False, threshold = 0.05):
    methods = ['chi_square']
    assert method in methods, "histogram distance method not recognized"
    hists_dist_dict = dict()
    if masked:
        y_pred = y_pred * tf.where(y_pred > threshold, 1., 0.)
    hist_01 = normalized_histogram(y_true)
    hist_02 = normalized_histogram(y_pred)
    if method == 'chi_square': hists_dist_dict['chi_square'] = chi_square_distance(hist_01, hist_02)
#     return [hists_dist_dict[key] for key in hists_dist_dict]
    return chi_square_distance(hist_01, hist_02)

def normalized_histogram(x, value_range = [0,1], nbins=100):
    hist    = tf.histogram_fixed_width(values = x, value_range = value_range, nbins=nbins)
    hist, _ = tf.linalg.normalize(tf.cast(hist, tf.float32))
    return hist

def chi_square_distance(hist_01, hist_02):
    eps = 1e-7
    chi_square_dist = 0.5*tf.reduce_sum((tf.square((hist_01 - hist_02)) / (eps + hist_01 + hist_02)))
    return chi_square_dist
