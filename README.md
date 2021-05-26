# ffhq-sampler
random sampler for NVlabs' ffhq dataset. part of dissertation project


## sampler

1. ensure ffhq-dataset-v2.json is in working directory (https://drive.google.com/open?id=16N0RV4fHI6joBuKbQAoG34V_cQk7vxSA)
2. $python extractor.py --size <SAMPLE_SIZE>
4. produces list of randomly sampled data from ffhq to out.json

## downloader
1. $python downloader.py
2. populates images folder with aforementioned sampled data
