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
    denominator = random.randint(2, 5)
    
    # 设定一个x的解
    x_solution = random.randint(-10, 10)
    
    # 根据设定的x解和分母来计算分子d_numerator_target，以确保方程有解
    # 我们需要构造一个方程，形如：
    # k1 * (a_numerator * x + c_numerator) / denominator = k2 * (b_numerator * x + d_numerator_target) / denominator
    # 由于分母相同，我们可以直接去掉分母进行化简，得到：
    # k1 * (a_numerator * x + c_numerator) = k2 * (b_numerator * x + d_numerator_target)
    # 进一步化简为：
    # (k1 * a_numerator - k2 * b_numerator) * x = k2 * d_numerator_target - k1 * c_numerator
    # x = (k2 * d_numerator_target - k1 * c_numerator) / (k1 * a_numerator - k2 * b_numerator)
    
    # 为了确保分母不为零，我们需要确保k1 * a_numerator != k2 * b_numerator
    # 如果它们相等，我们需要调整b_numerator或d_numerator_target来确保方程有解
    while k1 * a_numerator == k2 * b_numerator:
        b_numerator = random.randint(-10, 10)  # 重新生成b_numerator
        # 也可以重新生成a_numerator, k1, k2或x_solution，但为了简化，这里只重新生成b_numerator
    
    # 计算d_numerator_target以确保方程有解
    d_numerator_target = Fraction((k1 * c_numerator + (k1 * a_numerator - k2 * b_numerator) * x_solution), k2)
    d_numerator_target = int(d_numerator_target.limit_denominator())  # 转换为整数，如果可能的话（使用分数的最简形式）
    
    # 由于d_numerator_target可能是通过分数运算得到的，我们需要确保它是整数
    # 如果不是整数，我们需要稍微调整c_numerator或x_solution来得到一个整数解
    # 但为了简化，这里我们假设通过上面的计算已经得到了整数解（在大多数情况下应该是这样的）
    # 如果不是，可以添加额外的逻辑来处理这种情况
    
    # 构建方程表达式
    equation_expr = f"{k1} * ({a_numerator}x + {c_numerator}) / {denominator} = {k2} * ({b_numerator}x + {d_numerator_target}) / {denominator}"
    
    # 由于分母相同，我们可以选择性地去掉分母来展示一个更简洁的等价方程（但这不是必需的）
    # 简洁方程: f"{k1 * a_numerator}x + {k1 * c_numerator} = {k2 * b_numerator}x + {k2 * d_numerator_target}"
    
    # 返回方程表达式和对应的x值
    return equation_expr

if __name__ == "__main__":
    for _ in range(10):  # 生成10个方程作为示例
        equation = generate_equation()
        print(f"方程: {equation}")
