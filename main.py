import streamlit as st

def recommend_drone(purpose, budget):
    drones = {
        "촬영": [
            ("DJI Mavic Air 2", "고해상도 카메라 탑재, 안정적인 비행", 120),
            ("Autel EVO Lite+", "우수한 저조도 촬영 성능", 140),
            ("DJI Phantom 4 Pro", "전문가용 고성능 카메라", 200),
            ("Parrot Anafi", "휴대성 좋고 4K 촬영 지원", 100),
            ("Skydio 2", "자율 비행 및 장애물 회피 기능 우수", 180),
            ("DJI Air 2S", "1인치 센서로 고화질 촬영 가능", 160)
        ],
        "배송": [
            ("Zipline Drone", "의약품 및 긴급 화물 배송 특화", 300),
            ("Wing Drone", "도심 내 소규모 배송에 최적화", 250),
            ("Amazon Prime Air", "빠른 배송을 위한 고속 드론", 400),
            ("Flytrex", "도심 및 교외 배송용 드론", 280),
            ("Matternet M2", "의료품 배송에 특화된 드론", 350),
            ("Tuffwing", "산간 지역 배송에 적합", 220)
        ],
        "취미": [
            ("DJI Mini 3 Pro", "가볍고 조작이 쉬움", 80),
            ("Ryze Tello", "초보자용 저가형 드론", 30),
            ("Holy Stone HS710", "가성비 좋은 레저용 드론", 60),
            ("Hubsan Zino Mini Pro", "휴대성 좋은 취미용 드론", 70),
            ("Eachine E58", "입문용 드론, 저렴한 가격", 40),
            ("Potensic T18", "간단한 촬영 및 비행 연습용", 50)
        ]
    }

    candidates = [d for d in drones.get(purpose, []) if d[2] <= budget]

    if not candidates:
        return None

    candidates.sort(key=lambda x: x[2])
    return candidates[-1]

def main():
    st.title("드론 추천기")

    purpose = st.selectbox("드론 사용 목적을 선택하세요", ["촬영", "배송", "취미"])
    budget = st.number_input("예산을 입력하세요 (만원 단위)", min_value=10, max_value=1000, value=100)

    if st.button("추천 받기"):
        result = recommend_drone(purpose, budget)
        if result:
            name, desc, price = result
            st.subheader("추천 드론")
            st.write(f"**{name}** ({price} 만원)")
            st.write(desc)
            st.write("예산 내에서 가장 적합한 드론입니다.")
        else:
            st.write("예산 내에서 추천할 수 있는 드론이 없습니다.")

if __name__ == "__main__":
    main()
