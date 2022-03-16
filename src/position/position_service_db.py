from .position_model import Position
from typing import List


def create(title: str) -> Position:
    position: Position = Position(title=title)
    position.save_db()
    return position


def update(position_id: int, title: str) -> Position:
    position: Position = Position.query.filter_by(id=position_id).first()
    position.title = title
    position.update_db()
    return position


def delete(position_id: int) -> Position:
    position: Position = Position.query.filter_by(id=position_id).first()
    position.delete_db()
    return position


def get_by_title(title: str) -> Position:
    position: Position = Position.query.filter_by(title=title).first()
    return position


def get_by_id(position_id: int) -> Position:
    position: Position = Position.query.filter_by(id=position_id).first()
    return position


def get_all_ids() -> List[int]:
    positions: List[Position] = Position.query.all()
    position_ids: List[int] = []
    for position in positions:
        position_ids.append(position.id)
    return position_ids
