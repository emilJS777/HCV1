from .PositionModel import Position
from typing import List
from src.__general.helpers.paginate import get_page_items


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


def get_all(page: int, per_page: int) -> dict:
    # positions: List[Position] = Position.query.all()
    # position_ids: List[int] = []
    # for position in positions:
    #     position_ids.append(position.id)
    # return position_ids
    return get_page_items(
        Position.query
                .order_by(-Position.id)
                .paginate(page=page, per_page=per_page)
    )
