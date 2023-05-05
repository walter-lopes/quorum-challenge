from commands.generate_count_bills_command import GenerateCountBillsCommand
from dtos.bills_count_dto import BillsCountDto
from infrastructure.csv_writer import CsvWrite


class GenerateBillsCountCommandHandler:

    def __init__(self):
        pass

    def handle(self, command: GenerateCountBillsCommand):

        votes_by_id_map = {vote.id: vote for vote in command.votes}

        legislators_by_id_map = {legislator.id: legislator for legislator in
                                 command.legislators}

        bills_by_id = {bill.id: bill for bill in command.bills}

        bills_dto_by_id_map = {}

        for vote_result in command.vote_results:
            vote = votes_by_id_map[vote_result.vote_id]
            legislator = legislators_by_id_map.get(vote_result.legislator_id)

            if vote.bill_id in bills_dto_by_id_map:
                bill_dto = bills_dto_by_id_map[vote.bill_id]
                bill_dto.update_votes(vote_result)
            else:
                bill = bills_by_id[vote.bill_id]
                bills_dto_by_id_map[bill.id] = BillsCountDto(bill, legislator,
                                                             vote_result)

        CsvWrite().write(list(bills_dto_by_id_map.values()), 'bill.csv')
