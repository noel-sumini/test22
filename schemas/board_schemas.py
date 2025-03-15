from pydantic import BaseModel

class BoardItemSchema(BaseModel):
    board_item_id:str
    board_item_title:str
    board_item_contents:str
    board_item_creater:str
    
