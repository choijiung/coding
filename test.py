import numpy as np
import random

# 미로 설정 (5x5 크기)
maze = [
    [0, 0, 0, 0, 0],  # 0: 빈 공간, 1: 벽
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# 상태 공간 크기
n_states = 5 * 5

# Q-테이블 초기화
Q = np.zeros((n_states, 4))  # 4는 상, 하, 좌, 우

# 학습 파라미터
alpha = 0.1  # 학습률
gamma = 0.9  # 할인율
epsilon = 0.1  # 탐색 비율

# 행동을 선택하는 함수 (ε-greedy 정책)
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice([0, 1, 2, 3])  # 랜덤한 행동 선택
    else:
        return np.argmax(Q[state])  # Q값이 가장 큰 행동 선택

# 상태를 (x, y)로 변환하는 함수
def state_to_index(x, y):
    return x * 5 + y

# Q-learning 수행
for episode in range(1000):
    state = state_to_index(0, 0)  # 시작 위치 (0, 0)
    done = False
    
    while not done:
        action = choose_action(state)
        
        # 다음 상태 계산 (상, 하, 좌, 우)
        x, y = divmod(state, 5)
        
        if action == 0:  # 위
            next_state = state_to_index(max(x - 1, 0), y)
        elif action == 1:  # 아래
            next_state = state_to_index(min(x + 1, 4), y)
        elif action == 2:  # 왼쪽
            next_state = state_to_index(x, max(y - 1, 0))
        else:  # 오른쪽
            next_state = state_to_index(x, min(y + 1, 4))
        
        # 보상 계산
        if (x, y) == (4, 4):  # 목표 지점에 도달
            reward = 1
            done = True
        elif maze[x][y] == 1:  # 벽에 부딪힘
            reward = -1
            done = True
        else:  # 계속 진행
            reward = 0
        
        # Q값 업데이트
        Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        
        state = next_state  # 상태 업데이트

# 학습된 Q 테이블 출력
print(Q)
