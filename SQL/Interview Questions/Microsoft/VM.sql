-- Given the table VM, return the best performing VMs per region
-- Access the table VM with the syntax -> FROM VM

-- Solution 1
SELECT
    region,
    vm,
    MAX(kpi) AS max_kpi
FROM
    VM
GROUP BY
    region;

-- Solution 2
SELECT 
    region, 
    vm, 
    kpi
FROM 
    VM v1
WHERE 
    kpi = (
        SELECT 
            MAX(kpi) 
        FROM 
            VM v2 
        WHERE 
            v2.region = v1.region
    );

-- Solution 3
SELECT 
    region, 
    vm, 
    kpi
FROM (
    SELECT 
        region, 
        vm, 
        kpi,
        ROW_NUMBER() OVER (PARTITION BY region ORDER BY kpi DESC) AS rank
    FROM 
        VM
) ranked
WHERE 
    rank = 1;

-- Solution 4
SELECT 
    region, 
    vm, 
    kpi
FROM (
    SELECT 
        region, 
        vm, 
        kpi,
        RANK() OVER (PARTITION BY region ORDER BY kpi DESC) AS rank
    FROM 
        VM
) ranked
WHERE 
    rank = 1;

-- Solution 5
SELECT 
    region, 
    vm, 
    kpi
FROM 
    VM v1
WHERE 
    NOT EXISTS (
        SELECT 
            1 
        FROM 
            VM v2 
        WHERE 
            v2.region = v1.region 
            AND v2.kpi > v1.kpi
    );

-- Solution 6
SELECT 
    v1.region, 
    v1.vm, 
    v1.kpi
FROM 
    VM v1
LEFT JOIN 
    VM v2 ON v1.region = v2.region AND v2.kpi > v1.kpi
WHERE 
    v2.vm IS NULL;

-- Solution 7
SELECT 
    region, 
    vm, 
    kpi
FROM 
    VM v1
WHERE 
    kpi >= ALL (
        SELECT 
            kpi 
        FROM 
            VM v2 
        WHERE 
            v2.region = v1.region
    );