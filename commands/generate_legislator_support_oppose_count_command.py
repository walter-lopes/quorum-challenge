from typing import List

from model.legislator import Legislator
from model.vote_result import VoteResult


class GenerateLegislatorSupportOpposeCountCommand:
    def __init__(self, legislators: List[Legislator], vote_results: List[VoteResult]):
        self.legislators = legislators
        self.vote_results = vote_results