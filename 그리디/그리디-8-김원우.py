def solution(number, k):
    st = []

    for n in number:
        while st and st[-1] < n and k > 0:  # 새로 넣을 숫자가 스택 맨 위에 있는 숫자보다 크면 pop
            st.pop()
            k -= 1
        st.append(n)

    for i in range(k):  # k가 0이 아니면 끝부터 k만큼 빼주기
        st.pop()

    return "".join(st)