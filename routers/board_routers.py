from fastapi import APIRouter
from schemas.board_schemas import BoardItemSchema

router = APIRouter(prefix='/board')

@router.post('/create_board', status_code=200)
def create_board_item(data:BoardItemSchema):
    board_item_id = data.board_item_id
    board_item_title = data.board_item_title
    board_item_contents = data.board_item_contents
    board_item_creater = data.board_item_creater

    res = {
            'board_item_id' : board_item_id,
            'board_item_title' : board_item_title,
            'board_item_contents' : board_item_contents,
            'board_item_creater' : board_item_creater
        }

    return res

