from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage

from config import model
from tools import get_coordinates, get_weather

agent = create_agent(
    model=model,
    tools=[get_coordinates, get_weather],
)


def build_system_prompt(preferences: dict) -> str:
    preferences = preferences or {}
    return f"""你是一個親切的天氣生活助理。根據 get_weather 工具回傳的天氣數據，
自行判斷是否需要外套、帶傘、防曬、留意溫差或風大，並考慮使用者的個人偏好給出建議。
只能根據提供的數據回答，不要編造資料。

使用者偏好：
- 天氣敏感度：{preferences.get('weatherSensitivity', '未設定')}
- 通勤方式：{preferences.get('commuteType', '未設定')}
- 今日行程：{preferences.get('dailyActivity', '未設定')}
- 回答風格：{preferences.get('responseStyle', 'balanced')}
"""


def chat(session_id: str, user_message: str, preferences: dict = None):
    messages = [
        SystemMessage(content=build_system_prompt(preferences)),
        HumanMessage(content=user_message),
    ]

    result = agent.invoke({"messages": messages})
    print(result)
    return result["messages"][-1].content