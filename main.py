import streamlit as st

def recommend_drone(purpose):
    drones = {
        "촬영": [
            ("DJI Mavic Air 2", "고해상도 카메라 탑재, 안정적인 비행"),
            ("Autel EVO Lite+", "우수한 저조도 촬영 성능"),
            ("DJI Phantom 4 Pro", "전문가용 고성능 카메라")
        ],
        "배송": [
            ("Zipline Drone", "의약품 및 긴급 화물 배송 특화"),
            ("Wing Drone", "도심 내 소규모 배송에 최적화"),
            ("Amazon Prime Air", "빠른 배송을 위한 고속 드론")
        ],
        "취미": [
            ("DJI Mini 3 Pro", "가볍고 조작이 쉬움"),
            ("Ryze Tello", "초보자용 저가형 드론"),
            ("Holy Stone HS710", "가성비 좋은 레저용 드론")
        ]
    }
    return drones.get(purpose, [])

def main():
    st.title("드론 추천기")

    purpose = st.selectbox("드론 사용 목적을 선택하세요", ["촬영", "배송", "취미"])

    if st.button("추천 받기"):
        recommendations = recommend_drone(purpose)
        if recommendations:
            st.subheader(f"{purpose} 용 추천 드론 리스트")
            for name, desc in recommendations:
                st.write(f"- **{name}**: {desc}")
        else:
            st.write("적합한 드론이 없습니다.")

if __name__ == "__main__":
    main()
