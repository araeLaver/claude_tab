import anthropic

# 사용자 입력 받기
user_input = input("메시지를 입력하세요: ")

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="",
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=2021,
    temperature=0.9,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_input
                }
            ]
        }
    ]
)
print(message.content)


# prompt: Claude에게 전달할 프롬프트 텍스트입니다. 이전 대화 내용과 새로운 사용자 입력을 포함합니다.
# stop_sequences: Claude의 응답 생성을 중단시키는 시퀀스를 지정합니다. 여기서는 사용자 프롬프트를 의미하는 anthropic.HUMAN_PROMPT를 사용했습니다.
# max_tokens_to_sample: Claude이 생성할 수 있는 최대 토큰 수를 지정합니다.
# model: 사용할 Claude 모델의 이름을 지정합니다. 여기서는 "claude-v1"을 사용했습니다.

# Temperature는 생성 모델의 출력 결과의 무작위성을 조절하는 하이퍼파라미터입니다. 0에서 1 사이의 값을 가지며, 값이 높을수록 더 다양하고 창의적인 결과를 생성하지만, 일관성과 관련성은 떨어질 수 있습니다.

# Temperature = 0: 모델은 항상 가장 높은 확률의 다음 단어를 선택합니다. 출력 결과가 가장 안정적이고 일관성이 높지만, 변화가 적고 창의성이 제한될 수 있습니다.
# Temperature = 1: 모델은 확률 분포에 따라 다음 단어를 무작위로 선택합니다. 출력 결과가 가장 다양하고 창의적이지만, 일관성과 관련성이 떨어질 수 있습니다.
# 0 < Temperature < 1: 값이 높을수록 무작위성이 증가하고, 값이 낮을수록 안정성이 증가합니다.