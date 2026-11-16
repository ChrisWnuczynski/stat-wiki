# Completed-page self-checks

The first 37 completed articles now have two selected question-bank problems each in a “Check yourself” section. The page presents each question itself and links to its bank page; its worked answer is inside a collapsed callout. The 74 selected IDs live in `research/self-checks.json` and are validated against the bank during generation. None duplicates a bank question already embedded in that article's Examples section.

The citation test now rejects only a “Check yourself” section containing no prose beyond links and headings. It also requires two or three bank questions with the same number of collapsed answers on every completed page. This restores guided practice while keeping the larger list of all related bank questions in the generated “Used in” area.
