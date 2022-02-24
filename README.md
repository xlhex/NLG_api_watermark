# Protecting Intellectual Property of Language Generation APIs with Lexical Watermark

## Descriptions
This repo contains source code and pre-processed corpora for Protecting Intellectual Property of Language Generation APIs with Lexical Watermark (accepted to AAAI 2022) ([paper](https://arxiv.org/abs/2112.02701))


## Dependencies
* python3
* spacy==3.0.0
* numpy==1.19.5
* scipy==1.5.4
* nltk==3.5

## Usage
```shell
git clone https://github.com/xlhex/NLG_api_watermark.git
```

## Create watermark words
```shell
# obtain candidates words and their synonyms (in this example, the size of synonyms is 2)
python scripts/create_cand_pool.py meta_data/top800_syn_cand_adj.txt 2 > secret_set.txt 
# obtain watermarked words from candidates words and their synonyms (in this example, we use top10 candidate words)
python scripts/find_idx_4_watermark.py meta_data/test.tok.en secret_set.txt 10
```

## An example showing how to watermark a corpus
```shell
python scripts/watermark_sub_from_secret_lib.py test/clean_test.txt test/secret_set.txt test/secret_idx.txt > watermarked_data.txt
```

## An example showing how to calculate P-value
```shell
# clean data
python scripts/calcul_p_syn.py test/secret_idx.txt test/secret_set.txt test/clean_test.txt
# watermark data
python scripts/calcul_p_syn.py test/secret_idx.txt test/secret_set.txt test/watermarked_test.txt
```

## Pre-processed data and fairseq checkpoints
* Please download the watermarked training data and clean dev/test data [here](https://drive.google.com/file/d/1qMMSfC0qRQ4uUPb618stih9vuxF6BVzZ/view?usp=sharing) (please refer to [fairseq](https://github.com/pytorch/fairseq) for training)
* Please download the watermarked imitation model [here](https://drive.google.com/file/d/1enxCBnMNHtos3e5b6qUWWdbHeJpNpAra/view?usp=sharing) (please refer to [fairseq](https://github.com/pytorch/fairseq) for inference)


# Citation

Please cite as:

``` bibtex
@article{he2021protecting,
  title={Protecting intellectual property of language generation apis with lexical watermark},
  author={He, Xuanli and Xu, Qiongkai and Lyu, Lingjuan and Wu, Fangzhao and Wang, Chenguang},
  journal={arXiv preprint arXiv:2112.02701},
  year={2021}
}
```
