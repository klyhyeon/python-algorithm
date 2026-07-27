# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 매일 다른 조합의 옷
# 2차원 배열 두번째 인자가 옷 종류
# 옷 종류별 리스트 맵 {headgear: [hat, cat], eyewear: [sunglasses, glasses, goggle]}
# 모든 조합의 수 리턴
# clothes	return
# [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
# [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3
# 실패: 경우의 수 곱의 법칙
# 소요시간: 40분

from collections import defaultdict
from typing import List

def solution(clothes):
    # 경우의 수
    # 1. 1벌: clothes의 전체 인자 length
    # 2. 2벌, n벌...
    # n은 clothes 맵 key의 개수
    typed_clothes = defaultdict(list)
    answer = 1
    for cloth in clothes:
        value = cloth[0]
        type = cloth[1]
        typed_clothes[type].append(value)
    for item in typed_clothes.values():
        answer *= (len(item) + 1)
    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))