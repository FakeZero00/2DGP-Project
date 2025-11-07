from pico2d import get_time
from typing import List, Tuple, Optional

#커맨드 버퍼 클래스, 인스턴스 생성
class CommandBuffer:
    def __init__(self, BoundTime: float = 1.0):
        self.BoundTime = BoundTime
        self.buffer: List[Tuple[str, float]] = []

    def add(self, token: str, t: Optional[float] = None):
        if t is None:
            t = get_time()
        self.buffer.append((token, t))
        self.pop_old(t)

    def pop_old(self, now: float):
        cutoff = now - self.BoundTime
        self.buffer = [(tok, ts) for tok, ts in self.buffer if ts >= cutoff]

    def tokens(self) -> List[str]:
        return [tok for tok, _ in self.buffer]

    def last_token(self):
        return self.buffer[-1][0] if self.buffer else None

    def clear_last_n(self, n):
        for _ in range(min(n, len(self.buffer))):
            self.buffer.pop()

#  커맨드 인식기 클래스
class CommandRecognizer:
    def __init__(self, patterns):
        # 미리 입력해둔 패턴들을 긴 패턴을 먼저 감지하기 위해 길이의 내림차순으로 정렬
        self.patterns = sorted(patterns, key = lambda p: -len(p[0]))

    def match(self, buffer):
        tokens = buffer.tokens()
        if not tokens:
            return None
        for pattern, action in self.patterns:
            pattern_len = len(pattern)
            if pattern_len <= len(tokens) and tuple(tokens[-pattern_len:]) == pattern:
                return action, pattern_len
        return None
