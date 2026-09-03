# Write your MySQL query statement below
SELECT *,
    dna_sequence LIKE 'ATG%' AS has_start,
    (dna_sequence LIKE '%TAA' OR dna_sequence LIKE '%TAG' OR dna_sequence LIKE '%TGA') AS has_stop,
    dna_sequence LIKE '%ATAT%' AS has_atat,
    (dna_sequence LIKE '%GGG%' OR dna_sequence LIKE '%GGGG%') AS has_ggg
FROM Samples
ORDER BY sample_id ASC;