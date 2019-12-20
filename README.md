# 동네 식당 데이터 분류하기

## 개요

마을을 돌아다니면서 주변 식당에 관한 데이터를 수집하였습니다.

데이터 내용은 주차 공간, 식당 평수, 인기도 등을 수집하였습니다.

`restaurant.csv`의 `menu`의 번호는 다음을 가리킵니다.

| menu | name     |
| ---- | -------- |
| 1    | 돼지고기 |
| 2    | 닭고기   |
| 3    | 치킨     |
| 4    | 해물     |
| 5    | 횟집     |
| 6    | 술집     |
| 7    | 한식     |
| 8    | 햄버거   |
| 9    | 기타     |

## 데이터 읽기 및 처리

다음 코드를 사용하여 csv 파일을 읽기, 필요없는 컬럼 삭제, 데이터 확인을 할 수 있습니다. 

```python
df.read("restaurant.csv")
df.drop("id")
df.show()
```

## 데이터 시각화

다음 코드를 사용하여 데이터를 확인할 수 있습니다.

```python
df.myplot("peyong", "menu", "popularity")
df.heatmap()
```

## 데이터 학습 및 테스트

다음 코드를 사용하여 테스트합니다.

```python
df.run_svm(["menu", "peyong"], "popularity")
df.run_decision_tree_classifier(["menu", "peyong"], "popularity")
df.run_logistic_regression(["menu", "peyong"], "popularity")
df.run_neighbor_classifier(["menu", "peyong"], "popularity", 5)
```
