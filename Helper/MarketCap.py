# Large-cap: Market value of $10 billion or more; generally mature, well-known companies within established industries.

# Midcap: Market value between $3 billion and $10 billion; typically established companies within industries
# experiencing or expected to experience rapid growth.

# Small-cap: Market value of $3 billion or less; tend to be young companies that serve niche markets or emerging
# industries.


def get_risk_from_market_cap(market_cap):
    if market_cap > 10000000000:
        return "low"
    if market_cap > 3000000000:
        return "middle"
    return "high"
