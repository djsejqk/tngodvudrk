import streamlit as st

# 부품별 추천 후보 리스트 (부품명, 가격)
cpus = [
    ("Intel i3", 100),
    ("Intel i5", 200),
    ("Intel i7", 300),
    ("Intel i9", 500)
]

gpus = [
    ("GTX 1050", 150),
    ("RTX 2060", 350),
    ("RTX 3070", 600),
    ("RTX 4090", 1500)
]

rams = [
    ("8GB", 40),
    ("16GB", 80),
    ("32GB", 150)
]

ssds = [
    ("256GB SSD", 50),
    ("512GB SSD", 80),
    ("1TB SSD", 150)
]

def recommend_parts(budget):
    # 간단한 로직: 예산을 부품 4개에 적절히 배분 (CPU 30%, GPU 40%, RAM 15%, SSD 15%)
    cpu_budget = budget * 0.3
    gpu_budget = budget * 0.4
    ram_budget = budget * 0.15
    ssd_budget = budget * 0.15

    def pick_part(parts, budget):
        # 예산 내에서 가장 좋은 부품 선택
        candidates = [p for p in parts if p[1] <= budget]
        if candidates:
            return candidates[-1]  # 가장 비싼 것 선택
        else:
            return parts[0]  # 예산 부족시 가장 저렴한 것 선택

    cpu = pick_part(cpus, cpu_budget)
    gpu = pick_part(gpus, gpu_budget)
    ram = pick_part(rams, ram_budget)
    ssd = pick_part(ssds, ssd_budget)

    total_price = cpu[1] + gpu[1] + ram[1] + ssd[1]
    return cpu, gpu, ram, ssd, total_price

st.title("컴퓨터 견적 추천기")

budget = st.number_input("예산을 입력하세요 (단위: 만원)", min_value=10, max_value=10000, value=100)

if st.button("견적 내기"):
    cpu, gpu, ram, ssd, total = recommend_parts(budget)
    st.subheader("추천 견적")
    st.write(f"CPU: {cpu[0]} - {cpu[1]} 만원")
    st.write(f"GPU: {gpu[0]} - {gpu[1]} 만원")
    st.write(f"RAM: {ram[0]} - {ram[1]} 만원")
    st.write(f"SSD: {ssd[0]} - {ssd[1]} 만원")
    st.write(f"총 합계: {total} 만원")
    st.write(f"예산 대비 {budget - total} 만원 여유가 있습니다.")
