import re

regex = r"(?P<any_employee>.+)@(?P<domain>your-company\.com)"

test_str = (
    "test1@your-company.com\n"
    "person2@your-company.com\n"
    "bobby-tables@your-company.com\n"
    "bobby.tables@your-company.com\n"
    "some-guy@your-company.com\n"
    "test2@yourcompany.com\n"
    "test2@your-company.net\n"
    "someotheremail@gmail.com"
)

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print(
        "Match {matchNum} was found at {start}-{end}: {match}".format(
            matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()
        )
    )

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print(
            "Group {groupNum} found at {start}-{end}: {group}".format(
                groupNum=groupNum,
                start=match.start(groupNum),
                end=match.end(groupNum),
                group=match.group(groupNum),
            )
        )
