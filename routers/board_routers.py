from fastapi import APIRouter
from schemas.board_schemas import BoardItemSchema
from utils.db.postgres import get_db_connection
from uuid import uuid4

router = APIRouter(prefix="/board")




@router.get("/board_items/{item_id}")
def get_board_item(item_id:str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT * FROM board_items WHERE board_item_id = %s
        """,
        (item_id,)
    )
    
    item = cursor.fetchone()
    
    cursor.close()
    conn.close()

    return item


@router.post("/create_board", status_code=200)
def create_board_item(data:BoardItemSchema):
    board_item_id = str(uuid4())
    board_item_title = data.board_item_title
    board_item_contents = data.board_item_contents
    board_item_creater = data.board_item_creater
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO board_items (board_item_id, board_item_title, board_item_contents, board_item_creater)
            VALUES (%s, %s, %s, %s)
        """,
        (board_item_id, board_item_title, board_item_contents, board_item_creater)
    )

    conn.commit()


    res = {
            "board_item_id": board_item_id,
            "board_item_title" : board_item_title,
            "board_item_contents" : board_item_contents, 
            "board_item_creater" : board_item_creater
        }
    cursor.close()
    conn.close()
    return res

@router.put("/board_items/{item_id}", status_code=200)
def update_board_item(item_id:str, data:BoardItemSchema):
    conn = get_db_connection()
    cursor = conn.cursor()

    board_item_id = item_id
    board_item_title = data.board_item_title
    board_item_contents = data.board_item_contents
    board_item_creater = data.board_item_creater

    cursor.execute(
        """
            UPDATE board_items SET
                board_item_title=%s ,
                board_item_contents=%s , 
                board_item_creater=%s
            WHERE board_item_id=%s
            RETURNING *
        """,
        (board_item_title, board_item_contents, board_item_creater, board_item_id)
    )
    updated_item = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    return updated_item