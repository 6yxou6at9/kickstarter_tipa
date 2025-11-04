from fastapi import APIRouter
from database.transferservice import add_sum_on_campaign_db, get_all_campaign_transfer_db, get_exact_transfer_db, get_all_user_transfer_db
from api.transfer_api.schemas import TransferSchema, TransferRead

transfer_router = APIRouter(prefix='/transfer', tags=["Transfer API"])

def response_result(result):
    if result:
        return {"status": 1, 'message': result}
    return {'status': 0, 'message': result}

@transfer_router.post('/add_sum_on_campaign', response_model=TransferRead)
async def add_sum_on_campaign(transfer: TransferSchema):
    result = add_sum_on_campaign_db(transfer)
    return response_result(result)

@transfer_router.get('/get_all_campaign_transfer')
async def get_all_campaign_transfer(cid):
    result = get_all_campaign_transfer_db(cid=cid)
    return response_result(result)

@transfer_router.get('/get_all_user_transfer')
async def get_all_user_transfer(uid):
    result = get_all_user_transfer_db(uid=uid)
    return response_result(result)

@transfer_router.get('/get_exact_transfer')
async def get_exact_transfer(tid):
    result = get_exact_transfer_db(tid=tid)
    return response_result(result)