module State exposing (init, update)

import Types exposing (..)
import Routing exposing (parseLocation)
import Navigation exposing (Location)


init : Location -> ( Model, Cmd msg )
init location =
    let
        route =
            parseLocation location
    in
        ( Model route
        , Cmd.none
        )


update : Msg -> Model -> ( Model, Cmd msg )
update msg model =
    case msg of
        OnLocationChange location ->
            let
                newRoute =
                    parseLocation location
            in
                ( { model | route = newRoute }, Cmd.none )

        None ->
            ( model, Cmd.none )
