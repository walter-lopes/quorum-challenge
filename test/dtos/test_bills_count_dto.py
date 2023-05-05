import unittest

from dtos.bills_count_dto import BillsCountDto
from model.bill import Bill
from model.legislator import Legislator
from model.vote_result import VoteResult


class TestBillsCountDto(unittest.TestCase):

    def test_should_set_a_valid_dto(self):
        bill = Bill(1, 'Sample Bill', 2)
        legislator = Legislator(1, 'Sample Legislator')
        vote_result = VoteResult(1, 1, 1, 1)

        dto = BillsCountDto(bill, vote_result, legislator)

        assert dto.id == 1
        assert dto.title == 'Sample Bill'
        assert dto.primary_sponsor == 'Sample Legislator'
        assert dto.supporter_count == 1
        assert dto.opposer_count == 0

    def test_should_set_a_primary_sponsor_unknown(self):
        bill = Bill(1, 'Sample Bill', 2)
        vote_result = VoteResult(1, 1, 1, 1)

        dto = BillsCountDto(bill, vote_result, None)

        assert dto.primary_sponsor == 'Unknown'

    def test_should_increase_opposer_count(self):
        bill = Bill(1, 'Sample Bill', 2)
        legislator = Legislator(1, 'Sample Legislator')
        supporter_vote = VoteResult(1, 1, 1, 1)

        dto = BillsCountDto(bill, supporter_vote, legislator)

        opposer_vote = VoteResult(1, 1, 1, 2)

        dto.update_votes(opposer_vote)

        assert dto.opposer_count == 1
        assert dto.supporter_count == 1

    def test_should_increase_supporter_count(self):
        bill = Bill(1, 'Sample Bill', 2)
        legislator = Legislator(1, 'Sample Legislator')
        supporter_vote = VoteResult(1, 1, 1, 1)

        dto = BillsCountDto(bill, supporter_vote, legislator)

        supporter_vote_2 = VoteResult(1, 1, 1, 1)

        dto.update_votes(supporter_vote_2)

        assert dto.supporter_count == 2
        assert dto.opposer_count == 0