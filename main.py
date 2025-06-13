import streamlit as st

def recommend_parts(budget):
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

    cpu_budget = budget * 0.3
    gpu_budget = budget * 0.4
    ram_budget = budget * 0.15
    ssd_budget = budget * 0.15

    def pick_part(parts, budget):
        candidates = [p for p in parts if p[1] <= budget]
        if candidates:
            return candidates[-1]
        else:
            return parts[0]

    cpu = pick_part(cpus, cpu_budget)
    gpu = pick_part(gpus, gpu_budget)
    ram = pick_part(rams, ram_budget)
    ssd = pick_part(ssds, ssd_budget)

    total_price = cpu[1] + gpu[1] + ram[1] + ssd[1]
    return cpu, gpu, ram, ssd, total_price

def main():
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

if __name__ == "__main__":
    main()
