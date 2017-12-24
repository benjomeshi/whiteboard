module App exposing (..)

import Navigation
import State
import View
import Types exposing (..)
import Top.Types


main : Program Never Model Msg
main =
    Navigation.program OnLocationChange
        { init = State.init
        , update = State.update
        , view = View.root
        , subscriptions = (always Sub.none)
        }
