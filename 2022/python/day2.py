from utils import get_data

outcomes = {"AX": 3, "AY": 6, "AZ": 0, "BX": 0, "BY": 3, "BZ": 6, "CX": 6, "CY": 0, "CZ": 3}
shape_score = {"X": 1, "Y": 2, "Z": 3}
hands = [round.split(" ") for round in get_data(2)]


def hand_result(a_hand, b_hand):
    return outcomes[f"{a_hand}{b_hand}"]


def round_outcome(hand, hand_result):
    return shape_score[hand] + hand_result


def day2_1():
    return sum([round_outcome(b_hand, hand_result(a_hand, b_hand)) for a_hand, b_hand in hands])


def day2_2():
    match_outcome = {"X": 0, "Y": 3, "Z": 6}

    def get_desired_hand(a_hand, outcome):
        filtered_hands = [hand for hand in outcomes.keys() if hand[0] == a_hand]
        return [hand[1] for hand in filtered_hands if outcomes[hand] == outcome][0]

    b_hands = [get_desired_hand(a_hand, match_outcome[outcome]) for a_hand, outcome in hands]
    a_hands = [a_hand for a_hand, _ in hands]
    return sum([round_outcome(b_hand, hand_result(a_hand, b_hand)) for a_hand, b_hand in zip(a_hands, b_hands)])
