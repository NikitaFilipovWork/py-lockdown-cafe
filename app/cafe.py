import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor not vaccinated!")

        today_datetime = datetime.date.today()

        if today_datetime > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("Visitor has outdated vaccine!")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("Visitor is not wearing a mask!")

        return f"Welcome to {self.name}"
