import unittest

from dtos.legislator_support_oppose_count_dto import LegislatorSupportOpposeCountDto
from model.legislator import Legislator
from model.vote_result import VoteResult


class TestLegislatorSupportOpposeCountDto(unittest.TestCase):

    def test_should_set_a_valid_dto(self):
        legislator = Legislator(1, 'Sample Legislator')
        vote_result = VoteResult(1, 1, 1, 1)

        dto = LegislatorSupportOpposeCountDto(legislator, vote_result)

        assert dto.id == 1
        assert dto.name == 'Sample Legislator'
        assert dto.num_supported_bills == 1
        assert dto.num_opposed_bills == 0

    def test_should_increase_num_opposed_bills(self):
        legislator = Legislator(1, 'Sample Legislator')
        vote_result = VoteResult(1, 1, 1, 1)

        dto = LegislatorSupportOpposeCountDto(legislator, vote_result)

        opposer_vote = VoteResult(1, 1, 1, 2)

        dto.update_votes(opposer_vote)

        assert dto.num_opposed_bills == 1
        assert dto.num_supported_bills == 1

    def test_should_increase_num_supported_bills(self):
        legislator = Legislator(1, 'Sample Legislator')
        vote_result = VoteResult(1, 1, 1, 1)

        dto = LegislatorSupportOpposeCountDto(legislator, vote_result)

        supporter_vote_2 = VoteResult(1, 1, 1, 1)

        dto.update_votes(supporter_vote_2)

        assert dto.num_supported_bills == 2
        assert dto.num_opposed_bills == 0