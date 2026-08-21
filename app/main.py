from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    need_vaccine = 0
    cafe_ = cafe
    for friend in friends:
        try:
            cafe_.visit_cafe(friend)
        except VaccineError:
            need_vaccine += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if need_vaccine > 0:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe_.name}"
