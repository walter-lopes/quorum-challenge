from typing import  Set

from model.bill import Bill
from model.legislator import Legislator
from model.vote_result import VoteResult


class BillsCountDto:

    def __init__(self, bill: Bill, legislator: Legislator, vote_result: VoteResult):
        self.opposer_count = 0
        self.supporter_count = 0
        self.id = bill.id
        self.title = bill.title
        self.primary_sponsor = legislator.name if legislator else 'Unknown'
        self.update_votes(vote_result)

    def update_votes(self, vote_result: VoteResult):
        if vote_result.is_yes():
            self.supporter_count += 1
        else:
            self.opposer_count += 1

    @staticmethod
    def header() -> Set[str]:
        return {"id", "title", "supporter_count", "opposer_count", "primary_sponsor"}

    def __iter__(self):
        return iter([self.id, self.title, self.supporter_count, self.opposer_count,
                     self.primary_sponsor])
