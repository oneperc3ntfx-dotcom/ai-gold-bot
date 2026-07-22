from services.market import get_candles


# ==========================================
# EMA
# ==========================================

def ema(prices, period):

    if len(prices) < period:
        return None

    multiplier = 2 / (period + 1)

    ema_value = sum(prices[:period]) / period

    for price in prices[period:]:

        ema_value = (
            (price - ema_value)
            * multiplier
        ) + ema_value

    return ema_value


# ==========================================
# ATR
# ==========================================

def atr(candles, period=14):

    if len(candles) < period + 1:
        return 0

    trs = []

    for i in range(1, len(candles)):

        high = candles[i]["high"]
        low = candles[i]["low"]

        prev_close = candles[i - 1]["close"]

        tr = max(

            high - low,

            abs(high - prev_close),

            abs(low - prev_close)

        )

        trs.append(tr)

    return sum(trs[-period:]) / period


# ==========================================
# CANDLE STRENGTH
# ==========================================

def candle_strength(candle):

    body = abs(
        candle["close"] - candle["open"]
    )

    total = candle["high"] - candle["low"]

    if total == 0:
        return 0

    return body / total


# ==========================================
# TREND SCORE
# ==========================================

def trend_score(candles):

    closes = [

        c["close"]

        for c in candles

    ]

    ema20 = ema(
        closes,
        20
    )

    ema50 = ema(
        closes,
        50
    )

    ema200 = ema(
        closes,
        200
    )

    buy = 0
    sell = 0

    if ema20 and ema50:

        if ema20 > ema50:

            buy += 25

        else:

            sell += 25

    if ema50 and ema200:

        if ema50 > ema200:

            buy += 25

        else:

            sell += 25

    return {

        "buy": buy,

        "sell": sell,

        "ema20": ema20,

        "ema50": ema50,

        "ema200": ema200

    }


# ==========================================
# MOMENTUM SCORE
# ==========================================

def momentum_score(candles):

    buy = 0
    sell = 0

    recent = candles[-5:]

    bullish = 0
    bearish = 0

    for candle in recent:

        if candle["close"] > candle["open"]:

            bullish += 1

        else:

            bearish += 1

    if bullish > bearish:

        buy += 20

    elif bearish > bullish:

        sell += 20

    return {

        "buy": buy,

        "sell": sell,

        "bullish": bullish,

        "bearish": bearish

    }


# ==========================================
# CANDLE POWER
# ==========================================

def candle_score(candles):

    last = candles[-1]

    strength = candle_strength(
        last
    )

    buy = 0
    sell = 0

    if last["close"] > last["open"]:

        buy += int(
            strength * 20
        )

    else:

        sell += int(
            strength * 20
        )

    return {

        "buy": buy,

        "sell": sell,

        "strength": strength

    }

# ==========================================
# SWING HIGH / LOW
# ==========================================

def find_swing_points(candles, lookback=3):

    highs = []
    lows = []

    for i in range(
        lookback,
        len(candles) - lookback
    ):

        current = candles[i]

        high_zone = [
            c["high"]
            for c in candles[
                i-lookback:i+lookback+1
            ]
        ]

        low_zone = [
            c["low"]
            for c in candles[
                i-lookback:i+lookback+1
            ]
        ]


        if current["high"] == max(high_zone):

            highs.append(
                current["high"]
            )


        if current["low"] == min(low_zone):

            lows.append(
                current["low"]
            )


    return {

        "highs": highs,

        "lows": lows

    }



# ==========================================
# MARKET STRUCTURE
# ==========================================

def structure_score(candles):


    points = find_swing_points(
        candles
    )


    highs = points["highs"]

    lows = points["lows"]


    buy = 0
    sell = 0


    reason = []



    # Higher High

    if len(highs) >= 2:


        if highs[-1] > highs[-2]:

            buy += 15

            reason.append(
                "Higher High detected"
            )



        else:

            sell += 15

            reason.append(
                "Lower High detected"
            )



    # Higher Low

    if len(lows) >= 2:


        if lows[-1] > lows[-2]:

            buy += 15

            reason.append(
                "Higher Low detected"
            )



        else:

            sell += 15

            reason.append(
                "Lower Low detected"
            )



    return {

        "buy": buy,

        "sell": sell,

        "reason": reason

    }




# ==========================================
# BREAKOUT DETECTION
# ==========================================

def breakout_score(candles):


    recent = candles[-1]


    previous = candles[-10:-1]


    highest = max(

        c["high"]

        for c in previous

    )


    lowest = min(

        c["low"]

        for c in previous

    )


    buy = 0
    sell = 0

    reason = []



    if recent["close"] > highest:


        buy += 20

        reason.append(
            "Bullish breakout"
        )



    elif recent["close"] < lowest:


        sell += 20

        reason.append(
            "Bearish breakout"
        )


    return {

        "buy": buy,

        "sell": sell,

        "reason": reason

    }




# ==========================================
# PULLBACK DETECTION
# ==========================================

def pullback_score(candles):


    closes = [

        c["close"]

        for c in candles

    ]


    ema20 = ema(

        closes,

        20

    )


    last = candles[-1]


    buy = 0
    sell = 0

    reason = []



    if ema20 is None:

        return {

            "buy":0,

            "sell":0,

            "reason":[]

        }



    # Harga turun mendekati EMA
    # setelah trend naik


    if (

        last["low"] <= ema20

        and

        last["close"] > ema20

    ):


        buy += 10

        reason.append(
            "Bullish EMA pullback"
        )



    if (

        last["high"] >= ema20

        and

        last["close"] < ema20

    ):


        sell += 10

        reason.append(
            "Bearish EMA pullback"
        )



    return {

        "buy": buy,

        "sell": sell,

        "reason": reason

    }




# ==========================================
# VOLATILITY CHECK
# ==========================================

def volatility_score(candles):


    current_atr = atr(
        candles
    )


    last = candles[-1]


    candle_range = (

        last["high"]

        -

        last["low"]

    )


    buy = 0
    sell = 0


    reason = []



    if current_atr == 0:

        return {

            "buy":0,

            "sell":0,

            "reason":[]

        }



    if candle_range > current_atr:


        reason.append(
            "Strong volatility"
        )


        if last["close"] > last["open"]:

            buy += 10

        else:

            sell += 10



    return {

        "buy": buy,

        "sell": sell,

        "reason": reason

    }

# ==========================================
# FINAL MARKET ANALYSIS
# ==========================================

def analyze_market():


    candles = get_candles(

        interval="15min",

        outputsize=250

    )


    if len(candles) < 100:


        return {

            "bias": "BUY",

            "confidence": 50,

            "reason": [

                "Data market terbatas"

            ]

        }



    total_buy = 0
    total_sell = 0


    reasons_buy = []
    reasons_sell = []



    # ==========================
    # TREND
    # ==========================

    trend = trend_score(
        candles
    )


    total_buy += trend["buy"]

    total_sell += trend["sell"]



    if trend["buy"]:

        reasons_buy.append(
            "EMA trend bullish"
        )


    if trend["sell"]:

        reasons_sell.append(
            "EMA trend bearish"
        )




    # ==========================
    # MOMENTUM
    # ==========================

    momentum = momentum_score(
        candles
    )


    total_buy += momentum["buy"]

    total_sell += momentum["sell"]



    if momentum["buy"]:

        reasons_buy.append(
            "Bullish momentum"
        )


    if momentum["sell"]:

        reasons_sell.append(
            "Bearish momentum"
        )





    # ==========================
    # CANDLE
    # ==========================

    candle = candle_score(
        candles
    )


    total_buy += candle["buy"]

    total_sell += candle["sell"]



    if candle["buy"]:

        reasons_buy.append(
            "Bullish candle strength"
        )


    if candle["sell"]:

        reasons_sell.append(
            "Bearish candle strength"
        )





    # ==========================
    # STRUCTURE
    # ==========================

    structure = structure_score(
        candles
    )


    total_buy += structure["buy"]

    total_sell += structure["sell"]


    reasons_buy.extend(

        structure["reason"]

    )





    # ==========================
    # BREAKOUT
    # ==========================

    breakout = breakout_score(
        candles
    )


    total_buy += breakout["buy"]

    total_sell += breakout["sell"]


    reasons_buy.extend(

        breakout["reason"]

    )





    # ==========================
    # PULLBACK
    # ==========================

    pullback = pullback_score(
        candles
    )


    total_buy += pullback["buy"]

    total_sell += pullback["sell"]


    reasons_buy.extend(

        pullback["reason"]

    )





    # ==========================
    # VOLATILITY
    # ==========================

    volatility = volatility_score(
        candles
    )


    total_buy += volatility["buy"]

    total_sell += volatility["sell"]





    # ==========================
    # FINAL SCORE
    # ==========================

    total = (

        total_buy

        +

        total_sell

    )


    if total == 0:

        total = 1




    buy_percent = round(

        (

            total_buy

            /

            total

        )

        *

        100

    )



    sell_percent = round(

        (

            total_sell

            /

            total

        )

        *

        100

    )





    # ==========================
    # CHOOSE WINNER
    # ==========================


    if buy_percent >= sell_percent:


        bias = "BUY"

        confidence = buy_percent


        reasons = reasons_buy



    else:


        bias = "SELL"

        confidence = sell_percent


        reasons = reasons_sell





    # fallback alasan

    if not reasons:


        reasons = [

            "Market probability calculation"

        ]





    return {


        "bias": bias,


        "confidence": confidence,


        "buy_score": total_buy,


        "sell_score": total_sell,


        "reason": reasons[:5]

    }
