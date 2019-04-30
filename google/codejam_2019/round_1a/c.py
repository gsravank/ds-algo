# from collections import defaultdict
#
#
# class Node:
#     def __init__(self):
#         self.children = defaultdict()
#         self.words = list()
#
#
#
# class Trie():
#     def __init__(self):
#         self.root = Node()
#
#     def insert(self, word):
#         root = self.root
#         len1 = len(word)
#
#         for i in range(len1):
#             index = int(word[i])
#             root.words.append(word)
#             if index not in root.children:
#                 root.children[index] = Node()
#
#             root = root.children[index]
#
#
# def get_count(root, val_list):
#     curr_level_words = root.words
#     next_level_words = list()
#
#     for key in root.children:
#         next_level_words.extend(root.children[key].words)
#
#     n = len(set(next_level_words) - set(curr_level_words))
#     val_list[0] += 2 * int(n/2)
#
#     for key
#
#     return
#
#
# def get_answer(N, W):
#     trie = Trie()
#
#     for wi in W:
#         trie.insert(wi)
#
#
#     root = trie.root
#     answer_list = [0]
#
#     for key in root.children:
#         get_count(root.children[key], answer_list)
#
#     return answer_list[0]
#
#
# for ti in range(int(input())):
#     N = int(input())
#     W = list()
#     for _ in range(N):
#         W.append(input())
#
#     answer = get_answer(N, W)
#     print("Case #{}: {}".format(ti + 1, answer))