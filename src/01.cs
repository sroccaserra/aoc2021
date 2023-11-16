int Solve1(IEnumerable<int> numbers) {
    return (
            from pair in numbers.Zip(numbers.Skip(1))
            where pair.First < pair.Second
            select 1
        ).Count();
}

int Solve2(IEnumerable<int> numbers) {
	var by3 = from tuple in Enumerable.Zip(numbers, numbers.Skip(1), numbers.Skip(2))
		select tuple.First + tuple.Second + tuple.Third;
	
	return Solve1(by3);
}

var input = File.ReadAllText("src/01.in");
var numbers = from line in input.Split('\n')
    where line != ""
    select int.Parse(line);

Console.WriteLine(Solve1(numbers));
Console.WriteLine(Solve2(numbers));
