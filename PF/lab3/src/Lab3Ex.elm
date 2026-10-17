module Lab3Ex exposing (..)

-- sum l = 
--     case l of  
--         [] -> 0
--         x :: xs -> x + sum xs
-- functie de liste de parcurgere
-- 2 :: [] asa dam append
-- type Maybe a = Just a | Nothing
-- type Result error value = OK value | Err error
-- compare a b -> Order (Lt,GT,EQ)

safeDiv : Int -> Int -> Maybe Int
safeDiv a b = 
    if b == 0 then
        Nothing
    else
        Just (a // b)

lenNormal l =
    case l of   
        [] -> 0
        _ :: xs -> 1 + lenNormal xs

lenTail : List a -> Int

lenTail l =
    let
        helper list acc =
            case list of
                [] -> acc
                x :: xs -> helper xs (acc + 1)
    in
        helper l 0


last : List a -> Maybe a
last l = 
    case l of
        [] -> Nothing
        [x] -> Just x
        x :: xs -> last xs

-- safeArea : Shape -> Result String Float
-- indexList : Int List -> Result String Int
-- indexList i l = 
--     case l of
        