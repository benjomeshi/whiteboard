module Types exposing (..)

import Navigation exposing (Location)


-- Subpages

import Top.Types as Top


type alias Model =
    { route : Routes
    , top : Top.Model
    }


type Msg
    = None
    | TopMsg Top.Msg
    | OnLocationChange Location


type Routes
    = Top
    | NotFoundRoute
