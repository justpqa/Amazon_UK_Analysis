CREATE VIEW amazon_uk_2023_health_personal_care AS (
    SELECT * FROM amazon_uk_2023 
    WHERE "categoryName" = 'Health & Personal Care'
);