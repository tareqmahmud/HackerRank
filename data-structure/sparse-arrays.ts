/*
 * Complete the 'matchingStrings' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. STRING_ARRAY strings
 *  2. STRING_ARRAY queries
 */

function matchingStrings(strings: string[], queries: string[]): number[] {
    const result: any = [];
    // Write your code here
    queries.map((query) => {
        let fetchedStrings = strings.filter((str: any) => str === query);

        result.push(fetchedStrings.length);
    });

    return result;
}
