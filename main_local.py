import json
import os
import random

from fastapi import FastAPI, HTTPException
import time
from random import uniform
import rtmidi

from request_to_cmdaw_request_api.mode_1 import get_mode_1_request
from tech import make_request_to_request_cmdaw_request, \
    convert_song_sequence_response_to_delays_in_seconds_and_rtmidi_messages

app = FastAPI()

command = None

MIDI_PORT = int(os.getenv('MIDI_PORT'))


def play_midi():
    # open midi port
    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()
    print(f'available midi ports: {available_ports}')
    try:
        midiout.open_port(MIDI_PORT)  # ! CHANGE PORT IF NEEDED !
        print(f'CONNECTED to {available_ports[MIDI_PORT]}')
    except:
        print('NO MIDI PORTS, PLEASE SET UP VIRTUAL MIDI!')
        return
    # play one mode endlessly
    global command
    with midiout:
        while True:
            if command == 0:
                # SEND NOTE OFF TO ALL NOTES IN 1, 2 MIDI CHANNELS
                for midi_channel in range(2):
                    for pitch in range(128):
                        time.sleep(0.01)  # slow down sending messages little bit
                        midiout.send_message([0x80 | midi_channel, pitch, 0])
                del midiout
                return
            if command == 1:
                request_cmdaw_request_api = get_mode_1_request()
                speed_randomizer_amount = uniform(0.05, 0.2)
                velocity_randomizer_amount = 0.15
            elif command == 2:
                request_cmdaw_request_api = get_mode_1_request()
                speed_randomizer_amount = 0.08
                velocity_randomizer_amount = 0.15
            elif command == 3:
                request_cmdaw_request_api = get_mode_1_request()
                speed_randomizer_amount = 0.08
                velocity_randomizer_amount = 0.15
            elif command == 4:
                request_cmdaw_request_api = get_mode_1_request()
                speed_randomizer_amount = 0.08
                velocity_randomizer_amount = 0.08
            elif command == 5:
                request_cmdaw_request_api = get_mode_1_request()
                speed_randomizer_amount = 0.04
                velocity_randomizer_amount = 0.15
            else:
                raise ValueError('wrong command (0-5 available only)')
            # send request to cmdaw_request
            print(request_cmdaw_request_api)
            response = json.loads(
                make_request_to_request_cmdaw_request(request_cmdaw_request_api=request_cmdaw_request_api))
            delays_in_seconds_and_rtmidi_messages = convert_song_sequence_response_to_delays_in_seconds_and_rtmidi_messages(
                song_sequence_response=response, bpm=request_cmdaw_request_api['bpm']
            )
            # play midi
            for delay_in_seconds, rtmidi_message in delays_in_seconds_and_rtmidi_messages:
                if command == 0:
                    return
                # randomize time
                random_time_offset = delay_in_seconds * uniform(0, speed_randomizer_amount)
                time.sleep(delay_in_seconds + random_time_offset)
                # randomize velocity
                velocity = rtmidi_message[2]
                if velocity > 0:
                    humanized_velocity = int(
                        uniform(-velocity_randomizer_amount / 2, velocity_randomizer_amount / 2)
                        * velocity
                    )
                    rtmidi_message[2] = humanized_velocity if 0 < humanized_velocity < 128 else rtmidi_message[2]
                # send midi message
                midiout.send_message(rtmidi_message)
            # hold pause before next song
            time.sleep(random.uniform(2, 6))


@app.get("/play/{cmd}")
def play_command(cmd: int):
    global command
    if cmd < 0 or cmd > 5:
        raise HTTPException(status_code=400, detail='wrong command number (0-5 available only)')
    command = cmd
    play_midi()
    return {"message": f"command {command} successful"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=3333)
