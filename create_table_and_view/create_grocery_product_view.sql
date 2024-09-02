CREATE VIEW amazon_uk_2023_grocery AS (
    SELECT * FROM amazon_uk_2023 
    WHERE "categoryName" = 'Grocery'
);