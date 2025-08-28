result1 = pd.read_sql("""SELECT AVG(Win_Margin), Match_Winner
                        FROM Match
                        WHERE Season_Id==9
                        GROUP BY Match_Winner
                        ORDER BY AVG (Win_Margin);""", conn)

result1

result2 = pd.read_sql("""SELECT COUNT(DISTINCT Venue_Id)
FROM MATCH
WHERE Season_Id == 9; """, conn)

result2

throughout all the seasons 
result3 = pd.read_sql(""" SELECT MIN (Win_Margin), Max())