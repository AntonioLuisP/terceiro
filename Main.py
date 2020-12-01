from Algoritmos import *
import numpy as np

def main():
    textoComSequencia = 'AABEBCDDSSSS'
    tamanho = 100
    vetorAordenar = list(np.random.randint(tamanho, size=(tamanho)))
    print(longestRepeatedSubSeq(textoComSequencia)) 
    print(mergeSort(vetorAordenar))
main()