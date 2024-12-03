import random

def generate_equation():
    # 随机生成方程的系数（确保系数不为零）
    k1 = random.randint(1, 5)  # 方程左侧括号外的系数
    k2 = random.randint(1, 5)  # 方程右侧括号外的系数
    
    a_numerator = random.randint(1, 10)  # 方程左侧x的系数
    b_numerator = random.randint(-10, 10)  # 方程右侧x的系数
    c_numerator = random.randint(-20, 20)  # 方程左侧分子的常数项
    
    # 随机生成分母（确保不为零）
    denominator1 = random.randint(2, 5)  # 以允许整数系数
    denominator2 = random.randint(2, 5)
    while denominator1 == denominator2:  # 确保两个分母不相同
        denominator2 = random.randint(2, 5)
    
    # 设定一个x的整数解
    x_solution = random.randint(-10, 10)
    
    d_numerator_target = (k1 * (a_numerator * x_solution + c_numerator) * denominator2 - k2 * b_numerator * x_solution * denominator1) // (k2 * denominator1)
    
    # 构建方程表达式
    equation_expr = f"{k1} * ({a_numerator}x + {c_numerator}) / {denominator1} = {k2} * ({b_numerator}x + {d_numerator_target}) / {denominator2}"
    
    # 返回方程表达式
    return equation_expr

if __name__ == "__main__":
    for _ in range(10):  # 生成10个方程作为示例
        equation = generate_equation()
        print(f"方程: {equation}")
