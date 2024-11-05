WITH monthly_data AS (
    SELECT 
        d.year,
        d.month_name,
        d.month AS month_number,
        c.country,
        MAX(f.email_opens_cnt) AS max_emails_opened,
        SUM(f.email_opens_cnt) OVER (
            PARTITION BY c.country
            ORDER BY d.year, d.month
        ) AS running_total_emails,
        COUNT(DISTINCT f.customer_id) AS num_customers_sent
    FROM 
        emails_sent_fact f
    JOIN 
        date_dimension d ON f.date_id = d.id
    JOIN 
        customer_dimension c ON f.customer_id = c.id
    GROUP BY 
        d.year, d.month_name, d.month, c.country
)
SELECT * FROM monthly_data;