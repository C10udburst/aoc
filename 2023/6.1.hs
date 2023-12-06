-- Time:      7  15   30
-- Distance:  9  40  200

calcDists (held, time) = map (\h -> (time - h) * h) held
findWins (mine, record) = filter (\x -> x > record) mine

main = do
    fileLines <- fmap lines $ readFile "6.in"
    let times = map read $ drop 1 $ words $ head fileLines :: [Int]
    let records = map read $ drop 1 $ words $ last fileLines :: [Int]
    let possibleHeldTimes = map (\x -> [0..x]) times
    let myDistances = map calcDists $ zip possibleHeldTimes times
    let myWins = map findWins $ zip myDistances records
    let result = foldl (*) 1 $ map length myWins
    print $ show result