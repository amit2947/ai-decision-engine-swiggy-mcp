from mock_data import data

def get_weights(priority):
    if priority == "cheap":
        return {"price": 0.5, "rating": 0.2, "delivery": 0.2, "cuisine": 0.1}
    elif priority == "fast":
        return {"price": 0.2, "rating": 0.2, "delivery": 0.5, "cuisine": 0.1}
    else:
        return {"price": 0.2, "rating": 0.5, "delivery": 0.2, "cuisine": 0.1}

def score(item, weights, budget, cuisine):
    price_score = max(0, (budget - item["price"]) / budget)
    rating_score = item["rating"] / 5
    delivery_score = 1 - (item["delivery"] / 60)
    cuisine_score = 1 if item["cuisine"] == cuisine else 0.5

    return (
        weights["price"] * price_score +
        weights["rating"] * rating_score +
        weights["delivery"] * delivery_score +
        weights["cuisine"] * cuisine_score
    )

def recommend(budget, priority, cuisine):
    weights = get_weights(priority)
    scored = [(score(i, weights, budget, cuisine), i) for i in data]
    scored.sort(reverse=True)
    return [x[1] for x in scored[:3]]