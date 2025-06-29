import json
from pathlib import Path

ORDER_FILE = Path("orders.json")

def save_order_to_json(user_id: int, product_id: int, quantity: int):
    data = {}

    if ORDER_FILE.exists():
        with open(ORDER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    user_str = str(user_id)
    if user_str not in data:
        data[user_str] = {}

    if str(product_id) in data[user_str]:
        data[user_str][str(product_id)] += quantity
    else:
        data[user_str][str(product_id)] = quantity

    with open(ORDER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_orders_from_json(user_id: int):
    if not ORDER_FILE.exists():
        return {}

    with open(ORDER_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get(str(user_id), {})
