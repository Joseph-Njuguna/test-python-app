# main.py
import time
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Balance Checker API",
    description="A simple API to simulate checking a bank balance with a fixed 2-second processing time."
)

@app.get("/check_balance/{account_id}", summary="Check Account Balance")
def check_balance(account_id: int):
    """
    Simulates checking a bank balance.

    This endpoint artificially delays its response by 2 seconds
    to represent backend processing time and latency.
    """
    # In a real application, you would connect to a database here.
    # We use time.sleep to simulate that processing time.
    start_time = time.time()
    time.sleep(2)
    end_time = time.time()

    if account_id == 12345:
        # Placeholder for actual data retrieval
        balance_data = {
            "account_id": account_id,
            "balance": 1500.75,
            "currency": "USD",
            "processing_time_seconds": round(end_time - start_time, 2)
        }
        return balance_data
    else:
        # Simulate accounts not found or invalid
        raise HTTPException(status_code=404, detail="Account not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
