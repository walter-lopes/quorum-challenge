from typing import Set, List

from model.legislator import Legislator
from model.vote_result import VoteResult


class LegislatorSupportOpposeCountDto:
    def __init__(self, legislator: Legislator, vote_result: VoteResult):
        self.num_supported_bills = 0
        self.num_opposed_bills = 0
        self.id = legislator.id
        self.name = legislator.name
        self.update_votes(vote_result)

    def update_votes(self, vote_result: VoteResult):
        if vote_result.is_yes():
            self.num_supported_bills += 1
        else:
            self.num_opposed_bills += 1

    @staticmethod
    def header() -> List[str]:
        return ["id", "name", "num_supported_bills", "num_opposed_bills"]

    def __iter__(self):
        return iter([self.id, self.name, self.num_supported_bills, self.num_opposed_bills])
