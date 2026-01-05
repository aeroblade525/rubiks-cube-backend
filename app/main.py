from fastapi import FastAPI, HTTPException
from app.schemas import SolveRequest, SolveResponse
from app.solver import solve_cube
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Rubik's Cube Solver API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/solve", response_model=SolveResponse)
def solve(request: SolveRequest):
    print("Hi I received the request")
    try:
        solution = solve_cube(request.cube)
        print(solution)
        return {
            "solution": solution,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
