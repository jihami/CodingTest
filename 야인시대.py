def 솔루션(tupyoham):
    sy = 0      # 심영의 표
    kdh = 0     # 김두한의 표
    shij = 0    # 상하이조의 표

    # x는 tupyoham에 있는 모든 표를 순서대로 반복:
    for x in tupyoham:
        #만약 x가 "심영"이라면:
        if x == "심영":
            sy += 1
        if x == "김두한":
            kdh += 1
        if x == "상하이조":
            shij += 1
    # print("심영 :" , sy , " 김두한 :" , kdh , "상하이조 :" , shij)
    print(f"심영:{sy} 김두한:{kdh} 상하이조:{shij}")

tupyoham = ["심영", "심영", "김두한", "심영", "상하이조", "김두한", "심영"]
솔루션(tupyoham)