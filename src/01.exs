import Enum, only: [count: 2, map: 2, zip: 2]
import IO, only: [puts: 1, read: 2]
import String, only: [split: 3, to_integer: 1]

defmodule Day01 do
  @huge 9999

  ##
  # The "solve_1" solution is more in line with most other languages solutions
  def solve_1(numbers) do
    solve_1(numbers, @huge, 0)
  end

  def solve_1([], _, result) do
    result
  end

  def solve_1([n|rest], previous, result) do
    case n > previous do
      true -> solve_1(rest, n, result + 1)
      false -> solve_1(rest, n, result)
    end
  end

  ##
  # Here, the "part_1" solutions are more in line with the Haskell solutions
  def part_1(numbers) do
    zip(numbers, tl(numbers))
    |> count(fn {left, right} -> left < right end)
  end

  def part_2(numbers) do
    sum_by_3(numbers)
    |> part_1
  end

  defp sum_by_3(numbers) do
    case numbers do
      [x, y, z | rest] -> [x+y+z] ++ sum_by_3([y, z | rest])
      _ -> []
    end
  end
end

numbers = read(:stdio, :all)
          |> split("\n", trim: true)
          |> map(&to_integer/1)

puts Day01.solve_1(numbers)
puts Day01.part_2(numbers)
