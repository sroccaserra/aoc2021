int Solve1(IEnumerable<int> numbers)
{
    return (
            from pair in numbers.Zip(numbers.Skip(1))
            where pair.First < pair.Second
            select 1
        ).Count();
}

var input = File.ReadAllText("src/01.in");
var numbers = from line in input.Split('\n')
    where line != ""
    select int.Parse(line);

Console.WriteLine(Solve1(numbers));
