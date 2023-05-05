from commands.generate_count_bills_command import GenerateCountBillsCommand
from commands.generate_legislator_support_oppose_count_command import \
    GenerateLegislatorSupportOpposeCountCommand
from handlers.bills_count_command_handler import GenerateBillsCountCommandHandler
from handlers.generate_legislator_support_oppose_count_command_handler import \
    GenerateLegislatorSupportOpposeCountCommandHandler
from infrastructure.csv_reader import CsvReader
from infrastructure.csv_writer import CsvWriter
from model.bill import Bill
from model.legislator import Legislator
from model.vote import Vote
from model.vote_result import VoteResult

if __name__ == '__main__':

    print('Starting vote calculating...')

    reader = CsvReader()
    writer = CsvWriter()

    legislators = reader.read("legislators.csv", Legislator)
    bills = reader.read("bills.csv", Bill)
    votes = reader.read("votes.csv", Vote)
    vote_results = reader.read("vote_results.csv", VoteResult)

    command = GenerateCountBillsCommand(legislators, bills, votes, vote_results)
    GenerateBillsCountCommandHandler(writer).handle(command)

    command = GenerateLegislatorSupportOpposeCountCommand(legislators, vote_results)
    GenerateLegislatorSupportOpposeCountCommandHandler(writer).handle(command)

    print('Finished')