def quick_sort_sub(list, start, end):  # 정렬할 리스트(모집합), 시작 인덱스, 끝 인덱스
  if end - start <= 0: return  # 기본단계: 리스트 원소 1개일때 종료
  i = start  # 정렬할 리스트 범위 처음을 i로
  pivot = list[end]  # 피벗은 가장 마지막에
  for j in range(start, end):  # 하나하나 비교하면서
    if list[j] <= pivot:  # 피벗보다 작으면
      list[j], list[i] = list[i], list[
        j]  # i와 자리를 바꾼다. (피벗보다 작은 값을 피벗 왼쪽에 두는 것)
      i += 1  # i값을 증가시켜 피벗의 인덱스? 를 올려준다.
  list[i], list[end] = list[end], list[i]  # 마지막 피벗의 자리와 서로 교환
  quick_sort_sub(list, start, i - 1)  # 피벗보다 작은 리스트 재귀
  quick_sort_sub(list, i + 1, end)  # 피벗보다 큰 리스트 재귀


def quick_sort(list):
  quick_sort_sub(list, 0, len(list) - 1)


import random
l = [random.randint(1, 1000) for _ in range(100)]
print(l)
quick_sort(l)
print(l)
