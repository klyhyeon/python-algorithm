###  Binary Search - LeetCode

#### 최초 소요시간
- 50분 (첫 제출 테스트 실패, 실패 예외 수정 후 성공)
#### 최초 접근방식
- last, middle(first)만 두고 target 비교 조건을 세 가지로 나눠 반복
- 케이스들를 손으로 써가며 조건문을 수정, 끼워 맞추기식 풀이
- 어째저째 답은 나왔지만 풀이 시간이 오래걸린 점이 아쉬움, 알고리즘 시간 복잡도는 충족
#### 찾은 접근방식
- 1~100 UP, DOWN 놀이 방식 그대로 써서 코드로 구현하면 쉬움
- 답이 74일때 50이라 외치면 'UP'이라 범위를 51~100으로 조정
- 51(left), 100(right)로 놓고 left <= right 조건 내에서 반복 진행
- UP이면 left + 1. DOWN이면 right - 1

---
- 찾은 접근방식: Gemini
- 문제링크: https://leetcode.com/problems/binary-search/description/