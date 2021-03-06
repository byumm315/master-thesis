# 석사 학위 논문 #
'대응분석과 토픽모델링을 이용한 계층적 감성분석' 석사 학위논문 파이썬 CODE 입니다.

**1. Crawling 폴더**

크롤링하는 파이썬 코드와 크롤링 결과 파일(크롤링_Result_방역_경향신문.xlsx)가 있습니다.

**2. Sentimental_Analysis 폴더**

감성분석하는 파이썬 코드와 필요한 파일이 있습니다.

과정은 아래와 같습니다.

**1. 총선 기사 감성분석**
  1) 감성사전 품사 추출하기
  2) 총선기사 품사 추출하기
  3) 감성점수 매기기

**2. 개천절집회 기사 감성분석**
  1) 감성사전 품사 추출하기
  2) 개천절집회 기사 품사 추출하기
  3) 감성점수 매기기

**3. 방역 기사 감성분석**
  1) 감성사전 품사 추출하기
  2) 방역 기사 품사 추출하기
  3) 감성점수 매기기

**3. Topic Modeling 폴더**

방역 기사를 토픽모델링하는 파이썬 코드와 필요한 파일이 있습니다.

과정은 아래와 같습니다.

1. 데이터 불러오기
2. 한글제외 제거
3. Komoran 이용하여 형태소 분석 수행
4. 분리된 단어 통합
5. 필요없는 단어 삭제
6. 기사별 Phrase 결합
7. 토픽모델링 사전작업
8. 토픽수에 따른 Coherence Score 구하기
9. 토픽모델링 하기
10.토픽모델링 결과: 문서별 토픽 비율 정리

**4. Correspondence Analysis 폴더**

대응분석하는 SAS 코드와 필요한 파일이 있습니다.

1. 데이터 불러오기(예시: 조선일보의 주제별 분류된 감성 파일)
2. 대응행렬로 변환하기(주제와 감성간의 대응행렬)
3. 대응분석을 통해 이차원 공간에 시각화하기(주제와 감성간의 비대칭그림 표현)
