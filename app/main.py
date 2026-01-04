from fastapi import FastAPI, HTTPException
from app.schemas import SolveRequest, SolveResponse
from app.solver import solve_cube

app = FastAPI(title="Rubik's Cube Solver API")

@app.post("/solve", response_model=SolveResponse)
def solve(request: SolveRequest):
    print("Hi I received the request")
    try:
        solution = solve_cube(request.cube)
        return {
            "solution": solution,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
