module View exposing (root)

import Types exposing (..)
import Html exposing (..)
import Html.Attributes exposing (class)


-- Subpages

import Top.View as Top


root : Model -> Html Msg
root model =
    case model.route of
        Top ->
            Top.root model.top

        NotFoundRoute ->
            div
                [ class "hero"
                ]
                [ p [] [ text "No such route" ]
                ]
