module Top.State exposing (..)

import Top.Types exposing (..)
import Json.Decode as Decode
import Http


init : ( Model, Cmd Msg )
init =
    ( Model [ Room "No Rooms Loaded, Connect to internet scrub" ], getRooms )


update : Model -> Msg -> ( Model, Cmd Msg )
update model msg =
    case msg of
        GetRooms ->
            ( model, getRooms )

        GotRooms (Ok rooms) ->
            ( { model | rooms = rooms }, Cmd.none )

        GotRooms (Err _) ->
            ( model, Cmd.none )


getRooms : Cmd Msg
getRooms =
    -- TODO: Figure out how to route this
    Http.send GotRooms (Http.get "/rooms" decodeRooms)


decodeRooms : Decode.Decoder (List Room)
decodeRooms =
    Decode.list <|
        Decode.map
            (\single ->
                case List.head single of
                    Just str ->
                        Room str

                    Nothing ->
                        Room ""
            )
        <|
            Decode.list Decode.string
