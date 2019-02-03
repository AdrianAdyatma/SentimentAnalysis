#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 18:38:43 2019

@author: axl
"""
import numpy

kamusIndonesia = list(open('kata-dasar-all.txt'))

print(kamusIndonesia[1])
#
# def minimal(atas, serong, kiri):
#     hasil = 0
#     if atas < serong:
#         hasil = atas
#     else:
#         hasil = serong
#     if hasil < kiri:
#         hasil = kiri
#     return hasil
#
#
# def hitungMED(insertByUser, wordInDict):
#     p = insertByUser.lower()
#     q = wordInDict.lower()
#     panjangP = len(p)
#     panjangQ = len(q)
#     print("panjang P: {}\nPanjang Q: {}\n".format(panjangP, panjangQ))
#     table = numpy.zeros([panjangQ + 1, panjangP + 1])
#     print("Table Kosong :\n {}\n".format(table))
#     for i in range(panjangP + 1):
#         table[0, i] = i
#     for i in range(panjangQ + 1):
#         table[i, 0] = i
#
#     for j in range(panjangQ):
#         for i in range(panjangP):
#             if q[j] == p[i]:
#                 table[j + 1, i + 1] = table[j, i]
#             else:
#                 table[j + 1, i + 1] = min(table[j, i + 1], table[j, i], table[j + 1, i]) + 1
#
#     print("Table Isi :\n {}\n".format(table))
#     print("Panjang Minimal Edit Distance adalah : {}\n".format(table[panjangQ, panjangP]))
#     return table[panjangQ, panjangP]
#
#
# def wordCorrection(word):
#     lowWord = word.lower()
#     nilaiMED = -1
#     correctWord = lowWord
#     if lowWord in kamusIndonesia:
#         print("nilai MED terkecil adalah: {}\n ".format(nilaiMED))
#         return correctWord
#     else:
#         for dictWord in kamusIndonesia:
#             if nilaiMED < 0:
#                 nilaiMED = hitungMED(lowWord, dictWord)
#                 correctWord = dictWord
#             else:
#                 if hitungMED(lowWord, dictWord) < nilaiMED:
#                     nilaiMED = hitungMED(lowWord, dictWord)
#                     correctWord = dictWord
#
#         print("nilai MED terkecil adalah: {}\n ".format(nilaiMED))
#         return correctWord
#
#
# def sentencesCorrection(sentence):
#     print("Raw Sentence : {}\n".format(sentence.split()))
#     newSent = ""
#     for word in sentence.split():
#         newSent = newSent + ' ' + wordCorrection(word)
#
#     return newSent
#
#
# if __name__ == "__main__":
#     # d = numpy.matrix([[1,2,3],[4,5,6],[7,8,9]])
#     # d = numpy.zeros([5,6])
#     # d[1,2]=10
#     # d[1+1,2+1]=13
#     # print(d)
#     sent = input("Masukan Kalimat : ")
#     print("Mungkin Maksud Anda : {}\n".format(sentencesCorrection(sent)))
#
#     # print(wordCorrection(sent))
#     # hitungMED("tutour","tutor")
#     # print(d[0,0])
#     # for i in range(5)[1:]:
#     #   print(i)