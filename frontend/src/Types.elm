module Types exposing (..)

import Navigation exposing (Location)


type alias Model =
    { route : Routes
    }


type Msg
    = None
    | OnLocationChange Location


type Routes
    = NotFoundRoute
