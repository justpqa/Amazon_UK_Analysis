CREATE VIEW amazon_uk_2023_professional_med AS (
    SELECT * FROM amazon_uk_2023 
    WHERE "categoryName" = 'Professional Medical Supplies'
);