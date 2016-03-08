"""
prepare-yelp.py

description: prepare the Yelp data for training in DNNs
"""
import cPickle as pickle
import logging

import numpy as np

from nlpdatahandlers import YelpDataHandler
from textclf.wordvectors.glove import GloVeBox
from sklearn.feature_extraction.text import HashingVectorizer

LOGGER_PREFIX = ' %s'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def log(msg, logger=logger):
    logger.info(LOGGER_PREFIX % msg)

YELP_USEFUL_TRAIN = '../yelp-dataset/3votes_threshold/TrainSet_useful_491782'
YELP_USEFUL_DEV = '../yelp-dataset/3votes_threshold/DevSet_useful_491782'
YELP_USEFUL_TEST = '../yelp-dataset/3votes_threshold/TestSet_useful_491782'

YELP_FUNNY_TRAIN = '../yelp-dataset/3votes_threshold/TrainSet_funny_183246'
YELP_FUNNY_DEV = '../yelp-dataset/3votes_threshold/DevSet_funny_183246'
YELP_FUNNY_TEST = '../yelp-dataset/3votes_threshold/TestSet_funny_183246'

YELP_COOL_TRAIN = '../yelp-dataset/3votes_threshold/TrainSet_cool_218444'
YELP_COOL_DEV = '../yelp-dataset/3votes_threshold/DevSet_cool_218444'
YELP_COOL_TEST = '../yelp-dataset/3votes_threshold/TestSet_cool_218444'

GLOBAL_WV_FILE = './embeddings/wv/glove.42B.300d.120000.txt'
YELP_WV_FILE = './embeddings/wv/Yelp-GloVe-300dim.txt'
WORDS_PER_TEXT = 300
BOW_HASH_DIMENSION = 2500

if __name__ == '__main__':

    log('Building global word vectors from {}'.format(GLOBAL_WV_FILE))
    global_gb = GloVeBox(GLOBAL_WV_FILE)
    global_gb.build(zero_token=True, normalize_variance=False, normalize_norm=True)

    log('writing GloVeBox pickle...')
    pickle.dump(global_gb, open(GLOBAL_WV_FILE.replace('.txt', '-glovebox.pkl'), 'wb'), pickle.HIGHEST_PROTOCOL)

    log('Building global word vectors from {}'.format(YELP_WV_FILE))
    yelp_gb = GloVeBox(YELP_WV_FILE)
    yelp_gb.build(zero_token=True, normalize_variance=False, normalize_norm=True)

    log('writing GloVeBox pickle...')
    pickle.dump(yelp_gb, open(YELP_WV_FILE.replace('.txt', '-glovebox.pkl'), 'wb'), pickle.HIGHEST_PROTOCOL)

    yelp = YelpDataHandler()

    ##################################
    ### YELP USEFUL
    ##################################
    log('Saving "useful" votes data')
    (train_reviews, train_labels, test_reviews, test_labels) = \
        yelp.get_data(YELP_USEFUL_TRAIN, YELP_USEFUL_DEV, YELP_USEFUL_TEST)

    reviews_wvs_train = yelp.to_word_level_idx(train_reviews, global_gb, WORDS_PER_TEXT)
    # -- training data save
    np.save('Yelp_3votes_useful_train_fulltext_glove_300_X.npy', reviews_wvs_train)
    np.save('Yelp_3votes_useful_train_fulltext_glove_300_y.npy', train_labels)

    # reviews_wvs_train = yelp.to_word_level_idx(train_reviews, yelp_gb, WORDS_PER_TEXT)
    # # -- training data save
    # np.save('Yelp_useful_train_fulltext_Yelp_glove_300_X.npy', reviews_wvs_train)
    # np.save('Yelp_useful_train_fulltext_Yelp_glove_300_y.npy', train_labels)

    del reviews_wvs_train

    reviews_wvs_test = yelp.to_word_level_idx(test_reviews, global_gb, WORDS_PER_TEXT)
    # -- testing data save
    np.save('Yelp_3votes_useful_test_fulltext_glove_300_X.npy', reviews_wvs_test)
    np.save('Yelp_3votes_useful_test_fulltext_glove_300_y.npy', test_labels)

    # reviews_wvs_test = yelp.to_word_level_idx(test_reviews, yelp_gb, WORDS_PER_TEXT)
    # # -- testing data save
    # np.save('Yelp_useful_test_fulltext_Yelp_glove_300_X.npy', reviews_wvs_test)
    # np.save('Yelp_useful_test_fulltext_Yelp_glove_300_y.npy', test_labels)

    del reviews_wvs_test

    # log('Hashing BOW features, might be used by some NN models')
    # hv = HashingVectorizer(n_features=BOW_HASH_DIMENSION) # Int: maybe try without normalization
    # train_bow_hash = hv.transform(train_reviews)
    # test_bow_hash = hv.transform(test_reviews)
    # np.save('Yelp_useful_train_hashbow.npy', train_bow_hash.todense())
    # np.save('Yelp_useful_test_hashbow.npy', test_bow_hash.todense())

    ##################################
    ### YELP FUNNY
    ##################################
    log('Saving "funny" votes data')
    (train_reviews, train_labels, test_reviews, test_labels) = \
        yelp.get_data(YELP_FUNNY_TRAIN, YELP_FUNNY_DEV, YELP_FUNNY_TEST)

    reviews_wvs_train = yelp.to_word_level_idx(train_reviews, global_gb, WORDS_PER_TEXT)
    # -- training data save
    np.save('Yelp_3votes_funny_train_fulltext_glove_300_X.npy', reviews_wvs_train)
    np.save('Yelp_3votes_funny_train_fulltext_glove_300_y.npy', train_labels)

    # reviews_wvs_train = yelp.to_word_level_idx(train_reviews, yelp_gb, WORDS_PER_TEXT)
    # # -- training data save
    # np.save('Yelp_funny_train_fulltext_Yelp_glove_300_X.npy', reviews_wvs_train)
    # np.save('Yelp_funny_train_fulltext_Yelp_glove_300_y.npy', train_labels)

    del reviews_wvs_train

    reviews_wvs_test = yelp.to_word_level_idx(test_reviews, global_gb, WORDS_PER_TEXT)
    # -- testing data save
    np.save('Yelp_3votes_funny_test_fulltext_glove_300_X.npy', reviews_wvs_test)
    np.save('Yelp_3votes_funny_test_fulltext_glove_300_y.npy', test_labels)

    # reviews_wvs_test = yelp.to_word_level_idx(test_reviews, yelp_gb, WORDS_PER_TEXT)
    # # -- testing data save
    # np.save('Yelp_funny_test_fulltext_Yelp_glove_300_X.npy', reviews_wvs_test)
    # np.save('Yelp_funny_test_fulltext_Yelp_glove_300_y.npy', test_labels)

    del reviews_wvs_test

    # log('Hashing BOW features, might be used by some NN models')
    # hv = HashingVectorizer(n_features=BOW_HASH_DIMENSION) # Int: maybe try without normalization
    # train_bow_hash = hv.transform(train_reviews)
    # test_bow_hash = hv.transform(test_reviews)
    # np.save('Yelp_funny_train_hashbow.npy', train_bow_hash.todense())
    # np.save('Yelp_funny_test_hashbow.npy', test_bow_hash.todense())

    ##################################
    ### YELP COOL
    ##################################
    log('Saving "cool" votes data')
    (train_reviews, train_labels, test_reviews, test_labels) = \
        yelp.get_data(YELP_COOL_TRAIN, YELP_COOL_DEV, YELP_COOL_TEST)

    reviews_wvs_train = yelp.to_word_level_idx(train_reviews, global_gb, WORDS_PER_TEXT)
    # -- training data save
    np.save('Yelp_3votes_cool_train_fulltext_glove_300_X.npy', reviews_wvs_train)
    np.save('Yelp_3votes_cool_train_fulltext_glove_300_y.npy', train_labels)


    # reviews_wvs_train = yelp.to_word_level_idx(train_reviews, yelp_gb, WORDS_PER_TEXT)
    # # -- training data save
    # np.save('Yelp_cool_train_fulltext_Yelp_glove_300_X.npy', reviews_wvs_train)
    # np.save('Yelp_cool_train_fulltext_Yelp_glove_300_y.npy', train_labels)

    # del reviews_wvs_train

    reviews_wvs_test = yelp.to_word_level_idx(test_reviews, global_gb, WORDS_PER_TEXT)
    # -- testing data save
    np.save('Yelp_3votes_cool_test_fulltext_glove_300_X.npy', reviews_wvs_test)
    np.save('Yelp_3votes_cool_test_fulltext_glove_300_y.npy', test_labels)

    # reviews_wvs_test = yelp.to_word_level_idx(test_reviews, yelp_gb, WORDS_PER_TEXT)
    # # -- testing data save
    # np.save('Yelp_cool_test_fulltext_Yelp_glove_300_X.npy', reviews_wvs_test)
    # np.save('Yelp_cool_test_fulltext_Yelp_glove_300_y.npy', test_labels)
    #
    # del reviews_wvs_test

    # log('Hashing BOW features, might be used by some NN models')
    # hv = HashingVectorizer(n_features=BOW_HASH_DIMENSION) # Int: maybe try without normalization
    # train_bow_hash = hv.transform(train_reviews)
    # test_bow_hash = hv.transform(test_reviews)
    # np.save('Yelp_cool_train_hashbow.npy', train_bow_hash.todense())
    # np.save('Yelp_cool_test_hashbow.npy', test_bow_hash.todense())
