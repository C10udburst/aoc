import Data.Text (splitOn, pack, unpack)

main = do
    fileLines <- fmap lines $ readFile "6.in"
    let time = read $ unpack . last $ splitOn (pack ":") $ pack $ concat . words $ head fileLines :: Integer
    let record = read $ unpack . last $ splitOn (pack ":") $ pack $ concat . words $ last fileLines :: Integer
    let myDistances = map (\x -> (time - x) * x) [0..time]
    let myWins = filter (\x -> x > record) myDistances
    print $ show $ length myWins