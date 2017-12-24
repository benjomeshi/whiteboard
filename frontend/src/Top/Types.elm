module Top.Types exposing (..)

import Http


type Msg
    = GetRooms
    | GotRooms (Result Http.Error (List Room))


type alias Model =
    { rooms : List Room
    }


type alias Room =
    { name : String
    }
