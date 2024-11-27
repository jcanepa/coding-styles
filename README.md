# Coding Styles Exercise

This is a conceptual exercise that examines the tradeoffs of writing programs in various styles:

1. Naïve
2. Refined
3. Clever

## Naïve
This coding style is the easiest to read and understand at a micro-level, especially for the novice programmer. It is often has the most line count of all three styles, but does not rely on documentation or comments to parse it. There may be duplication, there may be lots of variables and certainly room for improvement.

## Refined
This coding style builds on the naïve aproach, and attempts to reduce or remove duplication, and clean up the code with slightly more advanced use of language constructs. It tends to be a little more difficult to parse. There is likely more of a need for inline comments to explain code statements.

## Clever
This is the most terse style, which heaviliy relies on programming language constructs that may not be widely familiar to all programmers. Some might call this "cryptic", in that there is nothing other than the neccesary. It may be harder to read and understand on a line-by-line basis, but it is likely easier to understand concepturally due to abstractions in place of procedural detail. This style heavily relies on comment documentation, and may require the reader to research how it works in order to maintain (change) it.

## Scenario
A secret club's guest list:
- select non-members are on a guest list
- they will arrive with a code, multiple people might have the same code
- guests arrive in sequence and tell us their name and a code
- we check whether or not they are on the list
- if they are, we check whether the code is registered to them
- if it is, we "let them in" and mark the code as expired
- if their name is not on the list, or the code they have is invalid, they are sent away
