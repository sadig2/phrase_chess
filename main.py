import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from chess import bishop, knight, queen

app = FastAPI()

class Item(BaseModel):
    n: int
    chess_pieces : str
 

functions_dict = {
    "queen":queen,
    "knight":knight,
    "bishop":bishop,
    "knight":knight
}


@app.post("/")
def post_item(item: Item):
    chess_piece = item.chess_pieces
    function = functions_dict[chess_piece]
    solutionsCount = function(item.n)
    result = {}
    result["solution_count"]=solutionsCount
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)