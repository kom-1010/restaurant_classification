from classification_util import ClassificationUtil

df = ClassificationUtil()

# 데이터 읽기
df.read("restaurant.csv")

# 필요없는 컬럼 id 삭제
df.drop("id")

# 데이터 보여주기
df.show()
df.myplot("peyong", "menu", "popularity")
df.heatmap()

# 데이터 학습 및 테스트
df.ignore_warning()
df.run_svm(["menu", "peyong"], "popularity")
df.run_decision_tree_classifier(["menu", "peyong"], "popularity")
df.run_logistic_regression(["menu", "peyong"], "popularity")
df.run_neighbor_classifier(["menu", "peyong"], "popularity", 5)

