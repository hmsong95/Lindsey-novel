# Lindsey-novel
Bigdata-AI
1.누구나 쉽게 배우는 챗봇 서비스
(모던 웹 기술로 구현하는 챗봇 실무 예제)
- 박경호, BJPUBLIC, 2018.06

    개요
    -------
    모던 웹 기술 ES6(ECMAScript 2016-최신 자바스크립트), 폴리머(Polymer), 파이어베이스(firebase), DialogFlow를 활용하여 AI챗봇을 만드는 방법
    ex) 챗봇의 예 : 애플-시리, 아마존-알렉사, MS-코타나, 구글-어시스턴트

    챗봇빌더
    -------
    Wit.ai, DialogFlow, Chatfuel, IBM watson
    - 구분 : 1) 위지윅 형태의 인터페이스 기반의 빌더, 2) 개발자를 위한 코드 기반의 빌더, 3)자연어 처리 엔진 기반

    개발환경
    -------
    Sublime, MS Visual Studio Code, Node.js v6.5.2

    소스코드
    -------
    https://github.com/bjpublic/easychatbot
    https://github.com/elegant651/modernwebwithbot

    

    DialogFlow (https://dialogflow.com)
    ------------------------------------------
    1.Agent 신규생성
    https://console.dialogflow.com/api-client/#/newAgent



2.스마트한 인공지능 챗봇 개발
(HTML5 웹 채틸에서 AI 챗봇 서비스까지 한 번에 개발하기)
- 강창훈, BJPUBLIC, 2018.07



 DialogFlow (https://dialogflow.com)
    ------------------------------------------
    1.Agent 신규생성
    https://console.dialogflow.com/api-client/#/newAgent

특징
---------
의도분석, 성분분석 등을 통해 자연어 처리를 제공하며 머신러닝의 저수준 개발까지 익히지 않아도 쉽게 챗봇개발이 가능.
현재 영어에 비해 한글에 대한 자연어 처리가 불완전한 상태지만, 점점 더 발전되고 있고 지원 언어를 늘리고 있다.


Text Analytics with Python, 2nd Edition
  ------------------------------------------
• Understand NLP and text syntax, semantics and structure
• Discover text cleaning and feature engineering
• Review text classification and text clustering
• Assess text summarization and topic models
• Study deep learning for NLP

1) 머신러닝 학습 : 사용자의 의도(intent)를 분석하고 이해하며, 예시 문장을 입력하면 이와 비슷한 문장을 자동으로 학습.
2) 멀티 플랫폼 지원 : 기존 플랫폼과 연동이 손쉽다. (슬랙, 알렉사, 페북 메신저, 텔레그램)
3) 멀티 개발 SDK 제공 : 스마트 디바이스(휴대폰, 웨어러블 디바이스, 스피커, 자동차)에 적합한 개발을 위한 다양한 SDK제공하며, 개발언어별 SDK는 물론, 안드로이드와 iOS등의 플랫폼SDK도 제공
4) 다국어지원 : 21개 언어 지원(2018년 5월 기준)

Intents & Entities
--------------------
ex) "10분후에 치킨집에서 치킨 주문해줘" 의 문장에서 Intents & Entities는 다음과 같다.



Intents : 어떤 문장이 어떤 의도를 가지고 있는지 분류한다.
Entities : 성분 추출 (10분후-시간, 치킨집-장소, 치킨-주성분)


The Best Chatbots/Bot Frameworks
----------------------------------
• https://woebot.io/
    • Can track your mood
    • Helps you feel better
    • Gives you insights by seeing your mood pattern
    • Teaches you how to be positive and high-energy

• https://qnamaker.ai/
    • Build, train, and publish a simple question-and-answer bot based
    on FAQ, URLs, and structured documents in minutes.
    • Test and refine responses using a familiar chat interface.

https://dialogflow.com/
    • Formerly known as api.ai and widely popular among chatbot
    enthusiasts.
    • Give users new ways to interact with your product by building
    engaging voice-and text-based conversational interfaces powered
    by AI.
    • Connect with users on the Google Assistant, Amazon Alexa,
    Facebook Messenger, and other popular platforms and devices.
    • Analyzes and understands the user’s intent to help you respond
    in the most useful way.

https://core.rasa.ai
    • A framework for building conversational software
    • You can implement the actions your bot can take in Python code.
    • Rather than a bunch of if…else statements, the logic of your
    bot is based on a probabilistic model trained on example
    conversations.

https://wit.ai
    • Wit.ai makes it easy for developers to build applications and
    devices that you can talk or text to.
    • Acquired by Facebook within 21 months of its launch, wit.ai team
    contributes toward Facebook’s own NLP engine inside Facebook.
    • You can use wit.ai for building chatbots, home automation, etc.
    • Wit.ai is similar to the way Dialogflow works but is not as featurerich
    as Dialogflow. People initially used wit.ai, as it was free and
    Dialogflow was not, but later on Dialogflow became free as well.

• https://www.luis.ai/
    • A machine learning-based service to build natural language into
    apps, bots, and IoT devices.
    • Quickly create enterprise-ready, custom models that
    continuously improve.

• http://botkit.ai
    • Visual conversation builder
    • Built-in stats and metrics
    • Can be easily integrated with Facebook, Microsoft, IBM Watson,
    Slack, Telegram, etc.
잡아라! 텍스트 마이닝 with 파이썬
(지금 바로 할 수 있는 데이터 추출과 분석)
- 서대호, BJPUBLIC, 2019.04

개요
-------
Text Mining : 비정형 데이터에서 사용자가 분석 도구를 이용하여 새롭고 유용한 정보를 찾아내는 과정 또는 기술을 뜻함. 
              데이터 마이닝과 마찬가지로 텍스트 마이닝은 비정형 텍스트 데이터로부터 의미 있는 패턴을 탐구하여 의미 있는 정보를 찾아냄.
              

Text Mining vs Data Mining
----------------------------
텍스트 마이닝은 데이터 근원이 문서에 있으며 데이터 형태가 데이터베이스에 정형화되지 않고 문서 안에 비정형화된 형태로 있다.

소스코드
-------
https://github.com/bjpublic/tmwithpython




