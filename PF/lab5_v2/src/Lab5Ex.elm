module Lab5Ex exposing(..)

all : (a -> Bool) -> List a -> Bool
all condition lista = 
    lista
        |> List.map condition
        |> List.foldl (&&) True

any : (a -> Bool) -> List a -> Bool
any condition lista =
    lista 
        |> List.map condition
        |> List.foldl (||) False


-- pb5.4.1
type alias Point = {x : Int, y : Int, z : Int}
type Color = Red | Green | Blue
type alias ColoredSphere = { center : Point, color : Color, radius : Int}

moveUpdate : ColoredSphere -> Int -> Int -> ColoredSphere
moveUpdate sphere dx dy = 
    {sphere | center = {x = sphere.center.x + dx, y = sphere.center.y + dy, z = sphere.center.z}}