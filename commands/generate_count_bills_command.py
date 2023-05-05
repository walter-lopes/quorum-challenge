from typing import List

from model.bill import Bill
from model.legislator import Legislator
from model.vote import Vote
from model.vote_result import VoteResult


class GenerateCountBillsCommand:
    def __init__(self, legislators: List[Legislator], bills: List[Bill],
                 votes: List[Vote], vote_results: List[VoteResult]):
        self.legislators = legislators
        self.bills = bills
        self.votes = votes
        self.vote_results = vote_results