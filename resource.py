import random
from fractions import Fraction

def generate_equation():
    # 随机生成方程的系数和x的值（确保系数不为零）
    k1 = random.randint(1, 5)  # 方程左侧括号外的系数
    k2 = random.randint(1, 5)  # 方程右侧括号外的系数（可以与k1不同）
    
    a_numerator = random.randint(1, 10)  # 方程左侧分子x的系数
    b_numerator = random.randint(-10, 10)  # 方程右侧分子x的系数
    c_numerator = random.randint(-20, 20)  # 方程左侧分子的常数项
    d_numerator_initial = random.randint(-20, 20)  # 方程右侧分子初始的常数项（将用于计算d_numerator_target）
    
    # 随机生成分母（确保不为零）
    denominator1 = random.randint(2, 5)
    denominator2 = random.randint(2, 5)
    while denominator1 == denominator2:  # 确保两个分母不相同
        denominator2 = random.randint(2, 5)
    
    # 设定一个x的解
    x_solution = random.randint(-10, 10)
    
    # 如果它们相等，我们需要调整b_numerator, d_numerator_initial, denominator1 或 denominator2来确保方程有解
    while k1 * a_numerator * denominator2 == k2 * b_numerator * denominator1:
        b_numerator = random.randint(-10, 10)  # 重新生成b_numerator
        # 也可以重新生成a_numerator, k1, k2, denominator1, denominator2或x_solution，但为了简化，这里只重新生成b_numerator
    
    # 计算d_numerator_target以确保方程有解
    d_numerator_target = Fraction((k1 * c_numerator * denominator2 + (k1 * a_numerator * denominator2 - k2 * b_numerator * denominator1) * x_solution), (k2 * denominator1))
    d_numerator_target = int(d_numerator_target.limit_denominator())  # 转换为整数，如果可能的话（使用分数的最简形式）
    
    # 构建方程表达式
    equation_expr = f"{k1} * ({a_numerator}x + {c_numerator}) / {denominator1} = {k2} * ({b_numerator}x + {d_numerator_target}) / {denominator2}"
    
    # 返回方程表达式和对应的x值（虽然这里没有直接返回x值，但可以在需要时打印或返回）
    return equation_expr

if __name__ == "__main__":
    for _ in range(10):  # 生成10个方程作为示例
        equation = generate_equation()
        print(f"方程: {equation}")
