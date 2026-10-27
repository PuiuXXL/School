module Lab4Ex exposing(..)


--pb1
enumerate : List a -> List (Int, a)
enumerate list =
   let
        helper index lista = 
            case lista of
                [] -> []
                x :: xs ->
                    (index, x) :: helper (index + 1) xs

    in
        helper 0 list

type Day = Mon | Tue | Wed | Thu | Fri | Sat | Sun

--pb2

repeat : Int -> a -> List a
repeat n elem = 
    if n <= 0 then
        []
    else   
        elem :: repeat (n - 1) elem

--pb3

isVowel: Char -> Bool
isVowel char = 
    if char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' then
        True
    else 
        False

countVowels : String -> Int
countVowels s = 
    let
        countHelper l = 
            case l of
                [] -> 0
                x :: xs ->
                    if isVowel x then
                        1 + countHelper xs
                    else  
                        countHelper xs
    in
        countHelper (String.toList s)
        -- ['a','b','c']

partition : List a -> (List a, List a)
