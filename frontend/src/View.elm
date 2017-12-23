module View exposing (root)

import Types exposing (..)
import Html exposing (..)
import Html.Attributes exposing (class)


root : Model -> Html Msg
root model =
    case model.route of
        NotFoundRoute ->
            div
                [ class "hero"
                ]
                [ p [] [ text "No such route" ]
                ]
