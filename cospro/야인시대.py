def 솔루션(tupyoham):
    #딕셔너리에 각각의 키에 대한 value를 0으로 초기화
    투표수 = {"심영":0, "김두한":0, "상하이조":0}

    # x는 키값으로 하여 딕셔너리에 접근
    for x in tupyoham:
        투표수[x]+= 1
    print(f"심영:{투표수['심영']} 김두한:{투표수['김두한']} 상하이조:{투표수['상하이조']}")
tupyoham = ["심영", "심영", "김두한", "심영", "상하이조", "김두한", "심영"]
솔루션(tupyoham)