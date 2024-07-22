import os
from typing import List

import requests
from dotenv import load_dotenv

load_dotenv()

# setup url
mode = 'prod'
if mode == 'prod':
    url = os.getenv('URL_CMDAW_REQUEST_SONG_SEQUENCER')
else:
    url = "http://localhost:10000/song_sequencer"


def make_request_to_request_cmdaw_request(request_cmdaw_request_api: dict):
    return requests.post(url, json=request_cmdaw_request_api).json()


def convert_song_sequence_response_to_delays_in_seconds_and_rtmidi_messages(
        song_sequence_response: dict, bpm: float
) -> List[list]:
    S_IN_BAR = 60 / bpm * 4

    MIDI_CH_PIANO = 1
    MIDI_CH_HARMONY = 2

    NOTE_ON_PIANO = 0x90 | (MIDI_CH_PIANO - 1)
    NOTE_OFF_PIANO = 0x80 | (MIDI_CH_PIANO - 1)

    NOTE_ON_HARMONY = 0x90 | (MIDI_CH_HARMONY - 1)
    NOTE_OFF_HARMONY = 0x80 | (MIDI_CH_HARMONY - 1)

    bass_layer_notes = song_sequence_response['bass']['notes']
    accomp_layer_notes = song_sequence_response['accomp']['notes']
    harmony_layer_notes = song_sequence_response['harmony']['notes']

    rtmidi_messages_by_position = {}
    for notes, note_on, note_off in [
        [bass_layer_notes+accomp_layer_notes, NOTE_ON_PIANO, NOTE_OFF_PIANO],
        [harmony_layer_notes, NOTE_ON_HARMONY, NOTE_OFF_HARMONY]
    ]:
        for note in notes:
            for position, note_message, pitch, velocity in [
                [note['position'], note_on, note['pitch'], note['velocity']],
                [note['position'] + note['length'], note_off, note['pitch'], 0]
            ]:
                if position not in rtmidi_messages_by_position:
                    rtmidi_messages_by_position[position] = []
                rtmidi_messages_by_position[position].append([note_message, pitch, velocity])
    # sort
    rtmidi_messages_by_position_sorted = {k: rtmidi_messages_by_position[k] for k in sorted(rtmidi_messages_by_position)}

    delays_in_seconds_and_rtmidi_messages = []
    last_position = 0
    for position, rtmidi_messages in rtmidi_messages_by_position_sorted.items():
        for rtmidi_message in rtmidi_messages:
            delay_in_bars = position - last_position
            delay_in_seconds = delay_in_bars * S_IN_BAR
            delays_in_seconds_and_rtmidi_messages.append(
                [delay_in_seconds, rtmidi_message]
            )
            last_position = position
    return delays_in_seconds_and_rtmidi_messages

