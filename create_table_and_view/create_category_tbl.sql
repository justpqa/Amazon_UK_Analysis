CREATE TABLE amazon_uk_2023_cat AS (
    SELECT "categoryName",
    COUNT(*) AS "num_product",
    AVG(Stars) AS Stars,
    AVG(Price) AS "avg_price",
    STDDEV(Price) AS "std_price",
    AVG(CAST("isBestSeller" AS INT)) AS "prop_best_seller",
    SUM("boughtInLastMonth") AS "count_bought_last_month"
    FROM amazon_uk_2023
    GROUP BY "categoryName"
    ORDER BY "categoryName"
);