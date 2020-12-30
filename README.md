# Project_CashFlow_v2

부동산 개발사업 관련 Project Financing 검토시 사업의 현금흐름을 추정하는 프로그램입니다.
* account 파일 : cashflow 분석을 위한 기본 모듈 포함
* Execution_Cashflow 파일 : account 모듈을 이용하여, 부동산개발사업의 현금흐름을 추정함.



## 분양 부동산 개발 사업에 대한 현금흐름 추정 모델
### 입력데이터
* 개발기간 : 24개월
* 대출만기 : 26개월
* 분양입금액 중 대출금 상환 비율 : 80%
* 분양가정
  * Product A : 900억원, (계약금 10%, 1차중도금 20%, 2차중도금 20%, 잔금 50%)
  * Product B : 500억원, (계약금 10%, 1차중도금 20%, 2차중도금 20%, 잔금 50%)
  * 분양 시나리오 : 시나리오에 따른 각각의 월에 전체 분양규모의 10%씩 분양되는 것으로 가정
* 비용 가정
  * 최초 지급 고정비 : 300억원(토지비 등)
  * 공정률에 따른 비용 : 400억원(공사비 등)
  * 분양률에 따른 비용 : 300억원(대행수수료 등)
* 대출 가정
  * 선순위 대출 : 700억원, 5.0%
  * 후순위 대출 : 300억원, 7.0%
  
### 결과물
* acc_oprtg.df : 운영계좌의 현금흐름
* acc_repay.df : 대출금 상환계좌의 현금흐름
* sales.df : 매출 실행 계좌의 현금흐름
* cost.df : 비용 지급 계좌의 현금흐름
* loanA.amt.df : 선순위대출 계좌의 현금흐름
* loanB.amt.df : 후순위대출 계좌의 현금흐름
* loanA.IR.df : 선순위대출의 이자지급 계좌 현금흐름
* loanB.IR.df : 후순위대출의 이자지급 계좌 현금흐름
