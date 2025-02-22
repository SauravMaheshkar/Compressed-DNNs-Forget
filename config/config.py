"""Project Config in JSON"""

CFG = {
    "data": {
        "data_folder": "data/CelebA/",
        "images_folder": "data/CelebA/img_align_celeba/img_align_celeba/",
        "IMG_HEIGHT": "218",
        "IMG_WIDTH": "178",
        "TRAINING_SAMPLES": "10000",
        "VALIDATION_SAMPLES": "2000",
        "TEST_SAMPLES": "2000",
    },
    "train": {
        "BATCH_SIZE": "64",
        "EPOCHS": "10",
    },
}
