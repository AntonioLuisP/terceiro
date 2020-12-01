#para encontrar itens repetidos
def longestRepeatedSubSeq(texto):
    n = len(texto)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (texto[i-1] == texto[j-1] and i != j):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    res = ''
    i = n
    j = n
    while (i > 0 and j > 0):
        if (dp[i][j] == dp[i-1][j-1] + 1):
            res += texto[i-1]
            i -= 1
            j -= 1
        elif (dp[i][j] == dp[i-1][j]):
            i -= 1
        else:
            j -= 1
    res = ''.join(reversed(res))
    return res

#para merge sort
def mergeSort(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergeSort(vetor, inicio, meio)
        mergeSort(vetor, meio, fim)
        merge(vetor, inicio, meio, fim)
    return vetor

def merge(vetor, inicio, meio, fim):
    left = vetor[inicio:meio]
    right = vetor[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            vetor[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            vetor[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            vetor[k] = left[top_left]
            top_left = top_left + 1
        else:
            vetor[k] = right[top_right]
            top_right = top_right + 1
