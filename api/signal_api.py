from fastapi import APIRouter


router = APIRouter()



@router.post("/signal")
async def receive_signal(data: dict):

    print("SIGNAL DARI BOT 1:")
    print(data)


    return {
        "status": "OK"
    }
