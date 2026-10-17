module Lab2Ex exposing (..)
import List exposing (length)

x = 23
pi = 3.14

type alias Person = {firstName:String, lastName:String}

mario = {firstName = "Mario", lastName = "Gearba"}
tudor = Person "CEva" "ceva"
-- fullName (Person "Marius" "Merdenea")

fullName person = person.firstName ++ " " ++ person.lastName

-- type Color = Red | Blue | Green
-- type Point = Point int int
-- type Person = Person String String int
-- fullname(Person fst . . ) = "Hello" ++ fst


type alias Address = {street:String, number: String,city: String, country: String}

formatAddress address = address.street ++ " " ++ address.number ++ " " ++ address.city ++ " " ++ address.country

-- > formatAddress {street = "ceva", number = "1", city = "deva", country = "Ro"}
-- "ceva 1 deva Ro" : String



type Point = Point Int Int

addPoint (Point y z) = Point(y + 1) (z + 1)

type Shape = Circle Float | Rectangle Float Float | Triangle Float Float Float
type ShapeRec 

    = CircleRec { radius : Float }
    | RectangleRec { width : Float, height : Float}
    | TriangleRec { sideA : Float, sideB : Float, sideC : Float}

howBigLetIn n =
    let 
        smallNumber = 10
        bigNumber = 100
    in
        if n < smallNumber then 
            "Small"
        else if n < bigNumber then
            "Medium"
        else 
            "Big"

heronShort a b c = 
    let
         s = (a + b + c) / 2
    in
        sqrt ( s * ( s - a ) * ( s- b ) * ( s - c ) )

double n = n * 2


type Person2  = Person2 String String Int
getFirstName (Person2 firstName2 _ _ ) = 
    firstName2
getSecondName ( Person2 _ lastName2 _ ) = 
    lastName2

area shape = 
    case shape of
        Circle radius -> radius * radius * pi
        Rectangle width lenght -> width * lenght
        Triangle a b c -> heronShort a b c

numberToMedal n = 
    case n of
        1 -> "Gold"
        2 -> "Silver"
        3 -> "Bronze"
        _ -> "data viitoare"

gabriel = Person2 "Gabriel" "gabi" 20

-- exercitiile 2.8

-- 2.8.1

type Dice
    = One 
    |Two
    |Three
    |Four
    |Five
    |Six

type alias DicePairAlias = {dice1: Dice, dice2 : Dice}

type DicePair = DicePair Dice Dice

luckyRoll dices = 
    if dices.dice1 == Six && dices.dice2 == Six then   
        "Very lucky"
    else if dices.dice1 == Six || dices.dice2 == Six then
        "Lucky"
    else
        "Meh"

luckyRollType (DicePair dice1 dice2) = 
    if dice1 == Six && dice2 == Six then
        "Very Lucky"
    else if dice1 == Six || dice2 == Six then
        "Lucky"
    else
        "Meh"


areaRec shape = 
    case shape of
        CircleRec { radius } -> pi * radius * radius
        RectangleRec {height, width } -> width * height 
        TriangleRec {sideA, sideB, sideC} -> heronShort sideA sideB sideC   
    

type alias Point2 = {x : Float,y : Float}
type Shapde2D 
    = Circle2D { center : Point2, radius : Float}
    |Rectangle2D { topLeftCorner : Point2, bottomRightCorner : Point2}
    |Triangle2D { pointA : Point2, pointB : Point2, pointC : Point2}

pointInShape point shape = 
    case shape of
        Circle2D { center, radius } ->
            let
                dx = point.x - center.x
                dy = point.y - center.y
            in
                sqrt(dx * dx - dy * dy) < radius
        Rectangle2D { topLeftCorner, bottomRightCorner } -> 
            point.x > topLeftCorner.x &&
            point.x < bottomRightCorner.x &&
            point.y < topLeftCorner.y &&
            point.y > bottomRightCorner.y
        Triangle2D { pointA, pointB, pointC } ->
              let
                distance p1 p2 =
                    sqrt ((p1.x - p2.x)^2 + (p1.y - p2.y)^2)

                triangleArea a b c =
                    heronShort (distance a b) (distance b c) (distance c a)

                areaABC = triangleArea pointA pointB pointC

                areaPAB = triangleArea point pointA pointB
                areaPAC = triangleArea point pointA pointC
                areaPBC = triangleArea point pointB pointC

                epsilon = 0.00001
            in
                abs (areaABC - (areaPAB + areaPAC + areaPBC)) < epsilon