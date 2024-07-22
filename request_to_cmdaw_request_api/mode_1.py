from random import choice, randint

OFFSET_SEMITONES = 48


def get_mode_1_request():
    # general tags and parameters
    bpm = randint(115, 165)
    scale = 'major'
    semitones_random = randint(0, 12)
    humanize_tag = choice(['humanize_mid', 'humanize_low', 'humanize_high'])
    swing_tag, swing_amount_tag = choice([
        ['groove_type_swing_triplet_8', choice(['groove_set_amount_low', 'groove_set_amount_mid'])],
        ['groove_type_swing_8', choice(['groove_set_amount_low', 'groove_set_amount_mid'])],
        ['groove_type_swing_16',
         choice(['groove_set_amount_low', 'groove_set_amount_mid', 'groove_set_amount_high'])]
    ])
    degrees_tag = 'degrees_by_importance_145_mostly'
    limit_degree_range_tag = choice(['limit_degree_range_14'])
    bass_sequence_tags = [
        choice([
            'create_from_data_bass_neoclassic_wedding_2_bars',
            'create_from_data_bass_neoclassic_wedding_1_bar'
        ]),
        degrees_tag,
        swing_tag,
        swing_amount_tag,
        humanize_tag,
        'create_from_data_set_slicer_each_note',
        limit_degree_range_tag,
        'transpose_degree_src_from_harmony_main',

        choice([
            'vary_continue_right_mid',
            'vary_continue_right_low',
            'vary_continue_right_high',
            '',
            ''
        ]),
        choice([
            'vary_continue_left_mid',
            'vary_continue_left_low',
            '',
            ''
        ])
    ]
    accomp_sequence_tags = [
        choice([
            'create_from_data_accomp_neoclassic_wedding_4_bars',
        ]),
        degrees_tag,
        swing_tag,
        swing_amount_tag,
        humanize_tag,
        'create_from_data_set_slicer_each_note',
        limit_degree_range_tag,
        'transpose_degree_src_from_harmony_main',

        choice([
            'vary_continue_right_mid',
            'vary_continue_right_low',
            'vary_continue_right_high'
        ]),
        choice([
            'vary_continue_left_mid',
            'vary_continue_left_low'
        ])
    ]
    harmony_sequence_tags = [
        choice([
            'create_from_data_harmony_neoclassic_wedding_4_bars',
            'create_from_data_harmony_neoclassic_wedding_8_bars',
            'create_from_data_harmony_neoclassic_wedding_8_bars',
            'create_from_data_harmony_neoclassic_wedding_8_bars'
        ]),
        'degree_progression_sequence_wedding',
        choice([
            'chords_intervals_13',
            'chords_intervals_14',
            'chords_intervals_15',
            'chords_intervals_16',
        ]),
        limit_degree_range_tag
    ]
    return {
        'scale': {
            'bass_main': scale,
            'accomp_main': scale,
            'harmony_main': scale,
            'bass_break_': scale,
            'accomp_break_': scale,
            'harmony_break_': scale,
            'bass_drop': scale,
            'accomp_drop': scale,
            'harmony_drop': scale
        },
        'semitones': {
            'bass_main': 0 + OFFSET_SEMITONES + semitones_random,
            'accomp_main': 12 + OFFSET_SEMITONES + semitones_random,
            'harmony_main': 12 + OFFSET_SEMITONES + semitones_random,
            'bass_break_': 0 + OFFSET_SEMITONES + semitones_random,
            'accomp_break_': 12 + OFFSET_SEMITONES + semitones_random,
            'harmony_break_': 12 + OFFSET_SEMITONES + semitones_random,
            'bass_drop': 0 + OFFSET_SEMITONES + semitones_random,
            'accomp_drop': 12 + OFFSET_SEMITONES + semitones_random,
            'harmony_drop': 12 + OFFSET_SEMITONES + semitones_random
        },
        'arrangement': [
            'create_by_three_next_chainer_neoclassic_short_parts'
        ],
        'microarrangement': [
            'create_by_three_next_flow_ambient_jungle_all_parts_with_harmony_break_without_kick_clap_change_rate_2_scenes',
        ],
        'sequence': {
            'kick_main': [],
            'clap_main': [],
            'hat_main': [],
            'ohat_main': [],
            'perc_main': [],
            'crash_main': [],
            'kick_fill_main': [],
            'clap_fill_main': [],
            'hat_fill_main': [],
            'ohat_fill_main': [],
            'perc_fill_main': [],
            'crash_fill_main': [],
            'bass_main': bass_sequence_tags,
            'accomp_main': accomp_sequence_tags,
            'harmony_main': harmony_sequence_tags,
            'riser_main': [],
            'impact_main': [],
            'hit_main': [],
            'speech_main': [],
            'kick_break_': [
                'create_by_copier_from_kick_main'
            ],
            'clap_break_': [
                'create_by_copier_from_clap_main'
            ],
            'hat_break_': [
                'create_by_copier_from_hat_main'
            ],
            'ohat_break_': [
                'create_by_copier_from_ohat_main'
            ],
            'perc_break_': [
                'create_by_copier_from_perc_main'
            ],
            'crash_break_': [
                'create_by_copier_from_crash_main'
            ],
            'kick_fill_break_': [
                'create_by_copier_from_kick_fill_main'
            ],
            'clap_fill_break_': [
                'create_by_copier_from_clap_fill_main'
            ],
            'hat_fill_break_': [
                'create_by_copier_from_hat_fill_main'
            ],
            'ohat_fill_break_': [
                'create_by_copier_from_ohat_fill_main'
            ],
            'perc_fill_break_': [
                'create_by_copier_from_perc_fill_main'
            ],
            'crash_fill_break_': [
                'create_by_copier_from_crash_fill_main'
            ],
            'bass_break_': choice([
                [
                    'create_by_copier_from_bass_main'
                ],
                bass_sequence_tags
            ]),
            'accomp_break_': choice([
                [
                    'create_by_copier_from_accomp_main'
                ],
                accomp_sequence_tags
            ]),
            'harmony_break_': [
                'create_by_copier_from_harmony_main'
            ],
            'riser_break_': [
                'create_by_copier_from_riser_main'
            ],
            'impact_break_': [
                'create_by_copier_from_impact_main'
            ],
            'hit_break_': [
                'create_by_copier_from_hit_main'
            ],
            'speech_break_': [
                'create_by_copier_from_speech_main'
            ],
            'kick_drop': [
                'create_by_copier_from_kick_main'
            ],
            'clap_drop': [
                'create_by_copier_from_clap_main'
            ],
            'hat_drop': [
                'create_by_copier_from_hat_main'
            ],
            'ohat_drop': [
                'create_by_copier_from_ohat_main'
            ],
            'perc_drop': [
                'create_by_copier_from_perc_main'
            ],
            'crash_drop': [
                'create_by_copier_from_crash_main'
            ],
            'kick_fill_drop': [
                'create_by_copier_from_kick_fill_main'
            ],
            'clap_fill_drop': [
                'create_by_copier_from_clap_fill_main'
            ],
            'hat_fill_drop': [
                'create_by_copier_from_hat_fill_main'
            ],
            'ohat_fill_drop': [
                'create_by_copier_from_ohat_fill_main'
            ],
            'perc_fill_drop': [
                'create_by_copier_from_perc_fill_main'
            ],
            'crash_fill_drop': [
                'create_by_copier_from_crash_fill_main'
            ],
            'bass_drop': choice([
                [
                    'create_by_copier_from_bass_main'
                ],
                bass_sequence_tags
            ]),
            'accomp_drop': choice([
                [
                    'create_by_copier_from_accomp_main'
                ],
                accomp_sequence_tags
            ]),
            'harmony_drop': [
                'create_by_copier_from_harmony_main'
            ],
            'riser_drop': [
                'create_by_copier_from_riser_main'
            ],
            'impact_drop': [
                'create_by_copier_from_impact_main'
            ],
            'hit_drop': [
                'create_by_copier_from_hit_main'
            ],
            'speech_drop': [
                'create_by_copier_from_speech_main'
            ]
        },
        'bpm': bpm,
        'length_seconds': 160.0,
        'scene_length': 8
    }

