from typing import List, Union

from midi_utils.constants import CHORDS
from midi_utils.utils import note_to_midi


def lookup_chord(root: Union[str, int], chord: str, **kwargs) -> List[int]:
    """
    Given a root and a chord name return a list of chord midi notes
    """
    midi_root = note_to_midi(root)
    base_notes = CHORDS.get(chord.upper().strip())
    if not base_notes:
        raise ValueError(
            f'Invalid chord name: {chord}. Choose from:{",".join(CHORDS.keys())}'
        )
    return [midi_root + note for note in base_notes]


def invert_chord(
    chord_notes: List[int], inversions: List[int] = [], **kwargs
) -> List[str]:
    """
    Given a list of chord notes and a list of inversions, return an inverted chord
    """
    if not len(inversions):
        return chord_notes

    inverted_chord = []
    for i, note in enumerate(chord_notes):
        inv = inversions[i % len(inversions)]
        note += inv * 12
        inverted_chord.append(note)
    return inverted_chord


def stack_chord(chord_notes: List[int], stack: int = 0, **kwargs):
    """
    Given a list of chord notes and a negative/positive integer, stack a chord and select its unique notes.
    """
    stacked_chord = [(stack * 12) + note for note in chord_notes]
    return list(sorted(list(set(stacked_chord + chord_notes))))


def midi_chord(
    root: Union[str, int], chord="MIN_6_9", inversions=[], stack=0, **kwargs
):
    """
    Given a chord root, chord name, list of inversions, and a number and direction to stack, generate a chord.
    """
    chord_notes = lookup_chord(root, chord)
    return stack_chord(invert_chord(chord_notes, inversions), stack)
