from typing import Set, List

from model.bill import Bill
from model.legislator import Legislator
from model.vote_result import VoteResult


class BillsCountDto:

    def __init__(self, bill: Bill, vote_result: VoteResult, primary_sponsor: Legislator=None):
        self.opposer_count = 0
        self.supporter_count = 0
        self.id = bill.id
        self.title = bill.title
        self.primary_sponsor = primary_sponsor.name if primary_sponsor else 'Unknown'
        self.update_votes(vote_result)

    def update_votes(self, vote_result: VoteResult):
        if vote_result.is_yes():
            self.supporter_count += 1
        else:
            self.opposer_count += 1

    @staticmethod
    def header() -> List[str]:
        return ["id", "title", "supporter_count", "opposer_count", "primary_sponsor"]

    def __iter__(self):
        return iter([self.id, self.title, self.supporter_count, self.opposer_count,
                     self.primary_sponsor])
