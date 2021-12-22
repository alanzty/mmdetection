_base_ = './yolox_tiny_8x8_300e_coco.py'

runner = dict(max_epochs=12)
checkpoint_config = dict(interval=1)
evaluation = dict(interval=1)
data = dict(
    samples_per_gpu=24,
    workers_per_gpu=12)
