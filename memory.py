import uuid
from typing import List, Tuple, Dict, Optional

class DialogManager:
    def __init__(self):
        self._sessions: Dict[str, List[Tuple[str, str]]] = {}  # role: "human"/"ai"

    def create_session(self, session_id: str = None) -> str:
        """Создаёт новую сессию. Если session_id передан, использует его, иначе генерирует UUID."""
        if session_id is None:
            session_id = str(uuid.uuid4())[:8]
        if session_id not in self._sessions:
            self._sessions[session_id] = []
        return session_id

    def get_history(self, session_id: str) -> List[Tuple[str, str]]:
        """Возвращает историю сообщений (список кортежей (role, content))."""
        return self._sessions.get(session_id, [])

    def add_message(self, session_id: str, role: str, content: str):
        """Добавляет сообщение в историю сессии."""
        if session_id in self._sessions:
            self._sessions[session_id].append((role, content))

    def delete_session(self, session_id: str) -> bool:
        """Удаляет сессию. Возвращает True, если сессия существовала."""
        return self._sessions.pop(session_id, None) is not None

    def session_exists(self, session_id: str) -> bool:
        return session_id in self._sessions

    def list_sessions(self) -> List[str]:
        return list(self._sessions.keys())