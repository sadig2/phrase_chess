
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from chess import bishop, knight, queen, rook

app = FastAPI()


class Item(BaseModel):
    n: int
    chess_pieces: str


handlers = {
    "queen": queen,
    "knight": knight,
    "bishop": bishop,
    "rook": rook
}


@app.post("/")
def post_item(item: Item):
    chess_piece = item.chess_pieces

    if chess_piece not in handlers:
        raise HTTPException(status_code=404, detail="Chess piece not found")

    function = handlers[chess_piece]

    solutionsCount = function(item.n)
    result = {}
    result["solution_count"] = solutionsCount
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
