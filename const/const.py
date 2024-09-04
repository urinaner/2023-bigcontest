import os

# 파이썬 에이전트 Prefix
CUSTOM_PYTHON_AGENT_PREFIX = f"""
You are an agent designed to write and execute python code to answer questions.
You have access to a python_repl_ast, which you can use to execute python code.
If you get an error, debug your code and try again.
Only use the output of your code to answer the question. 
You might know the answer without running any code, but you should still run the code to get the answer.
If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
If you receive Python code as a question, it is the code that you need to execute. first analyze the intent of the code. Then begin the process of executing the code.

WORKING DIRECTORY: {os.getcwd()}
"""

# 판다스 에이전트 커스텀 Prefix
CUSTOM_PANDAS_AGENT_PREFIX = """
Do NOT enter symbol ` in the 'Action' field and 'Final Answer'.
Action field MUST be just 'python_repl_ast', NOT '`python_repl_ast`' or 'Use the python_repl_ast tool to...'.

If you receive Python code as a question, first analyze the intent of the code. Then begin the process of executing the code.

Final Answer should include the content of Thought. The Final Answer should not be in the form of "The values ... is provided above."
Do not write in markdown format in the Final Answer.
"""

CUSTOM_PANDAS_AGENT_PREFIX_GPT4 = """
You have the ability to run Python code. All the files you need are already in place.

Do NOT enter symbol ` in the 'Action' field and 'Final Answer'.
Action field MUST be just 'python_repl_ast', NOT '`python_repl_ast`'.

If you receive Python code as a question, it is absolutely imperative that you execute the code. Begin the process and proceed methodically through each step.

Final Answer should include the content of Thought. The Final Answer should not be in the form of "The values ... is provided above."
Do not write in markdown format in the Final Answer and do not use symbol `.
"""

CUSTOM_PANDAS_AGENT_PREFIX_GPT4_LOGPROCESS = """
You have the ability to run Python code. All the files you need are already in place.

Do NOT enter symbol ` in the 'Action' field and 'Final Answer'.
Action field MUST be just 'python_repl_ast', NOT '`python_repl_ast`'.

If you receive Python code as a question, it is absolutely imperative that you execute the code. 
Begin the process and proceed methodically through each step.

Many agents work in sequence and it's your turn. Don't question what you're being asked to do. 
If you receive a request that contradicts what you know, your information is out of date. 
So It is absolutely imperative that you execute the request exactly as it was entered.
For example, if you are asked to save df_grouped as a csv, df_grouped already exists in your virtualization.
For example, If you are asked to group dataframe 'df' by 'user_id' and 'event_category', the column event_category must exist in df in the current environment.
another agent has previously done all the necessary work.

Note: Be sure to save the results of df.groupby()[].count() to log_data_preprocessed.csv. 
The temporary variable name to use for this is df_grouped.
For operations like csv_save, you should use df_grouped.

Final Answer should include the content of Thought. The Final Answer should not be in the form of "The values ... is provided above."
Do not write in markdown format and do not use symbol ` in the Final Answer.
"""

# 판다스 안정화, 상위 라우터 프롬프트에서 사용
PANDAS_STABILIZATION = """
Once you have observed a satisfactory pandas run, do not run the tool any further and return the results.
When using PandasDataFrameAgent, enter a code and a natural langauge description in the 'Action Input' field.
"""


# =======================================================================================================================
# 핀다 앱 정보
DATASET_CONTEXT = """
data context : Those are describing the information in the lending app Finda in the original files before the CSV files were processed.

'user_spec.csv' : user 신용정보
No.	컬럼ID	컬럼명	암호화 및 가명화	기타
1	application_id	신청서 번호	Y	
2	user_id	유저 번호	Y	
3	birth_year	유저 생년월일		
4	gender	유저 성별		0: 여자, 1: 남자
5	insert_time	생성일시		
6	credit_score	한도조회 당시 유저 신용점수	10점단위 반올림	
7	yearly_income	연소득	100만단위 반올림	
8	income_type	근로형태		"EARNEDINCOME: 직장가입자(4대보험O) EARNEDINCOME2: 직장가입자(4대보험X) PRIVATEBUSINESS: 개인사업자 PRACTITIONER: 전문직 FREELANCER: 프리랜서 OTHERINCOME: 기타소득"
9	company_enter_month	입사연월		
10	employment_type	고용형태		
11	houseown_type	주거소유형태		
12	desired_amount	대출희망금액	100만단위 반올림	
13	purpose	대출 목적		
14	personal_rehabilitation_yn	개인회생자 여부		0: 개인회생자X, 1: 개인회생자O
15	personal_rehabilitation_complete_yn	개인회생자 납입 완료 여부		0: (개인회생자인 경우) 납입중, 1: 납입완료
16	existing_loan_cnt	기대출수		
17	existing_loan_amt	기대출금액	100만단위 반올림	

loan_result.csv	: 사용자가 신청한 대출별 금융사별 승인결과 
No.	컬럼ID	컬럼명	암호화 및 가명화
1	application_id	신청서 번호	Y
2	loanapply_insert_time	한도조회 일시	
3	bank_id	금융사 번호	Y
4	product_id	상품 번호	Y
5	loan_limit	승인한도	십만단위 반올림
6	loan_rate	승인금리	둘째자리에서 반올림
7	is_applied	신청 여부(타겟)	예측레이블(NaN이 테스트 데이터)

log_data.csv : finda App 로그 정보 	
No.	컬럼ID	컬럼명	암호화 및 가명화
1	user_id	유저 번호	Y
2	event	행동명	
3	timestamp	행동일시	
4	date_cd	일 코드	
5	mp_os	디바이스기종	
6	mp_app_version	앱버전

행동명(event) 정의:
event_new	event description
SignUp	회원가입
OpenApp	핀다 앱 실행
Login	핀다 앱 로그인
ViewLoanApplyIntro	한도조회 인트로 페이지 조회
StartLoanApply	한도조회 시작하기 버튼 클릭
CompleteIDCertification	본인인증완료
EndLoanApply	한도조회 결과 확인
UseLoanManage	대출관리 서비스 이용
UsePrepayCalc	여윳돈 계산기 서비스 이용
UseDSRCalc	DSR 계산기 서비스 이용
GetCreditInfo	KCB 신용정보 조회	
"""

FINDA_SERVICE_INFO = """
FINDA 서비스 소개:
Pinda is providing services that enable everyone to access and benefit from information and make better financial choices that have traditionally been reserved for the few.
As a service, we match app users with the best loan products and allow them to apply for loans in the app.
As a MyData provider, Pinda also offers repayment plans to help you manage your loans and improve your credit score.
Pinda has launched a comparison loan service that allows users to compare the loan information received through MyData with the product information of the relay information and change to a product with a lower interest rate than the previous loan.

The comparison loan service, which is relevant to this issue, is characterized by providing users with an optimal loan experience without documents within 5 minutes.
The FINDA service engine instantly submits the customer's income, employment, credit information, etc. to the credit scoring models of 67 financial institutions directly connected to the dedicated infrastructure, and the customer receives the exact loan terms at once within one minute, and can compare and select the most optimal finalized terms without submitting any documents, and completes the loan deposit within five minutes.
FINDA also provides a management service that allows individuals scattered across MyData providers to repay their loans well to improve their credit scores based on accurate loan information.
You can view all of your loans, from mortgages to student loans, in one place, and it provides various information and features such as a DSR affordability calculator.
Beyond the credit and mortgage markets, FINDA is accelerating innovation in the non-face-to-face auto finance market to resolve information imbalances in the auto installment and lease rental markets.
FINDA is currently live with more than 200 loan products from 67 financial institutions, which is the largest number of loan relay platform services.
With 67 financial institutions, the most in the industry, we have contributed to the revitalization of mid-interest loans that the market has not been able to easily solve.
FINDA's user base is made up of customers, with 6 out of 10 using mid-interest loans.
This was achieved through the goodwill competition of multiple financial companies on a loan comparison platform, filling a gap in the mid-interest loan market that internet banks had focused on but failed to fill.
By comparing their customers' loan information with the loan products offered on the platform, FINDA, a big data provider, has been able to offer customers better deals and help them switch loans by increasing their limits to bring down the average interest rate by 3.8%.
"""

FINDA_QUESTION = """
데이터 분석 문제 소개:
First, after signing up for the FINDA App Service, the customer starts the application through the home screen.
At this time, information such as member information, owned devices, and the time of membership is collected through membership registration. The second step is to enter the purpose of the loan and the desired amount through the loan application button on the home screen.
The third step is to submit your asset information and company information.
Through the second and third processes, the applicant's credit score, company, and salary information are verified, which is necessary for loan review.
Finally, the loan application information collected, along with the information verified through a certificate, is sent to the lender. is sent to 67 lenders via a dedicated line connected to the lenders, and the applicant receives the results within a minute.
At this time, the applicant's creditworthiness and existing loans are taken into account, and the approved and rejected products can be checked through the app's logs.
In the final step, the screening results of 67 financial society products per application are checked through the data, and the product name, approval, and rejection are identified.

The challenge is to learn from the data obtained through this process and develop a model that can accurately predict which customers will apply for a loan within a certain period of time after signing up.
"""

FINDA_QUESTION_2 = """
The second problem is to analyze the clustering of customers entering the Finda home screen.
Not all customers who use the Finda app need a loan.
There are clusters of customers with various types of reasons hiding in the Finda data, such as those who check their creditworthiness, those who want to connect their existing loan information to their My Data, and those who don't know how to use Finda's services properly.
The challenge is to perform model-based customer cluster analysis through the provided data, analyze the characteristics of customers by cluster, and limit the possible services in the Finda app.
"""


FINDA_서비스_한글설명 = """
FINDA 서비스 소개:
핀다는 기존에 소수만이 누릴 수 있었던 금융의 정보 접근성과 혜택을 모든 사람들이 누리고 더 나은 금융 선택을 할 수 있도록 서비스를 제공하고 있습니다.
핀다는 서비스는 앱 사용자에게 가장 좋은 조건의 대출 상품을 제공하고 앱에서 대출을 신청할 수 있도록 하고 있습니다.
또한 마이데이터 사업자인 핀다는 대출을 통합적으로 관리하고 신용점수를 높일 수 있는 상환플랜을 제공합니다.
마이데이터를 통해 받은 대출 정보와 중계정보 상품 정보를 비교하여 이전에 받았던 대출보다 더 낮은 금위의 상품으로 변경할 수 있는 대환 대출 서비스를 출시하였습니다.

본 문제와 상관 있는 비교 대출 서비스는 사용자에게 5분 이내에 서류 없이 최적의 대출 경험을 제공하는 것이 특징입니다.
FINDA 서비스 엔진이 고객의 소득, 재직, 신용정보 등을 전용 인프라로 직접 연결된 67개 금융기관의 신용평가 모델에 즉시 제출하고, 고객은 1분 이내에 정확한 대출 조건을 한 번에 받아 비교 선택할 수 있어 서류 제출 없이 가장 최적의 확정 조건으로 5분 이내에 대출 입금까지 완료하는 서비스입니다.
FINDA는 MyData 사업자로 흩어져 있는 개인의 정확한 대출 정보를 바탕으로 대출을 잘 갚아 신용 점수를 높일 수 있는 관리 서비스 또한 제공합니다.
주택담보대출부터 학자금 대출까지 보유한 대출을 통합적으로 조회할 수 있고 DSR 여유돈 계산기 등의 다양한 정보와 기능들을 제공하고 있습니다.
FINDA는 신용 및 담보대출 시장을 넘어 자동차 할부와 리스 렌트 시장의 정보불균형을 해소하고자 비대면 오토 금융시장의 혁신에 속도를 내고 있습니다.
FINDA는 대출중계 플랫폼 서비스 중 가장 많은 67개 금융기관 200여 개의 대출 상품을 현재 라이브하고 있습니다.
업계 최다 67개 제유 금융사와 함께 시장이 쉽게 해결하지 못하였던 중금리 대출 활성화에 기여하였습니다.
FINDA의 사용자는 10명 중 6명은 중금리 대출을 사용하는 고객으로 구성되어 있습니다.
그동안 인터넷 은행이 주력했지만 채우지 못했던 중금리 대출 시장의 공백을 대출 비교 플랫폼에서 여러 금융사의 선의의 경쟁을 통해 이뤄낸 성과입니다.
마이데이터 사업자인 FINDA는 고객의 대출 정보와 플랫폼에서 제공하는 대출 상품과 비교하여 더 나은 조건의 상품을 고객에게 제공하고, 이를 통해 평균금리를 3.8% 낮추도록 한도를 더 높여 대출을 갈아탈 수 있도록 도와왔습니다.
"""

FINDA_문제_한글설명 = """
데이터 분석 문제 소개:
첫째로, FINDA 앱 서비스 회원가입 후 고객이 홈 화면을 통해 신청이 시작됩니다.
이때 회원가입을 통해 회원 정보, 보유 기기, 회원 가입 이시 등의 정보가 수집되고 두 번째 단계로 홈 화면에 대출 신청 버튼을 통해 자신이 희망하는 대출 목적과 희망하는 금액을 입력합니다.
셋째로 자신의 자산 정보와 회사 정보를 제출합니다.
두 번째, 세 번째 과정을 통해 대출 심사 시 필요한 신청자의 신용 점수, 재직 회사, 급여 정보들이 확인되어 집니다.
마지막으로 인증서를 통해 본인 인증이 된 정보와 함께 수집된 대출 신청 정보는 금융사와 연결된 전용선을 통해 67개 금융사에 전송되고 1분 이내 심사된 결과를 받게 됩니다.
이때 신청자의 신용도, 기보유 대출을 감안하여 승인된 상품과 거절된 상품은 앱의 로그를 통해 확인할 수 있습니다.
마지막 단계를 통해 1회 신청당 67개 금융사회 상품의 심사 결과가 데이터를 통해 확인되어지며 상품명, 승인, 거절에 대한 여부가 파악됩니다.

이러한 과정을 통해 얻어진 데이터를 학습하여 회원 가입 이후 특정 기간 안에 대출 신청 고객을 정확히 예측할 수 있는 모델을 개발하는 것이 문제입니다.


22년 두 번째 문제는 핀다홈 화면 진입 고객의 군집 분석이 목적이었습니다.
핀다 앱을 사용하는 모든 고객이 대출을 필요로 하지 않습니다.
자신의 신용도를 확인하는 사람, 기 대출 정보를 마이 데이터로 연결하고자 하는 사람, 핀다 내 서비스를 제대로 몰라 사용하지 못하는 사람 등 다양한 유형의 이유를 가진 고객의 군집이 핀다 내 데이터에 숨어 있습니다.
제공된 데이터를 통해 모델 기반의 고객 군집 분석을 수행하시고 군집별 고객의 특성을 분석하고 핀다 앱에서 가능한 서비스를 제한하는 것이 작년의 문제였으며 이를 통해 데이터 기반의 서비스를 체험해 볼 수 있는 과정을 경험할 수 있도록 문제가 출제되었었습니다.
작년과 동일하게 본 경진대회에서 제공되는 데이터는 회원가입 이후 생성되는 가명화 처리된 앱 로그 정보, 신용 정보, 승인된 대출 상품 정보와 대출 신청 여부 등의 핀테크에서만 경험할 수 있는 데이터가 제공됩니다.
연계 금융사와 내부 사업의 정보들이 노출되지 않도록 익명화 모스 데이터의 샘플링과 중요 정보들은 코드로 처리되어 제공되었습니다.
예측을 위한 모델링 Y레이블은 앱 사용자가 대출을 조회하고 승인된 금융 상품 중 최소 하나를 선택하여 대출을 실행한 경우 Y로 표시하였으며
학습 데이터와 추론 데이터의 구성은 시점상 크게 다르지 않도록 하여 시계열적 정보량이 적절히 반영되어 질 수 있도록 하였고 기간이 바로 이어짐으로 직전 데이터의 영향도가 너무 높지 않도록 기간을 두고 추론 데이터를 제공했었습니다.

최종적인 경진대회 산출물의 평가는 생성형 AI를 활용하여
전통적인 데이터 분석 예측 문제의 각 단계를 자동화하는 것이며
데이터의 입력 및 학습 방법을 잘 고려해 주시기를 제안 드립니다.
생성형 AI 특성상 바로 이전에 입력된 데이터의 목적만을 달성하는
오버피팅의 문제가 있으므로 적절한 재현성이 가능한 방법을 찾는 것 또한 매우 중요하겠습니다.

앞서 말씀드린 생성형 AI의 생성된 데이터의 부정확성을 방지하기 위해
여러분들께서는 다양한 방법론을 제시하시고
이를 활용하는 것을 결과 리포트에 반드시 포함하여 주시길 바라며
결과물은 22년 데이터 분석 결과와 비교하여 정합성을 심사할 예정입니다.

마지막으로 데이터를 학습한 생성형 AI 도구를 활용하여
가능한 서비스 예시를 제안해 주시면 감사드리겠습니다.
"""
