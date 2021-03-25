main = do  
    foo <- putStrLn "BALLS? "  
    name <- getLine  
    putStrLn ("BALLS" ++ name ++ "BALLS")  
