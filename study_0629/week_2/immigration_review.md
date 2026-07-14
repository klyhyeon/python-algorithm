###  Binary Search - LeetCode

#### 최초 소요시간
- 30분 (첫 제출 실패, 풀이 보고 다시 풀어봄)
#### 최초 접근방식
- 이분탐색 문제인 건 알았지만, 타겟 기점을 뭘로 두고 탐색해야할지 고민됨
#### 찾은 접근방식
- 이분탐색 범위을 소요시간 left, right로 두고 소요시간(time_limit) 내 심사관마다 처리 가능한 입국자 수(customers)를 더해 총 입국자 수(n)와 비교하니 쉬워짐

#### 예외로직
- 이분탐색 반복문에서 `customers == n`이 나오더라도 최적의 해를 찾아야 하기 때문에 `right = middle - 1` 해주는 것이 주요
- 빼먹어서 틀림

---
- 찾은 접근방식: Gemini
- 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/43238