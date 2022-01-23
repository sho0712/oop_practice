"""
class *:
    関連しそうな属性:
        - 身長
        - 体重
        - BMIという値そのもの
    ルール:
        - BMIは10以上40以下 <- 常識的な範囲
        - 表示するときは小数点第2位まで
            - ex: 23.689 => 23.69
            - ex: 23.681 => 23.68
    できること:
        - BMIの計算

"""


class BMI:
    def __init__(self, height_m, weight_kg):
        self.height_m = height_m
        self.weight_kg = weight_kg


# tanaka_bmi = BMI(height=1.80, weight=67.0)
# sasaki_bmi = BMI(height=1.58, weight=80.0)
takahashi = BMI(height_m=1.65, weight_kg=68.0)

print(takahashi.height_m)
print(takahashi.weight_kg)
