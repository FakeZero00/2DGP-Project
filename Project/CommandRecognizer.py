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
