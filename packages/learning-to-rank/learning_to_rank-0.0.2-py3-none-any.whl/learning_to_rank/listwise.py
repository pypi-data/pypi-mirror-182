from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pickle
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from learning_to_rank.utils import group_by, get_pairs, compute_lambda, ndcg_k


class LambdaMART:
    def __init__(self, training_data=None, number_of_trees=10, lr = 0.001,max_depth=50):
        self.training_data = training_data
        self.number_of_trees = number_of_trees
        self.lr = lr
        self.trees = []
        self.max_depth = max_depth

    def fit(self):
        """
        train the model to fit the train dataset
        """
        qid_doc_map = group_by(self.training_data, 1)
        query_idx = qid_doc_map.keys()
        # true_scores is a matrix, different rows represent different queries
        true_scores = [self.training_data[qid_doc_map[qid], 0] for qid in query_idx]
        order_paris = []
        for scores in true_scores:
            order_paris.append(get_pairs(scores))
        sample_num = len(self.training_data)
        predicted_scores = np.zeros(sample_num)
        for k in range(self.number_of_trees):
            print('Tree %d' % k)
            lambdas = np.zeros(sample_num)
            w = np.zeros(sample_num)
            temp_score = [predicted_scores[qid_doc_map[qid]] for qid in query_idx]
            zip_parameters = zip(true_scores, temp_score, order_paris, query_idx)

            for ts, temps, op, qi in zip_parameters:
                sub_lambda, sub_w, qid = compute_lambda(ts, temps, op, qi)
                lambdas[qid_doc_map[qid]] = sub_lambda
                w[qid_doc_map[qid]] = sub_w
            tree = DecisionTreeRegressor(max_depth=self.max_depth)
            tree.fit(self.training_data[:, 2:], lambdas)
            self.trees.append(tree)
            pred = tree.predict(self.training_data[:, 2:])
            predicted_scores += self.lr * pred

            # print NDCG
            qid_doc_map = group_by(self.training_data, 1)
            ndcg_list = []
            for qid in qid_doc_map.keys():
                subset = qid_doc_map[qid]
                sub_pred_score = predicted_scores[subset]

                # calculate the predicted NDCG
                true_label = self.training_data[qid_doc_map[qid], 0]
                topk = len(true_label)
                pred_sort_index = np.argsort(sub_pred_score)[::-1]
                true_label = true_label[pred_sort_index]
                ndcg_val = ndcg_k(true_label, topk)
                ndcg_list.append(ndcg_val)
            # print('Epoch:{}, train dataset: NDCG : {}'.format(k, np.nanmean(ndcg_list)))

    def predict(self, data):
        """
        predict the score for each document in testset
        :param data: given testset
        :return:
        """
        qid_doc_map = group_by(data, 1)
        predicted_scores = np.zeros(len(data))
        for qid in qid_doc_map.keys():
            sub_result = np.zeros(len(qid_doc_map[qid]))
            for tree in self.trees:
                sub_result += self.lr * tree.predict(data[qid_doc_map[qid], 2:])
            predicted_scores[qid_doc_map[qid]] = sub_result
        return predicted_scores

    def validate(self, data, k):
        """
        validate the NDCG metric
        :param data: given th testset
        :param k: used to compute the NDCG@k
        :return:
        """
        qid_doc_map = group_by(data, 1)
        ndcg_list = []
        predicted_scores = np.zeros(len(data))
        for qid in qid_doc_map.keys():
            sub_pred_result = np.zeros(len(qid_doc_map[qid]))
            for tree in self.trees:
                sub_pred_result += self.lr * tree.predict(data[qid_doc_map[qid], 2:])
            predicted_scores[qid_doc_map[qid]] = sub_pred_result
            # calculate the predicted NDCG
            true_label = data[qid_doc_map[qid], 0]
            pred_sort_index = np.argsort(sub_pred_result)[::-1]
            true_label = true_label[pred_sort_index]
            ndcg_val = ndcg_k(true_label, k)
            ndcg_list.append(ndcg_val)
        average_ndcg = np.nanmean(ndcg_list)
        return average_ndcg, predicted_scores

    def save(self, fname):
        pickle.dump(self, open('%s.lmart' % (fname), "wb"), protocol=2)

    def load(self, fname):
        model = pickle.load(open(fname, "rb"))
        self.training_data = model.training_data
        self.number_of_trees = model.number_of_trees
        self.learning_rate = model.learning_rate
        self.trees = model.trees



class ListNet_Net(nn.Module):
    def __init__(self,n_feature,h1_units,h2_units):
        super(ListNet_Net,self).__init__()
        self.l1 = nn.Linear(n_feature,h1_units)
        self.l2 = nn.Linear(h1_units,h2_units)
        self.out = nn.Linear(h2_units,1)
    def forward(self,x):
        x = self.l1(x)
        x = F.relu(x)
        x = self.l2(x)
        x = F.relu(x)
        x = self.out(x)
        return x
# class ListNet():
#     def __init__(self):
