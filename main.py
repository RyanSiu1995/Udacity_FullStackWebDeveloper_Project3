from query import Logs
from decimal import Decimal


if __name__ == "__main__":
    # Initialize the Logs object with the database name
    log = Logs('news')
    # Initialize the output file
    file = open("output.txt", "w")
    # Answer to first question
    file.write(
        "First Question: What are the most popular" +
        " three articles of all time?\n")
    firstAnswer = log.popularArticles(3)
    for answer in firstAnswer:
        file.write(answer[0] + " - " + str(answer[1]) + "\n")
    # Answer to second question
    file.write(
        "Second Question: Who are the most " +
        "popular article authors of all time?\n")
    secondAnswer = log.popularAuthors()
    for answer in secondAnswer:
        file.write(answer[0] + " - " + str(answer[1]) + "\n")
    # Answer to third question
    file.write(
        "Third Question: On which days did " +
        "more than 1% of requests lead to errors?\n")
    thirdAnswer = log.errorReport()
    for answer in thirdAnswer:
        file.write(
            answer[0].date().isoformat() +
            " - " + str(round(Decimal(answer[1]), 2)) + "%")
    # close the file
    file.close()
