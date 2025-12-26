from pydantic import BaseModel

class SolveRequest(BaseModel):
    cube: list[list[list[int]]]
    # cube: str              # e.g. "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
    # method: str = "cfop"   # optional solver choice

class SolveResponse(BaseModel):
    solution: str
    # solution: list[str]    # ["R", "U", "R'", "U'"]
    # move_count: int