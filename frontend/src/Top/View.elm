module Top.View exposing (..)

import Top.Types exposing (..)
import Html exposing (..)
import Html.Attributes exposing (..)


root : Model -> Html msg
root model =
    div [] <| List.map (\room -> div [] [ p [] [ text room.name ] ]) model.rooms
